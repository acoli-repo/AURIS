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