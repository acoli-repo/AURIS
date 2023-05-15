PoCoS Coreference Scheme (October 25, 2005)

Christian Chiarcos,  University of Potsdam, <chiarcos@ling.uni-potsdam.de>

Olga Krasavina, Humboldt-University of Berlin, <krasavio@rz.hu-berlin.de>

Abstract

This document outlines the guidelines for anaphoric annotation applied to the RST Discourse Treebank (Carlson et al. 2003) and Potsdam
Commentary Corpus (Stede 2004). Anaphoric annotation is notoriously problematic, because it often leads to ambiguous and subjective interpretation. As a result, existing schemes are either too general
(Hirschman 1998) or too specific and therefore of limited applicability. We have achieved a compromise between these two extremes as follows:

-   We have introduced scheme instantiations of different granularity by distinguishing between fundamental and project-specific levels of annotation (cf. Poesio et al. \[1999\]): a core scheme, which is general and reusable, and an extended scheme, which supports a wider range of features. A final set of extended features can be determined according to varying research goals.

-   We have provided a hierarchical formulation of feature values allowing for the possibility of underspecification on either level.

Both strategies of underspecification guarantee that the scheme remains flexible for possible extensions, enabling the researcher to choose between a higher or lower level of detail in the annotation.
Furthermore, our scheme is of dynamic character in its provision of the option of continuous adjustment: it can be adapted to new decisions made respective to initially unanticipated issues.

In addition to the introduction of underspecification as a central concept, the proposed scheme implements preferences for ambiguity resolution, in order to increase inter-annotator agreement. Evaluation of the annotation is currently in progress. The primary application of this scheme covers both English and German corpora.

As an as yet unique feature, both corpora will combine annotation of coreference and discourse structure with regard to Rhetorical
Structure Theory (Mann/Thompson 1988, Reiter/Stede 2003). The scheme's field of application encompasses natural language generation, text summarisation, anaphora resolution and corpus-based analysis of discourse structure and anaphora.

# General remarks

Definition: Anaphoric annotation

Most texts involve repeated mentions of the same entity as well as references to objects related in various ways to what has already been discussed. Annotating corpora with information about such relations between elements of a text is useful both from a linguistic point of view and for applications such as information extraction.

Subsequent mentions of an entity can have the same surface form - as when the expression *the Lord Provost* is encountered twice in a text - or different ones. Anaphoric expressions are used to indicate that elements of a text are correlated. The simplest forms of anaphoric expression are used to indicate a subsequent mention of an object already introduced: typical examples of this type of anaphoric expression are pronouns such as *he* in the text *John arrived.
[He] looked tired.* In the preferred reading of this text, the pronoun *he* is interpreted as an 'abbreviated reference,' to the individual John which is denoted by the expression *John*. (Poesio et al. 1999)

## Goals

The current scheme is intended to be used for corpus annotation of coreference, which has to serve the following purposes:

-   theoretical research

    -   rhetorical distance and accessibility

    -   properties of referential expressions

    -   salience heuristics

-   NLG and related fields of practical application

    -   generating referring expressions

    -   substitution tests for evaluation

    -   summarization

    -   anaphora resolution

Besides coreference annotation itself, we include a set of linguistic features of markables for later evaluation (see Sec. 3 and 7.3)

## Structure

This document consists of:

-   General annotation scheme:

a core scheme, which incorporates the basic features and is intended to be general and reusable ( see Sections 2-6)

an extended scheme, which involves optional features, which are defined for each project specifically, i.e. the level of detail is set up with particular goals in mind (see Section 7)

-   Scheme adjusted to pecularities of German and English

-   Annotation guidelines for annotation with the MMAX annotation tool

All examples below, unless noted otherwise, have been extracted from the corpora, on the basis of which this scheme was built and for which exploration it is designed: Potsdam Commentary Corpus (PCC) (Stede
2004) and RST Discourse Treebank (Carlson et al. 2003).

## Scope of the annotation

### Markables

Definition Principally, markables are defined as a cover-term of anaphors and (potential) antecedents of anaphors. Semantically, these expressions denote prototypical entities or "(discourse) referents"
(Karttunen 1975). A discourse referent is an entity that is being referred to in the discourse. Syntactically, a markable is typically a noun phrase or a prepositional phrase.

However, we suggest a definition in both syntactic and semantic terms by splitting the annotation of markables into two steps.

1.  [primary] [markables] prototypically express anaphors, e.g. third-person personal pronouns (further - pronouns).

2.  [secondary] markables are normally non-anaphoric (e.g. generic NPs, sentences) per se and are subject to annotation only if being an antecedent for a primary markable.

Below a syntactically-based heuristics of identifying both primary and secondary markables is presented.

primary markables

-   pronouns

-   definite noun phrases (defNPs)

-   proper names

-   pronominal adverbs

-   prepositional phrases

-   zeros (X)

-   reflexives (X)

-   interrogatives (X)

secondary markables

-   indefinite descriptions

-   indefinite pronouns

-   clauses or groups of clauses

### Relations

We distinguish between two major types of anaphoric relations: nominal and non-nominal relations, see fig. 1

# Core scheme

## Markables

Markables are textual expressions between which anaphoric relations can be established. Only nominal expressions are considered in the core scheme.

## Primary and secondary markables

The scheme distinguishes between primary and secondary markables.
Primary markables are *always* subject to annotation. Secondary markables are only annotated if they happen to serve as antecedents for primary markables.

primary markables

-   personal pronouns and demonstrative pronouns

-   definite and possessive descriptions

-   proper names and titles

-   pronominal adverbs

Coordination of primary markables, e.g. *Bush and Putin* is also a primary markable! ^1^

\(1\) *\[\[Bush\] and \[Putin\]\]*

secondary markables

-   indefinite descriptions

-   other markables that are not labelled as primary markables but serve as antecedents for them (cf. ex. 20, p. 10). Note that this does not apply to sentences!

So, if the antecedent of an anaphor is an indefinite expression, declare it as a new markable. In this case, indefinite descriptions can be markables as well. Otherwise, do not annotate indefinite descriptions as markables, even if they are in some (non-anaphoric) relation to other discourse entities.

Indefinite descriptions include

-   nominal descriptions with an indefinite article (*a dog*)

-   nominal descriptions without an article (*business, two companies*)

Principle 1 (Primacy of markables as antecedents) *If there are primary markables that can be antecedents of a markable, establish a link to these, rather than declaring secondary markables, even if a primary markable is located further to the left from the anaphor compared to the possible secondary markable.*

## Semantic description of primary markables

### Definite descriptions

A description is [definite] if it contains a determiner
*both*^2^ (2a, 2b), a demonstrative (2c) or possessive pronoun (2d) or a genitive attribution (2e). Quantified NPs *(some of them, all the members)* are annotated as either definite or indefinite, whereas each case has to be considered individually. Substitution test: *all days*
−→ *all these days* −→ definite.

*Both* in nominal use is annotated as a personal pronoun.

^1^In case of coordination of a primary and a secondary markables, the whole coordinated NP must be annotated as a primary markable. If the markables within a coordination have different features, annotate the values of these features as *other*.

^2^We regard NPs with certain quantifiers in determiner position such as *both* as definite, since German *beide* as English *both* normally presupposes the existence of exactly two discourse-old entities (cf.
Zifonun et al. 1997).

(2.a) *the pizza*

(2.b) *both pizzas*

(2.c) *that pizza, this pizza*

(2.d) *his pizza*

(2.e) *John's pizza*

Boarder-line cases:

-   *in US efforts*

Test: in the US efforts −→ definite

### Possessive descriptions

(3.a) *his house*

(3.b) *the old man's house*

