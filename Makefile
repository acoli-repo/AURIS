SHELL=bash

all: ready-for-annotation

# generates statistics
stats:
	@SRCDIR=annotators/;\
	IFS=$$'\n';\
	files=$$(for file in `find $$SRCDIR | grep '\.xlsx$$'`; do basename $$file; done | sort -u);\
	for file in $$files; do \
		freq=`find $$SRCDIR \
			| grep $$file'$$' \
			| wc -l`;\
		status=`find $$SRCDIR \
			| grep $$file'$$' \
			| cut -f 5 -d / \
			| sort -u`;\
		langs=`find $$SRCDIR \
			| grep $$file'$$' \
			| cut -f 4 -d / \
			| sort -u`;\
		for lang in $$langs; do \
			for stat in $$status; do \
				annotators=`find $$SRCDIR \
							| grep $$file'$$' \
							| grep /$$lang/ \
							| cut -f 2-3 -d / \
							| sort -u`;\
				echo $$file'	'$$lang'	'$$status'	'$$annotators;\
			done;\
		done;\
		# DEBUG :\
		#find $$SRCDIR \
		#| grep $$file'$$';\
		#echo;\
	done | \
	sort -b -u

update: update-conllu
	if [ -e ready-for-annotation ]; then rm -rf ready-for-annotation; fi;
	make update-ready-for-annotation

ready-for-annotation: update-ready-for-annotation

update-ready-for-annotation: update-conllu
	make update-discourse_pre
	make update-refexp
	
	@LANGS=`find discourse_pre/*/ refexp/*/ | cut -f 2 -d '/' | sort -u | egrep '[a-z][a-z]'`;\
	 for lang in $$LANGS; do \
			#echo language $$lang 1>&2;\
			FILES=`find discourse_pre/$$lang/ refexp/$$lang/ \
				   | egrep 'tsv$$' \
				   | sed -e s/'.*\/'//g -e s/'\.tsv$$'// -e s/'\.conllu$$'//g -e s/'\.conll$$'//g \
				   | sort -u`;\
			for file in $$FILES; do \
				#echo  $$lang: $$file 1>&2;\
				disc=`find discourse_pre/$$lang/ | grep 'tsv$$' | grep -m 1 '/'$$file`;\
				ref=`find refexp/$$lang/ | grep -m 1 '/'$$file`;\
				path=`if [ ! dirname $$disc 2>/dev/null ]; then dirname $$ref; fi | sed s/'^[^\/]*\/'//`;\
				path=ready-for-annotation/$$lang/$$path;\
				if [ ! -e $$path ]; then mkdir -p $$path; fi;\
				tgt=$$path/$$file.xlsx;\
				if [ ! -e $$tgt ]; then \
					ARGS="scripts/tsvs2excel.py -s $$disc -w $$ref $$tgt";\
					if echo $$disc | grep -v '/' >&/dev/null; then \
						ARGS="scripts/tsvs2excel.py -w $$ref $$tgt";\
					fi;\
					if echo $$ref | grep -v '/' >&/dev/null; then \
						ARGS="scripts/tsvs2excel.py -s $$disc $$tgt";\
					fi;\
					echo python3 $$ARGS 1>&2;\
					python3 $$ARGS;\
				fi;\
			done;\
			echo 1>&2;\
	 done;\
	
rdf4discourse:
	if [ ! -e rdf4discourse ]; then \
		git clone https://github.com/acoli-repo/rdf4discourse;\
	fi;

discourse_pre: 
	if [ ! -e discourse_pre ]; then make update-discourse_pre; fi

