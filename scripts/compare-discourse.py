import sys,re,os,argparse
args=argparse.ArgumentParser(description="compare discourse annotations")
args.add_argument("-s", "--SRC", type=str, nargs="+", help="TSV files with discourse annotations, annotator 1", default=[])
args.add_argument("-t", "--TGT", type=str, nargs="+", help="TSV files with discourse annotations, annotator 2", default=[])
id_col=0
tgt_col=7
rel_col=8
args.add_argument("--id_col", type=int, help=f"ID column, defaults to {id_col}", default=id_col)
args.add_argument("--tgt_col", type=int, help=f"TARGET column, defaults to {tgt_col}", default=tgt_col)
args.add_argument("--rel_col", type=int, help=f"RELATION column, defaults to {rel_col}", default=rel_col)

args=args.parse_args()

# eval 1: SPANS_ACC: did annotators connect the same arguments (= TED-MDB 1)
# eval 1': SPANS_UNDIR_ACC: same as SPANS_ACC, but undirected
# eval 1": SPANS_1_ACC: same as SPANS_ACC, but only for SPANS annotated in the first file 
# eval 1''': SPANS_2_ACC: same as SPANS_ACC, but only for SPANS annotated in the second file 

# eval 2: SPANS_SENSE_ACC: if the same arguments were connected: did annotators identify the same relation (= TED-MDB 2)
# eval 2': MSR_SENSE_ACC: for every boundary between utterances: retrieve the minimal spanning relation(s): did annotators identify the same relation (~ TED-MDB 2)
#			this is a variant designed for comparability with RST-style annotations
# eval 2": UTT_SENSE_ACC: for every utterance: did annotators annotate the same relation (~ TED-MDB2)
# 			this is a baseline for relation identification
# eval 3: UTT_CVG: coverage: for every utterance, did annotators annotate a target

# prep

if len(args.SRC)!=len(args.TGT):
	sys.stderr.write("you need to provide paired (positionally corresponding) files, lists of SRC and TGT files differ in length\n")
	sys.exit(1)

offset=0
for src,tgt in zip(args.SRC,args.TGT):
	sys.stderr.write(f"compare {src} and {tgt}\n")
	sys.stderr.flush()

	diff=0
	with open(src,"rt") as input:
		sid_tgt_rels=[ (offset+int(row.split("\t")[args.id_col]), offset+int(row.split("\t")[args.tgt_col]), row.split("\t")[args.rel_col].strip()) for row in input if len(row.split("\t"))> max(args.id_col,args.tgt_col,args.rel_col) and re.match(r"^[0-9]+$",row.split("\t")[args.id_col]) and re.match(r"^[0-9]+$",row.split("\t")[args.tgt_col]) ]
		diff=len(input.readlines())
	with open(tgt,"rt") as input:
		tid_tgt_rels=[ (offset+int(row.split("\t")[args.id_col]), offset+int(row.split("\t")[args.tgt_col]), row.split("\t")[args.rel_col].strip()) for row in input if len(row.split("\t"))> max(args.id_col,args.tgt_col,args.rel_col) and re.match(r"^[0-9]+$",row.split("\t")[args.id_col]) and re.match(r"^[0-9]+$",row.split("\t")[args.tgt_col]) ]
		diff=max(diff,len(input.readlines()))
	offset+=diff+1

# eval 1: PAIR_ACC: did annotators connect the same arguments (= TED-MDB 1)
sid2tgt={ sid:tgt for sid,tgt,_ in sid_tgt_rels}
tid2tgt={ tid:tgt for tid,tgt,_ in tid_tgt_rels}
SPANS_TP=0
SPANS_TOTAL=0

for id in set(list(sid2tgt.keys())+list(tid2tgt.keys())):
	SPANS_TOTAL+=1
	if id in sid2tgt and id in tid2tgt:
		if sid2tgt[id]==tid2tgt[id]:
			SPANS_TP+=1
SPANS_ACC=SPANS_TP/SPANS_TOTAL
print("SPANS_ACC",SPANS_ACC)
print()

# eval 1': SPANS_UNDIR_ACC: same as SPANS_ACC, but undirected
tgt2tids={}
for tid,tgt,_ in tid_tgt_rels:
	if not tgt in tgt2tids: tgt2tids[tgt]=[]
	if not tid in tgt2tids[tgt]: tgt2tids[tgt].append(tid)
SPANS_UNDIR_TP=SPANS_TP
for id in set(list(sid2tgt.keys())+list(tid2tgt.keys())):
	if id in sid2tgt and not id in tid2tgt:
		tgt=sid2tgt[id]
		if tgt in tgt2tids and id in tgt2tids[tgt]:
			SPAN_UNDIR_TP+=1
			continue
SPANS_UNDIR_ACC=SPANS_UNDIR_TP/SPANS_TOTAL
print("SPANS_ACC_UNDIR",SPANS_UNDIR_ACC)
print()

# eval 1": SPANS_1_ACC: same as SPANS_ACC, but only for SPANS annotated in the first file 
SPANS_1_TOTAL=0
SPANS_1_TP=0
for id in sid2tgt.keys():
	SPANS_1_TOTAL+=1
	if id in sid2tgt and id in tid2tgt:
		if sid2tgt[id]==tid2tgt[id]:
			SPANS_1_TP+=1
