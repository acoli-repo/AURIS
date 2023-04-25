all: conllu

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

