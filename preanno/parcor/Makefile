SHELL=bash

all: conll wmt17_test/split

parcor-full:
	if [ ! -e parcor-full ]; then \
		git clone https://github.com/chardmeier/parcor-full.git;\
	fi;

conllu: conll ../../conllu
	for file in `find conll | egrep '\.conll$$'`; do \
		src=../../conllu/`echo $$file | cut -f 2- -d /`u;\
		if [ -e $$src ]; then \
			tgt=`echo $$src | cut -f 3- -d '/'`;\
			tgtdir=`dirname $$tgt`;\
			if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi;\
			echo $$src '>' $$tgt 1>&2;\
			cp $$src $$tgt; \
		else \
			echo 1>&2;\
			echo warning: Did not find $$src, skipping $$file 1>&2;\
			echo 1>&2;\
		fi;\
	done;

../../conll-rdf:
	@cd ../..; make conll-rdf

../../conll-merge:
	@cd ../..; make conll-merge

../../refexp:
	@cd ../..; make refexp

refexp: conllu conll ../../refexp ../../conll-rdf ../../conll-merge
	@for conllu in `find conllu | egrep '\.conllu$$'`; do \
		conll=conll/`echo $$conllu | cut -f 2- -d / | sed s/'\.conllu'//`.conll;\
		refexp=../../refexp/`echo $$conllu | cut -f 2- -d /`.tsv;\
		if [ ! -e $$refexp ]; then \
			echo 1>&2;\
			echo warning: Did not find $$refexp, skipping $$conllu 1>&2;\
			echo 1>&2;\
		else \
			if [ ! -e $$conll ]; then \
				echo 1>&2;\
				echo warning: Did not find $$conll, skipping $$conllu 1>&2;\
				echo 1>&2;\
			else \
				tgt=`echo $$refexp | cut -f 3- -d /`;\
				tgtdir=`dirname $$tgt`;\
				if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi;\
				echo $$conllu '+' $$conll '>' $$tgt 1>&2;\
				# JAVA CoNLL-Merge works nicely, but sometimes creates locks and then stops \
				# conll-merge $$conllu $$conll 1 1 -f\
				echo python3 ../../conll-merge/experimental/align.py 500 $$conllu'=1' $$conll'=1' 1>&2;\
				python3 ../../conll-merge/experimental/align.py 500 $$conllu'=1' $$conll'=1' \
				| tee $$tgt.1.merged \
				| grep -v '^?' \
				| sed s/'\t[?]'/'\t_'/g \
				| sed s/'"'/"''"/g \
				| egrep '^[0-9]' \
				| sed s/'^1\s'/'\n\n&'/g \
				| tee $$tgt.2.pruned \
         		| ../../conll-rdf/run.sh CoNLLStreamExtractor \
                                         '#' \
                                         ID FORM LEMMA UPOS XPOS FEATS HEAD EDGE DEPS MISC \
                                         `egrep -v ':' $$conll | egrep -m 1 '#' | cut -f 2- -d '#'` \
                                         -u conll2auris_coref.sparql \
                | grep -v "ERROR org.apache.jena.riot" \
                | tee $$tgt.3.ttl \
                | ../../conll-rdf/run.sh CoNLLRDFFormatter \
                	-conll ID FORM coref_coref_class \
                | grep -v '#' \
                > $$tgt.4.unmerged; \
                # | conll-merge $$refexp -- 0 1 \
                echo python3 ../../conll-merge/experimental/align.py 500 $$refexp=0 $$tgt.4.unmerged=1 1>&2;\
                python3 ../../conll-merge/experimental/align.py 500 $$refexp=0 $$tgt.4.unmerged=1 \
                | sed s/'\t[?]'/'\t'/g \
                | tee $$tgt;\
                if egrep -m 1 'OLD|NEW' $$tgt >/dev/null; then \
                	if egrep -m 1 'set_' $$tgt > /dev/null; then \
                		rm $$tgt.*;\
                	else \
                		echo '  warning: '$$tgt contains no ParCor markables 1>&2;\
                	fi;\
                else \
                	echo '  warning: '$$tgt contains no AURIS pre-annotation 1>&2;\
                fi;\
			fi;\
		fi;\
	done;

