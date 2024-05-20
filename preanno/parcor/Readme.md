# ParCor corpus

build with

	$> make

## Licensing

- Originally distributed via https://www.statmt.org/wmt17/translation-task.html
	- As of May 20, 2024, this URL is not operational
	- Original usage conditions on this site stated "The data released for the WMT17 new translation task can be freely used for research purposes, we just ask that you cite the WMT17 shared task overview paper:"

		@InProceedings{bojar-EtAl:2017:WMT1,
		  author    = {Bojar, Ond
		{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huang, Shujian  and  Huck, Matthias  and  Koehn, Philipp  and  Liu, Qun  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Rubino, Raphael  and  Specia, Lucia  and  Turchi, Marco},
		  title     = {Findings of the 2017 Conference on Machine Translation (WMT17)},
		  booktitle = {Proceedings of the Second Conference on Machine Translation, Volume 2: Shared Task Papers},
		  month     = {September},
		  year      = {2017},
		  address   = {Copenhagen, Denmark},
		  publisher = {Association for Computational Linguistics},
		  pages     = {169--214},
		  url       = {http://www.aclweb.org/anthology/W17-4717}
		}

- Note that this license statement needs to be carried over for the news data. The Teddy data is compiled independently, after we figured out the ID mapping.

## ID mapping

| ParCor, TED ID | Teddy TED ID |
| -------------- | ------------ |
| 000_779		 | 1030         |
| 001_769        | 1154         |
| 002_792        | 1132         |
| 003_799        | 1124         |
| 004_767        | 918          |
| 005_790        | 744          |
| 006_785        | 807          |
| 007_783        | 901          |
| 008_824        | 1325         |
| 009_805 (broken) | 953        |
| 010_837        | 1429         | 

| ParCor, DiscoMT ID | Teddy TED ID |
| ------------------ | ------------ |
| 000_1756           | 1322         |
| 001_1819           | 1293         |
| 002_1825           | 1469         |
| 003_1894           | 1323         |
| 005_1938           | 1558         |
| 006_1950           | 1319         |
| 007_1953           | 4467         |
| 009_2043           | 1755         |

| ParCor, News ID    | WMT17 ID       |
| ------------------ | -------------- |
| 01                 | abcnews.199762 |
| 03                 | an-online.de.224441 |
| 04                 | ard.27823      |
| 05                 | augsburger-allgemeine.de.44740 |
| 07                 | bbc.242334     |
| 08                 | bbc.242405     |
| 09                 | bbc.242418     |
| 10                 | bbc.242436     |
| 13                 | bbc.242497     |
| 16                 | braunschweiger-zeitung.de.48722 |
| 17                 | brisbanetimes.com.au.130272 |
| 18                 | cbsnews.146232 |
| 19                 | cbsnews.146237 |
| 20                 | cbsnews.146271 |
| 21                 | cbsnews.146291 |
| 22                 | cbsnews.146310 |
| 23                 | cnn.167026 |
| 24                 | dailymail.co.uk.170661 |
| 25                 | dailymail.co.uk.170665 |