all: givenness.json

givenness.json:
	if [ ! -e givenness.json ]; then \
		python3 annotate-givenness.py > givenness.json;\
	fi;
