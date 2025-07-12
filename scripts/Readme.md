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