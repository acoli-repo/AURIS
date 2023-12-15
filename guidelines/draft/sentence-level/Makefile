all:
	FILES="discourse.md";\
	for file in $$FILES;  do \
		cat $$file; \
		echo;\
		echo;\
	done |\
	( echo '# Table of Contents'; \
	cat all.md | egrep '^#' | egrep '[0-9]' | \
	sed -e s/'#\s'/'- '/g \
		-e s/'#'/'\t'/g; \
	echo;\
	cat $$FILES;\
	) | \
	pandoc -f markdown -t html > all.html