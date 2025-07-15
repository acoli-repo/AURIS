all:
	#cd ../../../preanno/ted-mdb; make
	@for file in ../../../preanno/ted-mdb/*/*/*.xlsx; do \
		if [ -e $$file ]; then \
			lang=`basename $$(dirname $$file)`;\
			echo $$file $$lang;\
			tgt=$$lang/annotated/`basename $$file`;\
			if [ ! -e $$tgt ]; then \
				if [ ! -e `dirname $$tgt` ]; then mkdir -p `dirname $$tgt`; fi;\
				echo $$file '>' $$tgt 1>&2;\
				cp $$file $$tgt;\
			fi;\
		fi;\
	done;