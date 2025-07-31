# Conversion tools

## Excel generation

- `tsvs2excel.py` main libary, converts pre-annotations in TSV to Excel spreadsheet, if a mapping table is provided with (`-sm`), we map discourse relations and transformation errors

	expected input format for sentence-level annotations:
	
	- SENTENCE_ID
	- PREDICATE_ID (or "_")
	- MARKER_CANDIDATE (or "_")
	- PREDICATE (or "_")
	- TEXT
	- URL (or "_", optional)
	- TARGET (optional, from pre-annotation)
	- RELATION (optional, from pre-annotation)


## RST conversion

- `rst2tsv.py` converts RST annotations to sentence-level TSV pre-annotation. This is based on the strict nuclearity principle and the the head-first interpretation for multi-nuclears. Note that it keeps the original relation labels.

- `txt2rst.py` create pre-split RS3 files from text

	- e.g., from stdin: take CoNLL-U file, extract '# text' content

Example calls

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

- **TODO**
	
	- add optional reference segmentation to `rst2tsv.py`
	- cf. `align.py` from https://github.com/acoli-repo/conll-merge, version of 2024-07-12
		- for aligning TSV files with one-word-per-line (aka "CoNLL") annotations

## PDTB workflow

We don't annotate PDTB, we only convert existing data.

- `pdtb2tsv.py` to convert annotations created with the PDTB Annotator (Liu et al. 2016, https://aclanthology.org/C16-2026.pdf)
	
	- note: requires edu segmentation, otherwise, falls back to \n-segmentation of base text (typically paragraphs!)
	- for segment alignment, we align with the longest (and, if ambiguous, the first) overlapping segment from the external segmentation

Example call with mapping from TED-MDB

```
$> python3 pdtb2tsv.py ted-mdb-1927.raw.txt ted-mdb-1927.ann.txt ted-mdb-1927.seg.txt  > ted-mdb-1927.tsv 2> text-msdb-1927.log
$> python3 tsvs2excel.py -s ted-mdb-1927.tsv -sm pdtb2auris.tsv ted-mdb-1927.xlsx
```

- **TODO**

	- add optional reference segmentation to `pdtb2tsv.py`
	- perform actual alignment (we align heuristically only, without checking overlapping characters)
	- cf. `align.py` from https://github.com/acoli-repo/conll-merge, version of 2024-07-12
		- for aligning TSV files with one-word-per-line (aka "CoNLL") annotations


