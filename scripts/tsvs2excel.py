# https://pypi.org/project/XlsxWriter/
# https://xlsxwriter.readthedocs.io/example_pandas_conditional.html
# https://www.tutorialspoint.com/python_xlsxwriter/python_xlsxwriter_formula_and_function.htm
# https://xlsxwriter.readthedocs.io/working_with_formulas.html

import xlsxwriter,sys,io,re,traceback,argparse

args=argparse.ArgumentParser(description="""given files with word-level and sentence-level pre-annotation, 
	produce an Excel file
	""")
args.add_argument("outfile",type=str,help="output file, Excel format")
args.add_argument("-s","--sentences", type=str, help="sentence-level pre-annotation in TSV format", default=None)
args.add_argument("-sm", "--sentence_relation_mapping", type=str, help="(requires -s) mapping table for discourse relations, should be a TSV file with SRC<TAB>TGT(<TAB>COMMENT), can contain #-marked comments",default=None)
args.add_argument("-w","--words", type=str, help="word-level pre-annotation in TSV format", default=None)

args=args.parse_args()

if args.words==None and args.sentences==None:
	raise Exception("at least one -s or -w argument needs to be provided")

sRel2auris={}
if args.sentence_relation_mapping!=None:
	if args.sentences==None: raise Exception("using -sm without -s")
	with open(args.sentence_relation_mapping,"rt",errors="ignore") as input:
		for line in input:
			line=line.strip()
			if "\t" in line and not line.startswith("#"):
				fields=line.split("\t")
				try:
					sRel=fields[0].strip()
					auris=fields[1].strip()
					if sRel!="" and auris!="":
						if not sRel in sRel2auris: 
							sRel2auris[sRel]=auris
						elif not auris in sRel2auris[sRel].split("|"):
							sRel2auris[sRel]+="|"+auris
				except Exception:
					pass

workbook = xlsxwriter.Workbook(args.outfile)

