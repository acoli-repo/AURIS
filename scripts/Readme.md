# Conversion tools

- `tsvs2excel.py` main libary, converts pre-annotations in TSV to Excel spreadsheet

	expected input format for sentence-level annotations:
	
	- SENTENCE_ID
	- PREDICATE_ID (or "_")
	- MARKER_CANDIDATE (or "_")
	- PREDICATE (or "_")
	- TEXT
	- URL (or "_", optional)
	- TARGET (optional, from pre-annotation)
	- RELATION (optional, from pre-annotation)

- `rst2tsv.py` converts RST annotations to sentence-level TSV pre-annotation. This is based on the strict nuclearity principle and the the head-first interpretation for multi-nuclears. Note that it keeps the original relation labels.

- `txt2rst.py` create pre-split RS3 files from text

		- e.g., from stdin: take CoNLL-U file, extract '# text' content

- `align.py` from https://github.com/acoli-repo/conll-merge, version of 2024-07-12
	- for aligning TSV files with one-word-per-line (aka "CoNLL") annotations

TODOS:

- `pdtb2tsv.py` to convert annotations created with the PDTB Annotator (Liu et al. 2016, https://aclanthology.org/C16-2026.pdf)
- add optional mapping table to `rst2tsv.py` and `pdtb2tsv.py`
- add optional reference segmentation to `rst2tsv.py` and `pdtb2tsv.py`

Example call

```
$> egrep '# text =' rotkaeppchen_khm-026_grimm.conllu \
   | cut -f 2 -d '=' \
   | python3 txt2rs3.py \
   > rotkaeppchen_khm-026_grimm_schema_test.rs3
$> rsttool rotkaeppchen_khm-026_grimm_schema_test.rs3 # do some annotation
$> python3 rst2tsv.py rotkaeppchen_khm-026_grimm_schema_test.rs3 \
   > rotkaeppchen_khm-026_grimm_schema_test.tsv
$> python3 tsvs2excel.py -s rotkaeppchen_khm-026_grimm_schema_test.tsv rotkaeppchen_khm-026_grimm_schema_test.xslx
```