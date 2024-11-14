import os,re,sys,json
from lxml import etree
import argparse
from pprint import pprint

args=argparse.ArgumentParser(description="""MMAX2CoNLL conversion for parcor-full. Should support any markable-based annotation; not tested for relations; known issues: continuous markables, only""")
args.add_argument("mmax_file",type=str,help="*.mmax file")
args.add_argument("-c","--common_paths",type=str,help="common_paths.xml, defaults to `dirname(mmax_file)/common_paths.xml`", default=None)
args.add_argument("-d","--debug",action="store_true", help="if set, use original word ids instead of CoNLL IDs")
args=args.parse_args()

if args.common_paths==None:
	args.common_paths=os.path.join(os.path.dirname(args.mmax_file),"common_paths.xml")

# prep
######

# trying to recover from broken XML (should be ok, because we only derive coref IDs and CoNLL-Merge can recover from broken or incomplete text)
parser = etree.XMLParser(recover=True)

# read config files
###################

common_paths=etree.parse(args.common_paths,parser)
mmax_file=etree.parse(args.mmax_file,parser)

paths={ "basedata_path":None, "markable_path":None , "scheme_path":None}
for p in list(paths):
	paths[p]=common_paths.find(f".//{p}[1]").text.strip()
	if not ":" in paths[p] and not paths[p][0]=="/":
		paths[p]=os.path.join(os.path.dirname(args.mmax_file),paths[p])

annos={ }
for l in common_paths.findall(".//annotations/level"):
	annos[l.text]=dict(l.attrib)
	schemefile=os.path.join(paths["scheme_path"],annos[l.text]["schemefile"])
	annos[l.text]["schemefile"]=schemefile
	annos[l.text]["attribs"]=["id","span"]
	for a in etree.parse(schemefile,parser).findall("//attribute"):
		a=a.attrib["name"].lower()
		if not a in annos[l.text]["attribs"]: 
			annos[l.text]["attribs"].append(a)

words=os.path.join(paths["basedata_path"],mmax_file.find(f".//words[1]").text)

config={"paths":paths, "annos":annos, "words":words}

# read words
############

id_word={}
if not os.path.exists(words):
	sys.stderr.write(f"warning: file {words} declared but not found\n")
	sys.stderr.flush()
else:
	id_word=[ (w.attrib["id"],w.text) for w in etree.parse(words,parser).findall("//word") ]

# read markables
################

level2header={}
level2id2att2val={}

for anno in config["annos"]:
	level=annos[anno]["name"]
	if not level in level2id2att2val:
		level2id2att2val[level]={}
		level2header[level]=annos[anno]["attribs"]
	file=os.path.join(paths["markable_path"],re.sub(r"_words.xml$","", os.path.basename(words))+"".join(anno.split("$")))
	if not os.path.exists(file):
		sys.stderr.write(f"warning: markable file {file} declared but not found\n")
		sys.stderr.flush()
	else:
		with open(file,"rt") as input:
			markables=input.readlines()
			markables=[ line for line in markables if (" ".join(line.strip().split())).startswith("<markable ")]
		for m in markables: # etree.parse(file).findall("//markable"): # not parseable !?
			m = " ".join(m.strip().split())
			m=re.sub(r"<markable (.*)/>",r"\1",m).strip()
			m= { m.split("=")[0]:"".join(m.split("=")[1].split('"')) for m in m.split('" ')}
			id=m["id"]
			level2id2att2val[level][id]=m
			for a in m:
				if not a in level2header[level]:
					level2header[level].append(a)

# align ids and markables
#########################

word2level2marks={}
words=[ w for w,_ in id_word ]

for level,id2att2val in level2id2att2val.items():
	for id,att2val in id2att2val.items():
		if "span" in att2val:
			span=att2val["span"].strip()
			start=re.sub(r"^([a-z_0-9]+)[^a-z_0-9].*",r"\1",span)
			end=re.sub(r".*[^a-z_0-9]([a-z_0-9]+)$",r"\1",span)
			if start in words:
				#print("span",span, start, words.index(start), end, words.index(end))
				start=words.index(start)
				if end in words:
					end=words.index(end)+1
				else:
					end=min(len(words),start+2)

				for x in range(start,end):
					word=words[x]
					#print(word,level,id)
					if not word in word2level2marks:
						word2level2marks[word]={}
					if not level in word2level2marks[word]:
						word2level2marks[word][level]=[id]
					elif not id in word2level2marks[word][level]:
						word2level2marks[word][level].append(id)

# prune level2header
####################

# dropable arguments (unconditional)
droppable_atts=["span","mmax_level"]

# dropable arguments (selected levels only)
droppable_level2atts={
	"sentence": ["orderid","imported"] 
}

# drop
for l,headers in list(level2header.items()):
	level2header[l]= [ h for h in headers 
						if not h in droppable_atts and 
						   not (l in droppable_level2atts and h in droppable_level2atts[l]) ]

# monolithic table
##################

header=["id","word"]
body=[]

# header
for l,headers in level2header.items():
	for h in headers:
		header.append(f"{l}_{h}")
# body
for id,word in id_word:
	if word==None:
		sys.stderr.write(f"warning: missing word form for {id}\n")
		word="_"
	annos=[id,word]
	for l,headers in level2header.items():
		for h in headers:
			anno=[]
			if id in word2level2marks:
				if l in word2level2marks[id]:
					for m in word2level2marks[id][l]:
						if m in level2id2att2val[l]:
							if h in level2id2att2val[l][m]:
								anno.append(level2id2att2val[l][m][h])
			anno="|".join(anno)
			if anno=="":
				anno="_"
			annos.append(anno)
	body.append(annos)

# print as CoNLL
################

# error msges
sys.stderr.flush()

# header
print("# "+"\t".join( [ h for h in header if not h.startswith("sentence_")] ))
print()

# body
sentence=[]
last_anno={"sentence_id":None}
for row in body:

	anno= { h:v  for h,v in zip(header,row) if v!="_"}

	# print sentence
	if "sentence_id" in anno and not "sentence_id" in last_anno:
		sys.stderr.write(f"warning: no sentence id in {last_anno}\n")
		sys.stderr.flush()
	if "sentence_id" in anno and (not "sentence_id" in last_anno or anno["sentence_id"]!=last_anno["sentence_id"]):
		if len(sentence)>0:
			for h,v in last_anno.items():
				if h.startswith("sentence_") and v!="_":
					if h!="sentence_id":
						print("# "+"_".join(h.split("_")[1:])+": "+v)
			print("# text: "+" ".join([r[1] for r in sentence if r!=None and len(r)>1])) 

			print("\n".join(["\t".join(row) for row in sentence ]))
			print()
		sentence=[]
		sentence_atts={}

	# epilogue
	last_anno=anno

	# build sentence
	anno=[v for h,v in zip(header,row) if not h.startswith("sentence_")]
	if not args.debug:
		anno[0]=str(1+len(sentence))
	sentence.append(anno)

if len(sentence)>0:
	for h,v in last_anno.items():
		if h.startswith("sentence_") and v!="_":
			if not h=="sentence_id":
				print("# "+"_".join(h.split("_")[1:])+": "+v)
	print("# text: "+" ".join([r[1] for r in sentence if len(r)>1])) 

	print("\n".join(["\t".join(row) for row in sentence ]))
	print()

