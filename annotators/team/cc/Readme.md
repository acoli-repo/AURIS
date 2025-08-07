- `rs3-raw` automatically created using `../../scripts/txt2rs3.py`

		$> for file in ../../../../conllu/de/ted-mdb.*; do \
			tgt=`basename $file | sed s/'\.conllu'//`.rs3; \
			echo $file '>' $tgt 1>&2; \
			cat $file \
			| egrep '^[0-9]' \
			| sed s/'^1\t'/'\n&'/g \
			| cut -f 2 \
			| perl -pe 's/(.)\n/\1 /g; s/\n/\n\n/g;' \
			| python3 ../../../../scripts/txt2rs3.py \
			> $tgt; \
		  done 

- `rs3` annotation with RSTTool, using AURIS labels

	| ted talk     | tok  | min | tok/min          |
	|--------------|------|-----|------------------|
	| ted-mdb 1927 | 1844 | 180 | 10.2444444444444 |
	| ted-mdb-1971 | 647  | 50  | 12.94            |
	| ted-mdb-1976 | 1396 | 70  | 19.9428571428571 |
	| ted-mdb-1978 | 2070 | 64  | 32.34375         |
	| ted-mdb-2009 | 792  | 16  | 49.5             |
	| ted-mdb-2150 | 1024 | 15  | 68.2666666666667 |

	- I guess the annotation of hypophora might be systematically different from PDTB
		- systematic difference from "normal" AURIS is that the direction follows nuclearity, whereas "normal" AURIS follows discourse markers, different exhaustivity constraints (annotate every discourse marker vs. attach every utterance, because sometimes we annotate the relation at the nucleus, depending on directionality)
		- second-level AURIS relations are actually argument roles, technically, these can be expanded to a full role set to leverage the directionality
		- evaluate not labels, but shortest spanning relation for every pair of utterances (difference in directionality doesn't count as difference!)
		- no annotation of long-distance relations in AURIS
	- we annotate mononuclear, only, so that the anchor span is uniquely identifiable, and the direction is chosen accordingly. because we need to make sure that spans remain accessible to future attachments, this leads to a preference of having the second span as target (because it leads to shorter relations for forthcoming utterances). however, it is understood that symmetric relations are in fact multinuclear 

- `rs3-xslx` converted from `rs3/` using

		$> for file in ted-mdb.*rs3; do python3 ../../../../scripts/rst2tsv.py $file > ../rs3-xlsx/`basename $file | sed s/'\.rs3'//g`.xlsx; done