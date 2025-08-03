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

	- ca. 10 token/minute
		- ted-mdb-1927 1844 tokens, ca. 3 Stunden (09:00 - 13:05, 1 Std. Telco dazwischen)
		- ted-mdb-1971 647 tokens, ca. 50 min (08:15 - 09:06)

- I guess the annotation of hypophora might be systematically different from PDTB