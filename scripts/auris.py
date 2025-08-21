import sys,os,re,pandas,math,traceback

class AlignmentException(Exception):
	pass

class AURISSentence:
	""" note that all annotations must be aligned """

	def __init__(self, toks: list):
		if isinstance(toks,str):
			toks=toks.split()
		self.id2feat2val={nr+1: {"WORD": tok} for nr,tok in enumerate(toks)}
		self.feat2val={}

	def get_text(self, cut_after=0):
		text=" ".join([ self.id2feat2val[nr]["WORD"] for nr in sorted(self.id2feat2val.keys())])
		if isinstance(cut_after,int) and cut_after>0 and len(text.split())>cut_after+1:
			text=" ".join(text.split()[:cut_after+1])+" ..."
		return text

	def to_dict(self):
		""" copy word- and sentence-level annotations as dict """
		result={ id : feat2val for id,feat2val in self.id2feat2val.items() }
		result[0]=self.feat2val
		return result

	def add_w_anno(self, id:int, feat2val:dict):
		if not id in self.id2feat2val:
			raise AlignmentException(f"unsupported id {id}")
		if "WORD" in feat2val and feat2val["WORD"]!=self.id2feat2val[id]["WORD"]:
			raise AlignmentException(f"WORD mismatch, found value {feat2val['WORD']} for expected {self.id2feat2val[id]['WORD']}. Full sequence:\n\t"+self.get_text())
		for f,v in feat2val.items():
			if not str(v) in ['nan','_','','???']:			
				new=v
				if f in self.id2feat2val[id]:
					old=self.id2feat2val[id][f]
					if old!=new:
						sys.stderr.write(f"{old} -> {new} for feature {f} of {v} (word nr {id})\n")
				self.id2feat2val[id][f]=new

	def add_w_annos(self, feat2vals: list):
		""" assume numerical ids, check surface form identity """
		if len(feat2vals)!=len(self.id2feat2val):
			sys.stderr.write(f"warning: length mismatch between word-level features and sentence tokens for {self.get_text(10)}\n")
		for nr,feat2val in enumerate(feat2vals):
			self.add_w_anno(nr+1,feat2val)

	def add_s_anno(self, feat2val: dict):
		for f,v in feat2val.items():
			if not str(v) in ['nan','_','','???']:
				if f in self.feat2val:
					if self.feat2val[f]!=v:
						sys.stderr.write(f"{self.feat2val[f]} -> {v} for feature {f}, sentence {self.get_text(10)}\n")
				self.feat2val[f]=v

	def get_annos(self):
		return self.feat2val

	def get_words(self):
		# similar to to_dict, but return word-level annotations only, and only as list
		# we don't check for consequitive keys
		return [ self.id2feat2val[key] for key in sorted(self.to_dict().keys()) if key>0]

class AURISText:

	wfeats=None

	def __init__(self, id:str, lang:str):
		self.id=id
		self.lang=lang
		self.sentences=[]
		self.max_key_length=0
	
	def add_sentence(self, sentence: AURISSentence):
		self.sentences+=[sentence]
		self.wfeats=None

	def print_sentences(self):
		for s in self.sentences:
			print("# "+s.get_text())
			if(len(s.get_annos())>0):
				if self.max_key_length==0:
					for k in s.get_annos():
						self.max_key_length=max(self.max_key_length,len(k))
				for k,v in s.get_annos().items():
					if len(k)>self.max_key_length:
						self.max_key_length=len(k)
					while(len(k)<self.max_key_length):
						k+=" "
					print(f"{k}\t{v}")
				print()

	def print_words(self):
		if self.wfeats==None:
			self.wfeats=[]
			for s in self.sentences:
				for feat2val in s.to_dict().values():
					for feat in feat2val:
						if not feat in self.wfeats:
							self.wfeats.append(feat)
		print("# "+"\t".join(self.wfeats))
		print()
		for s in self.sentences:
			print("# "+s.get_text())
			for id,feat2val in s.to_dict().items():
				row=[]
				for feat in self.wfeats:
					if not feat in feat2val:
						row.append("_")
					else:
						row.append(str(feat2val[feat]))
				print("\t".join(row))
			print()

	def __getitem__(self,id: int):
		return self.sentences[id]

	def __setitem__(self, id: int, sentence: AURISSentence):
		self.sentences[id]=sentence

	def __delitem__(self, id: int):
		self.sentences.__delitem__(id)

