# Preannotations derived from external corpora

## `parcor_coref` (Coreference preannotation derived from ParCor corpus)

	**DISCLAIMER**:
	This is not a full annotation, but limited to the top entities per text. Can be used for assessing annotator skills, though. 
	DO NOT DIRECTLY USE AS PART OF CORPUS.

	See [../../preanno/parcor](../../preanno/parcor), also for attribution.

	- The `raw/` files in this directory are just copies from `../../ready-for-annotation`
		- To be manually transferred into `annotated/`
	- The `annotated/` files in this directory are created by copying and pasting the `COREF` column from `../../preanno/parcor/refexp`, *not the full text* 
		- It seems this is not always complete, and also that head reduction was not always successful. Both is likely due to alignment errors.
	- This is coreference annotation only, no discourse, no REF, IS, CB.
	- They don't seem to have annotated first and second person, and maybe not even all referents.
	- They annotated spans, head reduction was conducted automatically.
		- Merging with automated pre-annotations was done automatically, mis-alignment is not impossible.
	- We did not correct parser errors.
	- We don't have a refexp extractor for Portuguese, yet, hence not included.
	- There are multiple annotations for two Portuguese files, not included here (should be "annotator" `pt2/`)
	- Naming schema of files is corrected to comply with Teddy corpus, resp. WMT.

	This data is to be verified, but can serve as a basis for manual verification. After verification, a `final/` folder is to be created.

## `ted-mdb` (Discourse preannotation derived from TED-MDB)

This is automatically converted from TED-MDB, and morphed to CoNLL sentence splits. As a result, some relations are lost.
Note that this annotation is not complete in the sense of AURIS, because not every segment is annotated.

With running `ted-mdb/Makefile`, the TED-MDB files are copied from [../preanno/ted-mdb](../preanno/ted-mdb).