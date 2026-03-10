# Augsburg Corpus for Reference and Information Structure (AURIS)

> Note: This is the release repository. **Please do not directly push into this repository.** Active development takes place under the private repository https://github.com/acoli-repo/AURIS_internal. Please contact [@chiarcos](https://github.com/chiarcos) or the [Chair for Applied Computational Linguistics (ACoLi) at the University of Augsburg, Germany](https://www.uni-augsburg.de/de/fakultaet/philhist/professuren/angewandte-computerlinguistik/) to request access to [AURIS_internal](https://github.com/acoli-repo/AURIS_internal).

AURIS is designed to build on and complement CoNLL-U corpora, and uses a custom CoNLL format. Moreover, it is designed to be used with conventional spreadsheet software and provides pre-annotation scripts and Excel-style formulas to facilitate annotation. All AURIS texts are multilingual in the sense that we have translations into 5-70 different languages. Release v.01 comprises the German subset, only.

## TODO

- [ ] create an initial release
- [ ] check version number ! (guidelines are v0.2!) what does the paper say?
- [ ] guidelines
- [ ] integrate as subtree into AURIS_internal
- [ ] synchronize with AURIS_internal
- [ ] routine to update from AURIS_internal
- [ ] cleanse and sync scripts/ and Makefile
- [ ] cleanse and sync conllu/
- [ ] cleanse txt/
- [ ] LICENSE
- [ ] make public

## Content 

- Guidelines: [guidelines`](guidelines)
- Release data
	- [`v.01`](v.01) AURIS v.01, 2025-03-06
		- German subset only, coref and discourse
- External evaluation data
	- [`eval/ted-mdb/`](eval/ted-mdb) TED-MDB data, converted to AURIS formats
	- [`eval/parcorfull/`](eval/parcorfull) ParCorFull data, News subsection, converted to AURIS formats

Data folders adopt the following organization:

- first level: corpus/release, e.g., [`v.01/`](v.01/), [`eval/ted-mdb/`](eval/ted-mdb), [`eval/parcorfull/`](eval/parcorfull)
- second level: language, e.g., `de` for German ([`v.01/de`](v.01/de), [`eval/ted-mdb/de`](eval/ted-mdb/de), etc.)
- third level: format, i.e., `disc` and `coref` for native TSV formats for discourse and coreference annotations, `corefud` for CorefUD, `xlsx` for the native spreadsheet format (identical to `disc` and `coref` in content)
- fourth (and deeper) levels: directories that represent different sources of information

## Source data

ACoLi is designed to complement and enrich existing annotations. It overlaps (and builds on) the following corpora, but provides original annotations (except for the data under `eval/`)

- TED-MDB corpus (https://github.com/MurathanKurfali/Ted-MDB-Annotations), i.e., ted-mdb.1927, ted-mdb.1971, ted-mdb.1976, ted-mdb.1978, ted-mdb.2009, ted-mdb.2150
- ParCor-News: News texts from WMT17