class AURISParser:

	def __init__(self, lang:str):
		self.lang=lang

	def parse(self, xlsx:str, conllu=None):
		""" returns an AURIS Text from an xslx file 
		"""

		if conllu!=None:
			sys.stderr.write("CoNLL-U support not implemented yet\n")

		word_level=None
		try:
			word_level=pandas.read_excel(xlsx,"word-level annotation")	
		except Exception as e:
			traceback.print_exc()
	
		sentence_level=None
		try:
			sentence_level=pandas.read_excel(xlsx,"sentence-level annotation")	
		except Exception as e:
			traceback.print_exc()

		# init text
		text=AURISText(xlsx,self.lang)
		
		# init sentences
		# TODO: if available, we take sentences from CoNLL-U
		sentences=[]
		if not isinstance(word_level,pandas.core.frame.DataFrame):
			row2col2content=sentence_level.transpose().to_dict()
			sentences=[ row2col2content[row]["TEXT"] for row in sorted(row2col2content) if "TEXT" in row2col2content[row] and str(row2col2content[row]["TEXT"])!='nan']
		else:
			# special rules for '--' because this arises as an artifact of the current built process (from grepping)
			# todo: suppress this!
			row2col2content=word_level.transpose().to_dict()
			sentences.append("")
			for _,row in sorted(row2col2content.items()):
				if not "WORD" in row or str(row["WORD"])=='nan' or row["WORD"].split("#")[0].strip()=="":
					if len(sentences[-1])>0 and sentences[-1].strip()!="--":
						sentences[-1]=sentences[-1].strip()
						sentences.append("")
				else:
					sentences[-1]+=row["WORD"]+" "
			sentences[-1]=sentences[-1].strip()

			# to remove grep artifacts in word-level annotations
			sentences=[ re.sub("^-- ","",sentence) for sentence in sentences ]

			if len(sentences[-1])==0:
				sentences=sentences[:-1]
		for s in sentences:
			text.add_sentence(AURISSentence(s))

		# process sentence-level annotations
		if not isinstance(sentence_level,pandas.core.frame.DataFrame):
			sys.stderr.write(f"warning: no sentence_level annotations found for {xlsx}\n")
		else:
			row2col2content=sentence_level.transpose().to_dict()
			nr=0
			for row in sorted(row2col2content):
				row=row2col2content[row]
				if len(row)>0:
					if "TEXT" in row and str(row["TEXT"])!='nan':
						if "".join(row["TEXT"].split()).lower()!="".join(text[nr].get_text().split()).lower():
							sys.stderr.write(f"warning: possible mismatch between word_level and sentence_level annotations:\ns: {row['TEXT']}\nw: {text[nr].get_text()}\n\n")
					text[nr].add_s_anno(row)
					nr+=1
					
		# process word-level annotations
		if not isinstance(word_level,pandas.core.frame.DataFrame):
			sys.stderr.write(f"warning: no word_level annotations found for {xlsx}\n")
		else:
			sys.stderr.write("warning: word-level annotations still to be done\n")

			# we skip the first token of a sentence if it has word value '--' 
			# to account for an artifact of the current built process (from grepping)
			# TODO: fix in data/re-build/drop this workaround
			row2col2content=word_level.transpose().to_dict()
			
			words=[]
			col2contents=[]
			snr=0
			for _,row in sorted(row2col2content.items()):
				if not "WORD" in row or str(row["WORD"])=='nan' or row["WORD"].split("#")[0].strip()=="":
					if len(words)>0:
						if len(words)>1 or words[0].strip()!='--':
							text[snr].add_w_annos(col2contents)
							snr+=1
					words=[]
					col2contents=[]
				elif row["WORD"].strip()=='--' and len(row)==1 and len(words)==0:
					continue # skip sentence-initial '--', unless annotated
				else:
					words.append(row["WORD"])
					col2contents.append(row)
			if len(col2contents)>0:
				text[snr].add_w_annos(col2contents)


			if len(sentences[-1])==0:
				sentences=sentences[:-1]


		sys.stderr.flush()

		return text


if __name__=="__main__":

	import argparse
	args=argparse.ArgumentParser(description="""parse AURIS Excel and (optionally) accompanying CoNLLU file.
		Note that we currently require that word-level, sentence-level and conll-u annotations use the same sentence splits""")
	args.add_argument("xlsx", type=str, help="AURIS xlsx file to be converted")
	args.add_argument("conllu", type=str, nargs="?", help="optional CoNLL-U file", default=None)
	args=args.parse_args()

	parser=AURISParser("de")
	text=parser.parse(args.xlsx,conllu=args.conllu)
	print("="*30+" SENTENCE_LEVEL "+"="*30)
	text.print_sentences()
	print("="*30+"   WORD_LEVEL   "+"="*30)
	text.print_words()



