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

In spreadsheet-based annotations, some of the values for refentiality are automatically suggested (`REF_AUTO`). This may help your decision for the annotation of `REF`, but please make sure to verify that properly.

Follow the following steps (and see below for additional instructions on the annotation of `REF`):

- If the markable introduces a new discourse referent, annotate it with a new index and the reference type `NEW` (or `SIT` for first person, second person or dates). This the default for indefinites and bare nouns.
- If a markable refers to previously introduced referent, annotate it with the index used for the antecedent and annotate its reference type.
- If a markable is not a referring expression, annotate it with an empty index (`_`) and annotate the type of non-reference.
- If a markable refers to two (or more) distinct, previously mentioned discourse refents ("group reference"), create a new index for the group, followed by `\>` and the comma-separated indices of all discourse referents. Assign it the reference type `GROUP`.

Use the `COMMENT` column to annotate ambiguity and provide comments as needed. If you need to come back to a passage to confirm your annotation, put that into comment, as well.

For every referent, after annotating discourse referent index and referentiality, annotate information status. In the spreadsheet, this is partially automated, but need to be confirmed.

## 4.3 Coreference (`COREF`)

For annotating coreference, use user-defined abbreviation/mnemnonic/tag that indicates which referent a referring expression refers to, or `_` if the expression is not referential.

> Note: The discourse referent tag, or "index", is an abbreviation that a user should chose at the first mention of the referent. Chains of antecedents and anaphors should all have the same index.	

> Note: In this document, we use numerical indexes for presentational reasons. In annotation, create abbreviations/mnemnonics as you see fit. Numerical indices are discouraged in actual annotation. 

## 4.3.1 Substitution Test

A replacement test can be used to check whether a referential expression e belongs to a chain k: If it is true for every noun s (noun, proper noun) in k, that the replacement of e by s changes the interpretation of the text is not changed, then e belongs to chain k and a coreference relation to the last element of the chain is to be annotated.

According to this scheme, we only annotate coreference relations that
express a real identity between discourse objects. A "semantically loose"
connection between a definite NP and another nominal is therefore not sufficient. For this purpose the following

*Test*: To find out if two nominal descriptions are coreferent, try to substitute them with each other. (Certain transformations may be necessary, such as removing prepositions from markables.) Note that every previous coreferent markable has to be compatible with this substitution as well.

Note that this test has some issues with metonymy, i.e., substituting a word for another word closely associated with it. Cases of metonymy in text should be annotated as coreferent if and only if the subsitution test holds for all coreferring nominals: *the State Department said\... - the State Department officials claimed\...*.

> (1) *Als 1999 die im Rahmen der Dorferneuerung neu gestaltete
     \[Radeweger\]~1~ Ablage inklusive Seebrücke mit viel Pomp eingeweiht wurde\... Doch mit der Nachrüstung tut sich \[Radewege\]~1~ schwer \... Zu teuer, zu hässlich sei die Anlage, sagen die Meinungsführer \[im Gemeinderat\]~?~*  (maz-6488)

In (1), *\[Gemeinderat\]* could be considered coreferent with *\[Radewege\]~1~*. Yet, although both are exchangeable by means of metonymy, the substitution test fails for *\[Radewege\]~1~* , since *neu gestaltete Gemeinderatsablage* is not appropriate *in that context*. Accordingly, *\[Gemeinderat\]* should receive a separate index.

### 4.3.2 Event Anaphor

Pronominal event anaphors are annotated along with their antecents. 

The antecedent of an event anaphor is normally a sentence, a clause or verb phrase. If so, select the main (lexical) verb as antecedent. Hence, in this example, we annotate *gewonnen* as we encounter the referring expression *das* "this".

> (2) *Gestern hat Bayern München schon wieder gewonnen~1~. \[Das\]~1~ hat Jan ziemlich gestört. Marianne hingegen war \[davon\]~1~ begeistert.* (Non-event anaphors skipped.)

