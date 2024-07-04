# B. Technical Appendix

# B.1. Automated Pre-Annotation of Referring Expressions (Markables)

This text extends Sect. 3 with information about the automated pre-annotation of candidate referring expressions.

Texts for annotation should be automatically pre-annotated for referring expressions. 
This document contains the guidelines for the algorithm. Normally, this is irrelevant for manual annotation and can be skipped by annotators.

- their morphosyntactic type (`NP_FORM`)
- for potential anaphors, their expected referentiality (`REF_AUTO`, only value is currently `?OLD`), and
- their grammatical role (`GR`).

We describe `NP_FORM` and `REF_AUTO` as part of markable identification. `GR` annotation is described separately.

## B.1.1 Types of Markables

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

## B.1.2 Identifying the Syntactic Head

We only annotate the syntactic heads of markables according to the Universal Depenency syntax (See Sect. 3.3). Markables must never overlap, so we annotate at most one markable per word.

Automated pre-annotation builds on an existing layer of syntactic annotation *which will remain untouched* (even if it contains errors).

This also entails that referring expressions can *only* be annotated if they are identified as independent words by the word segmentation procedure adopted for that particular language. In (1), *Denver* and *bancruptcy* can only be identified as markables if they are (automatically annotated as) independent tokens.

> (1) *The \[Denver\]?-based concern, which emerged from bancruptcy \... its new, post-\[bancruptcy\]? law structure \...\"* (WSJ, 1328)

When converting head-based annotation to span-based annotation in downstream tasks, we assume that all dependents of a syntactic head are to be included in the markable:

> (2.a) *\[This <ins>right</ins>\]<sub>right</sub> may not be invoked \[in the case of <ins>prosecutions</ins> arising from acts contrary \[to the <ins>purposes</ins> \[of the United <ins>Nations</ins>\]UN\]purp\]prosec.* ([www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

> (2.b) *\[Dieses <ins>Recht</ins>\]<sub>right</sub> kann nicht in Anspruch genommen werden \[im Falle einer <ins>Strafverfolgung</ins> auf Grund von Handlungen, die \[gegen die <ins>Ziele</ins> \[der Vereinten <ins>Nationen</ins>\]<sub>UN</sub>\]<sub>purp</sub> verstoßen\]<sub>prosec</sub>.* (German, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

> (2.c) *\[Это <ins>право</ins>\]<sub>right</sub> не может быть использовано \[в случае
<ins>преследования</ins>, основанного на совершении деяния, противоречащего
\[<ins>целям</ins> \[Организации Объединенных <ins>Наций</ins>\]<sub>UN</sub>\]<sub>purp</sub>\]<sub>prosec</sub>.*
(Russian, [www.unhchr.ch/udhr](http://www.unhchr.ch/udhr), shortened)

## B.1.3 Primary Markables (`REF_AUTO`=`?OLD`)

Primary markables are automatically extracted from a syntactic analysis.<sub>[2](lit.md#refexp2)</sub>
The following criteria define the algorithm. Normally, annotators do not have to annotate PMs and they can skip this section. However, if you feel there may be an anaphoric expression that was missed in automated extraction, please resort to these definitions.

> Note: Incorrect PM prediction can result from parser errors. Annotators should mark manually introduced PMs with the comment `manual PM`.

> Note: Annotators must never delete an incorrectly extracted PM annotation, but you can mark it as non-referential and add the comment `parser error` to the annotation.

### B.1.3.1 Pronouns (`NP_TYPE`=`pron`)

As defined in Sect. 3.4.1., pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and possessived pronouns and *both* in nominal use (i.e. not as a determiner),<sup>[3](lit.md#refexp3)</sup>, e.g.,

> (3) *\[I\] saw \[her\] yesterday.*

If automated pre-annotation operates on a language/annotation schema that doesn't distinguish these types of pronouns from other (non-referring) types of pronouns, *every* pronoun should be annotated as primary markable.

> Note: Interrogative pronouns are not primary markables, but can serve as secondary markables.

> Note: Relative and reflexive pronouns are not primary markables. Their automated `NP_TYPE` annotation can be deleted.

- **Personal Pronouns** (`NP_TYPE`=`pron.pper`) include (the language-specific counterparts of) English *I, me, you, he, him, she, her, it, we, us, they, them* (see Section 3.4.1).  Every pronoun should be annotated as `REF_AUTO=?OLD` if it is **formally identical with a personal pronoun**, regardless of its actual syntactic function or reference.
- **Possessive Pronouns** (`NP_TYPE`=`pron.ppos`) include (the language-specific counterparts of) English *my, mine, your, yours, \...*.
- **Demonstrative Pronouns** (`NP_TYPE`=`pron.pds`) with optional sub-classes: 
	- `NP_TYPE=pron.pds-prox`: proximal *this, these*, *this one*, German *der, die, das, \...*
	- `NP_TYPE=pron.pds-dist`: distal *that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes, derjenige,* and the like.
- **Pronominal Adverbs** (`NP_TYPE`=`pron.padv`) are derived from pronouns but grammaticalized as adverbs. If a pronominal adverb is unambiguous as to that it is a referring expressiong (e.g., German *deswegen* "because of this") it is to be annotated as `REF_AUTO=?OLD`, otherwise not as a referring expression. We explicitly exclude references to time and place of the speaker (*here*, *hence*) if these are unambiguous in their deictic function, as well as interrogative adverbs (*where*, etc.). 

Annotate semi-demonstrative pronouns (English *such*, German *solch*) as `REF_AUTO=?NEW`. Do not annotate (unambiguous cases of) bound pronouns, e.g., relative pronouns (English *which*). Pronouns that are formally ambiguous as to whether they are relative or demonstrative pronouns (e.g., English *that* in relative clauses), are PM, and should be manually marked as `REF=BOUND` in the annotation.


### B.1.3.2 Definite Descriptions (`NP_TYPE`=`def-np`)

A description (NP or PP) is definite if it contains the determiner *both*, a demonstrative or possessive pronoun or a genitive attribution (Sect. 3.4.2). In automated pre-annotation, this should be made explicit with sub-types:

> Note: In languages without morphosyntactic definiteness marking, automated preannotation should consider every NOUN that is the head of a noun phrase a potential anaphor, and thus annotate these as `NP_TYPE=def-np.bare`.

- **demonstrative NP** (`NP_TYPE`=`def-np.dem`)

	> (4) *\[that <ins>pizza</ins>\]*, *\[this <ins>pizza</ins>\]*

	If a language distinguishes demonstratives with respect to their relative proximity, this should be reflected in the corresponding sub-type:

	- `NP_TYPE=def-np.dem-prox`: proximal *this man*, \...
	- `NP_TYPE=def-np.dem-dist`: distal *that man*, \...

- **possessive NP** (`NP_TYPE`=`def-np.poss`) for constructions with possessive pronouns:

	> (5) *\[his <ins>pizza</ins>\]*

	Also includes potentially genitive or possessive modifier, **but only** if these are annotated as `REF_AUTO=?OLD`:

	> (6.a) *\[John\'s <ins>pizza</ins>\]*

	> (6.b) *\[the <ins>pizza</ins> of John\]*

	**but not**: *\[a man's pizza\]*

- **Quantified Definite NPs** (`NP_TYPE`=`def-np.quant`) this includes cases where a quantifier is combined with a definite article (`the two men`) or with determiner \'both\'

	> (7.a) *\[the two <ins>pizzas</ins>\]*
	> (7.b) *\[both <ins>pizzas</ins>\]*

	But not: *two pizzas*. As for constructions like *two of these pizzas*, this is formally a possessive construction.

	> Note: Stede et al. (2016) include *all*+NP here. needs to be double-checked.

- **definite NP with "other"** (`NP_TYPE`=`def-np.other`), i.e., definite NPs containing adjectives like *other*

	> (9) *the other man*

	Note that the `other` flag can be attached after *any* def-np subtype, so, the following tags are valid:

	- `def-np.other` (for otherwise unclassified definite NPs)
	- `def-np.dem.other` (for otherwise unclassified demonstrative NPs)
	- `def-np.dem.prox.other`: *this other man*
	- `def-np.dem.dist.other`: *that other man*
	- `def-np.poss.other`: *his other goal*
	- `def-np.quant.other`: *the two other guys*
	- `def-np.the.other`: *the other man* 

- **NP with definite article** (`NP_TYPE`=`def-np.the`): any NP with a definite article not covered by any aforementioned def-np category

	> (8) *\[the <ins>pizza</ins>\]*

- *in languages without morphosyntactic definiteness marking*: NP without determiner for which a definite interpretation cannot be ruled out should be annotated `NP_TYPE=def-np.bare`. Note that this applies to the heads of noun phrases only.

	> (8.a) *Я стоял \[на <ins>коврике</ins> у камина\]* (Russian)
	> "I stood upon the hearth-rug" (the original source sentence, Doyle, Hound of the Baskervilles)

### B.1.3.3  Proper Names and Titles (`NP_TYPE`=`ne`)

Proper names include names of geographic places, persons, companies, political, social or financial institution names (Sect. 3.4.3).

Standalone titles that can stand in for an individual (*Mr./Ms./Dr./President/Chairman*) are treated like proper names, e.g., 

> (10) *Schröder<sub>1</sub>\...Fischer<sub>2</sub> \... Die anfängliche Überreaktion von <ins>Kanzler</ins><sub>1</sub> und <ins>Außenminister</ins><sub>2</sub>\...*

In (11), *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite

Complex proper names are only treated as a single markable and are not further divided. Parts of complex proper names can thus not be analyzed separately. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

> (11.b) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*

## B.1.4 Secondary Markables (no `REF_AUTO` annotation, but annotations for `NP_TYPE`)

Every nominal phrase or pronoun which is neither primary markable nor (confirmed to be) syntactically bound, is subject to automated pre-annotation. Secondary markables are referring expressions that are unlikely/impossible anaphors, but that could *introduce* new discourse referents.

> Note: At the moment, these are automatically annotated for `NP_FORM`, but not for referentiality (`REF_AUTO`).

Common types of secondary markables the following `NP_TYPE`s:

- Indefinite NPs (`NP_TYPE`=`indef-np`) With optional sub-types:

	- `NP_TYPE=indef-np.a`: NP with an indefinite article, e.g., *a fox*:
	
		> (12.a) *There is a \[a <ins>fox</ins>\] running across the street. <ins>It</ins>'s fast!.*
	
		> (12.b) *I last saw \[a <ins>fox</ins>\] about three years ago! <ins>It</ins> came from the forest.*

		Also includes indefinites with other, e.g. *another man* 

	- `NP_TYPE=indef-np.quant`:   NPs with indefinite quantifier, also including quantified expressions not otherwise annotated as primary markables

		> (13.a) *\[some people\]*

		> (13.b) *\[some plants\]*

		> (14.c) *\[thirty grams\]*, *\[two companies\]* (quantified indefinite NP)

	- `NP_TYPE=indef-np.bare`: articleless NP, especially \"bare plurals\", but also singular expressions.

	    > (14.a) *I have eaten \[cookies\]SM* (bare plural)

	    > (14.b) *Today will be \[good weather\]SM* (bare singular) 


- Non-anaphoric pronouns (`NP_TYPE`=`pron`) With optional sub-types:

	- `NP_TYPE=pron.pint`: interrogative pronouns: *who, where, when, \...*

	- `NP_TYPE=pron.pds`: indefinite demonstrative pronouns, e.g., *such*, in German *solch*

	- `NP_TYPE=pron.pind`: indefinite pronouns, e.g., *somebody*, or German *man*. Also includes pronominal indefinite quantifiers, e.g., *some* in *some of that*.

- Other expressions (`NP_TYPE`=`other`), e.g., for foreign language expressions (`X` in Universal Dependencies), if identifiable as a syntactic argument of a verb.

## B.1.5 Automated Pre-Annotation

- Check every nominal, pronoun, prepositional phrase, or proper name 
- If it is a primary markable, pre-annotate it with referentiality `?OLD`
- If it is a secondary markable, do not annotate it for referentiality.

> Note: Alternatively, annotate secondary markables with referentiality `?NEW`.

For every markable, annotate the syntactic head (as defined by the Universal Dependencies, exceptions as mentioned above) for type of referring expression.

## B.1.6 Trouble-Shooting

### B.1.6.1 Demonstratives

NPs with demonstrative determiner (English *this NP*, *that NP*, German *diese NP*, *jene NP*), and demonstrative pronouns (German *dieser*, English *this*, *that* [if not used as relative pronoun]) are primary markables.

The demonstrative pronoun *such* (German *solch*) is considered as indefinite. Refererring expressions with *such* should not be annotated as primary markables.

### B.1.6.2 Bound Pronouns

Do not annotate bound pronoun, if these can be identified on grounds of their form or annotations. If a pronoun is ambiguous in its surface form and cannot be unambiguously confirmed as bound pronoun from the syntactic annotation, treat it like a primary markable and annotate with referentiality `?OLD`. Only in these cases, the annotator should then annotate referentiality `BOUND`.

### B.1.6.3 Treatment of Quantifiers

Quantified NPs *(some of them, all the members)* are annotated as either definite or indefinite, whereas each case has to be considered individually. Substitution test: *all days* −→ *all these days* −→ definite.
In automated pre-annotation, every nominal phrase whose form does not rule out a definite interpretation should be treated as primary markable.

We regard NPs with certain quantifiers in determiner position such as *both* as definite, since German *beide* as English *both* normally presupposes the existence of exactly two discourse-old entities (cf. Zifonun et al. 1997).

*Both* in nominal use is annotated as a personal pronoun.

### B.1.6.4 Possessive NPs

Primary markables include

> (15.a) *his house*
> (15.b) *the old man's house*

Note that the possessor must be a primary markable, too: *\[\[his\] house\]*, *\[\[the old man's\] house\]*.

Descriptions with a genitive attribution are regarded as possessive iff. a definite genitive attribution replaces the determiner, except for *of* -constructions (cf. ex. 16.b).

> (16.a) *the old man's house* (definite possessive description, cf. *his house* and \**the the old man's house*)
> (16.b) *the house of the old man* (definite non-possessive description: determiner in *the house* relates to the house itself and not to its possessor)
> (16.c) *an old's man house*(this is not a primary markable - the possessor is indefinite)

Possessive NPs with indefinite possessor (16.c) are secondary markables. However, possessives with proper names should generally be considered as primary markables.

> (16.d)   *in US <ins>efforts</ins>*

This is a primary markable because there is a reading, where the phrase could be replaced with *in the US efforts*.

### B.1.6.5 Appositions

Appositions are treated like predications. That is, they serve neither as antecedents nor anaphors. So, in the following example, *chairman* in *chairman of
Petrie Stores Corp.* should not be annotated!

> (17) *\[Milton <ins>Petrie</ins>, chairman \[of Petrie Stores Corp.\] said\...*

### B.1.6.6 Stranded Quantifiers

An NP can be incomplete by elision and, at first glance, not meet the criteria of a markable.  For example, individual numerals are not usually PM, but íf their head noun is elided, they serve as heads of NPs, they can require an antecedent. 

> (18) *Now only three of the 12 judges - \[\[Pauline Newman\]n, (\[Chief
     Judge Howard T. Markey, 68\]m)two*1*, and (\[Giles Rich, 85\]r)two*
     2 *- have patent law backgrounds\]. \[The latter* *two\]<sub>two</sub> and \[Judge Daniel M. Friedman, 73\]<sub>f</sub> , are approaching senior status or retirement.* (WSJ corpus)

As these cases cannot be automatically identified, all pronominal numerals are to be annotated as primary markables. 

> 	(18') *Ich hatte \[zwei Stunden\]<sub>PM</sub> eingeplant, aber es wurden letzlich \[drei\]<sub>SM</sub>.* (German)
>	(18") *I had planned for \[two hours\], but in the end, it was \[three\]<sub>SM</sub>* (English)

### B.1.6.7 Proper Noun vs. definite NP

Note that if a proper noun is not a head of an NP, the NP is annotated as definite or indefinite respectively.

> (19) *the river Yukon* 

In (19), *Yukon* is the head. *Yukon* is a proper name, so the whole phrase is annotated as proper name.

> (20) *the Yukon office*

In (20), *office* is the head, *office* is not a proper name, so *the Yukon office* has to be annotated as a definite NP.

## B.1.6 Grammatical role annotation (`GR`)

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