Note, that the possessor must be a primary markable, too: *\[\[his\] house\]*, *\[\[the old man's\] house\]*.

Descriptions with a genitive attribution are regarded as possessive iff. a definite genitive attribution replaces the determiner, except for *of* -constructions (cf. ex. 4b).

(4.a) *the old man's house* (definite possessive description, cf. *his house* and \**the the old man's house*)

(4.b) *the house of the old man* (definite non-possessive description: determiner in *the house* relates to the house itself and not to its possessor)

(4.c) *an old's man house*(this is not a primary markable - the possessor is indefinite)

### Proper names and titles

Typical instances of proper names are geographic places
(*Philadelphia*), persons (*Judge Jenkins*), companies (*Morgan
Stanley & Co.*), newspaper titles (*The New York Times*), political, social or financial institution names (*Congress, European Investment
Bank* ). Proper names can include noun modifiers or be heads of a definite or indefinite description. In this case, the whole description has to be marked up, not just the head.

(5.a) *Berthold Brecht* (full name) (5.b) *Bert Brecht* (reduced full name) (5.c) *Brecht* (surname)

(5.d) *Berthold* (first name) (5.e) *Bert* (nickname)

(5.f) *BB* (abbreviated)

(5.g) *the well-known Brecht* (name, modified by a definite description)

(5.h) *Brecht, who is author of the "Dreigroschenoper"* (proper name + clause) (5.i) *the well-known Brecht* (name, modified by a definite description)

(5.j) *Brecht, author of the "Dreigroschenoper"* (proper name + apposition)

Titles in conjunction with proper names
(*Mr./Ms./Dr./President/Chairman*) or standing alone are treated like proper names as well, e.g.

(6) *Schr¨oder~s~\...Fischer~f~ \... Die anf¨angliche U¨berreaktion von
    Kanzler~s~ und Außenminister~f~\...*

Here, *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite and thus fall under the definition of primary markables.

Parts of complex proper names cannot be analyzed separately. Proper names are primitive. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

(7) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*

Note that if a proper noun is not a head of an NP, the NP is annotated as definite or indefinite respectively.

(8) *the river Yukon* - *Yukon* is the head. *Yukon* is a proper name, so the whole phrase is annotated as proper name.

(9) *the Yukon office* - *office* is the head, *office* is not a proper name, so *the Yukon office* has to be annotated as a definite NP.

### Pronouns

Pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and personal pronouns and *both* in nominal use, see fig.
8.1.1 in Appendix for detailed list of forms. In German, demonstrative pronouns include: *dieser, jener, der, die, derjenige,* and the like
Note that demonstrative pronouns *such*, in German *solch* and so-called "generic pronouns" (*we, you, they*, in German *wir, du, sie* (without specific reference), *man, einer*) are considered as indefinite, thus no primary markables.

### Do NOT annotate

-   expletive expressions

(10) *Then, when it would have been easier to resist them, nothing was done*

(expletive *it*).

-   *Es*-pronouns, pronominal adverbs, which are controllers of relative clauses

(11) *Dazu kommt, dass in Werder am 24. Februar ein Bu¨rgermeister gewa¨hlt wird und es bisher als sicher galt, dass CDU-Amtsinhaber
     Werner Gr¨oße unangefochten bleibt.*

*Dazu\...dass, es\...dass* should not be annotated as markables
(*Dazu* and *es* are controllers of relative clauses).

-   primary markables in idioms and collocations

(12) *It sent Kate into the pits when she learned from her "friend"
     Martha, who seemed to get off on laying bad trips on people, that
     Harvey was getting it on with Carol.* \[Gib94, p.265\]

According to Gibbs (??), we find several idiomatic phrases in this example, some of which contain pronouns or full NPs -- potential primary markables.

However, they should not be annotated as such, e.g. *into the pits* meaning "to be depressed", *get it on* meaning "having sexual relations", neither *the pits* nor *it* can be referred to.

Note that we consider only *conventionalized* idiomatic expressions as idioms in our sense,

i.e. markables within productive metaphors are annotated as usual, e.g. *das schlingernde City-Schiff City-Schiff* - a metaphor that occurred and can only be understood with respect to a specific text.

-   pronominal adverbs functioning as discourse markers

(13.a) *Ich habe dich angesprochen, damit du mir zuh¨orst*.

"I am talking to you to let you know that you must listen to me."
(13.b) *Ich habe dir das gesagt, damit du weißt, dass du mir zuh¨oren sollst*. (13.c) *Ich habe dir das gesagt, dass du weißt, dass du mir zuh¨oren sollst.*

-   relative pronouns

Relative pronouns are annotated together with the whole relative clause it triggers as one

single markable (cf. *\[The car that went through his garden wall\]\...*). If a form cannot be unambiguously classified as a relative pronoun, apply the following test: it is a relative pronoun if it can be substituted by "which" respectively "welch" in German.
However, relative pronouns in possessive constructions (i.e. for which the test for relative pronouns fails) are annotated as possessive pronouns (see possessive NPs, p. 10).

(14) *Und so schielen die Israelis nach Washington, an dessen /\*welchem
     Tropf sie wirtschaftlich und milit¨arisch h¨angen,\...*

cf. *Und so schielen die Israelis nach Washington, das/welches sie wirtschaftlich und milit¨arisch unterstu¨tzt* (*das* is a relative pronoun).

Alternatively, the following test can be applied: substitute a pronoun in question with a possessive construction. If it works, you have a possessive pronoun, not a relative one.

(15) *die Frau und deren Kinder = die Frau und ihre Kinder*

The annotation is as follows in this case:

(16) *Und so schielen \[die Israelis\]i \[(nach Washington)w, \[an
     \[dessen\]w Tropf\] \[sie\]i wirtschaftlich und milit¨arisch h¨angen\]~w~*′ *,\...*

     -   prepositional phrases with prepositions *as, than*, *bis, als, wie* (in German) Such prases are annotated as normal NPs, i.e. *bis* and *als* are not included. ^3^

     -   nominal premodifiers in compound nouns

(17) *peanut butter, airline analyst, the creditors commettee, investment bank*

*Peanut, airline, cretitors* and *investment* are no separate markables. Note that in *the creditor's opinion*, *the creditor's* is annotated as a markable, since it is a nominal in genitive and thus not a part of a compounds (see also 2.3.2, 2.3.3).

## Syntactic description of markables

Generally, prototypical markables are nominal descriptions, including prepositional phrases (PPs) and noun phrases (NP).

### Prepositional phrases

Prepositional phrases consist of a preposition and a complement, most typically in the form of a noun phrase. The typical prepositional phrase may indeed be viewed as a noun phrase extended by a link showing its connection to surrounding structures. \[Bib99, p.103\]

A similar linking function is fulfilled by case marking, too, thus we consider prepositional phrases and noun phrases to be instances of the same underlying category of markables.

We try to keep our scheme language-independent. Due to language-specific variation in the use of prepositional phrases or inflectional morphology we decided to provide a definition that subsumes both extremes under one label. Thus, whenever a NP appears as the complement of a PP, the whole PP is assigned the status of a markable, not the embedded NP itself.

Note that the following prepositions and nominal conjunctions, as mentioned in the previous subsection, should NOT be annotated:

-   bis: *Bis zum n¨achsten Schachzug*

-   als: *Als 1999 die im Rahmen der Dorferneuerung gestaltete Radweger
    Ablage\...eingeweiht wurde, \...*

In our scheme, this principle is applied to both English and German.
However, morphosyntactical motivation is primarily from German, where compound forms (pronominal adverbs) and inflected definite prepositions (*am Fenster*) exist, in which the preposition has become an integral part of the referring expression.

(18) *in the period, in Japan, at its factories, of the preferred stock*
     (preposition plus a noun phrase)

Pronominal adverbs are included in the class of primary markables, too. A list for German pronominal adverbs in provided in Appendix in fig. 8.1.3.

Postpositions are treated like prepositions, i.e. such phrases as *two years ago*, *von Beruf wegen*

are prepositional phrases.

### Size of markables

The boundaries of a markable are defined according to the Maximum Size
Principle.

Principle 2 (Maximum size principle) *Markables of maximum size are subject to annotation. That is:*

1.  *one markable includes all attributes of its head noun: relative clauses, appositions, modifiers and complements, right and left dislocations -- marked bold in the examples below,*

2.  *coordinated NPs/PPs are double-annotated: 1) members of a coordinated NP/PP separately and 2) the whole coordinated NP/PP as one markable.*

