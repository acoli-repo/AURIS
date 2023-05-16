**sources**: 
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- Olga Krasavina and Christian Chiarcos (2007), PoCoS. Potsdam Coreference Scheme, First Linguistic Annotation Workshop (LAW-2007), held in conjunction with ACL-2007, Prague, Czech Republic, June 2007
- NOT YET: Christian Chiarcos and Olga Krasavina (2005), PoCoS. Potsdam Coreference Scheme. University of Potsdam, Germany
- consolidated and revised by Christian Chiarcos
- see Readme.md for contributors and revision history

# Automated Pre-Annotation of Markables

Texts for annotation should be automatically pre-annotated for nominal referring expressions. This document contains the guidelines for the algorithm. Normally, this is irrelevant for manual annotation and can be skipped.

We provide a pre-annotation routine that identifies referring expressions along with

- their morphosyntactic type (`NP_FORM`)
- for potential anaphors, their expected referentiality (`REF_AUTO`, only value is currently `?OLD`), and
- their grammatical role (`GR`).

We describe `NP_FORM` and `REF_AUTO` as part of markable identification. `GR` annotation is described separately.

## Markables

The annotation task is to process each text in reading order and annotate/verify all markables (automatically pre-annotated) and their antecedents (including cases in which these are not pre-annotated).

The scheme distinguishes between primary and secondary markables.
Primary markables are *always* subject to annotation. Secondary markables are only annotated if they happen to serve as antecedents for primary markables. In earlier versions of this schema, explicit annotations for primary and secondary markables were included. This is, however, not necessary, as they are merely a technical device to guide the annotation process.

More specifically,

-   **primary markables** (PM, automatically annotated as `?OLD`) are candidate anaphors, i.e., noun phrases whose grammatical features suggest that their discourse referent is or could be identifiable by the hearer. For German and English, these are definite NPs and pronouns. For languages without grammatical marking of definiteness, these are all nominals and pronouns. 

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

This also entails that referring expressions can *only* be annotated if they are identified as independent words by the word segmentation procedure adopted for that particular language. In (2.c), *Denver* and *bancruptcy* can only be identified as markables if they are (automatically annotated as) independent tokens.

> (2.c) *The \[Denver\]?-based concern, which emerged from bancruptcy \... its new, post-\[bancruptcy\]? law structure \...\"* (WSJ, 1328)

When converting head-based annotation to span-based annotation in downstream tasks, we assume that all dependents of a syntactic head are to be included in the markable.

