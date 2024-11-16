# Augsburg Manual for the Annotation of Reference and Information Structure (AURIS)

At the moment, we provide an annotation manual, only, as well as build scripts. In the longer run, we aim to develop a corpus with corresponding annotations.

AURIS is designed to build on and complement CoNLL-U corpora, and uses a CoNLL format. Moreover, it is designed to be used with conventional spreadsheet software and provides pre-annotation scripts and Excel-style formulas to facilitate annotation.

## Guidelines

- [`guidelines/`](guidelines)
- [annotated sample file (for both sentence-level and word-level annotations)](annotators/teddy-4929.example.xlsx), [log file](annotators/teddy-4929.example.log)

## Corpus (under construction)

- [`txt/`](txt): Plain text files (input to pre-annotation)
- [`ready-for-annotation/`](ready-for-annotation/): Spreadsheet (Excel) files with pre-annotation
- [`annotators/`](annotators/): annotations by individual annotators, and their reports/logs. Note that this data is heterogeneous
- [`release/`](release/) [**NOT YET**]: directory that should contain consolidated annotations. This is the consolidated output from `annotators/`.

### For annotators

For the language `LANG` (say, English, i.e., `en`) you are working with, create a directory with your acronym (e.g., your initials) under `annotators/LANG/ACRONYM` (e.g., `annotators/en/xy`). Copy selected spreadsheets from `ready-for-annotation/LANG` into this directory, perform annotations. Also put your notes (logs) there. Please mark whether and if your annotations are complete.

### For text providers

- To add texts to the corpus, deposit them as plain text in `txt/$lang`, with `$lang` being the BCP47 identifier for your language (e.g., `en` for English) and run `make`. Note that only data from supported languages will be processed.

- Spreadsheet files are built from plain text with 

		make update

	(see [`Makefile`](Makefile))

Auxiliary files produced during pre-annotation

- [`conllu/`](conllu): Syntactically annotated files from `txt/` (automatically parsed, UD compliant)
- [`refexp/`](refexp): "Raw" word-level TSV/CoNLL files with automated (static) pre-annotation, input to manual annotation
- [`discourse_pre/`](discourse_pre): "Raw" sentence-level TSV files with automated (static) pre-annotation, input to manual annotation

Legacy data:

- [`is/`](is): Older manual annotations for coreference and information status, Excel format
- [`discourse_annotated/`](is): Older manual annotations for coreference and information status, Excel format

### For developers

- For adding new languages / data in your local installation, you need to install and build [UDpipe v1.0](https://ufal.mff.cuni.cz/udpipe/1/users-manual) under `udpipe/`. Our [`Makefile`](Makefile) assumes to find the executable under `udpipe/src/udpipe`.
- Models need to be installed separately. We expect modules to be found under `udpipe/models/$LANG/*.udpipe`, with `$LANG` to be replaced by a BCP47 language code (to be manually assigned). The command `make conllu` will use the *first* `\*.udpipe` file per directory for parsing.
- After adding a new language, you need to add the BCP47 code for the language to the variable `LANGS` under `update-conllu:` in [`Makefile`](Makefile) and then run `make update-conllu`. This will update the `conllu/` subdirectories, subsequent processing steps will take the language( tag)s from these subdirectories.
	- when running `make update-conllu`, the script will inform you about the installed UDPipe modules. Make sure these match the names of the subdirectories of `txt/`, as these files will serve as input.
- The repository provides pre-annotations
	- for English, using the [UD 2.5 EWT model](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131)
	- for German, using the [UD 2.5 GSD model](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131). Note that is relatively error-prone regarding the handling of pronominal constructions.
	- for French, using the [UD 2.5 GSD model](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131).
	- for Russian, using the [UD 2.5 SyntagRus model](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131).
	- [**IN PROGRRESS**] for European and Brazilian Portuguese, using [UD 2.5 Bosque model](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131). Note that this is the only UD corpus at the time to cover both European and Brazilian vernaculars.
- `make update-discourse_pre` seems to be blocked occasionally, esp., for longer files. When building new files for `ready-for-annotation`, these must be manually (timeout is implemented, but doesn't seem to grasp) terminated. As a possible workaround, start multiple `make update-discourse_pre` (resp. `make update`, etc.) threads shortly one after another. They are set up in a way that they don't overwrite each other's output, but skip files into which another instance is already writing into. 
- Current setup was developed under and tested within Ubuntu 22.04L.

## Known Issues

We currently provide preprocessed files for English, German and Russian, only. Other languages on demand.

- We remove multi-word expressions from the parser output, e.g., for German clitic determiners (*im*, *am*) are split off from prepositions (hence *in dem*, *von dem*). This may result in unnatural language in the token column, but the `# text` line on top should maintain the original forms. 
- There seem to occur infinite loops or blockings in `make update-discourse_pre`, so that these were manually interrupted. As a result, the sentence-level content in the files in `ready-for-annotation/` may be incomplete.
- Russian sentence-level: Discourse marker lexicon is incomplete, pre-annotation for sentence-level annotation is thus sub-standard.
- Russian word-level: Extraction of referring expressions not covered by UD Feats, hence form-based; check forms/lemmas against larger corpora
- French word-level: Quantifiers currently not supported

## Source data

- TED-MDB corpus (https://github.com/MurathanKurfali/Ted-MDB-Annotations), i.e., ted-mdb.1927, ted-mdb.1971, ted-mdb.1976, ted-mdb.1978, ted-mdb.2009, ted-mdb.2150
	- note that these are different TED talk ids than those from TED2020 and Teddy
- Bible: excerpts from the [ACoLi Bible Corpus](https://github.com/acoli-repo/acoli-corpora/tree/master/biblical)
- Doyle: selected pieces of Arthur Conan Doyle (also subject to [FrameNet annotations](https://framenet.icsi.berkeley.edu/fulltextIndex)
- ParCor: TED sub-corpus externally annotated for coreference (see [`preanno/parcor`](preanno/parcor/)).  
- ParCor: News texts from WMT17 (see [`preanno/parcor`](preanno/parcor/))
- **TODO**: TED core corpus
- **TODO**: add fairy tales
- **TODO**: any europarl coref/discourse annotations?

## Complementary Material

- [Augsburg Corpus of Bootstrapped Reference and Information Structure Annotations](https://github.com/acoli-repo/AURIS-bootstrap): extrapolated from over morphosyntactic marking in selected languages