Note that antecedents of event anaphors are not automatically pre-annotated but have to be manually created.

## 4.4 Ambiguity

Ambiguity can be annotated on demand in the `COMMENT` column.

### 4.4.1 Dealing with  Ambiguous Antecedents

The assignment of an antecedent will be fairly straightforward in most cases. However, it is possible that several interpretations are *equally* plausible in the eyes of the annotator. Consider ex. (3):

> (3) *Je kleiner die <ins>Kicker</ins>~2,OLD,AMBIG:COREF(2,1)~ daherkommen, desto größer wird der <ins>Gegner</ins>~1,OLD,AMBIG:COREF(1,2)~ geredet\...* (German, maz-10374)
>       "The smaller the kickers appear, the greater \[the rivals\]~d?/u?~ are rumoured to be." (PCC, 10374)

Antecedent of die Kicker "kickers" depends on the understanding of the "size" metaphor, it can be either the Ukrainian team (presented as having short players), or the German team (which has not been favored in the first match), or a generic description (which would mean that the sentence is not directly linked with the discourse). 

If different interpretations are equally possible, apply the following disambiguation preferences in the following order:

- prefer anaphoric interpretation to antecedentless one
- for antecedents, prefer a primary markable (`REF_AUTO=?OLD`, `REF=OLD`, etc.) over a secondary markable (no `REF_AUTO`, `REF=NEW`, etc.) or a group reference
- prefer a discourse referent that is more frequently mentioned in preceding discourse
- if several discourse referents are equally frequent, prefer the last mentioned discourse referent

For the example, the generic reading is excluded by the first preference.
However, we still have the choice between two possible antecedents. The substitution test (see above) fails to determine a unique antecedent, as both possible substitutions are plausible, depending on whether "size" refers to physical size or anticipated defeat. 
The second and third criteria are designed to produce longer anaphoric chains. They result in a preference for the German team as the antecedent of die Kicker.

In annotation, then, **mark the ambiguity** (in `COMMENT`)

### 4.4.2 Types of Ambiguity

Ambiguity is to be annotated in the `COMMENT` field, using pre-defined tags (if applicable) or plain text descriptions (otherwise). Optionally, ambiguity tags can be followed by a more detailed description in round parentheses `(...)`.

The following tags can be used to mark ambiguous 

