- b.MAT.1-5
	- initially annotated SoSe 2023 for COREF + IS
	- Guideline version: [v.0.1](https://github.com/acoli-repo/AURIS/blob/main/guidelines/v.0.1/draft-0.1-2023-05-22.pdf)
	- revised and extended 2025-11-14
	- sentence splitting not checked
- ted-mdb.1927
	- initially annotated SoSe 2023 for COREF + IS
	- Guideline version: [v.0.1](https://github.com/acoli-repo/AURIS/blob/main/guidelines/v.0.1/draft-0.1-2023-05-22.pdf)
	- marginally adjusted 2025-11-14
	- sentence splitting not checked
- ted-mdb.1971
	- initially annotated SoSe 2023 for COREF + IS by CC
	- Guideline version: [v.0.1](https://github.com/acoli-repo/AURIS/blob/main/guidelines/v.0.1/draft-0.1-2023-05-22.pdf)
	- marginally adjusted 2025-11-14
	- sentence splitting not checked
- ted-mdb.2009.eu-cc
	- tokens 1-470 initially annotated SoSe 2023 for COREF + IS by EU as part of a seminar/excercise
	- Guideline version: [v.0.1](https://github.com/acoli-repo/AURIS/blob/main/guidelines/v.0.1/draft-0.1-2023-05-22.pdf)
	- 2025-11-14 revised and extended by CC, CB annotation added
	- sentence splitting not checked
- ted-mdb.2009.ps
	- initially annotated SoSe 2023 for COREF + IS by EU as part of a seminar/excercise with CC
	- Guideline version: [v.0.1](https://github.com/acoli-repo/AURIS/blob/main/guidelines/v.0.1/draft-0.1-2023-05-22.pdf)
	- **not** verified
	- sentence splitting not checked

	


# observations

- see log files
- generally, possessive pronouns should have REF=BOUND, but they can nevertheless be annotated
- for generics with back references, use numbered IDs, e.g., anybody1, anybody2, etc. You can check via the REF column if these have been used before, e.g., "No one(nobody1,GEN) loses their(nobody1,BOUND) inner demons ..." (TED-MDB 2009)
- we need post-correction for TYPE and REFERENTIAL
- IS labels need to be normalized