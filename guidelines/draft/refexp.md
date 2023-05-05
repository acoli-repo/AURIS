**sources**: 
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- Christian Chiarcos and Olga Krasavina (2005), PoCoS. Potsdam Coreference Scheme. University of Potsdam, Germany
- consolidated and revised by Christian Chiarcos
- see Readme.md for contributors and revision history

# Automated Pre-Annotation of Markables

Texts for annotation should be automatically pre-annotated for nominal referring expressions. This document contains the guidelines for the algorithm. Normally, this is irrelevant for manual annotation and can be skipped.

We provide a pre-annotation routine that identifies referring expressions, their morphosyntactic type (`REFEXP`), their grammatical role (`GR`) and, for potential anaphors, their referentiality (`REF`, only value is currently `?OLD`).

## Markables

The annotation task is to process each text in reading order and annotate/verify all markables (automatically pre-annotated) and their antecedents (including cases in which these are not pre-annotated).

We distinguish between two types of markables, which are also to be marked as such:

-   **primary markable** (PM, automatically annotated as `?OLD`) are candidate anaphors, i.e., noun phrases whose grammatical features suggest that their discourse referent is or could be identifiable by the hearer. For German and English, these are definite NPs and pronouns. For languages without grammatical marking of definiteness, these are all nominals and pronouns. 

	Primary markables are automatically extracted. The task of annotation is to assign every primary markable either an antecedent or a flag that marks them as new or non-referential.

	> Note: This definition follows Krasavina and Chiarcos (2007). Chiarcos et al. (2016) singled out non-referential markables (NM)  from primary markables as they do not rely on automated pre-annotation.

-   **secondary markables** (SM, automatically annotated as `?NEW`) are antecedents for anaphoric expressions which have not been detected as primary markable.

	Typical secondary markables are  indefinite expressions (NP with indefinite article, *a dog*) or without article (*good weather*). 

In automated pre-annotation, all primary markables are assigned the referentiality `?OLD`, all secondary markables `?NEW`. The task of manual annotation is defined as annotating all primary markables and their antecedent from beginning to end, so that the presence of `?OLD` or `?NEW` indicates that a text has not been fully annotated.

Word forms that are confirmed to be syntactically bound are not to be annotated. Forms that are ambiguous between bound and anaphoric pronouns are annotated as primary markables and to be disambiguated manually.

For every text, 

- primary markables represent the set of all candidate anaphors,
- primary and secondary markables represent the set of all candidate referring expressions 

Candidate antecedents may also be outside this set, and will not be automatically annotated, in particular, event anaphor.

## Head-based Annotation

We only annotate the syntactic heads of markables according to the Universal Depenency syntax. Thus, markables must never overlap:

> (2.a) English: *\[<u>Hans</u> -- who always had \[a soft <u>spot</u>\] \[for <u>Susanne</u>\]  -- \]  was also there.*
> (2.b) German: *\[<u>Hans</u> -- der immer schon \[eine <u>Schwäche</u>\] \[für <u>Susanne</u>\] hatte -- \] war auch da.*

## Primary Markables (referentiality `?OLD`)

Primary markables are automatically extracted from a syntactic analysis. The following criteria define the algorithm. Normally, annotators do not have to annotate PMs and they can skip this section. However, if you feel there may be an anaphoric expression that was missed in automated extraction, please resort to these definitions. 

> Notes: 
> - Incorrect PM prediction can result from parser errors. Annotators should mark manually introduced PMs with the comment `manual PM`.
> - Annotators must never delete an incorrectly extracted PM annotation, but you can mark it as non-referential and add the comment `parser error` to the annotation.
> - From UD annotation, we cannot extract times and dates reliably. So, these receive no special handling (different from Stede et al. 2015).
> - Our pre-annotation predicts types of referring expressions, following Chiarcos and Krasavina (2005).

### a.  Pronouns

