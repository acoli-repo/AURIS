all: coref.log ted-mdb.log

ted-mdb:
	@if [ ! -e ted-mdb ]; then \
		cd ../../preanno/ted-mdb/; \
		make;\
		cd -;\
		echo 1>&2;\
		mkdir ted-mdb;\
		for file in `find ../../preanno/ted-mdb/ | grep '\.xlsx$$'`; do \
			lang=`echo $$file | cut -f 5 -d /`;\
			auris=`find ../*/$$lang/disc/ 2>/dev/null | grep $$(basename $$file | sed s/'\.xlsx$$'//).tsv'$$' | egrep -m 1 .` ;\
			if echo $$auris | egrep . >/dev/null; then \
				if [ -e $$auris ]; then \
					tgt=ted-mdb/$$lang/disc/$$(basename $$file | sed s/'\.xlsx$$'//).tsv;\
					if [ ! -e `dirname $$tgt` ]; then mkdir -p `dirname $$tgt`; fi;\
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
			fi;\
		done;\
	fi;\

ted-mdb.log: ted-mdb
	@for version in ../v*; do \
		SRC=""; TGT="";\
		for file in `find $$version/*/disc/ | grep '\.tsv$$'`; do \
			if [ -e $$file ]; then \
				lang=`echo $$file | cut -f 3 -d /`;\
				ted_mdb=`find ted-mdb/$$lang/ 2>/dev/null | grep -m 1 $$(basename $$file)'$$'`;\
				if echo $$ted_mdb | egrep .>/dev/null; then \
					if [ -e $$ted_mdb ]; then \
						SRC=$$SRC' '$$file;\
						TGT=$$TGT' '$$ted_mdb;\
						echo eval $$file $$ted_mdb 1>&2;\
						echo eval $$file $$ted_mdb | sed s/'.'/'='/g 1>&2;\
						echo;\
						python3 ../../../scripts/compare-discourse.py -s $$file -t $$ted_mdb --id_col 0 --tgt_col 3 --rel_col 4 1>&2;\
						echo 1>&2;\
						echo 1>&2;\
					fi;\
				fi;\
			fi;\
		done;\
		echo eval $$version ted_mdb 1>&2;\
		echo eval $$version ted_mdb | sed s/'.'/'='/g 1>&2;\
		echo;\
		python3 ../../../scripts/compare-discourse.py -s $$SRC -t $$TGT --id_col 0 --tgt_col 3 --rel_col 4 1>&2;\
		echo 1>&2;\
		echo 1>&2;\
	done 2>&1 \
	| tee ted-mdb.log 1>&2;


parcorfull:
	@for file in `find ../v*/*/corefud/ | grep '\.conllu$$'`; do \
		if [ -e $$file ]; then \
			lang=`echo $$file | cut -f 3 -d /`;\
			pcf=../../../preanno/parcor/refexp/$$lang/`basename $$file`;\
			if [ ! -e $$pcf ]; then pcf=../../../preanno/parcor/refexp/$$lang/`basename $$file`.tsv; fi;\
			if [ -e $$pcf ]; then \
				conll=../../../conllu/$$lang/`basename $$file`;\
				tgt=parcorfull/$$lang/corefud/`basename $$file`;\
				if [ ! -e $$tgt ]; then \
					if [ ! -e $$conll ]; then \
						echo "error: did not find "$$conll", skipping "$$pcf 1>&2;\
					else \
						echo $$pcf '+' $$conll '>' $$tgt 1>&2;\
						if [ ! -e `dirname $$tgt` ]; then mkdir -p `dirname $$tgt`; fi;\
						(echo "# global.Entity = eid-etype-head-other"; \
						 python3 ../../../scripts/align.py 100 $$conll=1 $$pcf=0 \
				         | cut -f 1-9,18 \
				         | sed -e s/'\([a-z].*\t\)$$'/'\1_'/ \
				               -e s/'\(\t?\)*$$'// -e s/'\t*$$'//g \
				         | grep -P '^[0-9#]|^$$' \
				         | sed s/'^\(\([0-9]*\)\t.*\t\)set_\([0-9]*\)$$'/'\1Entity=(e\3-entity-\2)'/\
				       ) > $$tgt;\
				    fi;\
				fi;\
			fi;\
		fi;\
	done 2>&1 \
	| tee parcorfull.log 1>&2;\
	echo 1>&2;\

coref.log: parcorfull
	@tmp=tmp;\
	if [ -e $$tmp ]; then \
		echo "warning: skipping eval, please remove directory "`pwd`/$$tmp" to resume" 1>&2;\
		exit 1;\
	fi;\
	\
	# eval coref \
	mkdir -p $$tmp;\
	for lang in parcorfull/*/; do \
		lang=`echo $$lang | cut -f 2 -d /`;\
		files=`find parcorfull/$$lang | grep 'conllu$$' | sed s/'.*\/'//g | sort -u`;\
		for file in $$files; do \
			pcf=`find parcorfull/$$lang | grep -m 1 $$file`;\
			for release in ../v*/; do \
				auris=`find $$release$$lang/corefud | grep -m 1 $$file`;\
				release=`echo $$release | cut -f 2 -d /`;\
				cat $$auris >> $$tmp/$$release.conllu;\
				echo >> $$tmp/$$release.conllu;\
				echo >> $$tmp/$$release.conllu;\
				\
				echo eval $$auris 1>&2;\
				python3 ../../../scripts/corefud-scorer/corefud-scorer.py $$pcf $$auris 1>&2;\
				echo 1>&2;\
			done;\
			cat $$pcf >> $$tmp/pcf.conllu;\
			echo >> $$tmp/pcf.conllu;\
			echo >> $$tmp/pcf.conllu;\
		done;\
	done;\
	for release in $$tmp/v*conllu; do \
		echo eval $$release 1>&2;\
		python3 ../../../scripts/corefud-scorer/corefud-scorer.py $$tmp/pcf.conllu $$release 1>&2;\
		echo 1>&2;\
	done 2>&1 | \
	tee coref.log;\
	rm -rf $$tmp;\
