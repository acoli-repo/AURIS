import sys,os,re,argparse
#from pprint import pprint as print

args=argparse.ArgumentParser(description="""convert PDTB-style standoff annotations (text-based format) created by the PDTB Annotator as used for TED-MDB, but also PDTB v.3.0""")
args.add_argument("base_text", type=str, help="text file that the standoff annotation has been performed against")
args.add_argument("anno_text", type=str, help="text(!) file that contains standoff annotations")
# args.add_argument("base_seg", type=str, nargs="?", help="base segmentation, if ommitted, we use a heuristic sentence-splitter", default=None)
args=args.parse_args()

##########################
# PDTB annotation schema #
##########################

def parse_anno_line(line:str):
	line=" ".join(line.strip().split())
	fields=["RelationType", "ConnSpanList", "ConnSrc", "ConnType", "ConnPol", "ConnDet", "ConnFeatSpanList", "Conn1", "SClass1A", "SClass1B", "Conn2", "SClass2A", "SClass2B", "Sup1SpanList", "Arg1SpanList", "Arg1Src", "Arg1Type", "Arg1Pol", "Arg1Det", "Arg1Feat", "Arg2SpanList", "Arg2Src", "Arg2Type", "Arg2Pol", "Arg2Det", "Arg2Feat", "Sup2SpanList", "AdjuReason", "AdjuDisagr", "PBRole", "PBVerb", "Offset", "Provenance", "Link"]
	result=dict(zip(fields,line.split("|")))
	
	if result["SClass1A"].strip()=='':
		# if that happens, nothing was annotated, this can happen in adjugation
		return None

	return result
		
	#	0	RelationType	Explicit, Implicit, AltLex, AltLexC, Hypophora, EntRel, NoRel
	#	1	ConnSpanList	SpanList of the Explicit Connective or the AltLex/AltLexC selection
	#	2	ConnSrc	Connective’s Source
	#	3	ConnType	Connective’s Type
	#	4	ConnPol	Connective’s Polarity
	#	5	ConnDet	Connective’s Determinacy
	#	6	ConnFeatSpanList	Connective’s Feature SpanList
	#	7	Conn1	Explicit Connective Head / First Implicit Connective
	#	8	SClass1A	First Semantic Class of the First Connective
	#	9	SClass1B	Second Semantic Class of the First Connective
	#	10	Conn2	Second Implicit Connective
	#	11	SClass2A	First Semantic Class of the Second Connective
	#	12	SClass2B	Second Semantic Class of the Second Connective
	#	13	Sup1SpanList	SpanList of the First Argument’s Supplement
	#	14	Arg1SpanList	SpanList of the First Argument
	#	15	Arg1Src	First Argument’s Source
	#	16	Arg1Type	First Argument’s Type
	#	17	Arg1Pol	First Argument’s Polarity
	#	18	Arg1Det	First Argument’s Determinacy
	#	19	Arg1Feat	SpanList SpanList of the First Argument’s Feature
	#	20	Arg2SpanList	SpanList of the Second Argument
	#	21	Arg2Src	Second Argument’s Source
	#	22	Arg2Type	Second Argument’s Type
	#	23	Arg2Pol	Second Argument’s Polarity
	#	24	Arg2Det	Second Argument’s Determinacy
	#	25	Arg2Feat	SpanList SpanList of the Second Argument’s Feature
	#	26	Sup2SpanList	SpanList of the Second Argument’s Supplement
	#	27	AdjuReason	The Adjudication Reason
	#	28	AdjuDisagr	The type of the Adjudication disagreement
	#	29	PBRole	The PropBank role of the PropBank verb
	#	30	PBVerb	The PropBank verb of the main clause of this relation
	#	31	Offset	The Conn SpanList of Explicit/AltLex/AltLexC tokens or the start point of the Arg2 of an Implicit/Hypophora/EntRel/NoRel tokens
	#	32	Provenance	Indicates whether the token is a new PDTB3 token or has a corresponding PDTB2 token (see 8.2)
	#	33	Link	The link id of the token

##################
# read base text #
##################

tok_start_ends=[]
with open(args.base_text, "rt") as input:
	base_text=input.read()
	tok=""
	start=0
	for pos,c in enumerate(base_text):
		if re.match(r"^\s+$",c):
			tok=tok.strip()
			if len(tok)>0:
				tok_start_ends.append((tok,start,pos))
			tok=""
			start=pos+1
		else:
			tok+=c

# print(tok_start_ends)

##################
# read anno text #
##################

