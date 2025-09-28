# build different output formats from xslx sources

all: 
	@make disc corefud paula 2>&1 \
	 | tee make.log 1>&2

refresh:
	@for dir in */disc/ */corefud; do \
		if [ -e $$dir ]; then rm -rf $$dir; fi;\
	done;\
	make all

disc: update_disc

corefud: update_corefud

check_xlsx:
	@echo 1>&2;\
	 echo files to be processed: 1>&2;\
	 for dir in */xlsx/; do \
		if [ ! -e $$dir ] ; then \
			echo 'ERROR: please deposit AURIS xslx files under '`pwd`'$$$$LANG/xlsx/' 1>&2;\
			echo 1>&2;\
			exit 1;\
		fi;\
		freq=`find $$dir | egrep '\.xlsx$$' | wc -l`;\
		if [ $$freq -gt 0 ]; then \
			echo '	'$$dir'	'$$freq'	('`find $$dir | egrep '\.xlsx$$' | cut -f 3 -d / | sort -u`')' 1>&2;\
		fi;\
	 done;\
	 echo 1>&2;\

update_disc: check_xlsx
	@for file in `find */xlsx/ | egrep '\.xlsx$$'`; do \
		if [ -e $$file ]; then \
			dir=`dirname $$file | cut -f 1 -d /`/disc/`dirname $$file | cut -f 3- -d /`;\
			if [ ! -e $$dir ]; then mkdir -p $$dir; fi;\
			tgt=$$dir/`basename $$file | sed s/'\.xlsx$$'//`.tsv;\
			echo -n $$file '>' $$tgt' ' 1>&2;\
			if [ -e $$tgt ]; then \
				echo found 1>&2;\
			else \
				python3 ../../../scripts/auris2tsv.py tsv $$file \
				| cut -f 1,5,7-9 \
				| egrep '.' \
				> $$tgt;\
				echo 'ok ('`cat $$tgt | egrep '^[0-9]' | wc -l`' utterances)' 1>&2;\
			fi;\
		fi;\
	done;\
	echo 1>&2;\

update_corefud: check_xlsx
	@for file in `find */xlsx/ | egrep '\.xlsx$$'`; do \
		if [ -e $$file ]; then \
			lang=`dirname $$file | cut -f 1 -d /`;\
			ud=`find ../../../conllu/$$lang/ | egrep -m 1 $$(basename $$file | sed s/'\.xlsx$$'//).conllu'$$'` ;\
			if [ ! -e $$ud ]; then \
				echo ERROR: Could not find CoNLL-U annotations for $$file in $$ud 1>&2;\
			else \
				dir=`dirname $$file | cut -f 1 -d /`/corefud/`dirname $$file | cut -f 3- -d /`;\
				if [ ! -e $$dir ]; then mkdir -p $$dir; fi;\
				tgt=$$dir/`basename $$file | sed s/'\.xlsx$$'//`.conllu;\
				echo -n $$file'+'$$ud '>' $$tgt' ' 1>&2;\
				if [ -e $$tgt ]; then \
					echo found 1>&2;\
				else \
					python3 ../../../scripts/auris2tsv.py corefud $$file \
					| python3 ../../../scripts/align.py 100 $$ud=1 --=1 \
					| perl -pe 's/[\t\?]*$$/\1/g; s/^[\t\?]*$$//g;'\
					| cut -f 1-10,20 \
					| perl -pe 's/\t([^\t]*)$$/|\1/g; s/_\|//g; s/\|_//g;'\
					> $$tgt;\
					echo 'ok ('`cat $$tgt | egrep '^[0-9]' | wc -l`' tokens, '`cat $$tgt | egrep '^[*]' | wc -l` alignment errors')' 1>&2;\
				fi;\
			fi;\
		fi;\
	done;\
	echo 1>&2;\

paula: update_paula

update_paula: check_xlsx
	@for file in `find */xlsx/ | egrep '\.xlsx$$'`; do \
	 	if [ -e $$file ]; then \
			lang=`dirname $$file | cut -f 1 -d /`;\
			ud=`find ../../../conllu/$$lang/ | egrep -m 1 $$(basename $$file | sed s/'\.xlsx$$'//).conllu'$$'` ;\
			if [ ! -e $$ud ]; then \
				echo ERROR: Could not find CoNLL-U annotations for $$file in $$ud 1>&2;\
			else \
				dir=`dirname $$file | cut -f 1 -d /`/paula/`dirname $$file | cut -f 3- -d /`;\
				if [ ! -e $$dir ]; then mkdir -p $$dir; fi;\
				tgt=$$dir/`basename $$file | sed s/'\.xlsx$$'//`;\
				echo -n $$file'+'$$ud '>' $$tgt' ' 1>&2;\
				if [ -e $$tgt ]; then \
					echo found 1>&2;\
				else \
					python3 ../../../scripts/auris2paula.py -c $$ud $$file $$tgt $$lang; \
					find $$tgt | grep '\.xml' | wc -l | sed s/'$$'/' files'/ 1>&2;\
				fi;\
			fi;\
		fi;\
	done;\
	echo 1>&2;