conll: parcor-full
	@if [ ! -e conll ]; then \
		for file in `find parcor-full | grep '.mmax$$'`; do \
			tgt=conll/`echo $$file | cut -f 2- -d '/' | sed s/'\.mmax$$'//`.conll;\
			echo $$file '>' $$tgt 1>&2;\
			tgtdir=`dirname $$tgt`;\
			if [ ! -e $$tgtdir ]; then \
				mkdir -p $$tgtdir;\
			fi;\
			(python3 parcor2conll.py $$file > $$tgt) 2>&1 | sed s/'^'/'  '/;\
		done;\
	fi;\
	for file in `grep -L '^[0-9]' $$(find conll | grep '\.conll$$')` \
				`grep -L -P '^[0-9]*\t[^\t]*\t.*[^_\t\n\r]' $$(find conll | grep '\.conll$$')`; do \
		if [ -e $$file ]; then \
			echo removing empty $$file 1>&2;\
			rm $$file;\
		fi;\
	done;\
	for file in `find conll/damaged | grep 'conll$$'`; do \
		tgt=conll/corpus/`echo $$file | cut -f 3- -d /`;\
		tgtdir=`dirname $$tgt`;\
		if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi;\
		echo $$file '>' $$tgt 1>&2;\
		mv $$file $$tgt;\
	done;\
	rm -rf conll/damaged conll/inter-anno-PT;\

	# restructuring
	@langs=`find conll | egrep '\.conll$$' | cut -f 4 -d / | sort -u | sed s/'.*'/'\L&'/g`;\
	for lang in $$langs; do \
		if [ ! -e conll/$$lang ]; then \
			mkdir -p conll/$$lang;\
		fi;\
	done;\

	# renaming
	@for dir in `cut -f 1 parcor2auris.tsv | sed s/'^'/'conll\/'/`; do \
		if [ -e $$dir ]; then \
			for subdir in $$dir/*; do \
				lang=`echo $$subdir | cut -f 4 -d / | sed s/'.*'/'\L&'/ | sort -u`;\
				for src_tgt in `sed s/'^'/'conll\/'/g parcor2auris.tsv | egrep $$dir  | cut -f 2,3 | sed s/'\t'/'>'/;`; do \
					 src=$$subdir/`echo $$src_tgt | cut -f 1 -d '>'`.conll;\
					 tgt=conll/$$lang/`echo $$src_tgt | cut -f 2 -d '>'`.conll;\
					 if [ -e $$src ]; then \
					 	echo $$src '>' $$tgt 1>&2; \
					 	sed '1s/^/# orig: parcor, '`echo $$src | cut -f 2- -d '/' | cut -f 1 -d . | sed s/'\/'/'\\\\\/'/g`'\n\n'/ \
					 		$$src > $$tgt;\
					 	rm $$src;\
					 	rmdir `dirname $$src` 2>/dev/null || echo > /dev/null;\
					fi;\
				done;\
				rmdir `dirname $$subdir` 2>/dev/null || echo > /dev/null;\
			done;\
		fi;\
		rmdir `dirname $$dir` 2>/dev/null || echo > /dev/null;\
	done;\


wmt17_test/split: wmt17_test/test
	if [ ! -e wmt17_test/split ]; then mkdir wmt17_test/split; fi
	for file in `find test | grep 'sgm$$'`; do \
		python3 split-wmt.py $$file wmt17_test/split/; \
	done;\

wmt17_test/test:
	if [ ! -e wmt17_test/ ]; then mkdir wmt17_test/; fi;
	if [ ! -e wmt17_test/test ]; then \
		cd wmt17_test/;\
		wget -nc http://data.statmt.org/wmt17/translation-task/test.tgz;\
		tar -xvf test.tgz;\
	fi;

update_txt_w_news: parcor-full-news-source
	#if [ ! -e news_txt ]; then \
	#	mkdir news_txt;\
	#fi;\

	for basename in \
		abcnews.199762  an-online.de.224441  ard.27823  augsburger-allgemeine.de.44740  bbc.242334  \
		bbc.242405  bbc.242418  bbc.242436  bbc.242497  braunschweiger-zeitung.de.48722  \
		brisbanetimes.com.au.130272  cbsnews.146232  cbsnews.146237  cbsnews.146271  cbsnews.146291  \
		cbsnews.146310  cnn.167026  dailymail.co.uk.170661  dailymail.co.uk.170665 ; do \
		for file in `find parcor-full-news-source | grep $$basename`; do \
			lang=`echo $$file | cut -f 3 -d '/'`;\
			tgtdir=../../txt/$$lang; \
			if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi; \
			if [ ! -e $$tgtdir ]; then mkdir -p $$tgtdir; fi;\
			cp $$file $$tgtdir/`basename $$file`;\
		done;\
	done;
