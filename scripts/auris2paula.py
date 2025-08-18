import sys,os,re,argparse,pandas,math,traceback
import numpy as np
import auris

args=argparse.ArgumentParser(description="""Convert/export from AURIS files into PAULA format.""")
args.add_argument("xlsx", type=str, help="XLSX file with coref annotation to be converted")
args.add_argument("-c","--conllu", type=str, nargs="?", help="CoNLL-U file, optional", default=None)
args.add_argument("tgt", type=str, help="corpus directory, we install into TGT/(basename XLSX), where basename returns the normalized basename, stripped of '.xslx', etc. TGT/(basename XLSX) must not exist, yet")
args.add_argument("lang", type=str, nargs="?", help=f"language, defaults to 'undef'", default="undef")
args=args.parse_args()

parser=auris.AURISParser(args.lang)
parsed=parser.parse(args.xlsx,conllu=args.conllu)
parsed.print_words()

docname=re.sub(r"[\\/]",".",re.sub(r"[^a-zA-Z0-9/\\]+","_",args.tgt).strip("_")).strip(".")+"."+re.sub(r"[^a-zA-Z0-9]+","_",re.sub(r"\.xlsx$","",os.path.basename(args.xlsx))).strip("_")

############################
# in-memory representation #
############################

# primary data, as written into text_xml
text=""

# sentence id to word id to start and end position
s2w2start_end={}

# todo: update to take separator information from CoNLL-U into account
for snr,sentence in enumerate(parsed):
	s2w2start_end[snr]={}
	for wnr,word in enumerate(sentence.get_words()):
		if "WORD" in word:
			s2w2start_end[snr][wnr+1]=(len(text),len(text)+len(word["WORD"]))
			text+=word["WORD"]
			text+=" "
	text+="\n"

#############
# spell out #
#############
args.tgt=os.path.join(args.tgt,re.sub(r"[^a-zA-Z0-9]+","_",re.sub(r"\.xlsx$","",os.path.basename(args.xlsx))).strip("_"))
if os.path.exists(args.tgt):
	raise Exception(f"ERROR: found target directory {args.tgt}, skipping {args.xlsx}")
os.makedirs(args.tgt)

text_xml=os.path.join(args.tgt,"text.xml")
with open(text_xml,"wt") as output:
	output.write(f"""<?xml version="1.0" standalone="no"?>
		<!DOCTYPE paula SYSTEM "paula_text.dtd">
		<paula version="1.1">
		<header paula_id="{docname}.text" type="text"/>
		<body>{text}</body>
		</paula>\n""")

# sentence2word2tokid
s2w2tokid={}
tok_xml=os.path.join(args.tgt,"tok.xml")
with open(tok_xml,"wt") as output:
	output.write(f"""<?xml version="1.0" standalone="no"?>
		<!DOCTYPE paula SYSTEM "paula_mark.dtd">
		<paula version="1.1">
		<header paula_id="{docname}.tok"/>
		<markList xmlns:xlink="http://www.w3.org/1999/xlink" type="tok" xml:base="{docname}.text.xml">\n""")
	nr=0
	for s,w2start_end in s2w2start_end.items():
		s2w2tokid[s]={}
		for w,(start,end) in w2start_end.items():
			nr+=1
			tokid=f"tok_{nr}"
			s2w2tokid[s][w]=tokid
			output.write(f"""\t\t\t\t<mark id="{tokid}" xlink:href="#xpointer(string-range(//body,'',{start+1},{end-start}))"/> <!-- {"_".join(parsed[s].get_words()[w-1]["WORD"].split("-"))} -->\n""")
	output.write("\t\t\t</marklist>\n\t\t</paula>")

# word-level annotations
# note: our annotations are actually directly over tokens, but as current coref visualizations has separate markables as basis,
#       we encode them in this way.
coref_seg_xml=os.path.join(args.tgt,"coref_seg.xml")
with open(coref_seg_xml,"wt") as output:
	corefid2last_mention={}
	output.write(f"""<?xml version="1.0" standalone="no"?>
		<!DOCTYPE paula SYSTEM "paula_mark.dtd">
		<paula version="1.1">
		<header paula_id="{docname}.coref_seg"/>
		<markList xmlns:xlink="http://www.w3.org/1999/xlink" type="mark" xml:base="{docname}.tok.xml">\n""")
	relnr=0
	mnr=0
	for snr,s in enumerate(parsed):
		for wnr,w in enumerate(s.get_words()):
			if "COREF" in w and not str(w["COREF"]) in ["","_","???","!!!","nan"]:
				corefid=w["COREF"]
				tokid=s2w2tokid[snr][wnr+1]
				mnr+=1
				mid=f"markable_{mnr}"
				output.write(f"""\t\t\t\t<mark id="{mid}" xlink:href="#{tokid}"/> <!-- {"_".join(w["WORD"].split("-"))} -->\n""")
				corefid2last_mention[corefid]=mid
#				if corefid in corefid2last_mention:
#					relnr+=1
	output.write(f"""\t\t\t</markList>\n\t\t\t</paula>\n""")