^3^The basic features of prepositions are 1) to control the case, 2) to occur in preposition to nominal or pronominal expresions (cf.
IDS:2078)

(19.a) \[*The car that went through his garden wall* \] \... (relative clause)

(19.b) \[*The pattern of industrial development in the US* \] \... (NP with modifiers) (19.c) \[*Jerald Lefcourt, a criminal defence attorney* \] \... (apposition)

(19.d) *\[That picture of a frog\]p*1 *, where is \[it\]p*2 (left dislocation)

(19.e) *I think \[he\]~d~*~1~*'s getting hooked on the taste of
Vaseline, \[that dog\]~d~*~2~*.* (right dislocation/afterthought)

(19.f) *\[\[Schr¨oder\] und \[Fischer\]\]*

If a possessive pronoun occurs in a construction like "head noun + participle/relative clause/apposition", we establish a *secondary* markable containing the controller (of a relative clause, a modifier

or a complement) alone.^4^ So, \[*his*\] below refers not to the whole description *\[(Judge Jenkins), now known in his courthouse\]*, but only to the secondary markable *(Judge Jenkins)*. In case of further references to the referent (*Judge Jenkins*), the whole phrase (i.e. of maximum size)

\- \[*(Judge Jenkins), now known in his courthouse as Shake'Em Down
Jenkins*\] - has to be annotated as antecedent.

\(20\) *"My belief is always, if you've got a settlement, you read it into the record," says \[(Judge Jenkins)j, now known \[in \[\[his\]j courthouse\]\] as \[Shake'Em Down Jenkins\]\].*

Markables including appositions, relative clauses, etc. are more complex in their nature and therefore receive a special tag in the scheme: "complex-np"(see 4). A simple test can be used, in order to determine if an NP is complex: *if a description consists of more than one nominal (not pronominal) phrase, consider it a complex description*. Nominal phrases "are phrases headed by nouns and able to function as complement in clause structure: "the dog barked"(subj), "I found the dog" (obj), "this is a dog" (predicative). " (cf. Longman)

(21.a) *its financial adviser* - not a compex NP (*its* is a pronoun and *financial* is an adjective)

(21.b) *of NBI shares* - NBI cannot be modified, cf. *the NBI shares, very popular NBI shares*: *the*, *very popular* modify *shares*, rather than *NBI*. Thus, *NBI* is not an independent noun phrase.

(21.c) *all \[the preferred stock\]* - the same Prototypical complex
NPs are:

(22.a) *the surplus or profit required under Delware law for payment of the dividend*

(22.b) *NBI, a maker of word processing systems*

(22.c) *its financial advisor and investment banker*

Border-line case:

(23.a) *the stock's holder* -- a complex np (*the stock's* is an independent NP)

(23.b) *the stock holder* -- not a complex np (*\[the\] stock* is not an independent NP: it cannot be modified, see below)

(23.c) *\*\[the great stock\] holder*

(23.d) *\*the \[great stock\] holder*

Titles constitute a border-line case for this test, as they can be modified: (24.a) *president Bush*

(24.b) *\[the American president\] Bush*

(24.c) *#the American Bush* (illustrates that *American* modifies
*president*, but not the head noun)

By default, these are regarded as being *not complex*.

X' constructions are not complex.

\(25\) *unter den J¨agern und Sammlern*

^4^Note, that the controller of a relative clause cannot be a primary markable. It is not a complete markable (of maximum size), thus, it would not have been annotated at all if there was no direct reference towards it.

On the other hand, the anaphoric possessive pronoun cannot refer to the established primary markable. If annotated in this way, the pronoun itself would be a part of its antecedent.

### Discontinuous markables

A markable does not necessarily consist of contiguous elements. As an example, consider split-NP constructions in German.

\(26\)

*\[Bu¨cher\]~b~*~2~

*books*

*hat has*

*Anna Anna*

*\[drei\]~b~*~2~ *three*

*"Anna has three books./As for books, Anna has three of them"*

(split-NP)

(27) *You'll meet \[a man\]m1 tomorrow \[carrying a heavy parcel\]m2*
     (Quirk et al. 2003:930) An important example of discontinuous markables is "group-references", see below.

### Group-references

Reference to groups can be carried out by means of plural pronouns
(e.g. *they*) and plural NPs, including quantified NPs (e.g.
*both*-NPs), which can have separate members of these groups as antecedents. So, antecedents of plural pronouns can be non-contiguous, i.e. mentioned in different parts of a sentence or in separate clauses.

