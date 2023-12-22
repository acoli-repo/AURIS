# Augsburg Manual for the Annotation of Reference and Information Structure (AURIS)

At the moment, we provide an annotation manual, only, as well as build scripts. In the longer run, we aim to develop a corpus with corresponding annotations.

AURIS is designed to build on and complement CoNLL-U corpora, and uses a CoNLL format. Moreover, it is designed to be used with conventional spreadsheet software and provides pre-annotation scripts and Excel-style formulas to facilitate annotation.

## Guidelines

- [`guidelines/`](guidelines)

## Corpus (under construction)

- [`txt/`](txt): Plain text files (input to pre-annotation)
- [`ready-for-annotation/`](ready-for-annotation/): Spreadsheet (Excel) files with pre-annotation

To add texts to the corpus, deposit them as plain text in `txt/$lang`, with `$lang` being the BCP47 identifier for your language (e.g., `en` for English) and run `make`. Note that only data from supported languages will be processed.

Spreadsheet files are built from plain text with 

	make update

(see [`Makefile`](Makefile))

Auxiliary files produced during pre-annotation

- [`conllu/`](conllu): Syntactically annotated files from `txt/` (automatically parsed, UD compliant)
- [`refexp/`](refexp): "Raw" word-level TSV/CoNLL files with automated (static) pre-annotation, input to manual annotation
- [`discourse_pre/`](discourse_pre): "Raw" sentence-level TSV files with automated (static) pre-annotation, input to manual annotation

Legacy data:

- [`is/`](is): Older manual annotations for coreference and information status, Excel format
- [`discourse_annotated/`](is): Older manual annotations for coreference and information status, Excel format

## Source data

- TED-MDB corpus (https://github.com/MurathanKurfali/Ted-MDB-Annotations), i.e., ted-mdb.1927, ted-mdb.1971, ted-mdb.1976, ted-mdb.1978, ted-mdb.2009, ted-mdb.2150
	- note that these are different TED talk ids than those from TED2020 and Teddy
- Bible: excerpts from the [ACoLi Bible Corpus](https://github.com/acoli-repo/acoli-corpora/tree/master/biblical)
- Doyle: selected pieces of Arthur Conan Doyle (also subject to [FrameNet annotations](https://framenet.icsi.berkeley.edu/fulltextIndex))  
- TODO: TED core corpus

## Complementary Material

- [Augsburg Corpus of Bootstrapped Reference and Information Structure Annotations](https://github.com/acoli-repo/AURIS-bootstrap): extrapolated from over morphosyntactic marking in selected languages