1. `AMBIG:COREF` (ambiguous antecedent):<sup>[7](lit.md#coref7)</sup> There is uncertainty as to which is the \"right\" antecedent for an anaphor (or, controller for a cataphor). See above for antecedent selection preferences, provide referent index for all equally likely antecedents in round parentheses

	> (4) *In a letter, \[prosecutors\]~p~ told \[Mr. Antar's lawyers\]~l~ that because of the recent Supreme Court rulings, \[they\]~p/l~*~?~ *could expect that any fees collected from Mr. Antar may be seized.*

2. `AMBIG:REL`: There is uncertainty as to whether an anaphoric relation exists or which type it is (anaphoric vs. bridging or event, i.e. contextual inference)

	This is sometimes the case with definite NPs. In the example below: If it is unclear whether the *confrontation* is identical to the *conflict*, the coreference should be annotated and the markable should be marked with this attribute. It is not necessary to provide a more detailed description.

	> (5) *This <ins>conflict</ins> is ... Therefore, the <ins>confrontation</ins> ...*

3. `AMBIG:IDIOM`: There is uncertainty as to whether a markable could be understood as a referential expression or as part of an idiom. Annotate anaphoric reading and mark the ambiguity.

4. `AMBIG:EXPL`: There is uncertainty as to whether a pronoun is an expletive (and therefore non-referring) or whether it is anaphoric. Annotate the anaphoric relations and mark the ambiguity. No description necessary.

	> (6) *At stake was an \$80,000 settlement involving who should pay what share of cleanup costs at the site of a former gas station, where underground fuel tanks had leaked and contaminated the soil. And the lawyers were just as eager as the judge to wrap \[it\] up.*

	*It* can either be interpreted as referring to *an \$80,000 settlement* or as a part of a lexicalized expression *to wrap it up* where *it* does not have any particular reference. 

	This can be made clearer with a constructed example:

	> (7.a) *She looks out of the window. <ins>It</ins>~EXPL~ is dark.* (expletive)
	
	> (7.b) *Your <ins>cat</ins>~1~ has a nice color. <ins>It</ins>~1~ is dark, much more so than mine.* (anaphoric)
	
	> (7.c) *The <ins>cat</ins>~1~ is hard to see. <ins>It</ins>~1,AMBIG:EXPL~ is dark.* (ambiguous)

5. `AMBIG:COREF_REL`: There is ambiguity with respect to both antecedent and relation

	> (8) "There seems to be a move around the world to deregulate the genera- tion of electricity," Mr. Richardson said, and Canadian Utilities hopes to capitalize on it.

	*On it* refers either to *a move around the world to deregulate the generation of electricity*, or to the whole clause beginning with
	*there* and ending with *electricity* (event anaphora).

6. `AMBIG:other`: other cases of ambiguity. Please provide a description in round parentheses.

If more than one kind of ambiguity applies, e.g., both ambiguity of antecedent and ambiguity of an anaphoric relation, then provide all of the corresponding tags (and descriptions), separated by comma.

## 4.3 Referentiality (`REF`)

Every markable that is not assigned an antecedent is to be annotated for referentiality. 

In spreadsheet-based annotations, some of the values are automatically suggested in `REF_AUTO`. Please make sure to verify all of them. Automated pre-annotation generates the value `?OLD` for all candidate anaphors ("primary markables") and, optionally, `?NEW` for all other candidate referring expressions ("secondary markables"). 

> **To be confirmed**: These values need to be manually replaced by the annotator. An annotation project that still contains `?OLD` or `?NEW` annotations will be considered incomplete and must not be further processed.

1. `OLD`: A unit of discourse that can be interpreted based on the preceding context ("discourse-old").<sup>[2](lit.md#coref2)</sup>

2. `NEW`: Discourse entity mentioned for the first time. This includes referents that can be inferred by the hearer ("discourse-new, but hearer-old"). <sup>[3](lit.md#coref3)</sup>

3. `CAT`: Discourse cataphor, i.e., reference to a new entity introduced into the discourse with an underspecified nominal expression whose exact denotation becomes clear only from subsequent descriptions. This "scene-setting" effect is a rhetorical device employed to engage readers in literary texts.<sup>[4](lit.md#coref4)</sup>

	When reading the text of the annotation example below, it is initially unclear what *Fußball-Weltmacht* and *Winzling* refer to. This becomes clear only in the next sentence, when the German team and Ukraine are mentioned.

	> Note: Syntactic cataphors are not included here. Syntactically bound pronominal cataphors are annotated as `BOUND`.

5. `GROUP`: Referring expressions that designate groups can serve as antecedents of nominal markables and can be annotated as a group. <sup>[5](lit.md#coref5)</sup>

	> (9.a) *\[Montedison\]~1~ now owns about 72% of \[Erbamont\'s\]~2~ shares outstanding.*

	> (9.b) *\[The companies\]~3\>1,2~ said ... a sale of all of \[Erbamont\'s\]~2~ assets \... \[to Montedison\]~1~ ...*

	> (9.c) *\[The companies\]~3~ said ...* (WSJ, 660)

	Note that the second reference to *the companies* in (9.c) is annotated as a **plain anaphoric reference** to the established group, not as a group reference to the individual companies mentioned in the meantime.

4. `BOUND`: Pronouns that are syntactically bound, e.g. reflexive pronouns. Also, possessive pronouns governed by nominal expressions in the same sentence are annotated as `BOUND`, cf. in (8.b) below *Mit <ins>seinem</ins>~3,BOUND~ Tor*.<sup>[6](lit.md#coref6)</sup>

	> Notes: Reflexive pronouns (which are obligatorily bound) are not annotated as markables if they can be identified on grounds of their form (e.g., English *himself*, German *sich*). Only if a form is ambiguous between a reflexive and pronominal reading (e.g., German *mich*), reflexive pronouns are annotated as `BOUND`.

5. `SIT`: situationally evoked. In written texts, this applies only to first and second person, non-reflexive pronouns and to temporal expressions.<sup>[5](lit.md#coref5)</sup>

	> Note: `SIT` is to be annotated at the first mention, only, subsequent references to the same entity are to be annotated as `OLD`.

6. `GEN`: The term *generic* denotes a special usage of a referring expression, such that not a particular individual or object is meant, but rather a class of entities or features of this class.

	> (10.a) *<ins>Whales</ins>~GEN~ are <ins>mammals</ins>~PRED~.*
	
	> (10.b)  *Der Pr¨asident wurde immer schon durch die Stimmenmehrheit bestimmt.* "The <ins>President</ins>~GEN~ has always been elected by majority <ins>vote</ins>~1,NEW~."

	Generics should not be annotated with a discourse referent index -- unless they are subsequently referred to:

	> (10.a') *<ins>Whales</ins>~1,GEN~ are <ins>mammals</ins>~PRED~. <ins>They</ins>~1,OLD~ descend from land <ins>animals</ins>~GEN~.* 

	This includes both nominal and pronominal markables. Generic pronouns such as *we*, *you*, *they* (in cases where they do not carry a specific reference), *someone*, *anyone*, *one*. Cf. German *man*.

	> (11.a) *Meier said to Müller: \"\[You\]~GEN~ should go now.\"*
	
	> (11.b) *Meier sagte zu Müller: „\[Man\]~GEN~ sollte jetzt gehen."* (German)

	> (11.c) *Meier said to Müller: \"Last year, \[they\]~GEN~ demolished a house here."*

	> (11.d) *Meier sagte zu Müller: „Letzes Jahr haben \[sie\]~GEN~ hier ein Haus abgerissen."* (German)

5. `EXPL`: Non-referring expression: Expletive 	expressions (English *it*) and pronominal adverbs that are controllers of relative clauses

	> (12.a) *<ins>It</ins> was raining.*

	> (12.b) *\[ ~~~It~~~ \] was also considered certain that . . .* (English)
	
	> (12.c) *\[~~~Es~~~\] galt zudem als sicher, dass . . .* (German)

6. `PRED`: Non-referring expression: Predicative NPs in copular sentences

	> (13.a) *Nicht, dass beide eine Mehrheit für ihre Koalition suchten, war \[das Ärgerliche in den vergangenen Tagen\] ...* (German)

	> (13.b) *The chief physician was \[a real professional\]~NM~.*
	
	> (13.c) *Max Müller is \[the greatest center forward of all time\]~NM~!*

7. `IDIOM`: Non-referring expression: apparent referring expressions (e.g., definite NPs) in fixed, conventionalized idioms and corresponding collocations:

	> (14.a) *jemandem auf die <ins>Nerven</ins> gehen* (German, "to annoy someone")
	
	> (14.b) *Er brachte mich auf \[die Palme\]~NM~* (German)
	
	> (14.c) *Und dann warf sie \[die Flinte\]~NM~ \[ins Korn\]~NM~.* (German)

	> Note: Referring expressions in productive, transparent metaphors that are sufficiently transparent should be annotated like anaphoric expressions. The annotator may add `AMBIG:IDIOM`if not sure about their annotation. In (7.d), *der Spatz in der Hand*, a definite NP in German, can be generic, part of an idiom, or referring:

	> (14.d) *Lieber \[der Spatz in der Hand\] als \[die Taube auf dem Dach\]*    (PCC, 12666) "A bird in the hand is worth two in the bush" (Context: a mayor finds an investor for his town willing to make only minimal investments).

	> (14.e) *So lässt sich \[das schlingernde City-Schiff\]~PM~ vielleicht doch noch auf einen erfolgversprechenden Kurs bringen.* (German, maz-18914, here, a reference to a city is made, but combined with the metaphorical image of a ship in troubled water, for which the substitution test would fail)

8. `other`: other, non-referring expression, please provide a description in round parentheses. Includes, for example, NPs under the scope of a negation that cannot be referred to

	> (15) *I didn\'t buy \[a new car\]~NM~ after all.*

### 4.4 Example

> (16.a) *\[Die einstige <ins>Fußball-Weltmacht</ins>\]~1,CAT~ zittert \[vor einem <ins>Winzling</ins>\]~2,CAT,AMBIG(2,6)~.*
>      "\[The former football World Power\]~d~ is shivering \[in the face of a mite\]~s~."
	
> (16.b) *Mit <ins>seinem</ins>~3,BOUND~ <ins>Tor</ins>~4,NEW~ zum <ins>1:0</ins>~5,NEW~ für die <ins>Ukraine</ins>~6,NEW~ stürzte der 1,62 Meter große \[<ins>Gennadi</ins> Subow\]~2,NEW~ die deutsche <ins>Nationalelf</ins>~1,NEW~ vorübergehend in ein <ins>Trauma</ins>~7,NEW~.*
>       "By \[his\]~s~ goal that set the score to 1:0 \[for Ukraine\]~u~ pitched \[Gennadi Subow\]~s~, 1.62 Meter tall, \[the German National Eleven\]~d~ in a shock for a while..."
	
> (16.c) *Je kleiner die <ins>Kicker</ins>~2,OLD,AMBIG:COREF(2,1)~ daherkommen, desto größer wird der <ins>Gegner</ins>~1,OLD,AMBIG:COREF(1,2)~ geredet\...* (German, maz-10374)
>       "The smaller the kickers appear, the greater \[the rivals\]~d?/u?~ are rumoured to be." (PCC, 10374)

Note that here, the antecedent of die Kicker "kickers" depends on the understanding of the "size" metaphor, it can be either the Ukrainian team (presented as having short players), or the German team (which has not been favored in the first match), or a generic description (which would mean that the sentence is not directly linked with the discourse).

## 4.5 Trouble Shooting

### 4.5.1 Recurring Group Reference

Here is a very compact, constructed example:

> (17.a) Peter~1~ and Malte~2~ went for a walk~3~. Both~4\>1,2~ wore hats~5~.

> (17.b) Peter~1~ had a coat~6~, Malte~2~ a rain jacket~7~. 

> (17.c) They~**4**~ reached\...

When annotating *They*, note that this group has been previously established. For this reason, we do *not* refer to the second respective mentions of *Peter* and *Malte*, but instead to the previously established index for the group introduced when annotating *Both*.

### 4.5.2 Quantified NPs

Quantified expressions are either `OLD`/`GROUP` or `NEW`:

1. They are `OLD` if the same group has been previously referred to.
2. Otherwise, they are `GROUP` if they describe a finte set of entities and all these entities are mentioned before individually.
3. Otherwise, they are `OLD` if they clearly delimit the \'set of objects\'.
4. Otherwise, they are `NEW`.

Leaving the first two cases aside, a substitution substitution test helps with the decision about `OLD` and `NEW`: If we can insert a definite article or demonstrative pronoun, does that change the meaning? If not, this is referring expression.

> (18) *people* −→ *all these people* → definite description −→ referential

### 4.5.3 Pronominal Adverbs

Depending on context, some words can be either referring expressions or not. This may be automatically pre-annotated, but must be marked as non-referring in their referentiality annotation (see above).

A notorious problem in German is the annotation of pronominal adverbs such as *damit* (in the sense "so that", not in the sense "with it"), if they act as a connector: 

> (19.a) *\[Auf dem <ins>Tisch</ins>\]~PM~ liegt \[eine <ins>Kneifzange</ins>\]~SM~. \[<ins>Damit</ins>\]~PM~ kann man viel anfangen.* (German, referential *damit* "with it")

> (19.b) *\[<ins>Ich</ins>\]~PM~ habe \[<ins>dir</ins>\]~PM~ \[den <ins>Brief</ins>\]~PM~ gezeigt, damit \[<ins>du</ins>\]~PM~ bescheid weißt.* (German, non-referential *damit" "so that")

### 4.5.4 Relative Possessive Pronouns

Relative pronouns are syntactically bound and not to be annotated, but relative posessive pronouns in possessive constructions are
treated as possessive pronouns. 

> Test for German: Ein (nicht-possessives) Relativpronomen ist genau dann gegeben, wenn es durch ‚*welch*' ersetzt werden kann:

> (20.a) *Und so schielten \[die Israelis\] \[nach Washington\], \[an \[dessen\]/*∗*welchem Tropf\] \[sie\] hängen.* (maz-19074)

> (20.b) *Und so schielten \[die Israelis\] \[nach Washington, das/welches \[sie\]* *wirtschaftlich stützt\].*

### 4.5.5 Cataphora

We distinguish two types of forward-referring expressions, discourse cataphora and syntactic cataphora.

#### 4.5.5.1 Discourse Cataphora (Anaphora of Anticipation)

Discourse cataphora is a label used for non-pronominal reference forward. Sometimes an author introduces a discourse referent by means of an underspecified NP, i.e. an NP that cannot be interpreted only on the basis of the reader's knowledge up to this point. This way the author tries to encourage the reader to continue reading, in order to catch up the missing information. In the example below, *die einstige
Fußball-Weltmacht* and *vor einem Winzling* should be annotated as discourse cataphors, since their referents cannot be identified until introduced explicitly in the following text (*Deutschland* and
*Ukraine* correspondingly).

> (21) *Die einstige Fußball-Weltmacht zittert vor einem Winzling* (newspaper article title)

In case one goes on reading the text, it becomes clear that *die einstige Fußball-Weltmacht* refers to Germany, whereas *ein Winzling* refers either to the Ukraine or the 1.62 meter tall ukranian footballer who made the most impact in the match ^5^. Discourse cataphors have to be annotated as normal anaphors, i.e. in accordance with the Chain Principle (p. 12), i.e. the most recent referent mention to the left (if any) is considered to be an antecedent.

#### 4.5.5.2 Syntactic cataphora

> (22) *Through \[his\] lawyers, \[Mr. Antar\] has denied allegations in the SEC suit \...* (WSJ)

Syntactic cataphors are to be annotated like pronominal anaphora, mark referentiality as `BOUND` or `OLD`, whichever appropriate.

The following examples (a nominal head followed by a restrictive modifier), although traditionally classified as cataphora, should
NOT be annotated as such.

> (23) \... \[*the car that went through his garden wall* \]\...

> (24) \... \[*the patterns of industrial development in the U.S* \]\....

In case of doubt between syntactic cataphora or anaphora, decision has to be made as follows.

> (25.a) *Die einstige Fußball-Weltmacht zittert \[vor einem
Winzling\]s.*

> (25.b) *\[Mit \[seinem\]s Tor zum 1:0 fu¨r die Ukraine\] stu¨rzte
\[der 1,62 Meter große Gennadi Subow\]s \[die deutsche Nationalelf\] voru¨bergehend in ein Trauma.*

In the example, *seinem* refers to *Gennadi Subow* who was introduced in the very first sentence as *vor einem Winzling*. Following the preferences, we establish an anaphoric (cataphoric) link to the right.
Thus, the anaphoric chain looks as follows:

-   *seinem* → *Gennadi Subow* (same-sentence)

-   *Gennadi Subow* → *vor einem Winzling* (right+previous, Chain
    Principle)
