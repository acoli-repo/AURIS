all: en_gum ru_rrg files.tsv

en_gum:
	git clone https://github.com/amir-zeldes/gum en_gum

ru_rrg:
	git clone --sparse https://github.com/tchewik/bilingualrsp ru_rrg;\
	cd ru_rrg;\
	git sparse-checkout set /data

files.tsv: en_gum ru_rrg
	@EN_RST=`find en_gum/rst/rstweb/ | grep '\.rs4$$' | sed -e s/'.*\/'//g -e s/'\.rs4$$'//`;\
	EN_COREF=`find en_gum/coref/gum/conll/ | grep '\.conll$$' | sed -e s/'.*\/'//g -e s/'\.conll$$'//`;\
	RU_RST=`unzip -l ru_rrg/data/RRG.zip \
			| grep RRG/ \
			| egrep '\.rs[3-9]$$' \
			| sed -e s/'.*\/'//g -e s/'\.rs[0-9]*$$'// -e s/'\_RU$$'//;`;\
	freq_file=`echo $$EN_RST $$EN_COREF $$RU_RST \
			| sed s/'\s'/'\n'/g \
			| sort \
			| uniq -c \
			| sort -rn \
			| sed s/'\s\s*'/':'/g \
			| cut -f 2- -d ':';`;\
	max_freq=`echo $$freq_file | sed s/'\s'/'\n'/g | head -n 1 | cut -f 1 -d ':'`;\
	for file in `echo $$freq_file | sed s/'\s'/'\n'/g | grep '^'$$max_freq':' | cut -f 2- -d ':' | sort -u`; do \
		echo -n $$file'	';\
		if echo $$EN_COREF | grep $$file > /dev/null; then echo -n 'en_coref	'; else echo -n "_	"; fi;\
		if echo $$EN_RST | grep $$file > /dev/null; then echo -n 'en_rst	'; else echo -n "_	"; fi;\
		if echo $$RU_RST | grep $$file > /dev/null; then echo -n 'ru_rst	'; else echo -n "_	"; fi;\
		cat en_gum/xml/$$file.xml \
		| perl -pe 's/\s+/ /g; s/</\n</g; s/>/>\n/g;' | grep '<text' -m 1 | sed s/'\s'/'\n'/g | grep sourceURL= | cut -f 2 -d '"';\
	done \
	> files.tsv

