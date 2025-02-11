# 3. Referring Expressions

> Note to annotators: In most cases, referring expressions should be automatically pre-annotated. 
In this case, this section is not relevant for annotation, but only for you to interpret the automated pre-annotations.

<!--
> Note to developers: Additional technical details can be found in the technical appendix [WHERE].
-->

# 3.1 Markables (things to be annotated)

Referring expressions are noun phrases, proper names and pronouns. 

- Annotate every definite noun phrase, every proper noun and every pronoun which is not syntactically bound as a potential anaphor ("primary markable").
- Check whether it has an antecedent in preceding text. If the antecedent has not been previously marked as a potential anaphor, create a new markable ("secondary markable")
- Annotate every markable as being non-referring or with the index of the coreference chain (i.e., the unique symbol that you chose to identify)

## 3.2 Manual annotation

- Please read the entire text first.
- The annotation task is to process each sentence and to annotate/verify all markables and their antecedents *in reading order*.

## 3.3 Head-based annotation

When annotating a word as markable, do not annotate the full span, but the syntactic head only. Thus, markables must never overlap.

Head identification is defined in lines of the Universal Dependencies, i.e.,

- The syntactic head of a single word span is the word
- The syntactic head of a noun phrase is the last nominal
- The syntactic head of a clause is the main verb
- The syntactic head of a prepositional phrase is the head of its noun phrase.
- The syntactic head of a multi-word proper name is the first proper noun
- The syntactic head of a conjunction is the first conjunct. If multiple conjuncts in a conjunction serve as antecedents, annotate each conjunct separately.
<example id="nr5">
> <sub id="nr5.a">(1) English: *\[<ins>Hans</ins> -- who always had \[a soft <ins>spot</ins>\] \[for <ins>Susanne</ins>\]  -- \]  was also there.*</sub>

> <sub id="nr5.b">(2) German: *\[<ins>Hans</ins> -- der immer schon \[eine <ins>Schwäche</ins>\] \[für <ins>Susanne</ins>\] hatte -- \] war auch da.*</sub>
</example>
## 3.4 Types of candidate anaphors (primary markables)

### 3.4.1 Pronouns