(28) *\[\[Montedison\]m\]c*1 *now owns about 72% of
     \[\[Erbamont's\]e\]c*2 *shares outstanding.*

*\[The companies\]c said the accord was unanimously approved by a special committee of \[Erbamont\]e directors unaffiliated with
\[Montedison\]m.*

Such groups can subsume markables with different properties (e.g. grammatical form and role). For these cases, we suggest an additional layer besides primary and secondary markables named groups. Groups can serve as antecedents of nominal markables (but not as anaphors). Thus, group references are annotated as follows:

1.  annotate separate elements (members of the group, here *Montedison* and *Erbamont*) as primary (or secondary) markables as usual,

2.  annotate the first element (*Montedison*) as a group markable,

3.  append the second element (*Erbamont*) to the first one, thus merging both elements into a "discontinuous markable".

We suggest the primacy of referent's identity to the recency of mention. In case individual referent's mentions have been annotated as a group somewhere, the reference is established to this group rather than to individual mentions even right-most (i.e. the closest to an anaphor). A referent of a group, although often being the sum of its parts, is not the same as a referent of one of its parts. So, in the example below, which represents a sample referential chain, *they* refers to *both*, rather than to individual mentions of *Sharon* and
*Arafat*, although these individual mentions are more recent and thus closer to the anaphor (*they)*.

(29) *Sharons\... Arafata\... boths*+*a \... Sharons \... Arafata \... theys*+*a\...*

Besides this, the principle proposed on page 6 can be extended as follows.

Principle 3 (Primacy of markables as antecedents (extended)) *If there are primary or secondary markables that can be antecedents of a markable, establish a link to these, rather than declaring group markables, even if a primary or secondary markable is located further to the left from the anaphor compared to the possible group markable.*

Border-line case:

(30) *Now only three of the 12 judges - \[\[Pauline Newman\]n, (\[Chief
     Judge Howard T. Markey, 68\]m)two*1*, and (\[Giles Rich, 85\]r)two*
     2 *- have patent law backgrounds\]. \[The latter*

*two\]~two~ and \[Judge Daniel M. Friedman, 73\]~f~ , are approaching senior status or retirement.*

Although *Chief Judge Howard T. Markey, 68* and *Giles Rich, 85* occur within the one and same sentence, the conjunction of them is not a separate markable, but just a part of a larger phrase.

# Relations between markables

## Anaphoric relations

Only *anaphoric* relations have to be annotated. The definition of anaphora used here conforms to the one used in MUC-based schemes: it is "identity-of-reference direct nominal anaphora, which can be regarded as the class of single-document identity coreference"
\[Mit00\].

Test: to find out, if two nominal descriptions are coreferent, try to substitute them with each other. Note that the anaphoric relation is inherently transitive, thus every previous coreferent markable has to be compatible with this substitution as well.

(31) *Als 1999 die im Rahmen der Dorferneuerung neu gestaltete
     \[Radeweger\]r Ablage inklusive Seebru¨cke mit viel Pomp eingeweiht wurde\... Doch mit der Nachru¨stung tut sich
     \[Radewege\]r* ′ *schwer\... Zu teuer, zu h¨asslich sei die Anlage, sagen die Meinungsfu¨hrer \[im Gemeinderat\]g*

In this example, *\[Gemeinderat\]* could be coreferent with
*\[Radewege\]r* ′ . Although both are exchangeable by means of metonymy, substitution test fails for *\[Radewege\]r* , since *neu gestaltete Gemeinderatsablage* is not appropriate in that context.

If a relation other than identity holds between a primary markable and its antecedent, annotate it as follows:

-   the value of referentiality feature is *referring* ;

-   BUT: the value of relation feature is *non* (rather than anaphoric)!

Cases of metonymy in text should also be annotated as anaphoric relations if the identity relation between the referents in a text retains (metonymy is substituting a word for another word closely associated with it): *the State Department said\... - the Stated
Department officials claimed\...*.

### 3.1.1 Choice of the antecedent 

For annotation of antecedents, the following principle is to follow:

Principle 4 (Chain Principle) *Any anaphoric markable has no more than one antecedent. Mark the most recent (i.e. right-most) previous referent's mention as antecedent; all mentions of the same referent make up an ordered chain.*

(32.a) *\[Die einstige Fußball-Weltmacht\]~d~ zittert vor einem
Winzling.*

(32.b) *Mit seinem Tor zum 1 : 0 fu¨r die Ukraine stu¨rzte der 1, 62
Meter große Gennadi Subow \[die deutsche Nationalelf\]~d~*~−*elf*~
*voru¨bergehend in ein Trauma.*

(32.c) *Je kleiner die Kicker*~?~ *daherkommen, desto gr¨oßer wird der
Gegner geredet\...*

In this example, an anaphoric relation between *die Kicker* and
*Fußball-Weltmacht* is possible, established through the relation of metonymy. But, according to the chain principle, the choice of the right-most (i.e. most previous) antecedent is enforced. So, the antecedent of *die Kicker* is *die deutsche Nationalelf* (ambig-ante).

## Cataphora

We distinguish two types of forward-referring expressions, discourse cataphora and syntactic cataphora.

### Discourse cataphora (anaphora of anticipation)

Discourse cataphora is a label used for non-pronominal reference forward. Sometimes an author introduces a discourse referent by means of an underspecified NP, i.e. an NP that cannot be interpreted only on the basis of the reader's knowledge up to this point. This way the author tries to encourage the reader to continue reading, in order to catch up the missing information. In the example below, *die einstige
Fußball-Weltmacht* and *vor einem Winzling* should be annotated as discourse cataphors, since their referents cannot be identified until introduced explicitly in the following text (*Deutschland* and
*Ukraine* correspondingly).

(33) *Die einstige Fußball-Weltmacht zittert vor einem Winzling*
     (newspaper article title)

In case one goes on reading the text, it becomes clear that *die einstige Fußball-Weltmacht* refers to Germany, whereas *ein Winzling* refers either to the Ukraine or the 1.62 meter tall ukranian footballer who made the most impact in the match ^5^. Discourse cataphors have to be annotated as normal anaphors, i.e. in accordance with the Chain Principle (p. 12), i.e. the most recent referent mention to the left (if any) is considered to be an antecedent.

### Syntactic cataphora

(34) *Through \[his\] lawyers, \[Mr. Antar\] has denied allegations in the SEC suit \...*

Syntactic cataphors are to be annotated like anaphoric links, that is, by means of a pointing relation, but with reverse direction (from left to right). Assign the feature referring in category referentiality
(sec. 4.1).

The following examples (a nominal head followed by a restrictive modifier), although traditionally classified as cataphora, should
NOT be annotated as such.

(35) \... \[*the car that went through his garden wall* \]\...

(36) \... \[*the patterns of industrial development in the U.S* \]\....

In case of doubt between syntactic cataphora or anaphora, decision has to be made as follows.

Principle 5 (Cataphora at the sentence level) *If antecedent can be found to the right of the anaphor, however, in the same sentence the anaphor belongs to, this antecedent should be preferred to the right-most (i.e. the closet to an anaphor) candidate antecedent in the previous discourse.*

(37.a) *Die einstige Fußball-Weltmacht zittert \[vor einem
Winzling\]s.*

(37.b) *\[Mit \[seinem\]s Tor zum 1:0 fu¨r die Ukraine\] stu¨rzte
\[der 1,62 Meter große Gennadi Subow\]s \[die deutsche Nationalelf\] voru¨bergehend in ein Trauma.*

In the example, *seinem* refers to *Gennadi Subow* who was introduced in the very first sentence as *vor einem Winzling*. Following the preferences, we establish an anaphoric (cataphoric) link to the right.
Thus, the anaphoric chain looks as follows:

-   *seinem* → *Gennadi Subow* (same-sentence)

-   *Gennadi Subow* → *vor einem Winzling* (right+previous, Chain
    Principle)

5The complete text is not provided here because of space limitations

## Ambiguous antecedents

In cases of doubt, if something is either related to some item in the previous discourse by an anaphoric relation or if no relation holds at all and something is used generically, as an expletive element, etc., use the following principle.

Principle 6 (Ambiguous antecedents) *By uncertainty, if anaphoric reference takes place or if a markable has no antecedent at all (i.e. is an expletive or idiomatic element, or of generic reference), prefer anaphoric reference and establish a link to a corresponding antecedent.*

(38) *At stake was an \$80,000 settlement involving who should pay what share of cleanup costs at the site of a former gas station, where underground fuel tanks had leaked and contaminated the soil. And the lawyers were just as eager as the judge to wrap \[it\] up.*

*It* can either be interpreted as referring to *an \$80,000 settlement* or as a part of a lexicalized expression *to wrap it up* where *it* does not have any particular reference. In case of doubt, the anaphoric interpretation has to be preferred and provided by the values ambig-ante or ambig-ante-rel, see 4) of the ambiguity feature.
Markables with ambiguous antecedents should NOT be used as antecedents if possible. This is an explicit exception from the chain principle
(p. 12).

(39.a) *Mit seinem Tor zum 1:0 \[fu¨r die Ukraine\]u stu¨rzte der 1,62
Meter große Gennadi Subow \[die deutsche Nationalelf\]~d~ voru¨bergehend in ein Trauma.* \...

(39.b) *Je kleiner \[die Kicker\]~u~*~?~ *daherkommen, desto gr¨oßer wird \[der Gegner\]~d~*~?~ *geredet.*

In this example, the antecedent of *die Kicker* is not completely clear, is it the Ukrainian team (described as less important and having smaller players), or the German team (which has not been favoured after the first match). To avoid inconsistencies, another mention of the Ukarainian team (or, in the other interpretation, the
German one) should not refer to *die Kicker*, but rather directly to
*fu¨r die Ukraine* (resp. *die deutsche Nationalelf* ).

So, if one considers generic interpretation of *die Kicker* as well, still the anaphoric interpretation has to be preferred in case of doubt.

# Markable Features: set of tags used in the core scheme

Below the tags employed in the implemented core annotation scheme are outlined, together with their short descriptions. For more detailed description, consider previous sections. The tags correspond to annotation features and their values. Values marked with \* are secondary markables.

## referentiality

The feature referentiality has tree values:

not specified *(default)* no decision has been made in the course of annotation

referring a discourse entity which can be interpreted on the basis of the previous context

discourse-new a discourse entity mentioned for the first time

discourse-cataphora refers to a new entity, introduced into a discourse by means of an expression with underspecified denotation
("scene-preparation" effect, p. 13).

Syntactic cataphors are not included here, see sec. 3.2.2.

other annotator cannot decide how to classify

Also, instances of generic and predicative descriptions or groups whose members have different referentiality features should be marked as other. The term *generic*

denotes a special usage of a referring expression, such that not a particular individual or object is meant, but rather a class of entities or features of this class.

Typical instances include generic descriptions such as *the lion* in example 40a or

*der Pr¨asident* in 40b.

(40.a) *The lion is an African carnivore.*

(40.b) *Der Pr¨asident wurde immer schon durch die Stimmenmehrheit bestimmt.*

'The president has always been elected by the majority of votes.'
Other cases to be classified as other are *predicative descriptions*.

41. *Nicht, dass beide eine Mehrheit fu¨r ihre Koalition suchten, war
    \[das A¨rgerliche*

*in den vergangenen Tagen\]* \... (predicative description)

42. *Und das ist \[das Dilemma der Regierenden\]* (predicative description, probably generic)

If a markable refers to something in text that cannot be declared as a primary/secondary markable (e.g. reference to a sentence), select a referring value of referentiality feature. But do NOT assign an antecedent to it.

By uncertainty, use the following preferences, which can be inferred from the Principle of Ambiguous Antecedents, see 3.3.

## direct-speech

text-level *(default)* reference on the text level, i.e. reference NOT into or within the quoted material

dir reference into or within direct speech

indir reference into or within indirect speech

## phrase-type

np *(default)* noun phrase (NP)

pp prepositional phrase (PP)

other phrase type which cannot be unambiguously classified

## np-form

The feature stands for the surface structure of markables

none *(default)*

ne proper names

def-np definite NP

\*indef-np indefinite NP pper personal pronouns ppos possessive pronouns, pds demonstrative pronouns padv pronominal adverbs

other for special purposes, we leave this option for later extensions, choosing other

enforces to add a comment describing the type of description Note that np-form has to be annotated both for NPs and PPs!

## ambiguity

not-ambig *(default)*

ambig-ante ambiguity of the antecedent of a markable in an anaphoric relation:

43. *In a letter, \[prosecutors\]~p~ told \[Mr. Antar's lawyers\]~l~ that because of the recent Supreme Court rulings,
    \[they\]~p/l~*~?~ *could expect that any fees collected from Mr.
    Antar may be seized.*

ambig-rel ambiguity with respect to the relation (anaphoric vs. bridging or event,

i.e. contextual inference)

ambig-idiom ambiguity with respect to whether a markable could be understood as referring expression or as an idiom

ambig-expl ambiguity with respect to whether a pronoun is expletive
(and therefore non-referring) or anaphoric

ambig-ante-rel ambiguity with respect to both antecedent and relation

44. "There seems to be a move around the world to deregulate the genera- tion of electricity," Mr. Richardson said, and Canadian Utilities hopes to capitalize on it.

*On it* refers either to *a move around the world to deregulate the generation of electricity*, or to the whole clause beginning with
*there* and ending with *electricity* (event anaphora).

ambig-other other cases of ambiguity

## anaphora-type

type of anaphoric relation

none *(default)* first-mention of a referent

anaphoric anaphoric relation

## complex-np

A description is complex if it contains more than one noun phrase (cf. sec. 2.4.2)

not-specified *(default)*

yes no

## grammatical-role

We use surface-oriented definitions of grammatical roles. So, if used in the position of predicate, an NP is annotated as a subject.

45. *NBI also said it has hired Prudential-Bache Securities Inc. as its financial adviser.*

46. *Brazil and Venezuela are the only two countries that haven't completed steel talks with the U.S.*

not specified

SBJ subject: the part of the sentence or clause about which something is being said. It is usually the doer of the action. It is normally a noun or a pronoun (in Nominative).

DIR-OBJ direct object: is a noun or pronoun (in Accusative) that receives the action of a verb or shows the result of the action. It answers the question *"What?"* or *"Whom?"* after an action verb (a transitive verb).

INDIR-OBJ indirect object: precedes the direct object and tells to whom or for whom the action of the verb is done and who is receiving the direct object. There must be a direct object to have an indirect object. Indirect objects are usually found with verbs of giving or communicating like *give, bring, tell, show, take*, or *offer*. An indirect object is always a noun or pronoun (Dative in German) which is not part of a prepositional phrase.^6^

other PPs and embedded elements

6"Die Handlungsrollen Sb, Obj and Partner \[i.e. indirect object\] werden durch die Flexive der Kasus Nominativ, Akkusativ und Dativ angezeigt, bisweilen auch durch ein Wechsel der Stellung bei den beteiligten Sprachzeichen (Weinrich 2003:25).

# Tagging Procedure: Overview

1.  identification of primary markables (with regard to Principle 2)

2.  connecting markables with anaphoric relations

    -   assigning any markable identified so far a unique (right-most) antecedent (with regard to Principles 1, 3 and 4)

    -   identify nominal anaphoric links using the test in 3.1

    -   if the antecedent has not been identified as a markable yet:

        -   annotate it as a primary markable if it has not been done before for some reason

        -   otherwise, annotate it as a secondary markable.

3.  for each markable, set up attribute values (referentiality, , etc.)

# Principles overview

Principle 1 (Primacy of markables as antecedents (primary and secondary)) *If there are primary markables that can be antecedents of a markable, establish a link to these, rather than declaring secondary markables, even if a primary markable is located further to the left from the anaphor compared to the possible secondary markable.*

Principle 2 (Maximum size principle) *Markables of maximum size are subject to annotation. That is:*

1.  *one markable includes all attributes of its head noun: relative clauses, appositions, modifiers and complements, right and left dislocations -- marked bold in the examples below,*

2.  *coordinated NPs/PPs are double-annotated: 1) members of a coordinated NP/PP separately and 2) the whole coordinated NP/PP as one markable.*