if args.sentences!=None:

	worksheet = workbook.add_worksheet("sentence-level annotation")

	# 1. Create header
	# 1.a formatting
	COLS=["ID", "PRED_ID", "MARKER_AUTO", "PREDICATE", "TEXT", "SENTENCE", "MARKER", "TARGET", "RELATION", "COMMENT"]
	FORMATS=[{'valign':'vcenter','bold': True, 'align':'center', 'locked':True} for c in COLS]
	FORMATS[6]['bg_color']='#F7D1D5' # MARKER
	FORMATS[7]['bg_color']='#FFF5CE' # TARGET
	FORMATS[8]['bg_color']='#DEDCE6' # RELATION
	FORMATS[9]['bg_color']='#B4C7DC' # COMMENT
	
	FORMATS=[workbook.add_format(layout) for layout in FORMATS ]

	# 1.b labels
	for col,label,layout in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",COLS,FORMATS): # extend IDs if necessary
		worksheet.write(f'{col}1', label, layout)

	# 2. Create body
	# 2.a formatting
	FORMATS=[
		{'valign':'top','align':'center','locked':True}, 											# ID
		{'valign':'top','align':'center','locked':True}, 											# PRED_ID, hidden
		{'valign':'top','align':'center','locked':True}, 											# MARKER_AUTO, hidden
		{'valign':'top','text_wrap':True,'align':'center','locked':False}, 						# PREDICATE
		{'valign':'top','text_wrap':True,'align':'left','locked':True}, 							# TEXT
		{'valign':'top','align':'center','locked':True}, 											# SENTENCE, hidden
		{'valign':'top','text_wrap':True, 'align':'center','locked':False,'bg_color': '#F7D1D5'}, 	# MARKER
		{'valign':'top','align':'center','locked':False,'bg_color': '#FFF5CE'}, 					# TARGET
		{'valign':'top','text_wrap':True, 'align':'center','bg_color': '#DEDCE6','locked':False}, 	# RELATION
		{'valign':'top','text_wrap': True, 'align':'left','bg_color': '#B4C7DC','locked':False}, 	# COMMENT
	]

	FORMATS=[workbook.add_format(layout) if layout!=None else None for layout in FORMATS ]

	# 2.b create content
	with open(args.sentences,"rt",errors="ignore") as input:
		for nr,line in enumerate(input):
			line=line.rstrip()
			fields=line.split("\t")

			if line!="":

				# Copy content
				for col,val,layout in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",fields, FORMATS):
					worksheet.write(f'{col}{nr+2}', val.strip(), layout)

				# Create formulas and placeholder values
				if line[0]!="#":

					comment_pre=""
					
					# MARKER
					if len(fields)>5 and not(fields[5].strip() in ["","_"]): 
						marker=fields[5].strip()
						worksheet.write(f'G{nr+2}', marker, FORMATS[6])
					else:
						worksheet.write_formula(f'G{nr+2}', 
							f'=IF(A{nr+2}=1,"_",IF(C{nr+2}="_","???",C{nr+2}))',
							FORMATS[6],'') # '' required to trigger recalculation in LibreOffice

					# TARGET
					target_pre="_"
					if len(fields)>6: target_pre=fields[6].strip()
					worksheet.write(f'H{nr+2}', target_pre, FORMATS[7])

					# RELATION
					relation_pre="_"
					if len(fields)>7: relation_pre=fields[7].strip()
					if relation_pre in ("_",""):
						relation_pre="_"
					else:

						if len(sRel2auris)>0:
							transformed_rel=[]
							for tmp in relation_pre.split("+"):
								for rel in tmp.split("|"):
									if len(rel)>0:
										if rel in sRel2auris:
											if not sRel2auris[rel].strip() in ("","_"):
												transformed_rel.append(sRel2auris[rel])
										else:
											sys.stderr.write(f"warning: discourse relation {rel} is not covered by the mapping\n")
							transformed_rel="+".join(sorted(set(transformed_rel)))

							if transformed_rel=="":
								comment_pre+="\n"+f"(unmappable relation)"
								transformed_rel=relation_pre
							else:
								pass #sys.stderr.write(f"{relation_pre} -> {transformed_rel}\n")

							if transformed_rel!=relation_pre:
								comment_pre+="\n"+f"(orig: {relation_pre})"
								relation_pre=transformed_rel

					worksheet.write(f'I{nr+2}', relation_pre, FORMATS[8]) # TODO: replace by marker lookup

					# COMMENT is empty
					comment_pre=comment_pre.strip()
					worksheet.write(f"J{nr+2}",comment_pre,FORMATS[9])

	# 3. overall layout
	worksheet.set_default_row(60)
	worksheet.set_column('B:C',None,None,{'hidden': True})
	worksheet.set_column('D:D', 10)
	worksheet.set_column('E:E', 80)
	worksheet.set_column('F:F', None,None,{'hidden':True})
	worksheet.set_column('G:G', 10)
	worksheet.set_column('I:I', 10)
	worksheet.set_column('J:J', 40) 
	worksheet.freeze_panes(1,5)
	worksheet.protect()