Pronouns include personal pronouns, demonstrative pronouns, pronominal adverbs, and possessived pronouns and *both* in nominal use (i.e. not as a determiner),<sup>[3](lit.md#refexp3)</sup> e.g.,

> <example id="nr6">(3) *\[I\] saw \[her\] yesterday.*</example>

We distinguish the following types:

- **Personal Pronouns** include (the language-specific counterparts of) English *I, me, you, he, him, she, her, it, we, us, they, them*.
- **Possessive Pronouns** include (the language-specific counterparts of) English *my, mine, your, yours, \...*.
- **Demonstrative Pronouns** include pronouns that establish a deictic reference. In many languages, there are multiple categories of demonstrative pronouns, e.g., proximal demonstratives in English and German (English *this, these*, *this one*, German *der, die, das, \...*) as opposed to distal demonstratives (*that, those*, *that one*, German *dieser, diese, dies(es), jener, jene, jenes, derjenige,* and the like).
- **Pronominal Adverbs** are derived from pronouns but grammaticalized as adverbs. If pronominal adverbs can still be interpreted as / replaced by a referring expression in a particular language, they should be annotated. However, we exclude references to time and place of the speaker (*here*, *hence*) if these are unambiguous in their deictic function, as well as interrogative adverbs (*where*, etc.). Pronominal adverbs in German include *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there"), *davor* "in front of that; before that", or *deswegen* "because of that". In English, pronominal adverbs are not recognized as referring expressions in English, but they can indeed be substituted with prepositional phrases. For English, we annotate adverbs (starting with) *there* (unless expletive) and *thence*, e.g., *there*, *thereafter*, *therefore*, *thence*, *thenceforth*. We exclude the analoguous *here* and *hence* because they are exclusively deictic, not anaphoric, whereas there and thence could also have an anaphoric function (*therefore* ~ *for this reason*, *thence* ~ *from there*).

Note: In general, every pronoun should be annotated that is **formally identical** with a pronoun of the aforementioned types. This also includes certain cases of of non-referring expressions. For them, leave all fields (incl. `COREF`) empty but annotate the specific type of non-referring expression in `REF`.

Frequent cases include:

- `REF=GEN`: So-called "generic pronouns" (*we, you, they* in the sense of "anyone", in German *wir, du, sie* (without specific reference), *man, einer*).
- `REF=BOUND`: Reflexive pronouns (English *herself*, etc.) which are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself").
- `REF=EXPL`: expletive *it*

See below [WHERE?] for forms of pronouns that are **not** to be annotated.

### 3.4.2 Definite Descriptions

A description (NP or PP) is definite if it contains the determiner *both*, a demonstrative or possessive pronoun or a genitive attribution. This includes the following sub-types:

- NP with definite article

	> <example id="nr7">(4) *\[the <ins>pizza</ins>\]*</example>

- demonstratve NP

	> <example id="nr8">(5) *\[that <ins>pizza</ins>\]*, *\[this <ins>pizza</ins>\]*</example>

- possessive NP (NP with possessive modifier) includes both constructions with possessive pronouns <ref id="nr10">(7)</ref> and with morphologically marked possessor arguments (e.g., genitive, as in <ref id="nr9">6</ref>).
<example id="nr9">
	> <sub id="nr9.a">(6.a) *\[John\'s <ins>pizza</ins>\]*</sub>

	> <sub id="nr9.b">(6.b) *\[the <ins>pizza</ins> of John\]*</sub>

	> <sub id="nr9.c">(6.c) *\[the other man's <ins>pizza</ins>\]*</sub>

	> <sub id="nr9.d">(6.d) *\[this man's <ins>pizza</ins>\]*</sub>
</example>
	> <example id="nr10">(7) *\[his <ins>pizza</ins>\]*</example>

- **Quantified Definite NP** includes cases where a quantifier is combined with a definite article (`the two men`) or with determiner \'both\'
<example id="nr11">
	> <sub id="nr11.a">(8.a) *\[the two <ins>pizzas</ins>\]*</sub>
	> <sub id="nr11.b">(8.b) *\[both <ins>pizzas</ins>\]*</sub>
</example>
	But not: *two pizzas*.

### 3.4.3  Proper Names and Titles

Typical instances of proper names are geographic places
(*Philadelphia*), persons (*Judge Jenkins*), companies (*Morgan
Stanley & Co.*), newspaper titles (*The New York Times*), political, social or financial institution names (*Congress, European Investment
Bank* ). 
<example id="nr12">
> <sub id="nr12.a">(10.a)  *\[Bertolt <ins>Brecht</ins>\]*</sub> (full name)

> <sub id="nr12.b">(10.b)  *\[Bert <ins>Brecht</ins>\]*</sub> (reduced full name)

> <sub id="nr12.c">(10.c)  *<ins>Brecht</ins>*</sub> (surname)
	
> <sub id="nr12.d">(10.d) 	*<ins>Bertolt</ins>*</sub> (first name)
	
> <sub id="nr12.e">(10.e) 	*<ins>Bert</ins>*</sub> (nickname)

> <sub id="nr12.f">(10.f)   *<ins>BB</ins>*</sub> (abbreviation)

> <sub id="nr12.g">(10.g)   *the well-known <U>Brecht</ins>*</sub> (name, modified by a definite description)

> <sub id="nr12.h">(10.h) *<ins>Brecht</ins>, who is author of the "Dreigroschenoper"*</sub> (proper name + clause)

> <sub id="nr12.i">(10.i) *<ins>Brecht</ins>, author of the "Dreigroschenoper"*</sub> (proper name + apposition)
</example>
Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.
<example id="nr13"> 
> <sub id="nr13.a">(10.j) \[Dr. <ins>Mueller</ins>\]</sub>

> <sub id="nr13.b">(10.k) \[Dr. <ins>Martin</ins> Luther King, Jr.\]</sub>

> <sub id="nr13.c">(10.l) \[Prince <ins>Dipangkorn</ins> Rasmijoti Sirivibulyarajakumar of Thailand\]</sub>

> <sub id="nr13.d">(10.m) \[Heidelberger <ins>Druckmaschinen</ins> Vertrieb Deutschland GmbH\]</sub>
</example>
Standalone titles that can stand in for an individual (*Mr./Ms./Dr./President/Chairman*) are treated like proper names, e.g., 

> <example id="nr14">(11.a) *Schröder<sub>1</sub>\...Fischer<sub>2</sub> \... Die anfängliche Überreaktion von <ins>Kanzler</ins><sub>1</sub> und <ins>Außenminister</ins><sub>2</sub>\...*</example> 

In <ref id="nr14">(11.a)</ref>, *Kanzler* and *Außenminister* have to be annotated as primary markables, because proper names are inherently definite

Parts of complex proper names cannot be analyzed separately. So, in the following example, *Petrie* in *\[of
Petrie Stores Corp.\]* should not be annotated!

> <example id="nr15">(11.b) *\[Milton Petrie, chairman \[of Petrie Stores Corp.\] said\...*</example>

## 3.5 Other forms of referring expressions

Other forms of referring expressions are only annotated if they serve as antecedents. Note that this excludes a number of entity mentions that are introduced by an indefinite NP and not subsequently referred to.

Types of referring expressions that are unlikely or impossible anaphors include indefinite NPs and indefinite or non-referring pronouns, see X.1.4 for a detailed catalog of forms and cases.

Annotate such an expression only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

> <example id="nr16">(12) *I saw \[a <ins>cat</ins>\] tonight in the street. <ins>It(= the cat)</ins> was gray.*</example>

**but not**: *I saw a cat tonight in the street. <ins>It(= the night/expletive?)</ins> was pitch black.*

### 3.6 Do NOT annotate

Annotate the following types of pronouns only if they either serve as antecedents of other referring expressions or they are formally ambiguous with one of the aforementioned categories.

### 3.6.1 Non-referring (`REF=GEN`, `REF=PRED`, `REF=EXPL`, `REF=other`) and bound (`REF=BOUND`) expressions

Non-referring markables (NM) are primary markables whose function is *not* to refer to a discourse referent. 
Non-referring markables are to be *manually* given the appropriate referentiality value in subsequent annotation (`GEN`, `EXPL`, `PRED`. `IDIOM` or `other`, see there). For automated extraction, they are treated like primary markables.

> Note: **TODO** merge

	- semi-demonstrative pronouns, e.g., *such*, in German *solch*. These are considered indefinite.
	- syntactically bound pronouns (relative pronouns as English *which*, etc.; reflexive pronouns such as English *himself*). If annotated as potentially referring expressions by the automated pre-annotation, they should be annotated as `REF=BOUND`
	- interrogative pronouns (English *who?*, *what?*, etc.) are not considered to be referential as they normally refer to an entity that is by definition unidentifiable to the the person asking the question. If annotated as potentially referring expressions by the automated pre-annotation, they should be annotated as `REF=CAT` (discourse cataphors) if the WH-words corresponds to a referring expression in the answer, or `REF=other` otherwise.

-   expletive expressions

	> <example id="nr17">(21) *Then, when it would have been easier to resist them, nothing was done* (expletive *it*).</example>

-   pronominal adverbs which are controllers of relative clauses

	> <example id="nr18">(22) *Dazu kommt, dass in Werder am 24. Februar ein Bürgermeister gewählt wird und es bisher als sicher galt, dass CDU-Amtsinhaber Werner Größe unangefochten bleibt.*</example>

	*Dazu\...dass, es\...dass* should not be annotated as markables (*Dazu* and *es* are controllers of relative clauses).

-   pronominal adverbs functioning as discourse markers
<example id="nr19">
	> <sub id="nr19.a">(23.a) *Ich habe dich angesprochen, damit du mir zuhörst.*</sub>
	> <sub id="nr19.b">(23.b) *Ich habe dir das gesagt, damit du weißt, dass du mir zuh¨oren sollst.*</sub>
	> <sub id="nr19.c">(23.c) *Ich habe dir das gesagt, dass du weißt, dass du mir zuh¨oren sollst.*</sub>
</example>
-   relative pronouns

	If a form cannot be unambiguously classified as a relative pronoun, apply the following test: it is a relative pronoun if it can be substituted by "which" respectively "welch" in German.

	> <example id="nr20">(23.d.) *The car that went through his garden wall\...*</example> (constructed)

	However, relative pronouns in possessive constructions (i.e. for which the test for relative pronouns fails) are annotated as possessive pronouns (see possessive NPs).
<example id="nr21">
	> <sub id="nr21.a">(24) *Und so schielen die Israelis nach Washington, an dessen /\*welchem Tropf sie wirtschaftlich und militärisch hängen,\...*</sub>
	> <sub id="nr21.b">(24') *Und so schielen die Israelis nach Washington, das/welches sie wirtschaftlich und militärisch unterstützt*</sub> (*das* is a relative pronoun).
</example>
	Alternatively, the following test can be applied: substitute a pronoun in question with a possessive construction. If it works, you have a possessive pronoun, not a relative one.

	> <example id="nr22">(25) *die Frau und deren Kinder = die Frau und ihre Kinder*</example>

	The annotation is as follows in this case:

	> <example id="nr23">(26) *Und so schielen \[die Israelis\]i \[(nach Washington)w, \[an \[dessen\]w Tropf\] \[sie\]i wirtschaftlich und milit¨arisch h¨angen\]<sub>w</sub>*′ *,\...*</example>

-   prepositional phrases with prepositions *as, than*, *bis, als, wie* (in German) Such prases are annotated as normal NPs, i.e. *bis* and *als* are not included. ^3^

-   nominal premodifiers in compound nouns

	> <example id="nr24">(27) *peanut butter, airline analyst, the creditors commettee, investment bank*</example>

	*Peanut, airline, cretitors* and *investment* are no separate markables. Note that in *the creditor's opinion*, *the creditor's* is annotated as a markable, since it is a nominal in genitive and thus not a part of a compounds.

### 1.6.2 Idioms and Collocations (`REF=IDIOM`)

Referring expressions in idioms and collocations.

> <example id="nr25">(28) *It sent Kate into the pits when she learned from her "friend" Martha, who seemed to get off on laying bad trips on people, that Harvey was getting it on with Carol.*</example> \[Gib94, p.265\]

According to Gibbs, we find several idiomatic phrases in this example, some of which contain pronouns or full NPs -- potential primary markables.

However, they should not be annotated as such, e.g. *into the pits* meaning "to be depressed", *get it on* meaning "having sexual relations", neither *the pits* nor *it* can be referred to.

Note that we consider only *conventionalized* idiomatic expressions as idioms in our sense, i.e. markables within productive metaphors are annotated as usual, e.g. *das schlingernde City-Schiff* - a metaphor that occurred and can only be understood with respect to a specific text.