# sentence-level markables
sent_xml=os.path.join(args.tgt,"sent_seg.xml") # this is not from a concrete example, just as a general markup file
with open(sent_xml,"wt") as output:
	output.write(f"""<?xml version="1.0" standalone="no"?>
		<!DOCTYPE paula SYSTEM "paula_mark.dtd">
		<paula version="1.1">
		<header paula_id="{docname}.sent_seg"/>
		<markList xmlns:xlink="http://www.w3.org/1999/xlink" type="sent" xml:base="{docname}.tok.xml">\n""")
	for nr,(s,w2tokid) in enumerate(s2w2tokid.items()):
		sid=f"sent_{s+1}"
		if len(w2tokid)==1:
			output.write("""\t\t\t\t<mark id="{sid}" xlink:href="#{w2tokid.values().next()}"/> <!-- {"_".join(parsed[s].get_words()[0]["WORD"].split("-"))} -->\n""")
		elif len(w2tokid)>1:
			start=w2tokid[min(w2tokid)]
			end=w2tokid[max(w2tokid)]
			output.write(f"""\t\t\t\t<mark id="{sid}" xlink:href="#xpointer(id('{start})/range-to(id({end})))"/> <!-- {"_".join(parsed[s].get_words()[0]["WORD"].split("-"))} ... {"_".join(parsed[s].get_words()[-1]["WORD"].split("-"))} -->\n""")
	output.write("\t\t\t</markList>\n\t\t</paula>")

# sentence-level annotations (feats only)
for feat in ["MARKER","RELATION"]:
	if len([ s.get_annos()[feat] for s in parsed if feat in s.get_annos()]) > 0:
		feat_xml=os.path.join(args.tgt,f"{feat}.xml")
		with open(feat_xml,"wt") as output:
			output.write(f"""<?xml version="1.0" standalone="no"?>
				<!DOCTYPE paula SYSTEM "paula_feat.dtd">
				<paula version="1.1">
				<header paula_id="{docname}.{feat}"/>
				<featList xmlns:xlink="http://www.w3.org/1999/xlink" type="{feat}" xml:base="{docname}.sent_seg">\n""")
			for s,sentence in enumerate(parsed):
				sid=f"sent_{s+1}"
				if feat in sentence.get_annos():
					output.write(f"""\t\t\t\t<feat xlink:href="#{sid}" value="{sentence.get_annos()[feat]}"/> <!-- {"_".join(parsed[s].get_words()[0]["WORD"].split("-"))} ... {"_".join(parsed[s].get_words()[-1]["WORD"].split("-"))} -->\n""")
			output.write("\t\t\t</featList>\n\t\t</paula>")

# discourse relations 
if len([ s.get_annos()["TARGET"] for s in parsed if "TARGET" in s.get_annos()]) > 0:
	discourse_xml=os.path.join(args.tgt,f"discourse.xml")
	discourse_RELATION_xml=os.path.join(args.tgt,f"discourse_RELATION.xml")
	with open(discourse_xml,"wt") as output:
		output.write(f"""<?xml version="1.0" standalone="no"?>
			<!DOCTYPE paula SYSTEM "paula_rel.dtd">
			<paula version="1.1">
			<header paula_id="{docname}.discourse"/>
			<relList xmlns:xlink="http://www.w3.org/1999/xlink" type="discourse" xml:base="{docname}.sent_seg">\n""")

		with open(discourse_RELATION_xml,"wt") as rels:
			rels.write(f"""<?xml version="1.0" standalone="no"?>
				<!DOCTYPE paula SYSTEM "paula_feat.dtd">
				<paula version="1.1">
				<header paula_id="{docname}.discourse_RELATION"/>
				<featList xmlns:xlink="http://www.w3.org/1999/xlink" type="RELATION" xml:base="{docname}.discourse.xml">\n""")

			relnr=0
			for snr,s in enumerate(parsed):
				sid=f"sent_{snr+1}"
				if "TARGET" in s.get_annos():
					try:
						tnr=[tnr for tnr,t in enumerate(parsed) if "ID" in t.get_annos() and str(t.get_annos()["ID"]).strip()==str(s.get_annos()["TARGET"]).strip()][0]
						tid=f"sent_{tnr+1}"
						relnr+=1
						relid=f"rel_{relnr}"
						output.write(f"""\t\t\t\t<rel id="{relid}" xlink:href="#{sid}" target="#{tid}"/>\n""")


						if "RELATION" in s.get_annos():
							rels.write(f"""\t\t\t\t<feat xlink:href="#{relid}" value="{s.get_annos()["RELATION"]}"/>\n""")

					except Exception:
						traceback.print_exc()
						sys.stderr.write(f"""while looking for TARGET {s.get_annos()["TARGET"]} and RELATION {s.get_annos()["RELATION"]}\n""")
			output.write(f"""\t\t\t</relList>\n\t\t</paula>\n""")
			rels.write(f"""\t\t\t</featList>\n\t\t</paula>\n""")
