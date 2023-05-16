all:
	for file in terms.md format.md refexp.md coreference.md information-status.md;  do \
		#Readme.md terms.md format.md refexp.md coreference.md information-status.md; do \
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