# Base data for AURIS annotations

This is compiled from several source corpora. Some of these may provide additional annotations. Different license conditions apply, but all are open source.

- languages
	- `de/` German
	- `en/` English
	- `lt/` Lithuanian
	- `pl/` Polish
	- `pt/` Portuguese
	- `ru/` Russian
	- `tr/` Turkish
	- more language to be provided upon request
- corpora
	- `*/ted-mdb.*.txt`: TED-MDB corpus, plain text files
		- license: [CC-BY 4.0](http://creativecommons.org/licenses/by/4.0/)
		- attribution: Zeyrek, Deniz et al. (2019), TED Multilingual Discourse Bank (TED-MDB): a parallel corpus annotated in the PDTB style, Journal of Language Resources and Evaluation (LREJ), 1-38
		- For annotations, see https://github.com/MurathanKurfali/Ted-MDB-Annotations.
	- `*/bibl.*.txt`: excerpts (selected books) of Bibles, from the [ACoLi corpora collection](https://github.com/acoli-repo/acoli-corpora/tree/master/biblical/data)
		- license: see accompanying LICENSE statement for the respective language, if none is provided, the text is assumed to be in the public domain (CC0).
	- `*/doyle.*.txt`: Arthur Conan Doyle, The Hound of the Baskervilles (chap. 14)
		- license: public domain
		- additional annotations are available as part of [FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/fulltextIndex), for example
- news data from WMT17 data set to be compiled as follows:

		$> cd ../
		$> make update_txt_w_news

## TODOs

- add Tiger of San Pedro (https://www.pagebypagebooks.com/Arthur_Conan_Doyle/The_Adventure_of_Wisteria_Lodge/The_Tiger_of_San_Pedro_p1.html), also in FrameNet corpus
- consider adding Le Petit Prince, if translations can be secured
- consider adding Orwell's 1984, if copyright for German and Romance can be cleared
