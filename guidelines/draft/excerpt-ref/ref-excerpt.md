# 1. Referring Expressions

(Excerpt from AURIS guidelines v.0.1, §3 / spring semester 2023, originally for automated annotation)


# 1.1 Markables (things to be annotated)

Referring expressions are noun phrases, proper names and pronouns. 

- Annotate every definite noun phrase, every proper noun and every pronoun which is not syntactically bound as a potential anaphor ("primary markable").
- Check whether it has an antecedent in preceding text. If the antecedent has not been previously marked as a potential anaphor, create a new markable ("secondary markable")
- Annotate every markable as being non-referring or with the index of the coreference chain (i.e., the unique symbol that you chose to identify)

## 1.2 Manual annotation

- Please read the entire text first.
- The annotation task is to process each sentence and to annotate/verify all markables and their antecedents *in reading order*.

## 1.3 Head-based annotation

When annotating a word as markable, do not annotate the full span, but the syntactic head only. Thus, markables must never overlap.

Head identification is defined in lines of the Universal Dependencies, i.e.,

- The syntactic head of a single word span is the word
- The syntactic head of a noun phrase is the last nominal
- The syntactic head of a clause is the main verb
- The syntactic head of a prepositional phrase is the head of its noun phrase.
- The syntactic head of a multi-word proper name is the first proper noun
- The syntactic head of a conjunction is the first conjunct. If multiple conjuncts in a conjunction serve as antecedents, annotate each conjunct separately.

> (1.a) English: *\[<ins>Hans</ins> -- who always had \[a soft <ins>spot</ins>\] \[for <ins>Susanne</ins>\]  -- \]  was also there.*

> (1.b) German: *\[<ins>Hans</ins> -- der immer schon \[eine <ins>Schwäche</ins>\] \[für <ins>Susanne</ins>\] hatte -- \] war auch da.*

This also entails that referring expressions can *only* be annotated if they are identified as independent words by the word segmentation procedure adopted for that particular language. In (1.c), *Denver* and *bancruptcy* can only be identified as markables if they are (automatically annotated as) independent tokens.

> (1.c) *The \[Denver\]?-based concern, which emerged from bancruptcy \... its new, post-\[bancruptcy\]? law structure \...\"* (WSJ, 1328)

## 1.4 Types of candidate anaphors (primary markables)

### 1.4.1 Pronouns

Pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and possessived pronouns and *both* in nominal use (i.e. not as a determiner),<sup>[3](lit.md#refexp3)</sup> e.g.,

> (3) *\[I\] saw \[her\] yesterday.*

If automated pre-annotation operates on a language/annotation schema that doesn't distinguish these types of pronouns from other (non-referring) types of pronouns, *every* pronoun should be annotated as primary markable.

> Note: Interrogative pronouns are not primary markables, but can serve as secondary markables.

> Note: Relative and reflexive pronouns are not primary markables.

#### 1.4.1.1 Personal Pronouns

Personal pronouns include (the language-specific counterparts of) English *I, me, you, he, him, she, her, it, we, us, they, them*.

Note that so-called "generic pronouns" (*we, you, they*, in German *wir, du, sie* (without specific reference), *man, einer*) are considered as indefinite, but that they cannot be automatically identified. Thus, they are annotated as primary markables.

> Note: Reflexive pronouns (English *herself*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself"), are PM, and should be manually marked as `REF=BOUND` in the annotation. 

> Note: Other non-referring pronouns (e.g., expletive *it* or generic *you* in the sense of "anyone") are likewise not to be deleted but to be annotated manually.

#### 1.4.1.2 Possessive Pronouns

Possessive pronouns include (the language-specific counterparts of) English *my, mine, your, yours, \...*.

#### 1.4.1.3 Demonstrative Pronouns 

Demonstrative pronouns occur with two optional sub-classes: 

- `NP_TYPE=pron.pds-prox`: proximal *this, these*, *this one*, German *der, die, das, \...*
- `NP_TYPE=pron.pds-dist`: distal *that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes, derjenige,* and the like.

Note that the semi-demonstrative pronouns, e.g., *such*, in German *solch*, are considered indefinite.

> Note: Relative pronouns (English *which*, etc.) are not PM.

#### 1.4.1.4 Pronominal Adverbs 

Pronominal adverbs are derived from pronouns but grammaticalized as adverbs. If pronominal adverbs can still be interpreted as / replaced by a referring expression in a particular language, they should be included as primary markables. However, we exclude references to time and place of the speaker (*here*, *hence*) if these are unambiguous in their deictic function, as well as interrogative adverbs (*where*, etc.). 

Examples: Pronominal adverbs in German include *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there"), *davor* "in front of that; before that", or *deswegen* "because of that".

> Note on English: Normally, pronominal adverbs are not recognized as referring expressions in English, but they can indeed be substituted with prepositional phrases. For English, we annotate adverbs (starting with) *there* (unless expletive) and *thence*, e.g., *there*, *thereafter*, *therefore*, *thence*, *thenceforth*. We exclude the analoguous *here* and *hence* because they are exclusively deictic, not anaphoric, whereas there and thence could also have an anaphoric function (*therefore* ~ *for this reason*, *thence* ~ *from there*).

### 1.4.2 Definite Descriptions

A description (NP or PP) is definite if it contains the determiner *both*, a demonstrative or possessive pronoun or a genitive attribution. Optionally, this can be made explicit with sub-types.

#### 1.4.2.1 With Demonstrative Determiner

> (4) *\[that <ins>pizza</ins>\]*, *\[this <ins>pizza</ins>\]*

Demonstrative NPs involve optional differences with respect to their relative proximity, with optional subtypes

- `NP_TYPE=def-np.dem-prox`: proximal *this man*, \...
- `NP_TYPE=def-np.dem-dist`: distal *that man*, \...

#### 1.4.2.2 With Possessive Modifier

Constructions with possessive pronouns.

> (5) *\[his <ins>pizza</ins>\]*

Also includes potentially genitive or possessive modifier, if these are (potentially) anaphoric

> (6.a) *\[John\'s <ins>pizza</ins>\]*

> (6.b) *\[the <ins>pizza</ins> of John\]*

> (6.c) *\[the other man's <ins>pizza</ins>\]*

> (6.d) *\[this man's <ins>pizza</ins>\]*

**but not**: *\[a man's pizza\]*

#### 1.4.2.3 Quantified Definite NP

At the moment, this includes cases where a quantifier is combined with a definite article (`the two men`) or with determiner \'both\'

> (7.a) *\[the two <ins>pizzas</ins>\]*
> (7.b) *\[both <ins>pizzas</ins>\]*

But not: *two pizzas*. As for constructions like *two of these pizzas*, this is formally a possessive construction.

#### 1.4.2.4 With Definite Article

Any NP with a definite article not covered by any aforementioned category

> (8) *\[the <ins>pizza</ins>\]*

#### 1.4.2.5 NP with "Other"

Definite NPs containing adjectives like *other*

> (9) *the other man*

### 1.4.3  Proper Names and Titles

Typical instances of proper names are geographic places
(*Philadelphia*), persons (*Judge Jenkins*), companies (*Morgan
Stanley & Co.*), newspaper titles (*The New York Times*), political, social or financial institution names (*Congress, European Investment
Bank* ). Proper names can include noun modifiers or be heads of a definite or indefinite description. In this case, the whole description has to be marked up, not just the head.

> (10.a)  *\[Bertolt <ins>Brecht</ins>\]* (full name)

> (10.b)  *\[Bert <ins>Brecht</ins>\]* (reduced full name)

> (10.c)  *<ins>Brecht</ins>* (surname)
	
> (10.d) 	*<ins>Bertolt</ins>* (first name)
	
> (10.e) 	*<ins>Bert</ins>* (nickname)

> (10.f)   *<ins>BB</ins>* (abbreviation)

> (10.g)   *the well-known <U>Brecht</ins>* (name, modified by a definite description)

> (10.h) *<ins>Brecht</ins>, who is author of the "Dreigroschenoper"* (proper name + clause)

> (10.i) *<ins>Brecht</ins>, author of the "Dreigroschenoper"* (proper name + apposition)

Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.
 
> (10.j) \[Dr. <ins>Mueller</ins>\]

> (10.k) \[Dr. <ins>Martin</ins> Luther King, Jr.\]

> (10.l) \[Prince <ins>Dipangkorn</ins> Rasmijoti Sirivibulyarajakumar of Thailand\]

> (10.m) \[Heidelberger <ins>Druckmaschinen</ins> Vertrieb Deutschland GmbH\]

Standalone titles that can stand in for an individual (*Mr./Ms./Dr./President/Chairman*) are treated like proper names, e.g., 

> (11.a) *Schröder<sub>1</sub>\...Fischer<sub>2</sub> \... Die anfängliche Überreaktion von <ins>Kanzler</ins><sub>1</sub> und <ins>Außenminister</ins><sub>2</sub>\...*

In (11.a), *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite

Parts of complex proper names cannot be analyzed separately. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

> (11.b) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*

## 1.5 Secondary Markables

Every nominal phrase or pronoun which is neither primary markable nor (confirmed to be) syntactically bound, is subject to automated pre-annotation. Secondary markables are referring expressions that are unlikely/impossible anaphors, but that could *introduce* new discourse referents.

Common types of secondary marakbles include: indefinite NPs and indefinite or non-referring pronouns.

Annotate the secondary markable only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

> (12) *I saw \[a <ins>cat</ins>\] tonight in the street. <ins>It(= the cat)</ins> was gray.*

**but not**: *I saw a cat tonight in the street. <ins>It(= the night/expletive?)</ins> was pitch black.*

### 1.5.1 Indefinite NPs

> (12.a) *There is a \[a <ins>fox</ins>\] running across the street. <ins>It</ins>'s fast!.*
	
> (12.b) *I last saw \[a <ins>fox</ins>\] about three years ago! <ins>It</ins> came from the forest.*

This also includes indefinites with other, e.g. *another man* 

NPs with indefinite quantifier, also including quantified expressions not otherwise annotated as primary markables

> (13.a) *\[some people\]*

> (13.b) *\[some plants\]*

> (14.c) *\[thirty grams\]*, *\[two companies\]* (quantified indefinite NP)

Borderline case: indefinite NPs with an article that is identical (or at least derived from) the cardinal number *one* should be considered as quantified iff. a corresponding set of individuals has been previously evoked and the membership relation marked as being relevant.

For English, the latter condition should hold for *one*, but not for
*an, a*, for German, the membership relation should be regarded as being prominent if a substitution of the indefinite article *ein, eine* by colloquial *'n, 'ne* appears to be unlikely.

Articleless NP, especially \"bare plurals\", but also singular expressions.

> (14.a) *I have eaten \[cookies\]SM* (bare plural)

> (14.b) *Today will be \[good weather\]SM* (bare singular) 


### 1.5.2 Non-anaphoric pronouns

With optional sub-types:

- interrogative pronouns: *who, where, when, \...*

- indefinite demonstrative pronouns, e.g., *such*, in German *solch*

- indefinite pronouns, e.g., *somebody*, or German *man*. Also includes pronominal indefinite quantifiers, e.g., *some* in *some of that*.


### 1.5.3 Other expressions

We consider every syntactic argument of a verb to be a potentially referring expression. If not matched by any of the aforementioned conditions, we treat verbal arguments as secondary markables. This can happen if an argument is a foreign language expression that is not assigned proper POS tags, but instead just marked as foreign (e.g., `X` in Universal Dependencies). Note that the annotation of referentiality for `other` nominals is tentative, only.

### 1.6 Do NOT annotate

### 1.6.1 Non-referring and bound expressions

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

	> (26) *Und so schielen \[die Israelis\]i \[(nach Washington)w, \[an \[dessen\]w Tropf\] \[sie\]i wirtschaftlich und milit¨arisch h¨angen\]<sub>w</sub>*′ *,\...*

-   prepositional phrases with prepositions *as, than*, *bis, als, wie* (in German) Such prases are annotated as normal NPs, i.e. *bis* and *als* are not included. ^3^

-   nominal premodifiers in compound nouns

	> (27) *peanut butter, airline analyst, the creditors commettee, investment bank*

	*Peanut, airline, cretitors* and *investment* are no separate markables. Note that in *the creditor's opinion*, *the creditor's* is annotated as a markable, since it is a nominal in genitive and thus not a part of a compounds.

### 1.6.2 Idioms and Collocations

Primary markables in idioms and collocations, if identifiable in automated pre-annotation.

> (28) *It sent Kate into the pits when she learned from her "friend" Martha, who seemed to get off on laying bad trips on people, that Harvey was getting it on with Carol.* \[Gib94, p.265\]

According to Gibbs, we find several idiomatic phrases in this example, some of which contain pronouns or full NPs -- potential primary markables.

However, they should not be annotated as such, e.g. *into the pits* meaning "to be depressed", *get it on* meaning "having sexual relations", neither *the pits* nor *it* can be referred to.

Note that we consider only *conventionalized* idiomatic expressions as idioms in our sense, i.e. markables within productive metaphors are annotated as usual, e.g. *das schlingernde City-Schiff City-Schiff* - a metaphor that occurred and can only be understood with respect to a specific text.