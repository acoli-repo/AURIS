all: split

split: test
	if [ ! -e split ]; then mkdir split; fi
	for file in `find test | grep 'sgm$$'`; do \
		python3 split-wmt.py $$file split/; \
	done;\

test:
	if [ ! -e test ]; then \
		wget -nc http://data.statmt.org/wmt17/translation-task/test.tgz;\
		tar -xvf test.tgz;\
	fi;
