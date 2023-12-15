SHELL=bash

all: prep compile excerpts full

prep:
	cd word-level; make
	cd sentence-level; make

compile: 
	for file in *.docx */*.docx; do \
		if [ -e $$file ]; then \
			libreoffice --headless --convert-to pdf $$file --outdir `dirname $$file`; \
		fi;\
	done

excerpts:
	for x in word sentence; do \
		pdftk $$x-level-title.pdf $$x-level/mini.pdf cat outout $$x-level-excerpt.pdf;\
		pdftk $$x-level-title.pdf $$x-level/all.pdf cat outout $$x-level.pdf;\
	done;\