Principle 3 (Primacy of markables as antecedents (groups)) *If there are primary or secondary markables that can be antecedents of a markable, establish a link to these, according to the Principle 1, rather than declaring group markables, even if a primary or secondary markable is located further to the left from the anaphor compared to the possible group markable.*

Principle 4 (Chain Principle) *Any anaphoric markable has no more than one antecedent. Mark the most recent (i.e. right-most) previous referent's mention as antecedent; all mentions of the same referent make up an ordered chain.*

Principle 5 ((Pronominal) cataphora at the sentence level) *If antecedent can be found to the right of the pronoun, however, in the same sentence the pronoun belongs to, this antecedent should be preferred to the right-most (i.e. the closet to an pronoun) candidate antecedent in the previous discourse.*

Principle 6 (Primacy of anaphora by ambiguous antecedents) *By uncertainty, if anaphoric reference takes place or if a markable has no antecedent at all (i.e. is an expletive or idiomatic element, or of generic reference), prefer anaphoric reference and establish a link to a corresponding antecedent.*

Principle rankings

Principle 2 is obligitory. Principles 3 and 4 have a similar weight.
Principle 5, being an exception from Principle 4, is of a higher weight.

# Extended Scheme

Extended scheme is a selection of extensions, which do not have to be applied completely. Extensions can be chosen, according to specific purposes.

## Primary Markables

Besides the primary markables as defined in the core scheme, the extended set of markables includes:

-   interrogatives

-   reflexive pronouns

-   zero pronouns

Note that none of these markable types can serve as an antecedent.^7^There is a possible exception for interrogatives or indefinite other-np's if another primary markable exists (accoding to the core scheme) that has no other antecedent but this one, e.g.

41. *\[Who\]w didn't brush hisw teeth today ?*

(Here, the interrogative pronoun is the only possible antecedent the possessive pronoun could have, so it would be annotated as a markable even according to the core scheme.)