Personal, demonstrative, possessive pronouns and pronominal adverbs (e.g. German *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there") as well as *both* and *all* in nominal use (i.e. not as a determiner) 

> (3) *\[I\] saw \[her\] yesterday.*

Reflexive pronouns (English *herself*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself"), are PM, and should be marked as `bound` in the annotation. Analoguously for other non-referring pronouns (e.g., expletive *it* or generic *you* in the sense of "anyone").

### b.  Definite and Possessive Descriptions

-   With definite article: 

	> (4) *\[the <u>house</u>\]*

-   With determiner \'both\': 

	> (5) *\[both <u>houses</u>\]*

-   With possessive pronouns: 
	
	> (6) *\[\[his house\]*

- With potentially anaphoric genitive or possessibe modifier

	> (7) 
	> a. *\[Harald\'s <u>house</u>\]*
	> b. *\[the <u>house</u> of Harald\]*
	> c. *\[the other man's <u>house</u>\]*
	> d. *\[this man's <u>house</u>\]*
	> **but not** e. *\[a man's house\]*

### c. Demonstratives

NPs with demonstrative determiner (English *this NP*, *that NP*, German *diese NP*, *jene NP*), and demonstrative pronouns (German *dieser*, English *this*, *that* [if not used as relative pronoun]) are primary markables.

The demonstrative pronoun *such* (German *solch*) is considered as indefinite. Refererring expressions with *such* should not be annotated as primary markables.

### d.  Proper Names and Titles

Typical types of proper nouns are geographic locations, people, societies, names of newspapers and magazines, and names of various social, political, and financial institutions.

Examples of personal names:

> (8)
	> a.   \[Bertolt Brecht\] (full name)
	> b.  \[Bert Brecht\] (abbreviated full name)
	> c. \[Bertolt\] (first name)
	> d.   \[BB\] (abbreviation)
	> d.   \[the famous Brecht\] (name modified via definite description)

Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.

> (9) 
> a. \[Dr. <u>Mueller</u>\]
> b. \[Dr. <u>Martin</u> Luther King, Jr.\]
> c. \[Prince <u>Dipangkorn</u> Rasmijoti Sirivibulyarajakumar of Thailand\]
> d. \[Heidelberger <u>Druckmaschinen</u> Vertrieb Deutschland GmbH\]

Standalone titles are also assigned to the \'proper noun\' category and receive the appropriate attribute 

> (10) \[the graduate <u>engineer</u>\] didn\'t like it.

## Secondary Markables

Every nominal phrase or pronoun which is neither PM nor confirmed to be syntactically bound, is subject to automated pre-annotation. Secondary markables are referring expressions that are unlikely/impossible anaphors, but that could *introduce* new discourse referents.

> Note: At the moment, these are automatically annotated for `REFEXP`, but not for referentiality (`REF`).

Common types of SMs include:

-   NP with an indefinite article (if subsequently referred to):
	
	> (12.a) *There is a \[a <u>fox</u>\] running across the street. <u>It</u>'s fast!.*
	> (12.b) *I last saw \[a <u>fox</u>\] about three years ago! <u>It</u> came from the forest.*

	Annotate the secondary markable only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

	> (12.c) *I saw \[a <u>cat</u>\] tonight in the street. <u>It(= the cat)</u> was gray.*
	> (12.d) **but not**: *I saw a cat tonight in the street. <u>It(= the night/expletive?)</u> was pitch black.*

-   NPs with indefinite quantifier

	> (13) 
	> a. \[some people\]
	> b. \[some plants\]

-   Articleless NP, especially \"bare plurals\" (I have \[cookies\]SM
    eaten),but also singular expressions like in Today will be \[good
    weather\]SMbeand quantities such as \[thirty grams\].

## Automated Pre-Annotation

- Create a markable for every primary or secondary markable
- If it is a primary markable, pre-annotate it with referentiality `?OLD`
- If it is a secondary markable, annotate it with referentiality `?NEW`

For every markable, annotate the syntactic head (as defined by the Universal Dependencies, exceptions as mentioned above)

## Trouble-Shooting

### Bound Pronouns

Do not annotate bound pronoun, if these can be identified on grounds of their form or annotations. If a pronoun is ambiguous in its surface form and cannot be unambiguously confirmed as bound pronoun from the syntactic annotation, treat it like a primary markable and annotate with referentiality `?OLD`. Only in these cases, the annotator should then annotate referentiality `BOUND`.

### Stranded Quantifiers

An NP can be incomplete by elision and, at first glance, not meet the criteria of a markable.  For example, individual numerals are not usually PM, but íf their head noun is elided, they serve as heads of NPs, they can be.

> 	(2.c) *Ich hatte \[zwei Stunden\]~PM~ eingeplant, aber es wurden letzlich \[drei\]~SM~.* (German)
>	(2.c') *I had planned for \[two hours\], but in the end, it was \[three\]~SM~* (English)

### Non-referring Primary Markables

Non-referring markables (NM) are primary markables whose function is *not* to refer to a discourse referent. 
Non-referring markables are to be *manually* given the appropriate referentiality value in subsequent annotation (`GEN`, `EXPL`, `PRED`. `IDIOM` or `other`, see there). For automated extraction, they are treated like primary markables.