update-discourse_pre: conllu conll-rdf rdf4discourse
	@if [ ! -e discourse_pre ]; then mkdir discourse_pre; fi
	@cd conllu;\
	TIMEOUT="nice timeout --preserve-status 1h ";\
	for lang in */; do \
		lang=`echo $$lang | sed s/'\/'//g;`;\
		if [ ! -e ../sparql/discourse1.$$lang.sparql ]; then \
			echo error: did not find ../sparql/discourse1.$$lang.sparql, skipping language $$lang 1>&2;\
		else \
			dimlex=`ls -l ../rdf4discourse/discourse-markers/linked/$$lang/*.ttl | sort -n -k 4 | head -n 1 | sed s/'.* '//g;`;\
			if [ ! -e $$dimlex ] ; then \
				echo error: did not find ../sparql/discourse1.$$lang.sparql, skipping language $$lang 1>&2;\
			else \
				for file in `find $$lang | grep 'conllu$$'`; do \
					echo $$file 1>&2; \
					tgt=../discourse_pre/`echo $$file | sed s/'\.conllu$$'//`.tsv;\
					tgtdir=`dirname $$tgt`;\
					if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi;\
					if [ -e $$tgt ]; then echo found $$tgt, keeping it 1>&2; \
					else \
						cat $$file \
						| $$TIMEOUT ../conll-rdf/run.sh CoNLLStreamExtractor \
							'file://conllu/'$$file'#' \
							ID FORM LEMMA UPOS XPOS FEATS HEAD EDGE DEPS MISC \
							-u ../sparql/discourse1.$$lang.sparql \
						| tee $$tgt.1.ttl \
						| $$TIMEOUT ../conll-rdf/run.sh CoNLLRDFUpdater -custom -model $$dimlex "http://purl.org/acoli/dimlex" \
							-updates ../sparql/discourse2_new.sparql \
						| tee $$tgt.2.ttl \
						| $$TIMEOUT ../conll-rdf/run.sh CoNLLRDFUpdater -custom \
							-updates ../sparql/discourse3.sparql \
						| tee $$tgt.3.ttl \
						| $$TIMEOUT ../conll-rdf/run.sh CoNLLRDFFormatter -query ../sparql/discourse4.sparql \
						| egrep '^[0-9]' \
						| tee $$tgt;\
					fi;\
				done > ../discourse_pre/$$lang.tsv;\
			fi;\
		fi;\
	done;

udpipe:
	if [ ! -e udpipe ]; then echo install UDPipe v.1.0 in `pwd`/udpipe 1>&2; exit 1; fi;