42. *\[Another boy\]~b~ didn't brush his~b~ teeth today.*

(dito)

zero pronouns Besides "classical" pronouns, elided structural arguments (i.e. subjects, direct or indirect objects that have to be inferred) are regarded as ∅-pronouns and have to be marked. This means, that ZERO has to be inserted whenever an annotator steps over an elided argument.

43. *Johnj stepped in the kitchen,* ZERO*j opened the fridge and* ZERO*j decided NO-ZERO to take a pizza.*

Note, that John is the (implicit) subject of the clause *to take a pizza*. However, this is not an instance of ∅-pronoun, since the insertion of *John* (no matter at which position within the phrase) would make the utterance ungrammatical. If not sure whether to annotate a ZERO or not, try to insert a full description of the corresponding referent. Note that zeros have to be sentential arguments, no adjuncts.

*Do NOT annotate*:

-   Zeros in Neither-ZERO-NPs

44. *Finnair and SAS said they plan to swap stakes in each other.
    Neither ZERO disclosed details pending board meetings next month.*(=neither of them)

    -   pronominal adverbs functioning as discourse markers

    -   zeros in V0 constructions like *Hans kauft Ø und schenkt Maria ein Buch.*

    -   pronominal adverbs functioning as discourse markers, see page 8

    -   Do not annotate expletive pronouns, e.g.: It is raining (cf. p.8)

    -   Do not annotate markables within idiomatic phrases, e.g. *on the other hand* (cf. p.8)

## Secondary markables

-   indefinite descriptions (cf. p.6)

-   clauses

7This is a consequence of the compatibility with the core scheme.
Since we adapt the chain principle, we would produce different chains in core and extended scheme if the set of primary markables was different.

## Relations

nominal anaphora Nominal anaphora as a type of anaphoric relations was introduced on (p. 12). Here annotation of subtypes of nominal anaphors is enabled as well:

modification : new lexical material has been added within the NP

45. .*.. federal prosecutors have warned lawyers for \[Eddie Antar\] that if \[the founder and former chairman of Crazy Eddie Inc.\] is indicted,* \...

synonymy (52) *the agreement* - *the pact*

repetition a *lexical* repetition of a whole NP or parts of it

(53) *der Kanzler* \... *der Kanzler*

(54) *der Bundeskanzler* \... *der Kanzler*

BUT: *der Kanzler* \... *der hoch gesch¨atzte Kanzler* (here, we find a modification

since new lexical material is added)

pronominal (55) *If the government succeeds in seizing \[Antar's\] assets, \[he\] could be left without top-flight legal representation, \...*

unspec unspecified (as default value)

Note that these features are set not only with respect to the last mention of the referent, but to all previous references to it as well.
So, if a particular form appeared already, we compare it to this one, not the direct antecedent. The underlying intuition is that a referent accumulates semantic information as the discourse unfolds and thus, the comparison is not between surface forms, but between the anaphor and the whole bunch of representations the referent has been associated with. In case of uncertainties, use the following preferences:

synonymy \> modification

non-nominal anaphor We distinguish the following types of non-nominal anaphors:

event references to events reported in text spans, sentences, clauses or nominalized clauses

\(56\) *\[She spent a month at an Aetna school in Gettysburg, Pa., learning all about the construction trade, including masonry, plumbing and electrical wiring.\] \[That\] was followed by three months at the
Aetna Institute in Hartford ..*.

spatio-temporal ^8^

The anaphor has to be a prepositional phrase or a cue phrase replaceable by a prepositional phrase.

This category is primarily intended for German spatio-temporal pronominal adverbs (*danach* "thereafter", *davor* "in front of this"), and locative and temporal prepositional phrases (*behind the door*, *after the WW-II*).

anaphoric NPs (but not idenitity of reference): *fu¨nf Jahre sp¨ater*

Antecedents of event anaphors Antecedents of an event anaphors can be clauses only. As a convention, we exclude non-finite clauses and sub-clausal phrases from the scope of potential antecedents for event anaphors.

Usually, event-anaphors are ambig-ante.

For such cases, we suggest a preference of *minimal* right-most antecedents according to the chain principle introduced above.

right+previous \> left+previous small \> large

preferences Additionally, the following preferences for ambiguity cases are foreseen.

8At the moment, these are intended to be annotated for German only.

event \> spatio-temporal

e.g. *dabei* - an ambiguous pronominal adverb: it can either be interpreted as event or spatiotemporal.

Event is preferred to spatio-temporal, because event is of a more concrete denotation.

Do NOT annotate as event-anaphora: Pronominal adverbs that are controllers of relative clauses or comparable constructions as in the following examples are not to be annotated as event anaphors, but rather regarded to be discourse markers, which are out of scope of this annotation.

(57.a) *Die Fußball-Kleinmacht von Dnepr steht kurz davor, das scheinbar mit einem Dauerabonnement fu¨r die WM ausgestattete Team in der schwarz-weißen Kluft und eine ganze Nation in das Tal der Tr¨anen zu treiben.*

(57.b) *Die Fußball-Kleinmacht von Dnepr steht kurz davor, dass das scheinbar mit einem Dauerabonnement fu¨r die WM ausgestattete Team in der schwarz-weißen Kluft und eine ganze Nation in das Tal der Tr¨anen getrieben wird.*

Bridging relations. Bridging is the term introduced in Clark 1975, which accounts for referents of definite descriptions, which are not directly related to some previously mentioned textual entities, but are rather inferred through lexical or world-knowledge of discourse participants.

Inspired by Gardent et al. (2003), we propose a hiearchy, which distinguishes between knowledge sources (domain knowledge vs. lexical knowledge) and type (proposition vs. referent vs. situation).
This hierarchy will appear in the next version of this annotation scheme.

Do NOT annotate as bridging:

-   If the relation between the definite NP bridging anaphor and preceding context has been made explicit by means additional linguistic information (possessive pronouns, attributes, etc.), this relation has not been evoked from the text, but rather from the world-knowledge of the hearer. Such definite NPs should NOT be considered as bridging anaphors. Cf.:

\(58\) *\[Ein neues Bildbearbeitungsprogramm\]B ist auf \[den Markt\]M gekommen. \[Die Fehlermeldungen\]F, \[die\]F \[es\]B ausgibt, bringen
\[\[seine\]B Benutzer\]U zur Verzweiflung. '\[A new graphic*

*editor\] appeared \[in the market\]. \[The error messages\] that
\[it\] produces bring its users in despair.'*

In this example, *Die Fehlermeldungen 'the error messages'* is not a bridging anaphor, since the relation of these *error messages* to the context is clarified by the following relative clause. In the same way, the relation between *Bilderbearbeitungsprogramm 'the graphic editor'* and *seine Benutzer 'its users'* is not a case of bridging, being explained through a possessive pronoun *seine 'its'*.

-   Indefinites and pronouns can NEVER be considered as bridging anaphors. Only full definite descriptions fall under the definition of bridging anaphora. We explicitly exclude examples like the following ones:

(59.a) *Westinghouse Electric Corp. said it will buy Shaw - Walker Co.
\[Terms\] weren't disclosed.* similar-NPs

(59.b) *the pact\... the accord\... \[a similar alliance\]\...* i.e. similar to the pact in question

special cases Consider the following example. Here, part-whole bridging takes place, rather than a spatio-temporal anaphoric relation. The deictic point is the moment outlined in the previous discourse, but the terms have been lexicalized in political discourse.

(60) *im Osten\... im Westen* (in reference to Deutschland - discourse referent introduced before)

Whenever you find a definite NP that can not be explained as anaphoric reference, consider if it can be the case of *bridging* relation.
Bridging is a relation other than identity between markables established by inference.

(61) *John ate pizza. There was nothing else in* the fridge*.*

Here *the fridge* is inferred by mentioning a pizza.

