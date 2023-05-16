# Augsburg Manual for the Annotation of Reference and Information Structure (AURIS)

At the moment, we provide an annotation manual, only, as well as build scripts. In the longer run, we aim to develop a corpus with corresponding annotations.

AURIS is designed to build on and complement CoNLL-U corpora, and uses a CoNLL format. Moreover, it is designed to be used with conventional spreadsheet software and provides pre-annotation scripts and Excel-style formulas to facilitate annotation.

## Guidelines

- [`guidelines/`](guidelines)

## Corpus (under construction)

- [`txt/`](txt): Plain text files (input to pre-annotation)
- [`conllu/`](conllu): Syntactically annotated files from `txt/` (automatically parsed, UD compliant)
- [`refexp/`](refexp): "Raw" files with automated (static) pre-annotation, input to manual annotation
- [`template.xlsx`](template.xlsx): Excel template, includes formulas for dynamic pre-annotation

Pre-annotated ("raw") files can be built from plain text with `make` (see [`Makefile`](Makefile)).

## Source data

- TED-MDB corpus (https://github.com/MurathanKurfali/Ted-MDB-Annotations), i.e., ted-mdb.1927, ted-mdb.1971, ted-mdb.1976, ted-mdb.1978, ted-mdb.2009, ted-mdb.2150
	- note that these are different TED talk ids than those from TED2020 and Teddy
- TODO: TED core corpus
