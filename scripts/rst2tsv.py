import sys,os,re,argparse,json
from lxml import etree
from pprint import pprint

args=argparse.ArgumentParser(description=\
""" read one rs3 (XML) file and produce TSV format with edu ID, target ID; no predicate extraction
	
	conversion principles:
	- if asymmetric: satellite points to nucleus
	- if symmetric: second nuc points to the first
	- keep relations intact

	For schemas, we apply the same principle, but the relation is composed of schema name and name of relation with dependent
""")
args.add_argument("rs3", type=str, help="RS3 (XML) file as produced by RSTTool")
args.add_argument("-j", "--json_output", action="store_true", help="if set, we return JSON (default TSV)")
args.add_argument("-d", "--debug", action="store_true", help="if set, we spell out the internal tree")
args=args.parse_args()

########
# defs #
########

def tree2str(tree, _indent=0):
	result=""
	relation=""
	if "relation" in tree: relation=" "+tree["relation"]
	result=" "*_indent+"("+tree["id"]+relation
	if "children" in tree:
		result+=" "
		for nr,c in enumerate(tree["children"]):
			if nr==0:
				result+=tree2str(c,_indent=_indent+2+len(relation)+len(tree["id"])).lstrip()
			else:
				result+="\n"+tree2str(c,_indent=_indent+2+len(relation)+len(tree["id"]))
	result+=")"
	return result

class RelSet:
	""" relation set: this is for calculating nuclearity
		we treat all relations as mononuclear, unless they are defined as schema or multinuclear """

	def __init__(self,multis=[],arg2schema=[]):
		self.multis=multis
		self.arg2schema=arg2schema

	def get_id2nuc(self, tree):
		""" every relation with more than one child not in multis or arg2schema is considered a mononuclear relation pointing from satellite to nucleus 
			tree structure:
			nonterminal: 'id', children, ?'relation'
			terminal: 'id', ?'relation'
		"""
		multis=self.multis
		arg2schema=self.arg2schema

		id2nuc={}
		if 'children' in tree:
			for c in tree["children"]:
				id2nuc.update(self.get_id2nuc(c))
			for c in tree["children"]:
				relation=""
				if "relation" in c:
					relation =c["relation"]
				if relation in ["","span"]+multis+list(arg2schema):
					id2nuc[tree["id"]]=id2nuc[c["id"]]
					#print(relation,"=>",tree["id"],"->",c["id"])
					break
		if not tree["id"] in id2nuc:
			id2nuc[tree["id"]]=tree["id"]
		return id2nuc

	def sort_tree_by_nuc_order(self, tree):
		""" from the tree, retrieve the first terminal, order all siblings according to terminal 
			NB: we don't order by nuc, but by current first terminal
		"""

		result={ k:v for k,v in tree.items() if k!='children' }
		if 'children' in tree:
			nuc2children={int(self.get_id2nuc(c)[c["id"]]):c for c in tree["children"]}
			children=[]
			for nuc in sorted(nuc2children.keys()):
				children.append(self.sort_tree_by_nuc_order(nuc2children[nuc]))
			result["children"]=children
		return result

	def _tree2rels(self,tree,id2nuc):
		""" implements tree2rels, but as a list of triples, with tree2rels, you get them as dict 
			also, we require tree to be sorted -- this is provided once by tree2rels """
		src_tgt_rels=[]
		
		pnuc=id2nuc[tree["id"]]
		if "children" in tree:
			for c in tree["children"]:
				cnuc=id2nuc[c["id"]]
				if pnuc!=cnuc:
					relation=""
					if "relation" in c:
						relation=c["relation"]
					if relation in self.multis:
						if int(pnuc)<int(cnuc):
							src_tgt_rels.append((cnuc,pnuc,relation))
						else:
							src_tgt_rels.append((pnuc,cnuc,relation))
					elif relation in self.arg2schema:
						relation=arg2schema[relation]+":"+relation
						if int(pnuc)<int(cnuc):
							src_tgt_rels.append((cnuc,pnuc,relation))
						else:
							src_tgt_rels.append((pnuc,cnuc,relation))
					else: # mononuclear
						src_tgt_rels.append((cnuc,pnuc,relation))
				src_tgt_rels+=self._tree2rels(c,id2nuc)

		return src_tgt_rels

	def tree2rels(self,tree):
		tree=self.sort_tree_by_nuc_order(tree)
		id2nuc=self.get_id2nuc(tree)
		src_tgt_rels=sorted(set(self._tree2rels(tree,id2nuc)))
		src2tgt2rel={}
		for s,t,r in src_tgt_rels:
			if not s in src2tgt2rel: 
				src2tgt2rel[s]={ t : r }
			elif not t in src2tgt2rel[s]:
				src2tgt2rel[s][t]=r
			elif r in src2tgt2rel[s][t]:
				raise Exception(f"two labels for edge {s} -> {t}: {src2tgt2rel[s][t]} and {r}")
		return src2tgt2rel

