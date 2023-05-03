all: conllu refexp

udpipe:
	if [ ! -e udpipe ]; then echo install UDPipe v.1.0 in `pwd`/udpipe 1>&2; exit 1; fi;

conllu: udpipe txt
	LANGS="en";\
	echo "warning: we're supporting only "$$LANGS" at the moment" 1>&2;\
	for lang in $$LANGS; do \
		for file in txt/$$lang/*.txt; do \
			if [ ! -e conllu/$$lang ]; then mkdir -p conllu/$$lang ; fi; \
			echo $$file 1>&2; \
			udpipe/src/udpipe `find udpipe/models/en/english* | head` --tokenize --tag --parse --output=conllu $$file > conllu/$$lang/`basename $$file | sed s/'.txt$$'//`.conllu;\
			echo 1>&2;\
		done;\
	done;

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
			| ../conll-rdf/run.sh CoNLLRDFFormatter -conll ID FORM GR REF_EXP REF \
			| egrep '^# text|^[0-9]|^$$' \
			| grep -B 1 -A 1 '^[0-9]' \
			| grep -v s/"^\-\-$$"// \
			| sed s/"^[0-9][0-9]*\t"// \
			| perl -pe "s/\t_/\t/g;" \
			> $$tgtdir/`basename $$file | sed s/'\.conll[u]?$$'//`.tsv; \
		done;\
	done;