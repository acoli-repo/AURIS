SHELL=bash

all: conllu refexp

udpipe:
	if [ ! -e udpipe ]; then echo install UDPipe v.1.0 in `pwd`/udpipe 1>&2; exit 1; fi;

txt/doyle:
	@if [ ! -e txt/doyle/de ]; then \
		mkdir -p txt/doyle/de; \
		cd txt/doyle/de; \
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
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1/g;' \
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
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1/g;' \
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
			| tee tmp.html | grep -m $$chap '.'  | tail -n 1 | tee tmp$$chap.html \
			| perl -pe 's/<P/\n<P/g; s/<\/P>/\n/g;' \
			| grep -a '<P' \
			| w3m -T text/html \
			| perl -pe 's/([^\s])\-\s*\n/\1/g; s/([^\s])\n/\1/g;' \
			> $$tgt;\
		done;\
		\
	fi;

	@for lang in txt/doyle/*; do \
		for file in doyle_bask.14.txt doyle_wist.2.txt; do \
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
				| grep -a '<seg[^<]*id="b.$$book' \
				| perl -pe 's/<[^>]*>//g; s/<.*//g; s/.*>//g; s/ +/ /;' \
				| egrep -a . \
				> $$tgt;\
			done;\
		done; \
	done || echo 'warning: unclear return code' 1>&2

conllu: udpipe txt txt/bibl txt/doyle
	@LANGS="en";\
	echo "warning: we're supporting only "$$LANGS" at the moment" 1>&2;\
	for lang in $$LANGS; do \
		for file in txt/$$lang/*.txt; do \
			if [ ! -e conllu/$$lang ]; then mkdir -p conllu/$$lang ; fi; \
			echo $$file 1>&2; \
			udpipe/src/udpipe `find udpipe/models/en/english* | head` --tokenize --tag --parse --output=conllu $$file > conllu/$$lang/`basename $$file | sed s/'.txt$$'//`.conllu;\
			echo 1>&2;\
		done;\
	done;\

conll-rdf:
	if [ ! -e conll-rdf ]; then \
		git clone https://github.com/acoli-repo/conll-rdf.git;\
		cd conll-rdf;\
		#./compile.sh;\
	fi;

refexp: conllu conll-rdf
	cd conllu;\
	for lang in */; do \
		lang=`echo $$lang | sed s/'\/'//g;`;\
		for file in `find $$lang | grep 'conllu$$'`; do \
			echo $$file 1>&2; \
			tgtdir=`dirname ../refexp/$$file`;\
			if [ ! -e $$tgtdir ]; then \
				mkdir -p $$tgtdir;\
			fi;\
			cat $$file \
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
			> $$tgtdir/`basename $$file | sed s/'\.conll[u]?$$'//`.tsv; \
		done;\
	done;