> (2.d) *\[This <u>right</u>\]~right~ may not be invoked \[in the case of <u>prosecutions</u> arising from acts contrary \[to the <u>purposes</u> \[of the United <u>Nations</u>\]UN\]purp\]prosec.* ([www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)
> (2.d') *\[Dieses <u>Recht</u>\]~right~ kann nicht in Anspruch genommen werden \[im Falle einer <u>Strafverfolgung</u> auf Grund von Handlungen, die \[gegen die <u>Ziele</u> \[der Vereinten <u>Nationen</u>\]~UN~\]~purp~ verstoßen\]~prosec~.* (German, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)
> (2.d'') *\[Это <u>право</u>\]~right~ не может быть использовано \[в случае
<u>преследования</u>, основанного на совершении деяния, противоречащего
\[<u>целям</u> \[Организации Объединенных <u>Наций</u>\]~UN~\]~purp~\]~prosec~.*
(Russian, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

## Primary Markables (referentiality `?OLD`)

Primary markables are automatically extracted from a syntactic analysis. The following criteria define the algorithm. Normally, annotators do not have to annotate PMs and they can skip this section. However, if you feel there may be an anaphoric expression that was missed in automated extraction, please resort to these definitions. 

> Notes: 
> - Incorrect PM prediction can result from parser errors. Annotators should mark manually introduced PMs with the comment `manual PM`.
> - Annotators must never delete an incorrectly extracted PM annotation, but you can mark it as non-referential and add the comment `parser error` to the annotation.
> - From UD annotation, we cannot extract times and dates reliably. So, these receive no special handling (different from Stede et al. 2015).
> - Our pre-annotation predicts types of referring expressions, following Chiarcos and Krasavina (2005).

### a.  Pronouns

Pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and personal pronouns and *both* in nominal use (i.e. not as a determiner) 

> (3) *\[I\] saw \[her\] yesterday.*

In German, demonstrative pronouns include: *dieser, jener, der, die, derjenige,* and the like
Note that demonstrative pronouns *such*, in German *solch* and so-called "generic pronouns" (*we, you, they*, in German *wir, du, sie* (without specific reference), *man, einer*) are considered as indefinite, thus no primary markables.

> Notes:
> - Personal pronouns also include pronominal adverbs (e.g. German *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there") 
> - Reflexive pronouns (English *herself*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself"), are PM, and should be marked as `bound` in the annotation. Analoguously for other non-referring pronouns (e.g., expletive *it* or generic *you* in the sense of "anyone").
> - Interrogative pronouns are not primary markables, but can serve as secondary markables.
> - Chiarcos and Krasavina (2005) also include zero (pro-drop) pronouns under pronouns. Here, we follow token-based annotation, so that zeros should not be annotated.

	> (43) *John~j~ stepped in the kitchen,* Ø*~j~ opened the fridge and* Ø*~j~ decided NO-ZERO to take a pizza.*

	Note, that John is the (implicit) subject of the clause *to take a pizza*. However, this is not an instance of ∅-pronoun, since the insertion of *John* (no matter at which position within the phrase) would make the utterance ungrammatical. If not sure whether to annotate a ZERO or not, try to insert a full description of the corresponding referent. Note that zeros have to be sentential arguments, no adjuncts.


> - Stede et al. (2016) treat *all*+NP like *both*+NP. needs to be double-checked.

### b.  Definite Descriptions

A description (NP or PP) is definite if it contains the determiner *both*, a demonstrative or possessive pronoun or a genitive attribution. 

-   With definite article: 

	> (4) *\[the <u>pizza</u>\]*
	
- With demonstrative determiner:

	> (15.c) *\[that <u>pizza</u>\]*, *\[this <u>pizza</u>\]*

-   With determiner \'both\': 

	> (5) *\[both <u>pizzas</u>\]*

-   With possessive pronouns: 
	
	> (6) *\[his <u>pizza</u>\]*

- With potentially anaphoric genitive or possessive modifier

	> (7) 
	> a. *\[John\'s <u>pizza</u>\]*
	> b. *\[the <u>pizza</u> of John\]*
	> c. *\[the other man's <u>pizza</u>\]*
	> d. *\[this man's <u>pizza</u>\]*
	> **but not** e. *\[a man's pizza\]*

### c.  Proper Names and Titles

Typical instances of proper names are geographic places
(*Philadelphia*), persons (*Judge Jenkins*), companies (*Morgan
Stanley & Co.*), newspaper titles (*The New York Times*), political, social or financial institution names (*Congress, European Investment
Bank* ). Proper names can include noun modifiers or be heads of a definite or indefinite description. In this case, the whole description has to be marked up, not just the head.

> (8)
	> a.  *\[Bertolt <u>Brecht</u>\]* (full name)
	> b.  *\[Bert <u>Brecht</u>\]* (reduced full name)
	> c.  *<u>Brecht</u>* (surname)
	> d. 	*<u>Bertolt</u>* (first name)
	> e. 	*<u>Bert</u>* (nickname)
	> f.   *<u>BB</u>* (abbreviation)
	> g.   *the well-known <U>Brecht</u>* (name, modified by a definite description)
	> h. *<u>Brecht</u>, who is author of the "Dreigroschenoper"* (proper name + clause) 
	> i. *<u>Brecht</u>, author of the "Dreigroschenoper"* (proper name + apposition)

Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.

> (9) 
> a. \[Dr. <u>Mueller</u>\]
> b. \[Dr. <u>Martin</u> Luther King, Jr.\]
> c. \[Prince <u>Dipangkorn</u> Rasmijoti Sirivibulyarajakumar of Thailand\]
> d. \[Heidelberger <u>Druckmaschinen</u> Vertrieb Deutschland GmbH\]

Standalone titles that can stand in for an individual (*Mr./Ms./Dr./President/Chairman*) are treated like proper names, e.g., 

> (10) *Schröder~1~\...Fischer~2~ \... Die anfängliche Überreaktion von <u>Kanzler</u>~1~ und <u>Außenminister</u>~2~\...*

In (10), *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite

Note that Parts of complex proper names cannot be analyzed separately. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

> (7) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*

## Secondary Markables

Every nominal phrase or pronoun which is neither PM nor confirmed to be syntactically bound, is subject to automated pre-annotation. Secondary markables are referring expressions that are unlikely/impossible anaphors, but that could *introduce* new discourse referents.

> Note: At the moment, these are automatically annotated for `NP_FORM`, but not for referentiality (`REF`).

Common types of SMs include:

-   NP with an indefinite article (if subsequently referred to), e.g., *a fox*:
	
	> (12.a) *There is a \[a <u>fox</u>\] running across the street. <u>It</u>'s fast!.*
	> (12.b) *I last saw \[a <u>fox</u>\] about three years ago! <u>It</u> came from the forest.*

	Annotate the secondary markable only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

	> (12.c) *I saw \[a <u>cat</u>\] tonight in the street. <u>It(= the cat)</u> was gray.*
	> (12.d) **but not**: *I saw a cat tonight in the street. <u>It(= the night/expletive?)</u> was pitch black.*

-   NPs with indefinite quantifier

	> (13.a) *\[some people\]*
	> (13.b) *\[some plants\]*

-   Articleless NP, especially \"bare plurals\", but also singular expressions and quantified NPs not otherwise annotated as primary markables.

    > (14.a) *I have eaten \[cookies\]SM* (bare plural)
    > (14.b) *Today will be \[good weather\]SM* (bare singular) 
    > (14.c) *\[thirty grams\]*, *\[two companies\]* (quantified indefinite NP)

## Automated Pre-Annotation

- Check every nominal, pronoun, prepositional phrase, or proper name 
- If it is a primary markable, pre-annotate it with referentiality `?OLD`
- If it is a secondary markable, do not annotate it for referentiality.

> Note: Alternatively, annotate secondary markables with referentiality `?NEW`.

For every markable, annotate the syntactic head (as defined by the Universal Dependencies, exceptions as mentioned above) for type of referring expression.

## Trouble-Shooting

### Demonstratives

NPs with demonstrative determiner (English *this NP*, *that NP*, German *diese NP*, *jene NP*), and demonstrative pronouns (German *dieser*, English *this*, *that* [if not used as relative pronoun]) are primary markables.

The demonstrative pronoun *such* (German *solch*) is considered as indefinite. Refererring expressions with *such* should not be annotated as primary markables.

### Bound Pronouns

Do not annotate bound pronoun, if these can be identified on grounds of their form or annotations. If a pronoun is ambiguous in its surface form and cannot be unambiguously confirmed as bound pronoun from the syntactic annotation, treat it like a primary markable and annotate with referentiality `?OLD`. Only in these cases, the annotator should then annotate referentiality `BOUND`.

### Treatment of quantifiers

Quantified NPs *(some of them, all the members)* are annotated as either definite or indefinite, whereas each case has to be considered individually. Substitution test: *all days* −→ *all these days* −→ definite.
In automated pre-annotation, every nominal phrase whose form does not rule out a definite interpretation should be treated as primary markable.

We regard NPs with certain quantifiers in determiner position such as *both* as definite, since German *beide* as English *both* normally presupposes the existence of exactly two discourse-old entities (cf. Zifonun et al. 1997).

*Both* in nominal use is annotated as a personal pronoun.

### Possessive NPs

Primary markables include

> (15.a) *his house*
> (15.b) *the old man's house*

Note that the possessor must be a primary markable, too: *\[\[his\] house\]*, *\[\[the old man's\] house\]*.

Descriptions with a genitive attribution are regarded as possessive iff. a definite genitive attribution replaces the determiner, except for *of* -constructions (cf. ex. 16.b).

> (16.a) *the old man's house* (definite possessive description, cf. *his house* and \**the the old man's house*)
> (16.b) *the house of the old man* (definite non-possessive description: determiner in *the house* relates to the house itself and not to its possessor)
> (16.c) *an old's man house*(this is not a primary markable - the possessor is indefinite)

Possessive NPs with indefinite possessor (16.c) are secondary markables. However, possessives with proper names should generally be considered as primary markables.

> (16.d)   *in US <u>efforts</u>*

This is a primary markable because there is a reading, where the phrase could be replaced with *in the US efforts*.

### Appositions

Appositions are treated like predications. That is, they serve neither as antecedents nor anaphors. So, in the following example, *chairman* in *chairman of
Petrie Stores Corp.* should not be annotated!

> (17) *\[Milton <u>Petrie</u>, chairman \[of Petrie Stores Corp.\] said\...*

### Stranded Quantifiers

An NP can be incomplete by elision and, at first glance, not meet the criteria of a markable.  For example, individual numerals are not usually PM, but íf their head noun is elided, they serve as heads of NPs, they can require an antecedent. 

> (18) *Now only three of the 12 judges - \[\[Pauline Newman\]n, (\[Chief
     Judge Howard T. Markey, 68\]m)two*1*, and (\[Giles Rich, 85\]r)two*
     2 *- have patent law backgrounds\]. \[The latter* *two\]~two~ and \[Judge Daniel M. Friedman, 73\]~f~ , are approaching senior status or retirement.* (WSJ corpus)

As these cases cannot be automatically identified, all pronominal numerals are to be annotated as primary markables. 

> 	(18') *Ich hatte \[zwei Stunden\]~PM~ eingeplant, aber es wurden letzlich \[drei\]~SM~.* (German)
>	(18") *I had planned for \[two hours\], but in the end, it was \[three\]~SM~* (English)

### Proper noun vs. definite NP

Note that if a proper noun is not a head of an NP, the NP is annotated as definite or indefinite respectively.

> (19) *the river Yukon* 

In (19), *Yukon* is the head. *Yukon* is a proper name, so the whole phrase is annotated as proper name.

> (20) *the Yukon office*

In (20), *office* is the head, *office* is not a proper name, so *the Yukon office* has to be annotated as a definite NP.

### Non-referring Primary Markables

Non-referring markables (NM) are primary markables whose function is *not* to refer to a discourse referent. 
Non-referring markables are to be *manually* given the appropriate referentiality value in subsequent annotation (`GEN`, `EXPL`, `PRED`. `IDIOM` or `other`, see there). For automated extraction, they are treated like primary markables.

### Do NOT annotate

-   expletive expressions

	> (21) *Then, when it would have been easier to resist them, nothing was done*

(expletive *it*).

-   *Es*-pronouns, pronominal adverbs, which are controllers of relative clauses

	> (22) *Dazu kommt, dass in Werder am 24. Februar ein Bu¨rgermeister gewa¨hlt wird und es bisher als sicher galt, dass CDU-Amtsinhaber Werner Gr¨oße unangefochten bleibt.*

	*Dazu\...dass, es\...dass* should not be annotated as markables (*Dazu* and *es* are controllers of relative clauses).

-   pronominal adverbs functioning as discourse markers

	> (23.a) *Ich habe dich angesprochen, damit du mir zuhörst*. "I am talking to you to let you know that you must listen to me."
	> (23.b) *Ich habe dir das gesagt, damit du weißt, dass du mir zuh¨oren sollst*.
	> (23.c) *Ich habe dir das gesagt, dass du weißt, dass du mir zuh¨oren sollst.*

-   relative pronouns

	Relative pronouns are annotated together with the whole relative clause it triggers as one single markable (cf. *\[The car that went through his garden wall\]\...*). If a form cannot be unambiguously classified as a relative pronoun, apply the following test: it is a relative pronoun if it can be substituted by "which" respectively "welch" in German.
	However, relative pronouns in possessive constructions (i.e. for which the test for relative pronouns fails) are annotated as possessive pronouns (see possessive NPs, p. 10).

	> (24) *Und so schielen die Israelis nach Washington, an dessen /\*welchem Tropf sie wirtschaftlich und militärisch hängen,\...*
	> (24') *Und so schielen die Israelis nach Washington, das/welches sie wirtschaftlich und militärisch unterstützt* (*das* is a relative pronoun).

	Alternatively, the following test can be applied: substitute a pronoun in question with a possessive construction. If it works, you have a possessive pronoun, not a relative one.

	> (25) *die Frau und deren Kinder = die Frau und ihre Kinder*

	The annotation is as follows in this case:

	> (26) *Und so schielen \[die Israelis\]i \[(nach Washington)w, \[an \[dessen\]w Tropf\] \[sie\]i wirtschaftlich und milit¨arisch h¨angen\]~w~*′ *,\...*

-   prepositional phrases with prepositions *as, than*, *bis, als, wie* (in German) Such prases are annotated as normal NPs, i.e. *bis* and *als* are not included. ^3^

-   nominal premodifiers in compound nouns

	> (27) *peanut butter, airline analyst, the creditors commettee, investment bank*

	*Peanut, airline, cretitors* and *investment* are no separate markables. Note that in *the creditor's opinion*, *the creditor's* is annotated as a markable, since it is a nominal in genitive and thus not a part of a compounds.

### Idioms and Collocations

Primary markables in idioms and collocations, if identifiable in automated pre-annotation.

> (23) *It sent Kate into the pits when she learned from her "friend" Martha, who seemed to get off on laying bad trips on people, that Harvey was getting it on with Carol.* \[Gib94, p.265\]

According to Gibbs, we find several idiomatic phrases in this example, some of which contain pronouns or full NPs -- potential primary markables.

However, they should not be annotated as such, e.g. *into the pits* meaning "to be depressed", *get it on* meaning "having sexual relations", neither *the pits* nor *it* can be referred to.

Note that we consider only *conventionalized* idiomatic expressions as idioms in our sense,

i.e. markables within productive metaphors are annotated as usual, e.g. *das schlingernde City-Schiff City-Schiff* - a metaphor that occurred and can only be understood with respect to a specific text.

## Grammatical role annotation (`GR`)

Grammatical role annotation is extrapolated from (automated) annotation according to Universal Dependencies conventions (either UD v.1 or v.2), with the following rules:

- `SBJ`: nominal subject (UD edge: starts with `nsubj`)
- `OBJ`: grammatical object  (UD edge: contains `obj`)
	
	> Note: Chiarcos and Krasavina (2005) distinguished indirect and direct objects. However, within the UD community, the notion of indirect object has been criticized, and the usage of `iobj` seems to be inconsistent.

- `other`: every other referring expression is annotated `other` (i.e., every element that carries `NP_FORM` annotation but has not been assigned a `GR` annotation before, includes both primary and secondary markables, but not antecedents of event anaphors)
- for referring expressions in dependent clauses or adnominal constructions, we append the depth of syntactic embedding as a numerical suffix (i.e., replace existing `GR` annotation `$gr` with `$gr`+`_depth`, e.g., `SBJ_2` for the subject a relative clause directly depending on the main clause. Embedding depth is calculated over UD trees.)

	> Note: In Chiarcos and Krasavina (2005), these were included under `other`

> Note: According to these rules, nominals that are not integrated into the clausal structure are considered as `other`.

These rules are implemented in `sparql/gr.sparql`.

> Note: TODO: update SPARQL script for new abbreviations

## Future extensions

The following features of the original PoCoS scheme are currently not annotated:

- column/feature `DIRECT_SPEECH`

	- default (`_`): reference on the text level, i.e. reference NOT into or within the quoted material
	- `DIR`: reference into or within direct speech
	- `INDIR`: reference into or within indirect speech

- column/feature `COMPLEX_NP`: A description is complex if it contains more than one noun phrase
	- `_` (default)
	- `yes`
	- `no`

- column/feature `SEMANTIC_ROLE`: ag, ben/dat, pat, loc, instr, other, unspec
- column/feature `quantification`: 

	- quant-np description involving a quantification 
		> (67.a) *most of them*	(quantified pronoun) 
		> (67.b) *many of the workers* (quantified NP)

	- num-np description involving cardinal numbers^10^

		> (68.a) *two dogs* (numeral + indefinite or definite NP) (68.b) *the two dogs* (numeral + definite NP)

		> (68.c) *two of them* (numeral + pronoun)

		> (68.d) *both (of them)* (two-dimensional group-referring pronoun)

	- no-quant neither quant-np nor num-np unspec no value set

	Borderline case: indefinite NPs with an article that is identical (or at least derived from) the cardinal number *one* should be considered as quantified iff. a corresponding set of individuals has been previously evoked and the membership relation marked as being relevant.

	For English, the latter condition should hold for *one*, but not for
	*an, a*, for German, the membership relation should be regarded as being prominent if a substitution of the indefinite article *ein, eine* by colloquial *'n, 'ne* appears to be unlikely.

- `ANIMACY`: 
	- animate i.e. lexical animacy, with the following sub-types
	- human
	- non-human
	- inaminate i.e. lexical inanimacy or abstract
	Note that abstract entities are always regarded as being inanimate.

- semantic class: abstract, person, physical object, action/event, collective, other, unspec

	Note that there exist subtle dependencies between semantic class and animacy. However, critical cases such as collectives (e.g. *a group of people* vs. *a group of hills*) and certain physical objects (e.g. *tree* vs. *stone*) could be either animate or inanimate. While semantic class has to do with the perception of an entity, animacy is primary a lexical feature. However, default values semantic class and animacy can be derived from WordNet resp. GermaNet for a majority of cases.

## TO INTEGRATE

Chiarcos and Krasavina (2005):
	
- np-form

	The feature stands for the surface structure of markables

	- 	none should be used only for non-nominal non-referring expressions, e.g. for clauses that serve as antecedents of event anaphors
	-	ne proper names
	-	def-np definite NP, with optional subtypes
		- poss-np possessive NP
		- other-np definite NPs containing adjectives like *other*, e.g. *the other man*
		- the-np any NP with a definite article not covered by another def-np category
		- dem-np demonstrative NPs involve several sub-types regarding differences with respect to their relative proximity, with optional subtypes
			- dem-np-prox: proximal *this man*, \...
			- dem-np-dist: distal *that man*, \...
	- \*indef-np indefinite NP pper personal pronouns ppos possessive pronouns, pds demonstrative pronouns padv pronominal adverbs, optional subtypes
		- bare-np indefinites without article, e.g. *men*, *water*, \... 
		- a-np indefinites with indefinite article, e.g. *a man*, \... 
		- another-np indefinites with other, e.g. *another man* 
	-	other for special purposes, we leave this option for later extensions, choosing other
		- enforces to add a comment describing the type of description Note that np-form has to be annotated both for NPs and PPs!
	- pron (referring) pronoun, with optional subtypes
		- pper personal pronouns, *I, me, you, he, him, she, her, it, we, us, they, them*
		- ppos possessive pronouns, *my, mine, your, yours, \...* prefl reflexive pronouns, *himself, herself, itself, \...* pint interrogative pronouns, *who, where, when, \...*
		- pds demonstrative pronouns, with optional sub-classes: 
			- pds-prox: proximal *this, these*, *this one*, German *der, die, das, \...*
			- pds-dist: distal *that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes*
		- padv: German only: pronominal adverbs, e.g. *davor, deswegen*

The top level (without reflexives and interrogatives) is in core scheme, remainder in extended scheme
