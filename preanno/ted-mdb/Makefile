xslx:
	@cd ../..; make update-refexp;
	...

prep: pdtb
	@cd ../..; make update-conllu
	@for file in pdtb/*/*raw.txt; do \
		lang=`basename $$(dirname $$file)`;\
		conllu=../../$$lang/ted-mdb.`basename $$file | sed s/'[^0-9]'//g`.conllu;\
		if [ -e $$conllu ]; then \
			src=$$conllu;\
			tgt=`echo $$file | sed s/'raw.txt$$'//`seg.txt;\
			if [ ! -e $$tgt ]; then \
				echo $$src '>' $$tgt 1>&2;\
				egrep '#' $$conllu \
				| grep 'text' \
				| grep = \
				| cut -f 2- -d = \
				| sed -e s/'^ *'//g -e s/' *$$'//g -e s/'\s\s*'/ /g \
				| egrep .\
				> $$tgt;\
			fi;\
		fi;\
	done;

pdtb: src
	@lang_tags="German_de English_en Lithuanian_lt Polish_pl Portuguese_pt Russian_ru Turkish_tr";\
	for lang_tag in $$lang_tags; do \
		lang=`echo $$lang_tag | cut -f 1 -d _`;\
		tag=`echo $$lang_tag | cut -f 2 -d _`;\
		if [ -d src/$$lang ]; then \
			if [ ! -d pdtb/$$tag ]; then mkdir -p pdtb/$$tag; fi;\
			for src in src/$$lang/ann/01/talk_*[^a].txt; do \
				if [ -e $$src ] ; then \
					tgt=pdtb/$$tag/ted-mdb.`basename $$src | sed s/'[^0-9]'//g`.ann.txt;\
					echo $$src '>' $$tgt 1>&2;\
					cp $$src $$tgt; \
				fi;\
			done;\
			for src in src/$$lang/raw/01/talk_*[^a].txt; do \
				if [ -e $$src ] ; then \
					tgt=pdtb/$$tag/ted-mdb.`basename $$src | sed s/'[^0-9]'//g`.raw.txt;\
					echo $$src '>' $$tgt 1>&2;\
					cp $$src $$tgt; \
				fi;\
			done;\
		fi;\
	done;

src:
	if [ ! -e src ]; then \
		mkdir src; \
		git clone https://github.com/MurathanKurfali/Ted-MDB-Annotations src;\
	else \
		cd src; git pull || echo 'warning: pulling failed' 1>&2;\
	fi;

