all:
	for file in Readme.md terms.md refexp.md coreference.md information-status.md; do \
		cat $$file; \
		echo;\
	done > all.md;
	(cat all.md | egrep '^#' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat all.md;) | \
	pandoc -f markdown -t docx > all.docx