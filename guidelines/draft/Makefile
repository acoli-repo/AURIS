SHELL=bash

all: prep compile pdf

prep:
	cd word-level; make
	cd sentence-level; make

compile: 
	for file in *.docx */*.docx; do \
		if [ -e $$file ]; then \
			libreoffice --headless --convert-to pdf $$file --outdir `dirname $$file`; \
		fi;\
	done

pdf:
	@# unfortunately, this fails because pdftk uses an outdated version of iText
	@for x in word sentence; do \
		pdftk $$x-level-title.pdf $$x-level/mini.pdf cat outout $$x-level-excerpt.pdf || echo $$x-level-excerpt.pdf failed 1>&2;\
		pdftk $$x-level-title.pdf $$x-level/all.pdf cat outout $$x-level.pdf || echo $$x-level.pdf failed 1>&2;\
	done;\
