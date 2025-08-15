import sys,os,re,argparse,pandas,math
import numpy as np

mode2description={
	"corefud": "export to Coref-UD format, skip CoNLL-U annotations (to be inserted afterwards)"
}

args=argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description="""convert/export from AURIS XLSX files into TSV format(s). Note that we don't add information not contained in the XLSX (e.g., CoNLL-U syntax). Instead, the respective fields are left open. Supported modes:\n """+ "\n ".join(sorted(["\""+mode+"\" "+desc for mode,desc in mode2description.items()])))

args.add_argument("mode", type=str, help=f"conversion mode, one of \""+"\", \"".join(sorted(mode2description))+"\"") 
args.add_argument("file", type=str, help="XLSX file with coref annotation to be converted")
args=args.parse_args()

if not args.mode in mode2description:
	sys.stderr.write(f"ERROR: invalid mode {args.mode}, use one of \""+"\", \"".join(sorted(mode2description))+"\"\n")
	sys.exit(1)

if not args.file.endswith("xlsx"):
	sys.stderr.write(f"ERROR: {args.file} does not seem to be an *.xslx file\n")
	sys.exit(2)

word_level=None
sentence_level=None
log=""

try:
	word_level=pandas.read_excel(args.file,"word-level annotation")	
except Exception as e:
	log+=f" - {e}\n"

try:
	sentence_level=pandas.read_excel(args.file,"sentence-level annotation")	
except Exception as e:
	log+=f" - {e}\n"

fileid=re.sub(r"[^a-zA-Z0-9]+","_",args.file).strip("_")

if args.mode=="corefud":

	aurisid2cuid={}

	if not isinstance(word_level,pandas.core.frame.DataFrame):
		sys.stderr.write(f"errors while reading {args.file}\n")
		sys.stderr.write(log)
		sys.exit(3)
	else:
		print("# global.Entity = eid-etype-head-other") # required by CorefUD
		row2col2content=word_level.transpose().to_dict()
		wnr=0
		for row in sorted(row2col2content):
			row=row2col2content[row]
			if not "WORD" in row or str(row["WORD"])=='nan' or row["WORD"].split("#")[0].strip()=="":
				if wnr>0:
					print()
					wnr=0
				continue
			wnr+=1
			word=row["WORD"]
			coref="_"
			if "COREF" in row and not f'{row["COREF"]}' in ["","nan","_"]:
				aurisid=f"{args.file} {'_'.join(row['COREF'].lower().strip().split())}"
				if not aurisid in aurisid2cuid:
					aurisid2cuid[aurisid]=f"e{len(aurisid2cuid)+1}"
					coref=f"Entity=({aurisid2cuid[aurisid]}-entity-{wnr})"
				else:
					coref=f"Entity=({aurisid2cuid[aurisid]})"
			line=[str(wnr),word]+["_"]*7+[coref]
			print("\t".join(line))

else:
	sys.stderr.write(f"ERROR: mode {args.mode} not supported yet, skipping {args.file}\n")