txt/doyle:
	@# for creating doyle files from bilinguis.com, do wget -r -np and run:
	@# for lang1 in *; do mkdir -p bask/$lang1; for file in `find $lang1 | grep html | grep -m 1 c14`; do echo '# url: ' https://bilinguis.com/book/baskerville/$file; echo; cat $file | xmllint --html --recover - --xpath "//div[@lang='"$lang1"']" 2>/dev/null; break; done | pandoc -f html -t markdown | grep -v ':::' | sed s/'^$'/'<br>'/g | perl -pe 's/\s+/ /g; s/<br>/\n\n/g;' > bask/$lang1/doyle_bask.14.txt; done
	@if [ ! -e txt/doyle/de ]; then \
		mkdir -p txt/doyle/de; \
		cd txt/doyle/de; \
		\
		for chap in {1..9} ; do \
			wget -nc https://www.projekt-gutenberg.org/doyle/baskervi/chap00$$chap.html; \
		done;\
		for chap in {10..15} ; do \
			wget -nc https://www.projekt-gutenberg.org/doyle/baskervi/chap0$$chap.html; \
		done;\
		for chap in {1..15} ; do \
			chap=`echo 0$$chap | sed s/'.*\(..\)$$'/'\1'/g;`;\
			file=`ls *0$$chap.html | head -n 1`;\
			tgt=doyle_bask.$$chap.txt;\
			echo txt/doyle/de/$$file '>' txt/doyle/de/$$tgt 1>&2; \
			cat $$file \
			| perl -pe 's/\s+/ /g; s/<h3/\n<h3/g;' \
			| egrep -m 1 '<h3' \
			| perl -pe 's/\s+/ /g; s/<p/\n<p/g; s/<\/p>/\n/g;' \
			| grep '<p' \
			| w3m -T text/html \
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1 /g;' \
			> $$tgt;\
		done;\
		\
		wget -nc https://www.projekt-gutenberg.org/doyle/sterbend/chap003.html -O doyle_wist.html; \
		for chap in {1..2}; do \
			mychap=`echo 0$$chap | sed s/'.*\(..\)$$'/'\1'/g;`;\
			tgt=doyle_wist.$$mychap.txt;\
			echo txt/doyle/de/doyle_wist.html '>' txt/doyle/de/$$tgt 1>&2; \
			cat doyle_wist.html \
			| iconv -f utf-8 -t utf-8 -c \
			| perl -pe 's/\s+/ /g; s/<h4/\n<h4/g;'   \
			| grep '<h4' \
			| grep -v '<h4>Inhalt' \
			| grep -m $$chap '.'  | tee tmp$$chap.full.html | tail -n 1 | tee tmp$$chap.tail.html  \
			| perl -pe 's/<p/\n<p/g; s/<\/p>/\n/g;' \
			| grep -a '<p' \
			| w3m -T text/html \
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1 /g;' \
			> $$tgt;\
		done;\
	fi;

	@if [ ! -e txt/doyle/en ]; then \
		mkdir -p txt/doyle/en; \
		cd txt/doyle/en; \
		\
		wget -nc https://gutenberg.org/cache/epub/3070/pg3070-images.html -O doyle_bask.html;\
		for chap in {1..15}; do \
			mychap=`echo 0$$chap | sed s/'.*\(..\)$$'/'\1'/g;`;\
			tgt=doyle_bask.$$mychap.txt;\
			echo txt/doyle/en/doyle_bask.html '>' txt/doyle/en/$$tgt 1>&2; \
			cat doyle_bask.html \
			| iconv -f utf-8 -t utf-8 -c \
			| perl -pe 's/\s+/ /g; s/<h3/\n<h3/g; s/End of the Project Gutenberg/\n/g;'  \
			| grep -a -m 2 'Chapter_'$$chap | tail -n 1 \
			| perl -pe 's/<p/\n<p/g; s/<\/p>/\n/g;' \
			| grep -a '<p' \
			| w3m -T text/html \
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1 /g;' \
			> $$tgt;\
		done;\
		\
		wget -nc https://www.gutenberg.org/files/2343/2343-h/2343-h.htm -O doyle_wist.html;\
		for chap in {1..2}; do \
			mychap=`echo 0$$chap | sed s/'.*\(..\)$$'/'\1'/g;`;\
			tgt=doyle_wist.$$mychap.txt;\
			echo txt/doyle/en/doyle_wist.html '>' txt/doyle/en/$$tgt 1>&2; \
			cat doyle_wist.html \
			| iconv -f utf-8 -t utf-8 -c \
			| perl -pe 's/\s+/ /g; s/<H3/\n<H3/g; s/End of the Project Gutenberg/\n/g;'   \
			| grep '<H3' \
			| grep -v '#chap01' \
			| grep -m $$chap '.'  | tail -n 1 \
			| perl -pe 's/<P/\n<P/g; s/<\/P>/\n/g;' \
			| grep -a '<P' \
			| w3m -T text/html \
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1 /g;' \
			> $$tgt;\
		done;\
		\
	fi;

	@for lang in txt/doyle/*; do \
		for file in doyle_bask.14.txt doyle_wist.02.txt; do \
			if [ -e $$lang/$$file ]; then \
				if [ ! -e txt/`basename $$lang` ]; then \
					mkdir -p txt/`basename $$lang`; \
				fi; \
				cp $$lang/$$file txt/`basename $$lang`/; \
			fi;\
		done;\
	done;\

txt/bibl:
	@if [ ! -e txt/bibl/de ]; then \
		mkdir -p txt/bibl/de; \
		cd txt/bibl/de; \
		src=luther1912; \
		wget -nc https://raw.githubusercontent.com/acoli-repo/acoli-corpora/master/biblical/data/germ/deu_german/German.xml -O $$src.xml || echo "warning: could not retrieve" German.xml 1>&2; \
		wget -nc https://raw.githubusercontent.com/acoli-repo/acoli-corpora/master/biblical/data/germ/deu_german/LICENSE  || echo "warning: could not retrieve" LICENSE 1>&2; \
	fi;
	@if [ ! -e txt/bibl/en ]; then \
		mkdir -p txt/bibl/en; \
		cd txt/bibl/en; \
		for src in web ; do # asv_utf8; do \
			wget -nc https://raw.githubusercontent.com/acoli-repo/acoli-corpora/master/biblical/data/germ/en_modern-english/$$src.xml  || echo "warning: could not retrieve" $$src.xml 1>&2; \
			wget -nc https://raw.githubusercontent.com/acoli-repo/acoli-corpora/master/biblical/data/germ/en_modern-english/LICENSE  || echo "warning: could not retrieve" LICENSE 1>&2; \
		done;\
	fi;

	@for lang in txt/bibl/*; do \
		for xml in $$lang/*.xml; do \
			if [ ! -e txt/`basename $$lang` ] ; then mkdir -p txt/`basename $$lang`; fi; \
			basename=`basename $$lang`_`basename $$xml | cut -f 1 -d '.' | cut -f 1 -d '_'`;\
			for book in GEN PSA MAT ACT; do \
				tgt=txt/`basename $$lang`/bibl.$$basename.$$book.txt;\
				echo $$xml '>' $$tgt 1>&2; \
				cat $$xml \
				| iconv -f utf-8 -t utf-8 -c \
				| perl -pe 's/\s+/ /g; s/<seg/\n<seg/g; s/<\/seg>/\n/g; ' \
				| grep -a '<seg[^>]*id="b.'$$book \
				| perl -pe 's/<[^>]*>//g; s/<.*//g; s/.*>//g; s/ +/ /;' \
				| egrep -a . \
				> $$tgt;\
			done;\
		done; \
	done || echo 'warning: unclear return code' 1>&2

