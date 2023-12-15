# 4. Nominal coreference 

We annotate referential chains by co-indexing all referring expressions that refer to the same referent.<sub>[1](lit.md#coref1)</sub>

##  4.1 Scope and Aim of Annotation

1. assign every referential expressing an index that unambiguously identifies its discourse referent 
2. annotate antecedents of anaphoric expressions accordingly (regardless of whether these are referring expressions or not)
3. annotate all remaining nominal and pronominal expressions as non-referential

Noun phrases, names and pronouns are automatically pre-annotated as markables. 

We annotate every markable with
- `COREF`: an abbreviation ("index") for the discourse referent (or its absence),
- `REF`: the type of reference (see below), and
- `COMMENT`: optional structured or free-text comment indicating uncertainties or design decisions. Note that this column is used for both coreference and following annotations

We do not consider syntactically bound expressions as coreferential with their controller (e.g., predicative nominals in copula sentences, or relative pronouns), as the relationship with the hypothetical antecedent is expressed by syntactic means.

## 4.2 Annotation Procedure

Annotate all referents in the order that they occur in the text with

1. `COREF` (discourse referent tag): which referent a referring expression refers to, or `_` if the expression is not referential

2. `REF` (referentiality): reference type as defined below

3. `COMMENT` (optional comment): can contain free-text comments as well as ambiguity annotations (see below).

> Note: In spreadsheet-based annotations, some of the values for refentiality are automatically suggested (`REF_AUTO`). This may help your decision for the annotation of `REF`, but please make sure to verify that properly.

Follow the following steps (and see below for additional instructions on the annotation of `REF`):

- If the markable introduces a new discourse referent, annotate it with a new index and the reference type `NEW` (or `SIT` for first person, second person or dates). This the default for indefinites and bare nouns.
- If a markable refers to previously introduced referent, annotate it with the index used for the antecedent and annotate its reference type.
- If a markable is not a referring expression, annotate it with an empty index (`_`) and annotate the type of non-reference.
- If a markable refers to two (or more) distinct, previously mentioned discourse refents ("group reference"), create a new index for the group, followed by `\>` and the comma-separated indices of all discourse referents. Assign it the reference type `GROUP`.

Use the `COMMENT` column to annotate ambiguity and provide comments as needed. If you need to come back to a passage to confirm your annotation, put that into comment, as well.

For every referent, after annotating discourse referent index and referentiality, annotate information status. In the spreadsheet, this is partially automated, but need to be confirmed.

## 4.3 Coreference (`COREF`)

For annotating coreference, use user-defined abbreviation/mnemnonic/tag that indicates which referent a referring expression refers to, or `_` if the expression is not referential.

> Note: The discourse referent tag, or "index", is an abbreviation that a user should chose at the first mention of the referent. Chains of antecedents and anaphors should all have the same index. Create abbreviations/mnemnonics as you see fit. 

> Note: If annotating **on paper**, a suitable means of annotation is with numerical indices. For reasons of space, we also follow this practice in this document. However, when doing annotation **with the computer**, numerical indices are discouraged. Instead, use mnemnonics and create meaningful abbreviations as you see fit. 

### 4.3.1 Substitution Test

A replacement test can be used to check whether a referential expression e belongs to a chain k: If it is true for every noun s (noun, proper noun) in k, that the replacement of e by s changes the interpretation of the text is not changed, then e belongs to chain k and a coreference relation to the last element of the chain is to be annotated.

According to this scheme, we only annotate coreference relations that
express a real identity between discourse objects. A "semantically loose"
connection between a definite NP and another nominal is therefore not sufficient. For this purpose the following

*Test*: To find out if two nominal descriptions are coreferent, try to substitute them with each other. (Certain transformations may be necessary, such as removing prepositions from markables.) Note that every previous coreferent markable has to be compatible with this substitution as well.

Note that this test has some issues with metonymy, i.e., substituting a word for another word closely associated with it. Cases of metonymy in text should be annotated as coreferent if and only if the subsitution test holds for all coreferring nominals: *the State Department said\... - the State Department officials claimed\...*.

> (1) *Als 1999 die im Rahmen der Dorferneuerung neu gestaltete
     \[Radeweger\]<sub>1</sub> Ablage inklusive Seebrücke mit viel Pomp eingeweiht wurde\... Doch mit der Nachrüstung tut sich \[Radewege\]<sub>1</sub> schwer \... Zu teuer, zu hässlich sei die Anlage, sagen die Meinungsführer \[im Gemeinderat\]<sub>?</sub>*  (maz-6488)

In (1), *\[Gemeinderat\]* could be considered coreferent with *\[Radewege\]<sub>1</sub>*. Yet, although both are exchangeable by means of metonymy, the substitution test fails for *\[Radewege\]<sub>1</sub>* , since *neu gestaltete Gemeinderatsablage* is not appropriate *in that context*. Accordingly, *\[Gemeinderat\]* should receive a separate index.

### 4.3.2 Event Anaphor

Pronominal event anaphors are annotated along with their antecents. 

The antecedent of an event anaphor is normally a sentence, a clause or verb phrase. If so, select the main (lexical) verb as antecedent. Hence, in this example, we annotate *gewonnen* as we encounter the referring expression *das* "this".

> (2) *Gestern hat Bayern München schon wieder gewonnen<sub>1</sub>. \[Das\]<sub>1</sub> hat Jan ziemlich gestört. Marianne hingegen war \[davon\]<sub>1</sub> begeistert.* (Non-event anaphors skipped.)

Note that antecedents of event anaphors are not automatically pre-annotated but have to be manually created.

## 4.4 Ambiguity

Ambiguity can be annotated on demand in the `COMMENT` column, see Appendix [WHERE].

### 4.4.1 Dealing with  Ambiguous Antecedents

The assignment of an antecedent will be fairly straightforward in most cases. However, it is possible that several interpretations are *equally* plausible in the eyes of the annotator. Consider ex. (3):

> (3) *Je kleiner die <ins>Kicker</ins><sub>2,OLD,AMBIG:COREF(2,1)</sub> daherkommen, desto größer wird der <ins>Gegner</ins><sub>1,OLD,AMBIG:COREF(1,2)</sub> geredet\...* (German, maz-10374)
>       "The smaller the kickers appear, the greater \[the rivals\]<sub>d?/u?</sub> are rumoured to be." (PCC, 10374)

Antecedent of die Kicker "kickers" depends on the understanding of the "size" metaphor, it can be either the Ukrainian team (presented as having short players), or the German team (which has not been favored in the first match), or a generic description (which would mean that the sentence is not directly linked with the discourse). 

If different interpretations are equally possible, apply the following disambiguation preferences in the following order:

- prefer anaphoric interpretation to antecedentless one
- for antecedents, prefer a primary markable (`REF_AUTO=?OLD`, `REF=OLD`, etc.) over a secondary markable (no `REF_AUTO`, `REF=NEW`, etc.) or a group reference
- prefer a discourse referent that is more frequently mentioned in preceding discourse
- if several discourse referents are equally frequent, prefer the last mentioned discourse referent

For the example, the generic reading is excluded by the first preference.
However, we still have the choice between two possible antecedents. The substitution test (see above) fails to determine a unique antecedent, as both possible substitutions are plausible, depending on whether "size" refers to physical size or anticipated defeat. 
The second and third criteria are designed to produce longer anaphoric chains. They result in a preference for the German team as the antecedent of die Kicker.

In annotation, then, **mark the ambiguity** (in `COMMENT`, see Appendix on details).

## 4.5 Referentiality (`REF`)

Every markable that is not assigned an antecedent is to be annotated for referentiality. 

In spreadsheet-based annotations, some of the values are automatically suggested in `REF_AUTO`. Please make sure to verify all of them. Automated pre-annotation generates the value `?OLD` for all candidate anaphors ("primary markables") and, optionally, `?NEW` for all other candidate referring expressions ("secondary markables"). 

> These values are useful for navigating in spreadsheets. They do not need to be manually corrected by the annotator. Instead, use the `REF` column to provide your own annotation. But also `?REF` can be automatically prepropulated, and any annotation project that still contains `?OLD` or `?NEW` annotations in the `REF` column will be considered incomplete and must not be further processed.

1. `OLD`: A unit of discourse that can be interpreted based on the preceding context ("discourse-old").<sup>[2](lit.md#coref2)</sup>

2. `NEW`: Discourse entity mentioned for the first time. This includes referents that can be inferred by the hearer ("discourse-new, but hearer-old"). <sup>[3](lit.md#coref3)</sup>

3. `CAT`: Discourse cataphor, i.e., reference to a new entity introduced into the discourse with an underspecified nominal expression whose exact denotation becomes clear only from subsequent descriptions. This "scene-setting" effect is a rhetorical device employed to engage readers in literary texts.<sup>[4](lit.md#coref4)</sup>

	When reading the text of the annotation example below, it is initially unclear what *Fußball-Weltmacht* and *Winzling* refer to. This becomes clear only in the next sentence, when the German team and Ukraine are mentioned.

	> Note: Syntactic cataphors are not included here. Syntactically bound pronominal cataphors are annotated as `BOUND`.

5. `GROUP`: Referring expressions that designate groups can serve as antecedents of nominal markables and can be annotated as a group. <sup>[5](lit.md#coref5)</sup>

	> (9.a) *\[Montedison\]<sub>1</sub> now owns about 72% of \[Erbamont\'s\]<sub>2</sub> shares outstanding.*

	> (9.b) *\[The companies\]<sub>3\>1,2</sub> said ... a sale of all of \[Erbamont\'s\]<sub>2</sub> assets \... \[to Montedison\]<sub>1</sub> ...*

	> (9.c) *\[The companies\]<sub>3</sub> said ...* (WSJ, 660)

	Note that the second reference to *the companies* in (9.c) is annotated as a **plain anaphoric reference** to the established group, not as a group reference to the individual companies mentioned in the meantime.

4. `BOUND`: Pronouns that are syntactically bound, e.g. reflexive pronouns. Also, possessive pronouns governed by nominal expressions in the same sentence are annotated as `BOUND`, cf. in (8.b) below *Mit <ins>seinem</ins><sub>3,BOUND</sub> Tor*.<sup>[6](lit.md#coref6)</sup>.

	> Notes: Reflexive pronouns (which are obligatorily bound) are not annotated as markables if they can be identified on grounds of their form (e.g., English *himself*, German *sich*). Only if a form is ambiguous between a reflexive and pronominal reading (e.g., German *mich*), reflexive pronouns are annotated as `BOUND`.

5. `SIT`: situationally evoked. In written texts, this applies only to first and second person, non-reflexive pronouns and to temporal expressions.<sup>[5](lit.md#coref5)</sup>

	> Note: `SIT` is to be annotated at the first mention, only, subsequent references to the same entity are to be annotated as `OLD`.

6. `GEN`: The term *generic* denotes a special usage of a referring expression, such that not a particular individual or object is meant, but rather a class of entities or features of this class.

	> (10.a) *<ins>Whales</ins><sub>GEN</sub> are <ins>mammals</ins><sub>PRED</sub>.*
	
	> (10.b)  *Der Pr¨asident wurde immer schon durch die Stimmenmehrheit bestimmt.* "The <ins>President</ins><sub>GEN</sub> has always been elected by majority <ins>vote</ins><sub>1,NEW</sub>."

	Generics should not be annotated with a discourse referent index -- unless they are subsequently referred to:

	> (10.a') *<ins>Whales</ins><sub>1,GEN</sub> are <ins>mammals</ins><sub>PRED</sub>. <ins>They</ins><sub>1,OLD</sub> descend from land <ins>animals</ins><sub>GEN</sub>.* 

	This includes both nominal and pronominal markables. Generic pronouns include certain usages of *we*, *you*, *they* (in cases where they do not carry a specific reference), *someone*, *anyone*, *one*, *many*, etc. Also cf. German *man*.

	> (11.a) *Meier said to Müller: \"\[You\]<sub>GEN</sub> should go now.\"*
	
	> (11.b) *Meier sagte zu Müller: „\[Man\]<sub>GEN</sub> sollte jetzt gehen."* (German)

	> (11.c) *Meier said to Müller: \"Last year, \[they\]<sub>GEN</sub> demolished a house here."*

	> (11.d) *Meier sagte zu Müller: „Letzes Jahr haben \[sie\]<sub>GEN</sub> hier ein Haus abgerissen."* (German)

    > (11.e) *... \[many\]<sub>GEN</sub> of the adventures* (TED-MDB 2009)

5. `EXPL`: Non-referring expression: Expletive 	expressions (English *it*) and pronominal adverbs that are controllers of relative clauses

	> (12.a) *<ins>It</ins> was raining.*

	> (12.b) *\[ <sub></sub><sub>It</sub><sub></sub> \] was also considered certain that . . .* (English)
	
	> (12.c) *\[<sub></sub><sub>Es</sub><sub></sub>\] galt zudem als sicher, dass . . .* (German)

6. `PRED`: Non-referring expression: Predicative NPs in copular sentences

	> (13.a) *Nicht, dass beide eine Mehrheit für ihre Koalition suchten, war \[das Ärgerliche in den vergangenen Tagen\] ...* (German)

	> (13.b) *The chief physician was \[a real professional\]<sub>NM</sub>.*
	
	> (13.c) *Max Müller is \[the greatest center forward of all time\]<sub>NM</sub>!*

7. `IDIOM`: Non-referring expression: apparent referring expressions (e.g., definite NPs) in fixed, conventionalized idioms and corresponding collocations:

	> (14.a) *jemandem auf die <ins>Nerven</ins> gehen* (German, "to annoy someone")
	
	> (14.b) *Er brachte mich auf \[die Palme\]<sub>NM</sub>* (German)
	
	> (14.c) *Und dann warf sie \[die Flinte\]<sub>NM</sub> \[ins Korn\]<sub>NM</sub>.* (German)

	> Note: Referring expressions in productive, transparent metaphors that are sufficiently transparent should be annotated like anaphoric expressions. The annotator may add `AMBIG:IDIOM` if not sure about their annotation. In (7.d), *der Spatz in der Hand*, a definite NP in German, can be generic, part of an idiom, or referring:

	> (14.d) *Lieber \[der Spatz in der Hand\] als \[die Taube auf dem Dach\]*    (PCC, 12666) "A bird in the hand is worth two in the bush" (Context: a mayor finds an investor for his town willing to make only minimal investments).

	> (14.e) *So lässt sich \[das schlingernde City-Schiff\]<sub>PM</sub> vielleicht doch noch auf einen erfolgversprechenden Kurs bringen.* (German, maz-18914, here, a reference to a city is made, but combined with the metaphorical image of a ship in troubled water, for which the substitution test would fail)

	Note that we also annotate apparent referring expressions in grammaticalized phrases as `IDIOM`, e.g., *in the face of* in (14.f)

	> (14.f) People in the **Face** of Modern Warfare (Fel, S., Niewiadomska, I., & Lenart-Kłoś, K. (2022). People in the Face of Modern Warfare: Relationships Between Resource Distribution and Behaviour of Participants in the Hostilities in Ukraine. V&R unipress.)

8. `other`: other, non-referring expression, please provide a description in round parentheses. Includes, for example, NPs under the scope of a negation that cannot be referred to

	> (15) *I didn\'t buy \[a new car\]<sub>NM</sub> after all.*

## 4.6 Example

> (16.a) *\[Die einstige <ins>Fußball-Weltmacht</ins>\]<sub>1,CAT</sub> zittert \[vor einem <ins>Winzling</ins>\]<sub>2,CAT,AMBIG(2,6)</sub>.*
>      "\[The former football World Power\]<sub>d</sub> is shivering \[in the face of a mite\]<sub>s</sub>."
	
> (16.b) *Mit <ins>seinem</ins><sub>3,BOUND</sub> <ins>Tor</ins><sub>4,NEW</sub> zum <ins>1:0</ins><sub>5,NEW</sub> für die <ins>Ukraine</ins><sub>6,NEW</sub> stürzte der 1,62 Meter große \[<ins>Gennadi</ins> Subow\]<sub>2,NEW</sub> die deutsche <ins>Nationalelf</ins><sub>1,NEW</sub> vorübergehend in ein <ins>Trauma</ins><sub>7,NEW</sub>.*
>       "By \[his\]<sub>s</sub> goal that set the score to 1:0 \[for Ukraine\]<sub>u</sub> pitched \[Gennadi Subow\]<sub>s</sub>, 1.62 Meter tall, \[the German National Eleven\]<sub>d</sub> in a shock for a while..."
	
> (16.c) *Je kleiner die <ins>Kicker</ins><sub>2,OLD,AMBIG:COREF(2,1)</sub> daherkommen, desto größer wird der <ins>Gegner</ins><sub>1,OLD,AMBIG:COREF(1,2)</sub> geredet\...* (German, maz-10374)
>       "The smaller the kickers appear, the greater \[the rivals\]<sub>d?/u?</sub> are rumoured to be." (PCC, 10374)

Note that here, the antecedent of die Kicker "kickers" depends on the understanding of the "size" metaphor, it can be either the Ukrainian team (presented as having short players), or the German team (which has not been favored in the first match), or a generic description (which would mean that the sentence is not directly linked with the discourse).

## 4.6 Trouble Shooting

### 4.6.1 Recurring Group Reference

Here is a very compact, constructed example:

> (17.a) Peter<sub>1</sub> and Malte<sub>2</sub> went for a walk<sub>3</sub>. Both<sub>4\>1,2</sub> wore hats<sub>5</sub>.

> (17.b) Peter<sub>1</sub> had a coat<sub>6</sub>, Malte<sub>2</sub> a rain jacket<sub>7</sub>. 

> (17.c) They<sub>**4**</sub> reached\...

When annotating *They*, note that this group has been previously established. For this reason, we do *not* refer to the second respective mentions of *Peter* and *Malte*, but instead to the previously established index for the group introduced when annotating *Both*.

### 4.6.2 Quantified NPs

Quantified expressions are either `OLD`/`GROUP` or `NEW`:

1. They are `OLD` if the same group has been previously referred to.
2. Otherwise, they are `GROUP` if they describe a finte set of entities and all these entities are mentioned before individually.
3. Otherwise, they are `OLD` if they clearly delimit the \'set of objects\'.
4. Otherwise, they are `NEW`.

Leaving the first two cases aside, a substitution substitution test helps with the decision about `OLD` and `NEW`: If we can insert a definite article or demonstrative pronoun, does that change the meaning? If not, this is referring expression.

> (18) *people* −→ *all these people* → definite description −→ referential

### 4.6.3 Pronominal Adverbs

Depending on context, some words can be either referring expressions or not. This may be automatically pre-annotated, but must be marked as non-referring in their referentiality annotation (see above).

A notorious problem in German is the annotation of pronominal adverbs such as *damit* (in the sense "so that", not in the sense "with it"), if they act as a connector: 

> (19.a) *\[Auf dem <ins>Tisch</ins>\]<sub>PM</sub> liegt \[eine <ins>Kneifzange</ins>\]<sub>SM</sub>. \[<ins>Damit</ins>\]<sub>PM</sub> kann man viel anfangen.* (German, referential *damit* "with it")

> (19.b) *\[<ins>Ich</ins>\]<sub>PM</sub> habe \[<ins>dir</ins>\]<sub>PM</sub> \[den <ins>Brief</ins>\]<sub>PM</sub> gezeigt, damit \[<ins>du</ins>\]<sub>PM</sub> bescheid weißt.* (German, non-referential *damit" "so that")

### 4.6.4 Relative Possessive Pronouns

Relative pronouns are syntactically bound and not to be annotated, but relative posessive pronouns in possessive constructions are
treated as possessive pronouns. 

> Test for German: Ein (nicht-possessives) Relativpronomen ist genau dann gegeben, wenn es durch ‚*welch*' ersetzt werden kann:

> (20.a) *Und so schielten \[die Israelis\] \[nach Washington\], \[an \[dessen\]/*∗*welchem Tropf\] \[sie\] hängen.* (maz-19074)

> (20.b) *Und so schielten \[die Israelis\] \[nach Washington, das/welches \[sie\]* *wirtschaftlich stützt\].*

### 4.6.5 Cataphora

We distinguish two types of forward-referring expressions, discourse cataphora and syntactic cataphora.

#### 4.6.5.1 Discourse Cataphora (Anaphora of Anticipation)

Discourse cataphora is a label used for non-pronominal reference forward. Sometimes an author introduces a discourse referent by means of an underspecified NP, i.e. an NP that cannot be interpreted only on the basis of the reader's knowledge up to this point. This way the author tries to encourage the reader to continue reading, in order to catch up the missing information. In the example below, *die einstige
Fußball-Weltmacht* and *vor einem Winzling* should be annotated as discourse cataphors, since their referents cannot be identified until introduced explicitly in the following text (*Deutschland* and
*Ukraine* correspondingly).

> (21) *Die einstige Fußball-Weltmacht zittert vor einem Winzling* (newspaper article title)

In case one goes on reading the text, it becomes clear that *die einstige Fußball-Weltmacht* refers to Germany, whereas *ein Winzling* refers either to the Ukraine or the 1.62 meter tall ukranian footballer who made the most impact in the match ^5^. Discourse cataphors have to be annotated as normal anaphors, i.e. in accordance with the Chain Principle (p. 12), i.e. the most recent referent mention to the left (if any) is considered to be an antecedent.

#### 4.6.5.2 Syntactic cataphora

> (22) *Through \[his\] lawyers, \[Mr. Antar\] has denied allegations in the SEC suit \...* (WSJ)

Syntactic cataphors are to be annotated like pronominal anaphora, mark referentiality as `BOUND` or `OLD`, whichever appropriate.

The following examples (a nominal head followed by a restrictive modifier), although traditionally classified as cataphora, should
NOT be annotated as such.

> (23) \... \[*the car that went through his garden wall* \]\...

> (24) \... \[*the patterns of industrial development in the U.S* \]\....

In case of doubt between syntactic cataphora or anaphora, decision has to be made as follows.

> (25.a) *Die einstige Fußball-Weltmacht zittert \[vor einem
Winzling\]s.*

> (25.b) *\[Mit \[seinem\]s Tor zum 1:0 für die Ukraine\] stürzte
\[der 1,62 Meter große Gennadi Subow\]s \[die deutsche Nationalelf\] vorübergehend in ein Trauma.*

In the example, *seinem* refers to *Gennadi Subow* who was introduced in the very first sentence as *vor einem Winzling*. Following the preferences, we establish an anaphoric (cataphoric) link to the right.
Thus, the anaphoric chain looks as follows:

-   *seinem* → *Gennadi Subow* (same-sentence)

-   *Gennadi Subow* → *vor einem Winzling* (right+previous, Chain
    Principle)