if args.words!=None:

	worksheet = workbook.add_worksheet("word-level annotation")

	# 1. Create header
	# 1.a formatting
	COLS=["WORD","GR","NP_TYPE","REF_AUTO", "COREF", "REF", "IS", "CB", "GR_ANTE", "REF_DIST", "REF_DIST_ANTE","COMMENT"]
	FORMATS=[{'bold': True, 'align':'center', 'locked':True} for c in COLS]
	FORMATS[4]['bg_color']='#FFF5CE' # COREF
	FORMATS[5]['bg_color']='#DDE8CB' # REF
	FORMATS[6]['bg_color']='#DEE6EF' # IS
	FORMATS[7]['bg_color']='#E0C2CD' # CB
	for x in range(8,11):			 # hidden
		FORMATS[x]['bg_color']='#EEEEEE' 
	FORMATS[11]['bg_color']='#B4C7DC' # COMMENT
	
	FORMATS=[workbook.add_format(layout) for layout in FORMATS ]

	# 1.b labels
	for col,label,layout in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",COLS,FORMATS): # extend IDs if necessary
		worksheet.write(f'{col}1', label, layout)

	# 2. Create body
	# 2.a formatting
	FORMATS=[
		{'locked':True}, # WORD
		{'align':'center','locked':False}, # GR
		{'align':'center','locked':False}, # NP_TYPE
		{'align':'center','locked':False}, # REF_AUTO
		{'align':'center','locked':False,'bg_color': '#FFF5CE'}, # COREF
		{'align':'center','locked':False,'bg_color': '#DDE8CB'}, # REF
		{'align':'center','locked':False,'bg_color': '#DEE6EF'}, # IS
		{'align':'center','locked':False,'bg_color': '#E0C2CD'}, # CB
		{'bg_color': '#EEEEEE','locked':True}, # hidden
		{'bg_color': '#EEEEEE','locked':True}, # hidden
		{'bg_color': '#EEEEEE','locked':True}, # hidden
		{'text_wrap': True, 'align':'left','bg_color': '#B4C7DC','locked':False} # COMMENT
	]

	FORMATS=[workbook.add_format(layout) if layout!=None else None for layout in FORMATS ]

	# 2.b create content
	with open(args.words,"rt",errors="ignore") as input:
		for nr,line in enumerate(input):
			line=line.rstrip()

			word=""
			# Copy content
			for col,val,layout in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",line.split("\t"), FORMATS):
				val=val.strip()
				if col=="A": word=val
				worksheet.write(f'{col}{nr+2}', val, layout) # we also "write" cells because of the locking !

			# Create formulas and conditional formatting
			if word!="" and word[0]!="#":
				
				# COREF
				worksheet.write_formula(f'E{nr+2}', 
					f'=IF(D{nr+2}="?OLD","!!!","")',
					FORMATS[4],'') # '' required to trigger recalculation in LibreOffice

				# REF
				worksheet.write_formula(f'F{nr+2}', 
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!"),"",IF(NOT(ISNA(VLOOKUP(E{nr+2},E$1:E{nr+1},1,FALSE()))),"OLD",IF(AND(E{nr+2}<>"",E{nr+2}<>"!!!"),"NEW","")))',
					FORMATS[5],' ') # whitespace to make sure it is *not* re-calculated

				# IS
				worksheet.write_formula(f'G{nr+2}', 
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!"),"",IF(OR(J{nr+2}=0,AND(J{nr+2}=1,K{nr+2}=1),AND(J{nr+2}=1,I{nr+2}="SBJ"),AND(J{nr+2}=1,I{nr+2}=0)),"?IN_FOCUS",IF(J{nr+2}<=2,"?ACTIVATED",IF(J{nr+2}<>"","?FAMILIAR",IF(F{nr+2}="NEW",IF(ISNA(VLOOKUP(E{nr+2},#REF!,1,FALSE())),"?TYPE_IDENTIFIABLE","?REFERENTIAL"),"_")))))',
					FORMATS[6],' ')

				# CB
				worksheet.write_formula(f"H{nr+2}",
					f'=IF(J{nr+2}<>1,"",IF(I{nr+2}="SBJ","CB","?"))',
					FORMATS[7],' ')

				# GR_ANTE
				worksheet.write_formula(f"I{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",INDEX(B{nr+1}:B$2,-1+SUMPRODUCT(MAX(ROW(E{nr+1}:E$2)*(E{nr+2}=E{nr+1}:E$2)))))',
					FORMATS[8],' ')

				# REF_DIST
				worksheet.write_formula(f"J{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",COUNTBLANK(OFFSET(A$1,,,SUMPRODUCT(MAX(ROW(E$2:E{nr+2})*(E{nr+2}=E$2:E{nr+2})))))-COUNTBLANK(OFFSET(A$1,,,SUMPRODUCT(MAX(ROW(E$1:E{nr+1})*(E2=E$1:E{nr+1}))))))',
					FORMATS[9],' ')

				# REF_DIST_ANTE
				worksheet.write_formula(f"K{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",INDEX(J$1:J{nr+1},SUMPRODUCT(MAX(ROW(E$1:E{nr+1})*(E{nr+2}=E$1:E{nr+1})))))',
					FORMATS[10],' ')

				# COMMENT is empty
				worksheet.write(f"L{nr+2}","",FORMATS[11])

	# 3. overall layout
	# worksheet.autofit()  # diabled, was meant for row height, but doesn't do it
	worksheet.set_column('A:A', 20)
	worksheet.set_column('C:C', 15)
	worksheet.set_column('D:D', 10)
	worksheet.set_column('I:K',None,None,{'hidden': True})
	worksheet.set_column('L:L', 40) 
	worksheet.freeze_panes(1,1)
	worksheet.protect()

workbook.close()