SPANS_1_ACC=SPANS_1_TP/SPANS_1_TOTAL
print("SPANS_1_ACC",SPANS_1_ACC)
print()

# eval 1''': SPANS_2_ACC: same as SPANS_ACC, but only for SPANS annotated in the second file 
SPANS_2_TOTAL=0
SPANS_2_TP=0
for id in tid2tgt.keys():
	SPANS_2_TOTAL+=1
	if id in sid2tgt and id in tid2tgt:
		if sid2tgt[id]==tid2tgt[id]:
			SPANS_2_TP+=1
SPANS_2_ACC=SPANS_2_TP/SPANS_2_TOTAL
print("SPANS_2_ACC",SPANS_2_ACC)
print()

# eval 2: PAIR_SENSE_ACC: if the same arguments were connected: did annotators identify the same relation (= TED-MDB 2)
sid2tgt2rel={ sid: {tgt : rel} for sid,tgt,rel in sid_tgt_rels }
tid2tgt2rel={ tid: {tgt : rel} for tid,tgt,rel in tid_tgt_rels }
PAIR_SENSE_TP=0
srel2trel2freq={}
for id,tgt in sid2tgt.items():
	if id in tid2tgt and tid2tgt[id]==tgt:
		srel=sid2tgt2rel[id][tgt].lower().strip()
		trel=tid2tgt2rel[id][tgt].lower().strip()
		if not srel in srel2trel2freq: srel2trel2freq[srel]={}
		if not trel in srel2trel2freq[srel]: srel2trel2freq[srel][trel]=0
		srel2trel2freq[srel][trel]+=1
		if srel==trel:
			PAIR_SENSE_TP+=1
PAIR_SENSE_ACC=PAIR_SENSE_TP/SPANS_TP
print("PAIR_SENSE_ACC",PAIR_SENSE_ACC)
print()
print("rel\tpredicted\ttp\tp\tr\tf\trels")
for srel in sorted(srel2trel2freq):
	tp=0
	if srel in srel2trel2freq[srel]:
		tp = srel2trel2freq[srel][srel]
	fp=sum(srel2trel2freq[srel].values())-tp
	fn=sum( [ trel2freq[srel] for _,trel2freq in srel2trel2freq.items() if srel in trel2freq]) - tp
	p=0
	r=0
	f=0
	if tp+fp>0: p=tp/(tp+fp)
	if tp+fn>0: r=tp/(tp+fn)
	if p+r>0: f=2*p*r/(p+r)
	print(f"{srel}\t{tp+fp}\t{tp}\t{p}\t{r}\t{f}",end="\t")
	freq_trel=[ (freq,trel) for trel,freq in srel2trel2freq[srel].items()]
	for f,t in reversed(sorted(freq_trel)):
		if t!=srel:
			print(f"{t} ({f})",end=" ")
	print()
print()

# eval 2': MSR_SENSE_ACC: for every boundary between utterances: retrieve the minimal spanning relation(s): did annotators identify the same relation (~ TED-MDB 2)
#			this is a variant designed for comparability with RST-style annotations
print("MSR_SENSE_ACC","postponed")

# eval 2": UTT_SENSE_ACC: for every utterance annotated in both files: did annotators annotate the same relation (~ TED-MDB2)
# 			this is a baseline for relation identification, regardless of argument identification
sid2rel={ sid: rel for sid,tgt,rel in sid_tgt_rels }
tid2rel={ tid: rel for tid,tgt,rel in tid_tgt_rels }
UTT_SENSE_TP=0
srel2trel2freq={}
for id,tgt in sid2tgt.items():
	if id in tid2tgt:
		srel=sid2rel[id].lower().strip()
		trel=tid2rel[id].lower().strip()
		if not srel in srel2trel2freq: srel2trel2freq[srel]={}
		if not trel in srel2trel2freq[srel]: srel2trel2freq[srel][trel]=0
		srel2trel2freq[srel][trel]+=1
		if srel==trel:
			UTT_SENSE_TP+=1
UTT_SENSE_ACC=UTT_SENSE_TP/len(set(sid2rel.keys()).intersection(tid2rel.keys()))
print("UTT_SENSE_ACC",UTT_SENSE_ACC)
print()
print("rel\tpredicted\ttp\tp\tr\tf\trels")
for srel in sorted(srel2trel2freq):
	tp=0
	if srel in srel2trel2freq[srel]:
		tp = srel2trel2freq[srel][srel]
	fp=sum(srel2trel2freq[srel].values())-tp
	fn=sum( [ trel2freq[srel] for _,trel2freq in srel2trel2freq.items() if srel in trel2freq]) - tp
	p=0
	r=0
	f=0
	if tp+fp>0: p=tp/(tp+fp)
	if tp+fn>0: r=tp/(tp+fn)
	if p+r>0: f=2*p*r/(p+r)
	print(f"{srel}\t{tp+fp}\t{tp}\t{p}\t{r}\t{f}",end="\t")
	freq_trel=[ (freq,trel) for trel,freq in srel2trel2freq[srel].items()]
	for f,t in reversed(sorted(freq_trel)):
		if t!=srel:
			print(f"{t} ({f})",end=" ")
	print()
print()


# eval 3: UTT_CVG: coverage: for every utterance, did annotators annotate a target
print("UTT_CVG","postponed")