Important note: antecedent can be only one markable, choose the most recent one, but mark it as ambig-ante (if the same bridging relation could point to another trigger) resp. ambig-rel (if different bridging relations could point to several different triggers), if unsure about ambig-ante or ambig-rel, choose ambig-other and write a comment.

Never allow bridging references from direct quotes to the textual level!

Following Gardent et al. \[GMK03\], we interpret the following examples as bridging: examples:

(62) T*oni Johnson pulls a tape measure across the front of \[what was once a stately Victorian home\]H. \[The chimney\]~part~*~o*f*(*H*)~
     *is a pile of bricks on the front lawn.*

(63.a) *A deep trench now runs along its north wall, exposed when the house lurched two feet off its foundation during last week's
\[earthquake\]e.*

(63.b) *The petite, 29-year-old Ms. Johnson \... has been on the move almost incessantly since last Thursday, when an army of adjusters, employed by major insurers, invaded the San Francisco area to help policyholders sift through \[the rubble\]~effect~ ~of~*~(*e*)~ *and restore some order to their lives.*

(64.a) *\[The Victorian house\]~h~ that Ms. Johnson is inspecting has been deemed unsafe by town officials. \...*

(64.b) *\[The owners\]~property~ ~of~*~(*h*)~*, William and Margie
Hammack, are luckier than many others.*

Trigger (antecedent)of bridging relations Antecedents, or triggers are sometimes difficult to be assigned to just one markable. It can be the whole context that evokes the information necessary for the interpretation of a bridging anaphor. If a single markable cannot be specified, choose the left-most one and mark it as "ambig-ante".

## World knowledge and situational references

Whenever a non-generic definite description cannot be explained as contextually accessible due to anaphoric reference or bridging inference, consider it to be inferrable from world knowledge or the situational environment.

\(65\) *This publication may not be reproduced, \...*

(situational reference to the reading environment)

(66.a) *Last Sunday, Ms. Johnson finally got a chance to water her plants, but stopped abruptly. "I realized I couldn't waste this water when there are people in Watsonville who don't have fresh water to drink."*

(situational reference to the reported context)^9^

Note that bridging references from direct quotes to the textual level are never subject to annotation! These are prototypical candidates for situational references.

To avoid waste-baket effects for situational and world-knowledge references, we mark situational references by relations pointing to a set of situationally prominent entities that are listed after the text itself, enclosed in \<situation\>, resp. in \<universe\> tags.

^9^In this case, we seem to have a bridging reference from direct speech to the predication *to water her plants*. However, it is less likely that Ms. Johnson refers to a text which had been written after she said that. So, it seems to be appropriate to classify such cases as situational anaphora, referring to situational environment at the moment of speaking.

## Ambiguities