# seg is a number
start2end2seg={}
seg2start_end={}
seg2seg2marker2rel={}

with open(args.anno_text, "rt") as input:
	for line in input:
		if "|" in line:
			key2val=parse_anno_line(line.strip())
			if(key2val!=None):
				marker=key2val["Conn1"]
				if key2val["RelationType"]!="Excplicit":
					marker=f"({marker})"

				rel=key2val["SClass1A"]

				src_span=key2val["Arg2SpanList"]
				src_start=min([int(x) for x in re.sub(r"[^0-9]+"," ",src_span).split()])
				src_end=max([int(x) for x in re.sub(r"[^0-9]+"," ",src_span).split()])

				src_seg=len(seg2start_end)
				if not src_start in start2end2seg: start2end2seg[src_start]={src_end : src_seg}
				if not src_end in start2end2seg[src_start]: start2end2seg[src_start][src_end] = src_seg
				src_seg=start2end2seg[src_start][src_end]
				seg2start_end[src_seg]=(src_start,src_end)

				tgt_span=key2val["Arg1SpanList"]
				tgt_start=min([int(x) for x in re.sub(r"[^0-9]+"," ",tgt_span).split()])
				tgt_end=max([int(x) for x in re.sub(r"[^0-9]+"," ",tgt_span).split()])

				tgt_seg=len(seg2start_end)
				if not tgt_start in start2end2seg: start2end2seg[tgt_start]={tgt_end : tgt_seg}
				if not tgt_end in start2end2seg[tgt_start]: start2end2seg[tgt_start][tgt_end] = tgt_seg
				tgt_seg=start2end2seg[tgt_start][tgt_end]
				seg2start_end[tgt_seg]=(tgt_start,tgt_end)

				if not src_seg in seg2seg2marker2rel: seg2seg2marker2rel[src_seg]={}
				if not tgt_seg in seg2seg2marker2rel[src_seg]: seg2seg2marker2rel[src_seg][tgt_seg]={marker:rel}
				# simplification: we always go with the first (implicit) discourse marker and its first sense

				# used:		
				#	0	RelationType	Explicit, Implicit, AltLex, AltLexC, Hypophora, EntRel, NoRel
				#	1	ConnSpanList	SpanList of the Explicit Connective or the AltLex/AltLexC selection
				#	7	Conn1	Explicit Connective Head / First Implicit Connective
				#	8	SClass1A	First Semantic Class of the First Connective
				#	14	Arg1SpanList	SpanList of the First Argument
				#	20	Arg2SpanList	SpanList of the Second Argument
				#	30	PBVerb	The PropBank verb of the main clause of this relation

				# skipped, but potentially relevant
				#	9	SClass1B	Second Semantic Class of ttok_start_endshe First Connective
				#	10	Conn2	Second Implicit Connective
				#	11	SClass2A	First Semantic Class of the Second Connective
				#	12	SClass2B	Second Semantic Class of the Second Connective
				# "PBVerb" 		empty in TED-MDB, hence ignored


##################
# resegmentation #
##################
# TODO: import edu segmentation


# build (sentence-level) segmentation from scratch

# tok_start_ends
edu2start_end={}
edu=1
edu_start=0
edu_end=1
edus=[""]
for tokid,(tok,start,end) in enumerate(tok_start_ends):
#	print((tokid,tok,start,end))
	edu_end=end
	edu2start_end[edu]=(edu_start,edu_end)
	edus[-1]=(edus[-1]+" "+" ".join(tok.split()).strip()).strip()
	if re.match(r".*[a-zA-Z].*",edus[-1]) and len(re.sub(r"[^a-zA-Z.!?]*$","",tok)) > 0 and re.sub(r"[^a-zA-Z.!?]*$","",tok)[-1] in [".","!","?"]:
		edus.append("")
		edu+=1
		edu_start=end+1
		edu_end=end+1
#		print("")

#print(edu2start_end)

# we align heuristically by maximum overlap
seg2edu={}
_,tok_start,_=tok_start_ends[0]
_,_,tok_end=tok_start_ends[-1]
edu_start,_=min(edu2start_end.values())
_,edu_end=max(edu2start_end.values())

