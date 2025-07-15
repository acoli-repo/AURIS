all: xlsx

xlsx: update_xlsx

update_xlsx: # update_tsv
	#@cd ../..; make update-refexp;
	@for dir in tsv/*/; do \
		lang=`echo $$dir | cut -f 2 -d /`;\
		for discourse_tsv in $$dir/*tsv; do \
			base=`basename $$discourse_tsv | sed s/'\.pdtb\.tsv'//`;\
			ref_tsv=`echo ../../refexp/$$lang/$$base*.tsv | sed s/'\s'/'\n'/g | egrep -m 1 .`;\
			if [ -e $$ref_tsv ]; then \
				tgt=xlsx/$$lang/$$base.xlsx;\
				echo $$discourse_tsv '>' $$tgt 1>&2;\
				if [ ! -e `dirname $$tgt` ]; then mkdir -p `dirname $$tgt`; fi;\
				python3 ../../scripts/tsvs2excel.py -s $$discourse_tsv -sm ../../scripts/pdtb2auris.tsv -w $$ref_tsv $$tgt 2>&1 \
				| tee $$tgt.log 1>&2;\
				echo 1>&2;\
			fi;\
		done;\
	done;\

update_tsv: prep
	@for dir in pdtb/*/; do \
		lang=`echo $$dir | cut -f 2 -d /`;\
		for seg in $$dir/*seg.txt; do \
			base=`echo $$seg | sed s/'.seg.txt$$'//`;\
			ann=$$base.ann.txt;\
			raw=$$base.raw.txt;\
			if [ -e $$seg ]; then \
				if [ -e $$ann ]; then \
					if [ -e $$raw ]; then \
						tgt=tsv/$$lang/`basename $$base`.pdtb.tsv;\
						if [ ! -e `dirname $$tgt` ]; then mkdir -p `dirname $$tgt`; fi;\
						echo $$ann '>' $$tgt 1>&2;\
						(python3 ../../scripts/pdtb2tsv.py $$raw $$ann $$seg \
						> $$tgt) 2>&1 \
						| tee $$tgt.log 1>&2;\
						echo 1>&2;\
					fi;\
				fi;\
			fi;\
		done;\
	done;\

prep: pdtb
	@cd ../..; make update-conllu
	@for file in pdtb/*/*raw.txt; do \
		lang=`basename $$(dirname $$file)`;\
		conllu=../../conllu/$$lang/ted-mdb.`basename $$file | sed s/'[^0-9]'//g`.conllu;\
		if [ -e $$conllu ]; then \
			src=$$conllu;\
			tgt=`echo $$file | sed s/'raw.txt$$'//`seg.txt;\
			if [ ! -e $$tgt ]; then \
				echo $$src '>' $$tgt 1>&2;\
				egrep '#' $$conllu \
				| grep 'text' \
				| grep = \
				| cut -f 2- -d = \
				| sed -e s/'^ *'//g -e s/' *$$'//g -e s/'\s\s*'/' '/g \
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

