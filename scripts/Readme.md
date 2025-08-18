# Conversion tools

## AURIS parser (with CSV output)

```
$> python3 auris.py ../annotators/team/tg/de/annotated/abcnews.199762.xlsx
```

## AURIS conversion (from Excel to different TSV formats)

TODO: revise on the basis of `auris.py`

```
$> python3 auris2tsv.py corefud ../annotators/team/tg/de/annotated/abcnews.199762.xlsx
```

Because AURIS doesn't actually contain syntax, it needs to be merged with CoNLL-U:

```
$> python3 auris2tsv.py corefud ../annotators/team/tg/de/annotated/abcnews.199762.xlsx \
	| python3 align.py 100 ../conllu/de/abcnews.199762.conllu=1 --=1 \
	| cut -f 1-9,20 \
	| sed -e s/'\(\t?\)*$'// -e s/'\t*$'//g \
	| grep -P '^[0-9#]|^$'
```

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

## Eval discourse

```
$> python3 compare-discourse.py -s ted-mdb.1971.dis.mdb.tsv -t ted-mdb.1971.dis.tg.tsv
```

## Eval coref

Note that we need to add `# global.Entity` for the CorefUD scorer.

Merge with CoNLL-U and convert annotated files to CorefUD format:

```
$> (echo "# global.Entity = eid-etype-head-other";
	python3 auris2tsv.py corefud ../annotators/team/tg/de/annotated/abcnews.199762.xlsx \
	| python3 align.py 100 ../conllu/de/abcnews.199762.conllu=1 --=1 \
	| cut -f 1-9,20 \
	| sed -e s/'\(\t?\)*$'// -e s/'\t*$'//g \
	| grep -P '^[0-9#]|^$') \
	> abcnews.199762.corefud.tg.conllu
```

As `align.py` can cope with tokenization mismatches, omissions, insertions and encoding alternatives, we can actually align it with (the syntax part of) external CorefUD files, for parcor-full, we do, however, compare with the AURIS-converted files.

Same for ParCorFull conversion

```
$> (echo "# global.Entity = eid-etype-head-other"; \
	python3 align.py 100 ../conllu/de/abcnews.199762.conllu=1 ../preanno/parcor/refexp/de/abcnews.199762.conllu.tsv=0 \
	| cut -f 1-9,18 \
	| sed -e s/'\([a-z].*\t\)$'/'\1_'/ \
			-e s/'\(\t?\)*$'// -e s/'\t*$'//g \
	| grep -P '^[0-9#]|^$' \
	| sed s/'^\(\([0-9]*\)\t.*\t\)set_\([0-9]*\)$'/'\1Entity=(e\3-entity-\2)'/) \
	> abcnews.199762.corefud.pcf.conllu
```

Then eval

```
$> python3 corefud-scorer/corefud-scorer.py abcnews.199762.corefud.pcf.conllu  abcnews.199762.corefud.tg.conllu
```

Note that ParCorFull (at least in our conversion) contains massive gaps in annotation. 