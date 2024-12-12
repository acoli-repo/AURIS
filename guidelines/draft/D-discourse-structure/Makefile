all:
	FILES="discourse.md appendix-mapping.md bib.md";\
	for file in $$FILES;  do \
		cat $$file; \
		echo;\
		echo;\
	done > all.md;\
	( echo '# Table of Contents'; \
	cat all.md | egrep '^#' | egrep '[0-9]' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat $$FILES;\
	) | \
	pandoc -f markdown -o all.docx

	FILES="discourse.md";\
	for file in $$FILES;  do \
		cat $$file; \
		echo;\
		echo;\
	done > mini.md;\
	( echo '# Table of Contents'; \
	cat mini.md | egrep '^#' | egrep '[0-9]' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat $$FILES;\
	) | \
	pandoc -f markdown -o mini.docx