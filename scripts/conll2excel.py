# https://pypi.org/project/XlsxWriter/
# https://xlsxwriter.readthedocs.io/example_pandas_conditional.html
# https://www.tutorialspoint.com/python_xlsxwriter/python_xlsxwriter_formula_and_function.htm
# https://xlsxwriter.readthedocs.io/working_with_formulas.html

import xlsxwriter,sys,io,re,traceback,argparse

args=argparse.ArgumentParser(description="""given files with word-level and sentence-level pre-annotation, produce an Excel file

	TODO: incorporate pre-annotation, work on CoNLL-U files, instead
	""")
args.add_argument("outfile",type=str,help="output file, Excel format")
args.add_argument("-s","--sentences", type=str, help="sentence-level pre-annotation in TSV format", default=None)
args.add_argument("-w","--words", type=str, help="word-level pre-annotation in TSV format", default=None)
args=args.parse_args()

if args.words==None and args.sentence==None:
	raise Exception("at least one -s or -w argument needs to be provided")

workbook = xlsxwriter.Workbook(args.outfile)

if args.words!=None:

	worksheet = workbook.add_worksheet()

	# formatting
	bold = workbook.add_format({'bold': True})
	coref_color=workbook.add_format({'bg_color': '#FFF5CE'})
	ref_color=workbook.add_format({'bg_color': '#DDE8CB'})
	is_color=workbook.add_format({'bg_color': '#DEE6EF'})
	cb_color=workbook.add_format({'bg_color': '#E0C2CD'})
	hid_color=workbook.add_format({'bg_color': '#EEEEEE'})
	comm_color=workbook.add_format({'bg_color': '#B4C7DC'})

	COLS=["WORD","GR","NP_TYPE","REF_AUTO", "COREF", "REF", "IS", "CB", "GR_ANTE", "REF_DIST", "REF_DIST_ANTE","COMMENT"]
	FORMATS=[bold]*len(COLS)
	FORMATS[4]=workbook.add_format({'bold':True, 'bg_color': '#FFF5CE'})
	FORMATS[5]=workbook.add_format({'bold':True, 'bg_color': '#DDE8CB'})
	FORMATS[6]=workbook.add_format({'bold':True, 'bg_color': '#DEE6EF'})
	FORMATS[7]=workbook.add_format({'bold':True, 'bg_color': '#E0C2CD'})
	FORMATS[8]=workbook.add_format({'bold':True, 'bg_color': '#EEEEEE'})
	FORMATS[9]=workbook.add_format({'bold':True, 'bg_color': '#EEEEEE'})
	FORMATS[10]=workbook.add_format({'bold':True, 'bg_color': '#EEEEEE'})
	FORMATS[11]=workbook.add_format({'bold':True, 'bg_color': '#B4C7DC'})
	COL_LABEL=zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",COLS,FORMATS) # extend IDs if necessary
	
	# Create header
	for col,label,layout in COL_LABEL: 
		worksheet.write(f'{col}1', label, layout)

	# Create body
	with open(args.words,"rt",errors="ignore") as input:
		for nr,line in enumerate(input):
			line=line.rstrip()
		
			word=""
			# Copy content
			for col,val in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",line.split("\t")):
				if col=="A":
					word=val.strip()
				if val.strip()!="":
					worksheet.write(f'{col}{nr+2}', val)

			# Create formulas and conditional formatting
			if word!="" and word[0]!="#":
				
				# COREF
				worksheet.write_formula(f'E{nr+2}', 
					f'=IF(D{nr+2}="?OLD","!!!","")',
					coref_color,'') # None and '' are required to trigger recalculation in LibreOffice

				# REF
				worksheet.write_formula(f'F{nr+2}', 
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!"),"",IF(NOT(ISNA(VLOOKUP(E{nr+2},E$1:E{nr+1},1,FALSE()))),"OLD",IF(AND(E{nr+2}<>"",E{nr+2}<>"!!!"),"NEW","")))',
					ref_color,'')

				# IS
				worksheet.write_formula(f'G{nr+2}', 
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!"),"",IF(OR(J{nr+2}=0,AND(J{nr+2}=1,K{nr+2}=1),AND(J{nr+2}=1,I{nr+2}="SBJ"),AND(J{nr+2}=1,I{nr+2}=0)),"?IN_FOCUS",IF(J{nr+2}<=2,"?ACTIVATED",IF(J{nr+2}<>"","?FAMILIAR",IF(F{nr+2}="NEW",IF(ISNA(VLOOKUP(E{nr+2},#REF!,1,FALSE())),"?TYPE_IDENTIFIABLE","?REFERENTIAL"),"_")))))',
					is_color,'')

				# CB
				worksheet.write_formula(f"H{nr+2}",
					f'=IF(J{nr+2}<>1,"",IF(I{nr+2}="SBJ","CB","?"))',
					cb_color,'')

				# GR_ANTE
				worksheet.write_formula(f"I{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",INDEX(B{nr+1}:B$2,-1+SUMPRODUCT(MAX(ROW(E{nr+1}:E$2)*(E{nr+2}=E{nr+1}:E$2)))))',
					hid_color,'')

				# REF_DIST
				worksheet.write_formula(f"J{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",COUNTBLANK(OFFSET(A$1,,,SUMPRODUCT(MAX(ROW(E$2:E{nr+2})*(E{nr+2}=E$2:E{nr+2})))))-COUNTBLANK(OFFSET(A$1,,,SUMPRODUCT(MAX(ROW(E$1:E{nr+1})*(E2=E$1:E{nr+1}))))))',
					hid_color,'')

				# REF_DIST_ANTE
				worksheet.write_formula(f"K{nr+2}",
					f'=IF(OR(E{nr+2}="",E{nr+2}="!!!",F{nr+2}="NEW"),"",INDEX(J$1:J{nr+1},SUMPRODUCT(MAX(ROW(E$1:E{nr+1})*(E{nr+2}=E$1:E{nr+1})))))',
					hid_color,'')

				# COMMENT
				worksheet.write(f"L{nr+2}","", comm_color)

	# column formatting
	worksheet.set_column('A:A', 20, None, {'align':'left'})
	worksheet.set_column('B:B',None,None,{'align':'center'})
	worksheet.set_column('C:C', 15,None,{'align':'center'})
	worksheet.set_column('D:D', 10,None,{'align':'center'})
	worksheet.set_column('E:H', None,None,{'align':'center'})
	worksheet.set_column('I:K',None,None,{'hidden': True})
	worksheet.set_column('L:L', 40,None,{'text_wrap': True, 'align':'left'}) # unfortunately, this is ignored by LibreOffice

if args.sentences!=None:

	print("TODO")

workbook.close()

