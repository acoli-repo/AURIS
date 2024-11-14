all: conll wmt17_test/split

parcor-full:
	if [ ! -e parcor-full ]; then \
		git clone https://github.com/chardmeier/parcor-full.git;\
	fi;

conll: parcor-full
	if [ ! -e conll ]; then \
		for file in `find parcor-full | grep '.mmax$$'`; do \
			tgt=conll/`echo $$file | cut -f 2- -d '/' | sed s/'\.mmax$$'//`.conll;\
			echo $$file '>' $$tgt 1>&2;\
			tgtdir=`dirname $$tgt`;\
			if [ ! -e $$tgtdir ]; then \
				mkdir -p $$tgtdir;\
			fi;\
			python3 parcor2conll.py $$file > $$tgt;\
			echo 1>&2;\
		done;\
	fi;\
	for file in `grep -L '^[0-9]' $$(find conll | grep '\.conll$$')` \
				`grep -L -P '^[0-9]*\t[^\t]*\t.*[^_\t\n\r]' $$(find conll | grep '\.conll$$')`; do \
		if [ -e $$file ]; then \
			echo removing empty $$file 1>&2;\
			rm $$file;\
		fi;\
	done;

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