conllu: 
	if [ ! -e conllu ]; then make update-conllu; fi;

update-conllu: udpipe txt txt/bibl txt/doyle
	@LANGS="de en fr ru pt pl";\
	echo "warning: we're supporting only "$$LANGS" at the moment" 1>&2;\
	for lang in $$LANGS; do \
		for file in txt/$$lang/*.txt; do \
			if [ ! -e conllu/$$lang ]; then mkdir -p conllu/$$lang ; fi; \
			tgt=conllu/$$lang/`basename $$file | sed s/'.txt$$'//`.conllu;\
			if [ ! -e $$tgt ] ; then \
				echo $$file 1>&2; \
				cat $$file \
				| grep -v '^#' \
				| sed s/'$$'/'\n'/g \
				| udpipe/src/udpipe `find udpipe/models/$$lang/*udpipe | head` --tokenize --tag --parse --output=conllu > $$tgt;\
				echo 1>&2;\
			fi;\
		done;\
	done;\

conll-rdf:
	if [ ! -e conll-rdf ]; then \
		git clone https://github.com/acoli-repo/conll-rdf.git;\
		cd conll-rdf;\
		#./compile.sh;\
	fi;

conll-merge:
	if [ ! -e conll-merge ]; then \
		git clone https://github.com/acoli-repo/conll-merge;\
	fi;

refexp: 
	if [ ! -e refexp ]; then mkdir update-refexp; fi

update-refexp: conll-rdf
	@make conllu;\
	cd conllu;\
	for lang in */; do \
		lang=`echo $$lang | sed s/'\/'//g;`;\
		if [ ! -e ../sparql/refexp.$$lang.sparql ]; then \
			echo "warning: did not find ../sparql/refexp."$$lang.sparql, skipping $$lang 1>&2;\
		else \
			for file in `find $$lang | grep 'conllu$$'`; do \
				echo $$file 1>&2; \
				tgtdir=`dirname ../refexp/$$file`;\
				if [ ! -e $$tgtdir ]; then \
					mkdir -p $$tgtdir;\
				fi;\
				tgt=$$tgtdir/`basename $$file | sed s/'\.conll[u]?$$'//`.tsv;\
				if [ -e $$tgt ]; then echo found $$tgt, keeping it 1>&2; \
				else \
					cat $$file \
					| egrep '^# text|^[0-9][0-9]*\s|^$$' \
					| ../conll-rdf/run.sh CoNLLStreamExtractor \
						'#' \
						ID FORM LEMMA UPOS XPOS FEATS HEAD EDGE DEPS MISC \
						-u 	../sparql/refexp.$$lang.sparql \
							../sparql/gr.sparql \
					| ../conll-rdf/run.sh CoNLLRDFFormatter -conll ID FORM GR NP_TYPE REF \
					| egrep '^# text|^[0-9]|^$$' \
					| grep -B 1 -A 1 '^[0-9]' \
					| grep -v s/"^\-\-$$"// \
					| sed s/"^[0-9][0-9]*\t"// \
					| perl -pe "s/\t_/\t/g;" \
					> $$tgt; \
				fi;\
			done;\
		fi;\
	done;

	# validation
	@for file in `grep -L -P '\t' $$(find refexp | grep '.tsv$$')`; do \
		echo warning: $$file is empty 1>&2;\
		mv $$file $$file.invalid;\
	done;
	@for file in `grep -L -P 'OLD|NEW' $$(find refexp | grep '.tsv$$')`; do \
		echo warning: $$file seems not to contain pre-annotation 1>&2;\
		mv $$file $$file.invalid;\
	done;