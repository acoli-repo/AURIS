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

	- < 10 token/minute
		- ted-mdb-1927 1844 tokens, ca. 3 Stunden (09:00 - 13:05, 1 Std. Telco dazwischen)
		- ted-mdb-1971 647 tokens, ca. 50 min (08:15 - 09:06)
		- ted-mdb-1976 1396 tokens, ca. 70 min
		- ted-mdb-1978 05:15-06:19, 2070 tokens
		- ted-mdb-2009 6:23-6:39 792 tokens

- I guess the annotation of hypophora might be systematically different from PDTB
	- systematic difference from "normal" AURIS is that the direction follows nuclearity, whereas "normal" AURIS follows discourse markers, different exhaustivity constraints (annotate every discourse marker vs. attach every utterance, because sometimes we annotate the relation at the nucleus, depending on directionality)
	- second-level AURIS relations are actually argument roles, technically, these can be expanded to a full role set to leverage the directionality
	- evaluate not labels, but shortest spanning relation for every pair of utterances (difference in directionality doesn't count as difference!)
	- no annotation of long-distance relations in AURIS
- we annotate mononuclear, only