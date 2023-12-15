all: all.docx mini.docx

all.docx:
	for file in terms.md format.md refexp.md coreference.md information-status.md topic.md appendix-comments.md appendix-preannotation.md lit.md Readme.md;  do \
		cat $$file; \
		echo;\
		echo;\
	done > all.md;
	( echo '# Table of Contents'; \
	cat all.md | egrep '^#' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat all.md;) | \
	pandoc -f markdown -t docx > all.docx

mini.docx:
	for file in terms.md format.md refexp.md coreference.md information-status.md topic.md appendix-comments.md ;  do \
		cat $$file; \
		echo;\
		echo;\
	done > mini.md;
	( echo '# Table of Contents'; \
	cat mini.md | egrep '^#' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat mini.md;) | \
	pandoc -f markdown -t docx > mini.docx