#############
# arguments #
#############

file=args.rs3

with open(file,"rt") as input:
	doc=etree.parse(input)

################
# relation set #
################

# by default, we treat every discourse relation as mononuclear, so we only need to keep track of multis and schemas
# monos=list(doc.xpath("//header/relations/rel[@type='rst']/@name"))
multis=list(doc.xpath("//header/relations/rel[@type='multinuc']/@name"))

# args seem to be unique, and the schema is the name of the entire thing
arg2schema={}
for rel in doc.xpath("//header/relations/rel[string-length(@schema)>0]"):
	arg=rel.attrib["name"]
	schema=rel.attrib["schema"]
	if not arg in arg2schema: 
		arg2schema[arg]=schema
	elif schema!=arg2schema[arg]:
		sys.stderr.write(f"warning: duplicate argument {arg} in schemas {schema} and {arg2schema[arg]}, I'll use {arg2schema[arg]}\n")

# everything not defined as multi or  schema is a mononuclear relation
relset=RelSet(multis,arg2schema)

############
# segments #
############

id2seg={}
for seg in doc.xpath("//body/segment"):
	text="\n".join(seg.xpath("text()"))
	id=seg.attrib["id"]
	if not id in id2seg: 
		id2seg[id]=text
	else:
		raise Exception(f"duplicate segment id {id}")

########
# tree #
########

unattached_ids=list(doc.xpath("//body/segment/@id"))+list(doc.xpath("//body/group/@id"))

# initialize trees
id2tree={}
for id in id2seg:
	tree={ "id":id }
	relations=doc.xpath(f"//body/*[@id='{id}']/@relname")
	if len(relations)>0:
		tree["relation"]=relations[0]
	id2tree[id]=tree
	unattached_ids.remove(id)

# build tree bottom-up
# note that non-terminal nodes (groups) with inaccessible elements, cycles or detached ids are silently skipped
updated=True
while(updated):
	updated=False
	for id in id2tree.keys():
		node=doc.xpath(f"//body/*[@id='{id}']")[0]
		name=node.tag
		if "parent" in node.attrib:
			parent=node.attrib["parent"]
			children=doc.xpath(f"//body/*[@parent='{parent}']/@id")
			inaccessible_children=[c for c in children if not c in id2tree]
			nonterminal_children=False
			for c in children:
				if nonterminal_children==False:
					for gc in doc.xpath(f"//body/*[@parent='{c}']/@id"):
						if gc in id2tree or gc in unattached_ids:
							nonterminal_children=True
							break
			if nonterminal_children==False and len(inaccessible_children)==0:
				subtrees=[]
				for c in children:
					child_node=doc.xpath(f"//body/*[@id='{c}']")[0]
					subtree=id2tree.pop(c)
					if "relname" in child_node.attrib:
						subtree["relation"]=child_node.attrib["relname"]
					subtrees.append(subtree)
				tree={'id':parent, 'children':subtrees }
				if parent in unattached_ids: unattached_ids.remove(parent)
				#print("id2tree:", sorted(set(id2tree.keys())))
				#print(tree2str(tree))
				id2tree[parent]=tree
				updated=True
				break

if len(id2tree)==1:
	tree=list(id2tree.values())[0]
else:
	sys.stderr.write("creating virtual root 0\n")

	tree={"id":"0", 'children': list(id2tree.values()) }

# sort tree 
tree=relset.sort_tree_by_nuc_order(tree)

if args.debug:
	sys.stderr.write(tree2str(tree)+"\n")
	sys.stderr.flush()

##############
# nuclearity #
##############
# implement the strict nuclearity principle

#id2nuc=relset.get_id2nuc(tree)
#print(id2nuc)
# used internally by tree2rels

###########################
# conversion to relations #
###########################

id2id2rel=relset.tree2rels(tree)

##########
# output #
##########

result=[]

nr_ids=[(int(id),id) for id in list(id2id2rel) + list(id2seg) ]
for id2rel in id2id2rel.values():
	for id in id2rel.keys():
		nr_ids.append((int(id),id))

for _,src in sorted(set(nr_ids)):
	utterance={"id":src, "text":""}
	if src in id2seg:
		utterance["text"]=id2seg[src]
	if src in id2id2rel:
		for tgt,rel in id2id2rel[src].items():
			if not "tgt" in utterance:
				utterance["tgt"]=tgt
				utterance["relation"]=rel
			else:
				utterance["tgt"]+="|"+tgt
				utterance["relation"]+="|"+rel

	if args.json_output:
		result.append(utterance)
	else: # tsv
		keys=["id",None,None,None,"text",None,"tgt","relation"]
		line="\t".join([utterance[k] if k in utterance else "_" for k in keys])
		print(line)

if args.json_output:
	json.dumps(result,sys.stdout)