#print(tok_start, tok_end)
for seg, (start, end) in seg2start_end.items():
	#print(seg,start,end)
	# we extrapolate from length differences, this may fail if the texts differ
	start=int(0.5+edu_start+start*(edu_end-edu_start)/(tok_end-tok_start))
	end=int(0.5+edu_start+end*(edu_end-edu_start)/(tok_end-tok_start))

	overlap=0
	edu=-1
	for cand,(cand_start,cand_end) in edu2start_end.items():
		cand_overlap=min(end,cand_end)-max(start,cand_start)
		#print(cand_overlap,end,cand_end,"min_end",min(end,cand_end),start,cand_start,"max_start",max(start,cand_start))
		if cand_overlap > overlap:
			overlap=cand_overlap
			edu=cand
	seg2edu[seg]=edu

# projection
edu2marker_edu_rel={}
for src, tgt2marker2rel in seg2seg2marker2rel.items():
	orig_src=src
	src=seg2edu[src]
	for tgt, marker2rel in tgt2marker2rel.items():
		orig_tgt=tgt
		tgt=seg2edu[tgt]
		if src==tgt:
			sys.stderr.write(f"warning (intra-segmental relation): skipping {src} ({orig_src}) --> {tgt} ({orig_tgt})\n")
		else:
			# intersegmental relation
			for marker,rel in marker2rel.items():
				if marker.strip() in ["_","","()"]:
					marker="_"
				if not src in edu2marker_edu_rel: 
					edu2marker_edu_rel[src]=(marker,tgt,rel)
				elif len(re.sub(r"[()\s_]","",edu2marker_edu_rel[src][0]).strip())==0 and len(re.sub(r"[()\s_]","",marker).strip())>0:
					# prefer annotation with marker over annotation without
					sys.stderr.write(f"warning (marker preference): skipping {src} -{edu2marker_edu_rel[src][2]}-> {edu2marker_edu_rel[src][1]} in favor of {src} -{marker}/{rel}-> {tgt}\n")
					edu2marker_edu_rel[src]=(marker,tgt,rel)
				elif (not marker.strip()[0] in "([") and edu2marker_edu_rel[src][0].strip()[0] in "([])":
					# prefer explicit over implicit and altlex
					sys.stderr.write(f"warning (explicit marker preference): skipping {src} -{edu2marker_edu_rel[src][2]}-> {edu2marker_edu_rel[src][1]} in favor of {src} -{marker}/{rel}-> {tgt}\n")
					edu2marker_edu_rel[src]=(marker,tgt,rel)
				elif tgt==edu2marker_edu_rel[src][1]:
					# merge annotations for (explicit xor implicit) markers if they point to the the same target
					if marker!=edu2marker_edu_rel[src][0]: marker+="+"+edu2marker_edu_rel[src][0]
					if rel!=edu2marker_edu_rel[src][2]: rel+="|"+edu2marker_edu_rel[src][2]
					edu2marker_edu_rel[src]=(marker,tgt,rel)
				elif abs(src-tgt)<abs(src-edu2marker_edu_rel[src][1]): 
					# prefer closest link
					sys.stderr.write(f"warning (proximity preference): skipping {src} -{edu2marker_edu_rel[src][2]}-> {edu2marker_edu_rel[src][1]} in favor of {src} -{rel}-> {tgt}\n")
					edu2marker_edu_rel[src]=(marker,tgt,rel)
				elif tgt<src:
					sys.stderr.write(f"warning (direction preference): skipping {src} -{edu2marker_edu_rel[src][2]}-> {edu2marker_edu_rel[src][1]} in favor of {src} -{rel}-> {tgt}\n")
					edu2marker_edu_rel[src]=(marker,tgt,rel)
					# prefer link to target in preceding discourse
				else:
					sys.stderr.write(f"warning (other): skipping {src} -{marker}/{rel}-> {tgt} in favor of {src} -{edu2marker_edu_rel[src][0]}/{edu2marker_edu_rel[src][2]}-> {edu2marker_edu_rel[src][1]}\n")

# serialize as TSV

for eduid,edu in enumerate(edus):
	eduid=eduid+1
	if len(edu.strip())>0:
		marker="_"
		rel="_"
		tgt="_"
		pred_id="_"
		predicate="_"
		if eduid in edu2marker_edu_rel:
			marker,tgt,rel=edu2marker_edu_rel[eduid]
		print(f"{eduid}\t{pred_id}\t{marker}\t{predicate}\t{edu}\t_\t{tgt}\t{rel}")
		

#        - SENTENCE_ID
 #       - PREDICATE_ID (or "_")
  #      - MARKER_CANDIDATE (or "_")
   #     - PREDICATE (or "_")
    #    - TEXT
     #   - URL (or "_", optional)
      #  - TARGET (optional, from pre-annotation)
       # - RELATION (optional, from pre-annotation)



