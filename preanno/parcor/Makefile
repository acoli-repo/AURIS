all: wmt17_test/split

parcor-full:
	if [ ! -e parcor-full ]; then \
		git clone https://github.com/chardmeier/parcor-full.git;\
	fi;

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
