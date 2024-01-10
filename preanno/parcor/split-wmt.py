import sys,os,re

files=sys.argv[1:]

tgtdir="."
if len(files) > 0:
	tgtdir=files[-1]
	files=files[:-1]

sys.stderr.write(f"set tgtdir to {tgtdir}\n")

if len(files) == 0:
	sys.stderr.write("reading from stdin\n")
	sys.stderr.write("warning: we don't know the languages for some files, then!\n")
	files=[sys.stdin]

sys.stderr.flush()

for file in files:
	outdir=None
	if isinstance(file,str):
		outdir=os.path.join(tgtdir,file.split(".")[-2]) # should contain language identifier
		sys.stderr.write(f"{file}\n")
		file=open(file,"rt",errors="ignore")
	sys.stderr.flush()
	outfile=None
	for line in file:
		line=line.strip()
		if outdir==None and "trglang=" in line:
			outdir=os.path.join(tgtdir,re.sub(r'.*trglang="([^"]+)".*',r"\1",line).strip().split()[0].lower())
			if outfile!=None: 
				outfile.close()
				outfile=None
		if "docid=" in line and outdir!=None:
			if outfile!=None: 
				outfile.close()			
			outfile=os.path.join(outdir,"_".join(re.sub(r'.*docid="([^"]+)".*',r"\1",line).strip().split())+".txt")
			if not os.path.exists(outdir):
				os.makedirs(outdir)
			outfile=open(outfile,"wt")
		line=re.sub(r"<[^>]*>","",line)
		if "<" in line: line=line.split("<")[0]
		if ">" in line: line=line.split(">")[1]
		line=" ".join(line.split()).strip()
		if len(line) > 0 and outfile!=None:
			outfile.write(line+"\n")
			outfile.flush()

	if outfile!=None: outfile.close()








	file.close()