In case of ambiguities, we suggest the following preferences. Below is the example outlined in the core scheme (p. 14 considered with respect to the options supported in the extended scheme and interpreted in accordance with these preferences.

anaphoric \> generic/idiomatic/expletive \> bridging \> situational

## Additional features

semantic-role

ag, ben/dat, pat, loc, instr, other, unspec

quantification

quant-np description involving a quantification (67.a) *most of them*
(quantified pronoun) (67.b) *many of the workers* (quantified NP)

num-np description involving cardinal numbers^10^

(68.a) *two dogs* (numeral + indefinite or definite NP) (68.b) *the two dogs* (numeral + definite NP)

(68.c) *two of them* (numeral + pronoun)

(68.d) *both (of them)* (two-dimensional group-referring pronoun)

no-quant neither quant-np nor num-np unspec no value set

Borderline case: indefinite NPs with an article that is identical (or at least derived from) the cardinal number *one* should be considered as quantified iff. a corresponding set of individuals has been previously evoked and the membership relation marked as being relevant.

For English, the latter condition should hold for *one*, but not for
*an, a*, for German, the membership relation should be regarded as being prominent if a substitution of the indefinite article *ein, eine* by colloquial *'n, 'ne* appears to be unlikely.

animacy

animate i.e. lexical animacy, with the following sub-types

human

non-human

metonymy sth. inanimate is denoted by an animate (human) , i.e. a book by its author

unspec

inaminate i.e. lexical inanimacy or abstract

pers (personified/personificated) sth. inanimate or abstract behaves like an animate entity, e.g. *the company said*

force sth. inanimate that usually occurs as causer of events *the wind, the fire, fate*

strictly-inanimate

metonymy sth. animate is denoted by an inanimate, e.g. *coffee's coming*, i.e. the one typically serving coffee is about to arrive

unspec unspec

Note that abstract entities are always regarded as being inanimate.

10Ordinal numbers are treated like adjectives as *other*, thus no own category here.

semantic class

abstract, person, physical object, action/event, collective, other, unspec

Note that there exist subtle dependencies between semantic class and animacy. However, critical cases such as collectives (e.g. *a group of people* vs. *a group of hills*) and certain physical objects (e.g.
*tree* vs. *stone*) could be either animate or inanimate. While semantic class has to do with the perception of an entity, animacy is primary a lexical feature. However, default values semantic class and animacy can be derived from WordNet resp. GermaNet for a majority of cases.

np-form surface structure of markables

none should be used only for non-nominal non-referring expressions, e.g. for clauses that serve as antecedents of event anaphors

proper names ne

definite description def-np involves several sub-types

unspec default value, this options allows to skip the sub-categorization of definite NPs Important note: This option is not intended to mark uncertainties, instead, choose other and drop a line

poss-np possessive NP

other-np definite NPs containing adjectives like *other*, e.g. *the other man*

the-np any NP with a definite article not covered by another def-np category

dem-np demonstrative NPs involve several sub-types regarding differences with respect to their relative proximity

unspec default, allows to skip sub-categorization

proximal *this man*, \...

distal *that man*, \...

other for special purposes, we leave this option for later extensions, choosing other

enforces to add a comment describing the type of demonstrative NP

other this option is left for cases, when an annotator experiences problems by classifying a definite NP. After choosing other, a comment of the annotator as to the type of definite NP has to be annotated as well.

indef-np unspec default

bare-np indefinites without article, e.g. *men*, *water*, \... a-np indefinites with indefinite article, e.g. *a man*, \... another-np indefinites with other, e.g. *another man* other allows further extensions for special purposes

pper personal pronouns, *I, me, you, he, him, she, her, it, we, us, they, them*

ppos possessive pronouns, *my, mine, your, yours, \...* prefl reflexive pronouns, *himself, herself, itself, \...* pint interrogative pronouns, *who, where, when, \...*

pds demonstrative pronouns, with the following sub-classes: unspec default, allows to skip sub-categorization proximal *this, these*,
*this one*, German *der, die, das, \...*

distal *that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes*

other for special purposes, we leave this option for later extensions, choosing other

enforces to add a comment describing the type of demonstrative pronoun

padv German only: pronominal adverbs, e.g. *davor, deswegen*

other for special purposes, we leave this option for later extensions, choosing other enforces to add a comment describing the type of description

only the top level (without reflexives and interrogatives) is in core scheme, remainder in extended scheme

## Tagging Procedure: overview

1.  identify reflexives, interrogatives and zeros as markables^11^, set their attributes and identify their anaphoric antecedents.

2.  annotate bridging and event anaphora

    -   for each definite (non-generic) markable to which no antecedent has been assigned yet, check, whether a bridging relation takes place

Note, however, that bridging relations cannot be carried out from direct speech into text (see above).

3.  annotate situational and world-knowledge references

    -   for each definite (non-generic) markable to which no anaphoric antecedent or bridging relation has been assigned yet, check, whether it could be a situational reference (text situation, reading situation, writing situation, reported situation, etc.) or an inference from world-knowledge

    -   if so, add an entry in the \<situation\> resp. the \<universe\> stack and mark an anaphoric relation pointing to it

11This separate step guarantees the exclusion of these items from the referential chain.

# Appendix

## Pronominal forms

### English pronouns among primary markables in the core scheme

+---+---+---+-------+-------+---------+--------+---------+----------+
|   |   |   | > per | > pro | > pos   | pr     | >       |          |
|   |   |   | sonal | nouns | sessive | onouns |  demons |          |
|   |   |   | >     | >     | >       |        | trative |          |
|   |   |   | >     | >     | > det   | n      | > p     |          |
|   |   |   |  nom. |  acc. | erminer | ominal | ronouns |          |
|   |   |   |       |       |         |        | >       |          |
|   |   |   |       |       |         |        | > p     |          |
|   |   |   |       |       |         |        | roximal |          |
|   |   |   |       |       |         |        | >       |          |
|   |   |   |       |       |         |        |  distal |          |
+===+===+===+=======+=======+=========+========+=========+==========+
| > | > |   | I     | > me  | > my    | > mine |         |          |
|   |   |   |       |       |         |        |         |          |
| 1 | s |   |       |       |         |        |         |          |
|   | g |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > |   | we    | > us  | > our   | > ours |         |          |
|   |   |   |       |       |         |        |         |          |
|   | p |   |       |       |         |        |         |          |
|   | l |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
| > | > |   | you   | > you | > your  | >      |         |          |
|   |   |   |       |       |         |  yours |         |          |
| 2 | s |   |       |       |         |        |         |          |
|   | g |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > |   | you   | > you | > your  | >      |         |          |
|   |   |   |       |       |         |  yours |         |          |
|   | p |   |       |       |         |        |         |          |
|   | l |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
| > | > | m | he    | > him | > his   | > his  | > this  | > that   |
|   |   | \ |       |       |         |        |         |          |
| 3 | s | . |       |       |         |        |         |          |
|   | g |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > | > | she   | > her | > her   | > hers | > this  | > that   |
|   |   |   |       |       |         |        |         |          |
|   | s | f |       |       |         |        |         |          |
|   | g | \ |       |       |         |        |         |          |
|   | . | . |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > | n | > it  | > it  | > its   | > its  | > this  | > that   |
|   |   | \ |       |       |         |        |         |          |
|   | s | . |       |       |         |        |         |          |
|   | g |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > |   | >     | >     | > both  |        |         |          |
|   |   |   |  both |  both |         |        |         |          |
|   | d |   |       |       |         |        |         |          |
|   | u |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+
|   | > |   | >     | >     | > their | >      | > these | > those  |
|   |   |   |  they |  them |         | theirs |         |          |
|   | p |   |       |       |         |        |         |          |
|   | l |   |       |       |         |        |         |          |
|   | . |   |       |       |         |        |         |          |
+---+---+---+-------+-------+---------+--------+---------+----------+

### German pronouns among primary markables in the core scheme

+---+---------+------+------+-------+----------+--------+-------------+
|   |         | pers |      |       | > po     | > d    |             |
|   |         | onal |      |       | ssessive | emonst |             |
|   |         | pron |      |       | >        | rative |             |
|   |         | ouns |      |       | >        | > pr   |             |
|   |         |      |      |       | pronouns | onouns |             |
|   |         | nom. |      |       |          | >      |             |
|   |         | acc. |      |       |          | > pr   |             |
|   |         | dat. |      |       |          | oximal |             |
|   |         |      |      |       |          | >      |             |
|   |         |      |      |       |          | distal |             |
+===+=========+======+======+=======+==========+========+=============+
| > | > sg.   | >    | >    | > mir | > mein   | > der  | > dieser    |
|   | >       |  ich | mich | >     | >        | > die  | > diese     |
| 1 | > pl.   | >    | >    | > uns | > unser  | > das  | >           |
| > | >       | >    | >    | > dir | > dein   | >      | > dies,     |
| > | > sg.   |  wir |  uns | >     | > euer   | > die  | > dieses    |
|   | >       | > du | >    |  euch | > Ihr    |        | >           |
| 2 | > pl.   | >    | dich | > Ihr | > sein   |        | > diese     |
| > | >       |  ihr | >    | > ihm | > ihr    |        |             |
| > | >       | >    | euch | > ihr | > sein   |        |             |
|   |  polite |  Sie | >    | > ihm | > beider |        |             |
| 3 | > sg.   | > er |  Sie | > b   | >        |        |             |
|   | > m.    | >    | >    | eiden | > ihr    |        |             |
|   | >       |  sie |  ihn | >     |          |        |             |
|   | > sg.   | > es | >    | >     |          |        |             |
|   | > f.    | >    |  sie | ihnen |          |        |             |
|   | >       | > b  | > es |       |          |        |             |
|   | > sg.   | eide | >    |       |          |        |             |
|   | > n.    | >    | > b  |       |          |        |             |
|   | > du.   | >    | eide |       |          |        |             |
|   | >       |  sie | >    |       |          |        |             |
|   | > pl.   |      | >    |       |          |        |             |
|   |         |      |  sie |       |          |        |             |
+---+---------+------+------+-------+----------+--------+-------------+

### Pronominal adverbs in German.

## Complex cases

appositions *a subcommette chairman, Rep. Bob Traxey* is a definite
NP. Test: *Rep. Bob Traxey* can be placed before *a subcommette chairman*.

definite NPs *e.g. Friday's close, July's crash*. Text: *this Friday's closse, this July's crash*

−→ definite.

definite article in prepositions *in the meantime, in the end of, in the absence of*, etc. have to be annotated as parts of PPs, rather than separate markables.

a primary markable within a secondary markable *other UAL executives*: just *UAL* is a markable, not the whole phrase.

lists of markables *Now only three of the 12 judges - Pauline Newman,
Chief Judge Howard*

*T. Markley and Giles Rich, 85 - have patent-law background. The latter two and Judge Daniel M. Friedman, 73 are approaching senior status or retirement.* The antecedent of *the latter two* is not a primary markable originally, so annotate it as a group.

referring secondary markables Assume the following referential chain:

*prosecutors1 \... they1 \... prosecutors2 \... they2 \...*

Prosecutors has no article, so it is considered indefinite according to our definitions. Here we have to annotation possibilities:

they2 −→ they1 \[primary preferred to secondary preference\] they2 −→ prosecutors2 \[recency preference, chain principle\]

NB: intuitively, an appropriate decision seems to be as follows: they2
−→ prosecutors2 prosecutors2 −→ they1

In cases like this, put ambig-ante value and write referring in comments.

coordinated markables if primary and secondary markables go together in a coordinated NP, e.g. *\[ \[Journalists\] and \[\[their\] families\] \]*, annotate such a whole coordinated NP as a markable, puting a value other in np-type.

proper names preferred annotation is marked bold in the following examples:

*\[in midtown \[Manhattan\]\]* ∼ *\[in midtown Manhattan\]*

*\[in the city of Bucaramanga\]* ∼ *\[in the city of
\[Bucaramanga\]\]*

\[in the city of Bucaramanga\] oder \[in the city of
\[Bucaramanga\]\]?

# References 

\[Bib99\] Douglas et al. Biber. *Longman Grammar of Spoken and Written
English*. Longman, 1999.

\[Gib94\] R.W. Gibbs. *The poetics of mind*. Cambridge University,
Cambridge, 1994. \[GMK03\] Claire Gardent, H´el\`ene Manu´elian, and
Eric Kow. Which bridges for bridging de-

scriptions. In *EACL Workshop on Linguistically Interpreted Corpora proceedings.*,

2003\.

\[Mit00\] R. et al. Mitkov. Coreference and anaphora: Developing annotating tools, annotating resources and annotations strategies.
In *Proc. DAARC 2000*, pages 49--58, Lancaster, UK, 2000.
