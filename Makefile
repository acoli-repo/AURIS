all: conllu refexp

udpipe:
	if [ ! -e udpipe ]; then echo install UDPipe v.1.0 in `pwd`/udpipe 1>&2; exit 1; fi;

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

conllu: udpipe txt txt/bibl
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