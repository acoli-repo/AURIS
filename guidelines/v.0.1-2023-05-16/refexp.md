# 3. Automated Pre-Annotation of Markables

Texts for annotation should be automatically pre-annotated for referring expressions. This document contains the guidelines for the algorithm. Normally, this is irrelevant for manual annotation and can be skipped by annotators.

We provide a pre-annotation routine that identifies referring expressions along with

- their morphosyntactic type (`NP_FORM`)
- for potential anaphors, their expected referentiality (`REF_AUTO`, only value is currently `?OLD`), and
- their grammatical role (`GR`).

We describe `NP_FORM` and `REF_AUTO` as part of markable identification. `GR` annotation is described separately.

## 3.1 Types of Markables

The annotation task is to process each text in reading order and annotate/verify all markables (automatically pre-annotated) and their antecedents (including cases in which these are not pre-annotated).

The scheme distinguishes between primary and secondary markables.
Primary markables are *always* subject to annotation. Secondary markables are only annotated if they happen to serve as antecedents for primary markables. In earlier versions of this schema, explicit annotations for primary and secondary markables were included. This is, however, not necessary, as they are merely a technical device to guide the annotation process.

More specifically,

-   **primary markables** (PM, pre-annotated for `REF_AUTO` as `?OLD`, and for `NP_FORM`) are candidate anaphors, i.e., noun phrases whose grammatical features suggest that their discourse referent is or could be identifiable by the hearer.<sup>[1](lit.md#refexp1)</sup> For German and English, these are definite NPs and pronouns. For languages without grammatical marking of definiteness, these are all nominals and pronouns.

	Primary markables are automatically extracted. The task of annotation is to assign every primary markable either an antecedent or a flag that marks them as new or non-referential.

-   **secondary markables** (SM, pre-annotated for `NP_FORM`, but not `REF_AUTO`) are antecedents for anaphoric expressions which have not been detected as primary markable.

	Typical secondary markables are  indefinite expressions (NP with indefinite article, *a dog*) or without article (*good weather*). 

In automated pre-annotation, all primary markables are assigned the referentiality (`REF_AUTO`) value `?OLD`. Secondary markables are annmotated for their `NP_FORM`, but not for `REF_AUTO`. The task of manual annotation is defined as annotating all primary markables and their antecedent from beginning to end, so that the presence of `?OLD` indicates that a text has not been fully annotated.

Word forms that are confirmed to be syntactically bound are not to be annotated. Forms that are ambiguous between bound and anaphoric pronouns are annotated as primary markables and to be disambiguated manually.

For every text, 

- primary markables represent the set of all candidate anaphors,
- primary and secondary markables represent the set of all candidate referring expressions 

Candidate antecedents may also be outside this set, and will not be automatically annotated, in particular, event anaphor.

## 3.2 Identifying the Syntactic Head

We only annotate the syntactic heads of markables according to the Universal Depenency syntax. Thus, markables must never overlap:

> (1.a) English: *\[<ins>Hans</ins> -- who always had \[a soft <u>spot</u>\] \[for <u>Susanne</u>\]  -- \]  was also there.*

> (1.b) German: *\[<u>Hans</u> -- der immer schon \[eine <u>Schwäche</u>\] \[für <u>Susanne</u>\] hatte -- \] war auch da.*

This also entails that referring expressions can *only* be annotated if they are identified as independent words by the word segmentation procedure adopted for that particular language. In (1.c), *Denver* and *bancruptcy* can only be identified as markables if they are (automatically annotated as) independent tokens.

> (1.c) *The \[Denver\]?-based concern, which emerged from bancruptcy \... its new, post-\[bancruptcy\]? law structure \...\"* (WSJ, 1328)

When converting head-based annotation to span-based annotation in downstream tasks, we assume that all dependents of a syntactic head are to be included in the markable:

> (2.a) *\[This <u>right</u>\]~right~ may not be invoked \[in the case of <u>prosecutions</u> arising from acts contrary \[to the <u>purposes</u> \[of the United <u>Nations</u>\]UN\]purp\]prosec.* ([www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

> (2.b) *\[Dieses <u>Recht</u>\]~right~ kann nicht in Anspruch genommen werden \[im Falle einer <u>Strafverfolgung</u> auf Grund von Handlungen, die \[gegen die <u>Ziele</u> \[der Vereinten <u>Nationen</u>\]~UN~\]~purp~ verstoßen\]~prosec~.* (German, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

> (2.c) *\[Это <u>право</u>\]~right~ не может быть использовано \[в случае
<u>преследования</u>, основанного на совершении деяния, противоречащего
\[<u>целям</u> \[Организации Объединенных <u>Наций</u>\]~UN~\]~purp~\]~prosec~.*
(Russian, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

## 3.3 Primary Markables (`REF_AUTO`=`?OLD`)

Primary markables are automatically extracted from a syntactic analysis.<sub>[2](lit.md#refexp2)</sub>
The following criteria define the algorithm. Normally, annotators do not have to annotate PMs and they can skip this section. However, if you feel there may be an anaphoric expression that was missed in automated extraction, please resort to these definitions.

> Note: Incorrect PM prediction can result from parser errors. Annotators should mark manually introduced PMs with the comment `manual PM`.

> Note: Annotators must never delete an incorrectly extracted PM annotation, but you can mark it as non-referential and add the comment `parser error` to the annotation.

### 3.3.1 Pronouns (`NP_TYPE`=`pron`)

Pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and possessived pronouns and *both* in nominal use (i.e. not as a determiner),<sup>[3](lit.md#refexp3)</sup> e.g.,

> (3) *\[I\] saw \[her\] yesterday.*

If automated pre-annotation operates on a language/annotation schema that doesn't distinguish these types of pronouns from other (non-referring) types of pronouns, *every* pronoun should be annotated as primary markable.

> Note: Interrogative pronouns are not primary markables, but can serve as secondary markables.

> Note: Relative and reflexive pronouns are not primary markables, if annotated by pre-annotation, they should be annotated as `REF=BOUND`. Their automated `NP_TYPE` annotation can be deleted.

#### 3.3.1.1 Personal Pronouns (`NP_TYPE`=`pron.pper`)

Personal pronouns include (the language-specific counterparts of) English *I, me, you, he, him, she, her, it, we, us, they, them*.

Note that so-called "generic pronouns" (*we, you, they*, in German *wir, du, sie* (without specific reference), *man, einer*) are considered as indefinite, but that they cannot be automatically identified. Thus, they are annotated as primary markables.

> Note: Reflexive pronouns (English *herself*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself"), are PM, and should be manually marked as `REF=BOUND` in the annotation. 

> Note: Other non-referring pronouns (e.g., expletive *it* or generic *you* in the sense of "anyone") are likewise not to be deleted but to be annotated manually.

#### 3.3.1.2 Possessive Pronouns (`NP_TYPE`=`pron.ppos`)

Possessive pronouns include (the language-specific counterparts of) English *my, mine, your, yours, \...*.

#### 3.3.1.3 Demonstrative Pronouns (`NP_TYPE`=`pron.pds`)

Demonstrative pronouns occur with two optional sub-classes: 

- `NP_TYPE=pron.pds-prox`: proximal *this, these*, *this one*, German *der, die, das, \...*
- `NP_TYPE=pron.pds-dist`: distal *that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes, derjenige,* and the like.

Note that demonstrative pronouns *such*, in German *solch*, are considered indefinite.

> Note: Relative pronouns (English *which*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are relative or demonstrative pronouns (e.g., English *that* in relative clauses), are PM, and should be manually marked as `REF=BOUND` in the annotation.

#### 3.3.1.4 Pronominal Adverbs (`NP_TYPE`=`pron.padv`)

Personal pronouns also include pronominal adverbs (e.g. German *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there"), *davor* "in front of that; before that", or *deswegen* "because of that".

### 3.3.2 Definite Descriptions (`NP_TYPE`=`def-np`)

A description (NP or PP) is definite if it contains the determiner *both*, a demonstrative or possessive pronoun or a genitive attribution. Optionally, this can be made explicit with sub-types.

#### 3.3.2.1 With Demonstrative Determiner (`NP_TYPE`=`def-np.dem`)

> (4) *\[that <u>pizza</u>\]*, *\[this <u>pizza</u>\]*

Demonstrative NPs involve optional differences with respect to their relative proximity, with optional subtypes

- `NP_TYPE=def-np.dem-prox`: proximal *this man*, \...
- `NP_TYPE=def-np.dem-dist`: distal *that man*, \...

#### 3.3.2.2 With Possessive Modifier (`NP_TYPE`=`def-np.poss`)

Constructions with possessive pronouns.

> (5) *\[his <u>pizza</u>\]*

Also includes potentially genitive or possessive modifier, if these are (potentially) anaphoric

> (6.a) *\[John\'s <u>pizza</u>\]*

> (6.b) *\[the <u>pizza</u> of John\]*

> (6.c) *\[the other man's <u>pizza</u>\]*

> (6.d) *\[this man's <u>pizza</u>\]*

**but not**: *\[a man's pizza\]*

#### 3.3.2.3 NP with "Other" (`NP_TYPE`=`def-np.other`)

Definite NPs containing adjectives like *other*

> (7) *the other man*

#### 3.3.2.4 Quantified Definite NP (`NP_TYPE`=`def-np.quant`)

At the moment, this includes cases where a quantifier is combined with a definite article (`the two men`) or with determiner \'both\'

> (8.a) *\[the two <u>pizzas</u>\]*
> (8.b) *\[both <u>pizzas</u>\]*

But not: *two pizzas*. As for constructions like *two of these pizzas*, this is formally a possessive construction.

> Note: Stede et al. (2016) include *all*+NP here. needs to be double-checked.

#### 3.3.2.4 With Definite Article (`NP_TYPE`=`def-np.the`)

Any NP with a definite article not covered by any aforementioned def-np category

> (7) *\[the <u>pizza</u>\]*

### 3.3.3  Proper Names and Titles (`NP_TYPE`=`ne`)

Typical instances of proper names are geographic places
(*Philadelphia*), persons (*Judge Jenkins*), companies (*Morgan
Stanley & Co.*), newspaper titles (*The New York Times*), political, social or financial institution names (*Congress, European Investment
Bank* ). Proper names can include noun modifiers or be heads of a definite or indefinite description. In this case, the whole description has to be marked up, not just the head.

> (8.a)  *\[Bertolt <u>Brecht</u>\]* (full name)

> (8.b)  *\[Bert <u>Brecht</u>\]* (reduced full name)

> (8.c)  *<u>Brecht</u>* (surname)
	
> (8.d) 	*<u>Bertolt</u>* (first name)
	
> (8.e) 	*<u>Bert</u>* (nickname)

> (8.f)   *<u>BB</u>* (abbreviation)

> (8.g)   *the well-known <U>Brecht</u>* (name, modified by a definite description)

> (8.h) *<u>Brecht</u>, who is author of the "Dreigroschenoper"* (proper name + clause)

> (8.i) *<u>Brecht</u>, author of the "Dreigroschenoper"* (proper name + apposition)

Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.
 
> (9.a) \[Dr. <u>Mueller</u>\]

> (9.b) \[Dr. <u>Martin</u> Luther King, Jr.\]

> (9.c) \[Prince <u>Dipangkorn</u> Rasmijoti Sirivibulyarajakumar of Thailand\]

> (9.d) \[Heidelberger <u>Druckmaschinen</u> Vertrieb Deutschland GmbH\]

Standalone titles that can stand in for an individual (*Mr./Ms./Dr./President/Chairman*) are treated like proper names, e.g., 

> (10) *Schröder~1~\...Fischer~2~ \... Die anfängliche Überreaktion von <u>Kanzler</u>~1~ und <u>Außenminister</u>~2~\...*

In (10), *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite

Parts of complex proper names cannot be analyzed separately. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

> (11) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*

## 3.4 Secondary Markables (no `REF_AUTO` annotation)

Every nominal phrase or pronoun which is neither primary markable nor (confirmed to be) syntactically bound, is subject to automated pre-annotation. Secondary markables are referring expressions that are unlikely/impossible anaphors, but that could *introduce* new discourse referents.

> Note: At the moment, these are automatically annotated for `NP_FORM`, but not for referentiality (`REF_AUTO`).

Common types of secondary marakbles include: indefinite NPs and indefinite or non-referring pronouns.

Annotate the secondary markable only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

> (12.c) *I saw \[a <u>cat</u>\] tonight in the street. <u>It(= the cat)</u> was gray.*

**but not**: *I saw a cat tonight in the street. <u>It(= the night/expletive?)</u> was pitch black.*


### 3.4.1 Indefinite NPs (`NP_TYPE`=`indef-np`)

With optional sub-types:

- `NP_TYPE=indef-np.a`: NP with an indefinite article (if subsequently referred to), e.g., *a fox*:
	
	> (12.a) *There is a \[a <u>fox</u>\] running across the street. <u>It</u>'s fast!.*
	
	> (12.b) *I last saw \[a <u>fox</u>\] about three years ago! <u>It</u> came from the forest.*

	Also includes indefinites with other, e.g. *another man* 

- `NP_TYPE=indef-np.quant`:   NPs with indefinite quantifier, also including quantified expressions not otherwise annotated as primary markables

	> (13.a) *\[some people\]*

	> (13.b) *\[some plants\]*

    > (14.c) *\[thirty grams\]*, *\[two companies\]* (quantified indefinite NP)

	Borderline case: indefinite NPs with an article that is identical (or at least derived from) the cardinal number *one* should be considered as quantified iff. a corresponding set of individuals has been previously evoked and the membership relation marked as being relevant.

	For English, the latter condition should hold for *one*, but not for
	*an, a*, for German, the membership relation should be regarded as being prominent if a substitution of the indefinite article *ein, eine* by colloquial *'n, 'ne* appears to be unlikely.

- `NP_TYPE=indef-np.bare`: articleless NP, especially \"bare plurals\", but also singular expressions.

    > (14.a) *I have eaten \[cookies\]SM* (bare plural)

    > (14.b) *Today will be \[good weather\]SM* (bare singular) 


### 3.4.2 Non-anaphoric pronouns (`NP_TYPE`=`pron`)

With optional sub-types:

- `NP_TYPE=pron.pint`: interrogative pronouns: *who, where, when, \...*

- `NP_TYPE=pron.pds`: indefinite demonstrative pronouns, e.g., *such*, in German *solch*

- `NP_TYPE=pron.pind`: indefinite pronouns, e.g., *somebody*, or German *man*. Also includes pronominal indefinite quantifiers, e.g., *some* in *some of that*.


## 3.5 Automated Pre-Annotation

- Check every nominal, pronoun, prepositional phrase, or proper name 
- If it is a primary markable, pre-annotate it with referentiality `?OLD`
- If it is a secondary markable, do not annotate it for referentiality.

> Note: Alternatively, annotate secondary markables with referentiality `?NEW`.

For every markable, annotate the syntactic head (as defined by the Universal Dependencies, exceptions as mentioned above) for type of referring expression.

## 3.6 Trouble-Shooting

### 3.6.1 Demonstratives

NPs with demonstrative determiner (English *this NP*, *that NP*, German *diese NP*, *jene NP*), and demonstrative pronouns (German *dieser*, English *this*, *that* [if not used as relative pronoun]) are primary markables.

The demonstrative pronoun *such* (German *solch*) is considered as indefinite. Refererring expressions with *such* should not be annotated as primary markables.

### 3.6.2 Bound Pronouns

Do not annotate bound pronoun, if these can be identified on grounds of their form or annotations. If a pronoun is ambiguous in its surface form and cannot be unambiguously confirmed as bound pronoun from the syntactic annotation, treat it like a primary markable and annotate with referentiality `?OLD`. Only in these cases, the annotator should then annotate referentiality `BOUND`.

### 3.6.3 Treatment of Quantifiers

Quantified NPs *(some of them, all the members)* are annotated as either definite or indefinite, whereas each case has to be considered individually. Substitution test: *all days* −→ *all these days* −→ definite.
In automated pre-annotation, every nominal phrase whose form does not rule out a definite interpretation should be treated as primary markable.

We regard NPs with certain quantifiers in determiner position such as *both* as definite, since German *beide* as English *both* normally presupposes the existence of exactly two discourse-old entities (cf. Zifonun et al. 1997).

*Both* in nominal use is annotated as a personal pronoun.

### 3.6.4 Possessive NPs

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

### 3.6.5 Appositions

Appositions are treated like predications. That is, they serve neither as antecedents nor anaphors. So, in the following example, *chairman* in *chairman of
Petrie Stores Corp.* should not be annotated!

> (17) *\[Milton <u>Petrie</u>, chairman \[of Petrie Stores Corp.\] said\...*

### 3.6.6 Stranded Quantifiers

An NP can be incomplete by elision and, at first glance, not meet the criteria of a markable.  For example, individual numerals are not usually PM, but íf their head noun is elided, they serve as heads of NPs, they can require an antecedent. 

> (18) *Now only three of the 12 judges - \[\[Pauline Newman\]n, (\[Chief
     Judge Howard T. Markey, 68\]m)two*1*, and (\[Giles Rich, 85\]r)two*
     2 *- have patent law backgrounds\]. \[The latter* *two\]~two~ and \[Judge Daniel M. Friedman, 73\]~f~ , are approaching senior status or retirement.* (WSJ corpus)

As these cases cannot be automatically identified, all pronominal numerals are to be annotated as primary markables. 

> 	(18') *Ich hatte \[zwei Stunden\]~PM~ eingeplant, aber es wurden letzlich \[drei\]~SM~.* (German)
>	(18") *I had planned for \[two hours\], but in the end, it was \[three\]~SM~* (English)

### 3.6.7 Proper Noun vs. definite NP

Note that if a proper noun is not a head of an NP, the NP is annotated as definite or indefinite respectively.

> (19) *the river Yukon* 

In (19), *Yukon* is the head. *Yukon* is a proper name, so the whole phrase is annotated as proper name.

> (20) *the Yukon office*

In (20), *office* is the head, *office* is not a proper name, so *the Yukon office* has to be annotated as a definite NP.

### 3.6.8 Non-referring Primary Markables

Non-referring markables (NM) are primary markables whose function is *not* to refer to a discourse referent. 
Non-referring markables are to be *manually* given the appropriate referentiality value in subsequent annotation (`GEN`, `EXPL`, `PRED`. `IDIOM` or `other`, see there). For automated extraction, they are treated like primary markables.

### 3.6.9 Do NOT annotate

-   expletive expressions

	> (21) *Then, when it would have been easier to resist them, nothing was done* (expletive *it*).

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

### 3.6.10 Idioms and Collocations

Primary markables in idioms and collocations, if identifiable in automated pre-annotation.

> (28) *It sent Kate into the pits when she learned from her "friend" Martha, who seemed to get off on laying bad trips on people, that Harvey was getting it on with Carol.* \[Gib94, p.265\]

According to Gibbs, we find several idiomatic phrases in this example, some of which contain pronouns or full NPs -- potential primary markables.

However, they should not be annotated as such, e.g. *into the pits* meaning "to be depressed", *get it on* meaning "having sexual relations", neither *the pits* nor *it* can be referred to.

Note that we consider only *conventionalized* idiomatic expressions as idioms in our sense,

i.e. markables within productive metaphors are annotated as usual, e.g. *das schlingernde City-Schiff City-Schiff* - a metaphor that occurred and can only be understood with respect to a specific text.

## 3.7 Grammatical role annotation (`GR`)

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

