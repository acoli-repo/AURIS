**source**: 
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale Koreferenz, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.71-85
- automatically translated using www.onlinedoctranslator.com and converted to Markdown using PanDoc
- revision by Christian Chiarcos
- see Readme.md for contributors and revision history

# Nominal coreference 

We annotate referential chains by co-indexing all referring expressions that refer to the same referent.

> Note: This differs from Chiarcos et al. (2016) who annotated anaphoric relations between anaphors and their antecedents, instead. Note that this means that we do not distinguish anaphoric (pronominal) and non-anaphoric (nominal) coreference, here.

##  Scope and Aim of Annotation

1. assign every referential expressing an index that unambiguously identifies its discourse referent 
2. annotate antecedents of anaphoric expressions accordingly (regardless of whether these are referring expressions or not)
3. annotate all remaining nominal and pronominal expressions as non-referential

Noun phrases, names and pronouns are automatically pre-annotated as markables. 

We annotate every markable with
- an abbreviation ("index") for the discourse referent (or its absence),
- the type of reference (see below), and
- optionally, with a free-text comment indicating uncertainties or design decisions

We do not consider syntactically bound expressions as coreferential with their controller (e.g., predicative nominals in copula sentences, or relative pronouns), as the relationship with the hypothetical antecedent is expressed by syntactic means.

## Annotation Procedure

Annotate all referents in the order that they occur in the text with

1. discourse referent tag: User-defined abbreviation/mnemnonic/tag that indicates which referent a referring expression refers to, or `_` if the expression is not referential.

	> Note: 
	> - The discourse referent tag, or "index", is an abbreviation that a user should chose at the first mention of the referent. Chains of antecedents and anaphors should all have the same index.	
	> - In this document, we use numerical indexes for presentational reasons. In annotation, create abbreviations/mnemnonics as you see fit. Numerical indices are discouraged. 

2. referentiality: reference type as defined below
3. (optionally) comment: can contain free-text comments as well as ambiguity annotations (see below).

In spreadsheet-based annotations, some of the values for refentiality are automatically suggested. Please make sure to verify all of them.

- If the markable introduces a new discourse referent, annotate it with a new index and the reference type `NEW` (or `SIT` for first person, second person or dates). This the default for indefinites and bare nouns.
- If a markable refers to previously introduced referent, annotate it with the index used for the antecedent and annotate its reference type.
- If a markable is not a referring expression, annotate it with an empty index (`_`) and annotate the type of non-reference.
- If a markable refers to two (or more) distinct, previously mentioned discourse refents ("group reference"), create a new index for the group, followed by `\>` and the comma-separated indices of all discourse referents. Assign it the reference type `GROUP`.

	> (3)
	> (a) *\[Montedison\]~1~ now owns about 72% of \[Erbamont\'s\]~2~ shares outstanding.*
	> (b) *\[The companies\]~3\>1,2~ said ... a sale of all of \[Erbamont\'s\]~2~ assets \... \[to Montedison\]~1~ ...*
	> (c) *\[The companies\]~3~ said ...* (WSJ, 660)

> Note that the second reference to *the companies* in (3.c) is annotated as a **plain anaphoric reference** to the established group, not as a group reference to the individual companies mentioned in the meantime.

Annotate ambiguity and provide comments as needed. If you need to come back to a passage to confirm your annotation, put that into comment, as well.

For every referent, after annotating discourse referent index and referentiality, annotate information status. In the spreadsheet, this is partially automated, but need to be confirmed.

## Referentiality

Every markable that is not assigned an antecedent is to be annotated for referentiality. 

In spreadsheet-based annotations, some of the values are automatically suggested. Please make sure to verify all of them.

1. `OLD`: A unit of discourse that can be interpreted based on the preceding context. 

	> Note: 
	> - Corresponds to "discourse old" according to Prince (1992). Originally abbreviated as `referring` (Chiarcos and Krasavina 2005).
	> - Automated pre-annotation generates the value `?OLD` for all candidate anaphors (Krasavina and Chiarcos 2007: "primary markables") and `?NEW` for all other candidate referring expressions (Krasavina and Chiarcos 2007: "secondary markables"). These values need to be manually replaced by the annotator. An annotation project that still contains `?OLD` or `?NEW` annotations will be considered incomplete and must not be further processed.

2. `NEW`: Discourse entity mentioned for the first time. This includes referents that can be inferred by the hearer. 

	> Note: Corresponds to "discourse new" according to Prince (1992). Originally abbreviated as `discourse-new` (Chiarcos and Krasavina 2005).

3. `CAT`: Discourse cataphor, i.e., reference to a new entity introduced into the discourse with an underspecified nominal expression whose exact denotation becomes clear only from subsequent descriptions. This "scene-setting" effect is a rhetorical device employed to engage readers in literary texts.

	When reading (8.a) in the example below, it is initially unclear what *Fußball-Weltmacht* and *Winzling* refer to. This becomes clear only in sentence (8.b), when the German team and Ukraine are mentioned.

	> Notes: 
	> - Originally abbreviated as `discourse-cataphora` by Chiarcos and Krasavina (2005).
	> - Syntactic cataphors are not included here.
	> - Syntactically bound pronominal cataphors are annotated as `BOUND`.

5. `GROUP`: Referring expressions that designate groups can serve as antecedents of nominal markables and can be annotated as a group. 

	> (4.a) *\[\[Montedison\]m\]c*1 *now owns about 72% of \[\[Erbamont's\]e\]c*2 *shares outstanding.*
	> (4.b) *\[The companies\]c said the accord was unanimously approved by a special committee of \[Erbamont\]e directors unaffiliated with \[Montedison\]m.* (WSJ corpus)

	> Note: Subsumed under `other` in the PoCoS core scheme (Chiarcos and Krasavina 2005)

4. `BOUND`: Pronouns that are syntactically bound, e.g. reflexive pronouns. Also, possessive pronouns governed by nominal expressions in the same sentence are annotated as `BOUND`, cf. in (8.b) below *Mit <u>seinem</u>~3,BOUND~ Tor*. 

	> Notes:
	> - Reflexive pronouns (which are obligatorily bound) are not annotated as markables if they can be identified on grounds of their form (e.g., English *himself*, German *sich*). Only if a form is ambiguous between a reflexive and pronominal reading (e.g., German *mich*), reflexive pronouns are annotated as `BOUND`.
	> - Not part of the original PoCoS core scheme (Chiarcos and Krasavina 2005)

5. `SIT`: situationally evoked. In written texts, this applies only to first and second person, non-reflexive pronouns and to temporal expressions. 

	> Notes: 
	> - `SIT` is to be annotated at the first mention, only, subsequent references to the same entity are to be annotated as `OLD`.
	> - Subsumed under `other` in the PoCoS core scheme (Chiarcos and Krasavina 2005)

6. `GEN`: The term *generic* denotes a special usage of a referring expression, such that not a particular individual or object is meant, but rather a class of entities or features of this class.

	> (7.a) *<u>Whales</u>~GEN~ are <u>mammals</u>~PRED~.*
	> (7.b)  *Der Pr¨asident wurde immer schon durch die Stimmenmehrheit bestimmt.* "The <u>President</u>~GEN~ has always been elected by majority <u>vote</u>~1,NEW~."

	> Notes:
	> - Abbreviated `generic` in the original PoCoS core scheme (Chiarcos and Krasavina 2005)

	Other cases to be classified as other are *predicative descriptions*.

	> (7.c) *Nicht, dass beide eine Mehrheit für ihre Koalition suchten, war
    \[das Ärgerliche* *in den vergangenen Tagen\]* \... (predicative description, PCC)
	> (7.d) *Und das ist \[das Dilemma der Regierenden\]* (predicative description, probably generic, PCC)

	Generics should not be annotated with a discourse referent index -- unless they are subsequently referred to:

		> (7.a') *<u>Whales</u>~1,GEN~ are <u>mammals</u>~PRED~. <u>They</u>~1,OLD~ descend from land <u>animals</u>~GEN~.* 

	This includes both nominal and pronominal markables. Generic pronouns such as *we*, *you*, *they* (in cases where they do not carry a specific reference), *someone*, *anyone*, *one*. Cf. German *man*.

	> (19.a) *Meier said to Müller: \"\[You\]~GEN~ should go now.\"*
	> (19.b) *Meier sagte zu Müller: „\[Man\]~GEN~ sollte jetzt gehen."* (German)

	> (20.a) *Meier said to Müller: \"Last year, \[they\]~GEN~ demolished a house here."*
	> (20.b) *Meier sagte zu Müller: „Letzes Jahr haben \[sie\]~GEN~ hier ein Haus abgerissen."* (German)

5. `EXPL`: Non-referring expression: Expletive 	expressions (English *it*) and pronominal adverbs that are controllers of relative clauses

	> (7.c.i) *<u>It</u>~EXPL~ was raining.*
	> (7.c.ii) *\[ ~~~It~~~ \]~NM~ was also considered certain that . . .* (English)
	> (7.c.iii) *\[~~~Es~~~\]~NM~ galt zudem als sicher, dass . . .* (German)

6. `PRED`: Non-referring expression: Predicative NPs in copular sentences

	> (7.d.i) *Nicht, dass beide eine Mehrheit für ihre Koalition suchten, war \[das Ärgerliche in den vergangenen Tagen\] ...* (German)
	> (7.d.ii) *The chief physician was \[a real professional\]~NM~.*
	> (7.d.iii) *Max Müller is \[the greatest center forward of all time\]~NM~!*

7. `IDIOM`: Non-referring expression: apparent referring expressions (e.g., definite NPs) in fixed, conventionalized idioms and corresponding collocations:

	> (7.e.i) *jemandem auf die <u>Nerven</u> gehen* (German, "to annoy someone")
	> (7.e.ii) *Er brachte mich auf \[die Palme\]~NM~* (German)
	> (7.e.iii) *Und dann warf sie \[die Flinte\]~NM~ \[ins Korn\]~NM~.* (German)

	> Note: Referring expressions in productive, transparent metaphors that are sufficiently transparent should be annotated like anaphoric expressions. The annotator may add `AMBIG:IDIOM`if not sure about their annotation. In (7.e.iv), *der Spatz in der Hand*, a definite NP in German, can be generic, part of an idiom, or referring:

	> (7.e.iv) *Lieber \[der Spatz in der Hand\] als \[die Taube auf dem Dach\]*    (PCC, 12666)
	> "A bird in the hand is worth two in the bush" (Context: a mayor finds an investor for his town willing to make only minimal investments).

	> (7.e.v) *So lässt sich \[das schlingernde City-Schiff\]~PM~ vielleicht doch noch auf einen erfolgversprechenden Kurs bringen.* (German, maz-18914, here, a reference to a city is made, but combined with the metaphorical image of a ship in troubled water, for which the substitution test would fail)

8. `other`: other, non-referring expression, please provide a description in round parentheses. Includes, for example, NPs under the scope of a negation that cannot be referred to

	> (7.f) *I didn\'t buy \[a new car\]~NM~ after all.*


### Example

	> (8.a) *\[Die einstige <u>Fußball-Weltmacht</u>\]~1,CAT~ zittert \[vor einem <u>Winzling</u>\]~2,CAT,AMBIG(2,6)~.*
	>      "\[The former football World Power\]~d~ is shivering \[in the face of a mite\]~s~."
	> (8.b) *Mit <u>seinem</u>~3,BOUND~ <u>Tor</u>~4,NEW~ zum <u>1:0</u>~5,NEW~ für die <u>Ukraine</u>~6,NEW~ stürzte der 1,62 Meter große \[<u>Gennadi</u> Subow\]~2,NEW~ die deutsche <u>Nationalelf</u>~1,NEW~ vorübergehend in ein <u>Trauma</u>~7,NEW~.*
	>       "By \[his\]~s~ goal that set the score to 1:0 \[for Ukraine\]~u~ pitched \[Gennadi Subow\]~s~, 1.62 Meter tall, \[the German National Eleven\]~d~ in a shock for a while..."
	> (8.c) *Je kleiner die <u>Kicker</u>~2,OLD,AMBIG:COREF(2,1)~ daherkommen, desto größer wird der <u>Gegner</u>~1,OLD,AMBIG:COREF(1,2)~ geredet\...* (German, maz-10374)
	>       "The smaller the kickers appear, the greater \[the rivals\]~d?/u?~ are rumoured to be." (PCC, 10374)

Note that here, the antecedent of die Kicker "kickers" depends on the understanding of the "size" metaphor, it can be either the Ukrainian team (presented as having short players), or the German team (which has not been favored in the first match), or a generic description (which would mean that the sentence is not directly linked with the discourse).

## Ambiguity

Ambiguity is to be annotated in the `COMMENT` field, using pre-defined tags (if applicable) or plain text descriptions (otherwise). Optionally, ambiguity tags can be followed by a more detailed description in round parentheses `(...)`.

The following tags can be used to mark ambiguous 

1. `AMBIG:COREF` (ambiguous antecedent): There is uncertainty as to which is the \"right\" antecedent for an anaphor (or, controller for a cataphor). See above for antecedent selection preferences, provide referent index for all equally likely antecedents in round parentheses

	> (9.x) *In a letter, \[prosecutors\]~p~ told \[Mr. Antar's lawyers\]~l~ that because of the recent Supreme Court rulings, \[they\]~p/l~*~?~ *could expect that any fees collected from Mr. Antar may be seized.*

	> Note: Abbreviated `ambig-ante` in Chiarcos and Krasavina (2005)

2. `AMBIG:REL`: There is uncertainty as to whether an anaphoric relation exists or which type it is (anaphoric vs. bridging or event, i.e. contextual inference)

	This is sometimes the case with definite NPs. In the example below: If it is unclear whether the *confrontation* is identical to the *conflict*, the coreference should be annotated and the markable should be marked with this attribute. It is not necessary to provide a more detailed description.

	> (9.a) *This <u>conflict</u> is ... Therefore, the <u>confrontation</u> ...*

3. `AMBIG:IDIOM`: There is uncertainty as to whether a markable could be understood as a referential expression or as part of an idiom. Annotate anaphoric reading and mark the ambiguity.
4. `AMBIG:EXPL`: There is uncertainty as to whether a pronoun is an expletive (and therefore non-referring) or whether it is anaphoric. Annotate the anaphoric relations and mark the ambiguity. No description necessary.

	> (9.b) *At stake was an \$80,000 settlement involving who should pay what share of cleanup costs at the site of a former gas station, where underground fuel tanks had leaked and contaminated the soil. And the lawyers were just as eager as the judge to wrap \[it\] up.*

	*It* can either be interpreted as referring to *an \$80,000 settlement* or as a part of a lexicalized expression *to wrap it up* where *it* does not have any particular reference. 

	This can be made clearer with a constructed example:

	> (9.b.i) *She looks out of the window. <u>It</u>~EXPL~ is dark.* (expletive)
	> (9.b.ii) *Your <u>cat</u>~1~ has a nice color. <u>It</u>~1~ is dark, much more so than mine.* (anaphoric)
	> (9.b.iii) *The <u>cat</u>~1~ is hard to see. <u>It</u>~1,AMBIG:EXPL~ is dark.* (ambiguous)

5. `AMBIG:COREF_REL`: There is ambiguity with respect to both antecedent and relation

	> (44) "There seems to be a move around the world to deregulate the genera- tion of electricity," Mr. Richardson said, and Canadian Utilities hopes to capitalize on it.

	*On it* refers either to *a move around the world to deregulate the generation of electricity*, or to the whole clause beginning with
	*there* and ending with *electricity* (event anaphora).

6. `AMBIG:other`: other cases of ambiguity. Please provide a description in round parentheses.

If more than one kind of ambiguity applies, e.g., both ambiguity of antecedent and ambiguity of an anaphoric relation, then provide all of the corresponding tags (and descriptions), separated by comma.

## Trouble Shooting

### Coreference Substitution Test

A replacement test can be used to check whether a referential expression e belongs to a chain k: If it is true for every noun s (noun, proper noun) in k, that the replacement of e by s changes the interpretation of the text is not changed, then e belongs to chain k and a coreference relation to the last element of the chain is to be annotated.

According to this scheme, we only annotate coreference relations that
express a real identity between discourse objects. A "semantically loose"
connection between a definite NP and another nominal is therefore not sufficient. For this purpose the following

*Test*: To find out if two nominal descriptions are coreferent, try to substitute them with each other. (Certain transformations may be necessary, such as removing prepositions from markables.) Note that every previous coreferent markable has to be compatible with this substitution as well.

Note that this test has some issues with metonymy, i.e., substituting a word for another word closely associated with it. Cases of metonymy in text should be annotated as coreferent if and only if the subsitution test holds for all coreferring nominals: *the State Department said\... - the State Department officials claimed\...*.

> (5.a) *Als 1999 die im Rahmen der Dorferneuerung neu gestaltete
     \[Radeweger\]~1~ Ablage inklusive Seebrücke mit viel Pomp eingeweiht wurde\... Doch mit der Nachrüstung tut sich \[Radewege\]~1~ schwer \... Zu teuer, zu hässlich sei die Anlage, sagen die Meinungsführer \[im Gemeinderat\]~?~*  (maz-6488)

In (5.a), *\[Gemeinderat\]* could be considered coreferent with *\[Radewege\]~1~*. Yet, although both are exchangeable by means of metonymy, the substitution test fails for *\[Radewege\]~1~* , since *neu gestaltete Gemeinderatsablage* is not appropriate *in that context*. Accordingly, *\[Gemeinderat\]* should receive a separate index.


### Dealing with  Ambiguous Antecedents

The assignment of an antecedent will be fairly straightforward in most cases. However, it is possible that several interpretations are *equally* plausible in the eyes of the annotator. Consider ex. (8.c) above:

	> (8.c) *Je kleiner die <u>Kicker</u>~2,OLD,AMBIG:COREF(2,1)~ daherkommen, desto größer wird der <u>Gegner</u>~1,OLD,AMBIG:COREF(1,2)~ geredet\...* (German, maz-10374)
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

### Recurring Group Reference

Here is a very compact, constructed example:

	> (5) 
	> a. Peter~1~ and Malte~2~ went for a walk~3~. Both~4\>1,2~ wore hats~5~.
	> b. Peter~1~ had a coat~6~, Malte~2~ a rain jacket~7~. 
	> c. They~**4**~ reached\...

When annotating *They*, note that this group has been previously established. For this reason, we do *not* refer to the second respective mentions of *Peter* and *Malte*, but instead to the previously established index for the group introduced when annotating *Both*.

### Event Anaphor

Pronominal event anaphors are annotated along with their antecents. 

The antecedent of an event anaphor is normally a sentence, a clause or verb phrase. If so, select the main (lexical) verb as antecedent. Hence, in this example, we annotate *gewonnen* as we encounter the referring expression *das* "this".

	> (6) *Gestern hat Bayern München schon wieder gewonnen~1~. \[Das\]~1~ hat Jan ziemlich gestört. Marianne hingegen war \[davon\]~1~ begeistert.* (Non-event anaphors skipped.)

> Note that antecedents of event anaphors are not automatically pre-annotated but have to be manually created.

### Quantified NPs

Quantified expressions are either `OLD`/`GROUP` or `NEW`:

1. They are `OLD` if the same group has been previously referred to.
2. Otherwise, they are `GROUP` if they describe a finte set of entities and all these entities are mentioned before individually.
3. Otherwise, they are `OLD` if they clearly delimit the \'set of objects\'.
4. Otherwise, they are `NEW`.

Leaving the first two cases aside, a substitution substitution test helps with the decision about `OLD` and `NEW`: If we can insert a definite article or demonstrative pronoun, does that change the meaning? If not, this is referring expression.

    > (6) *people* −→ *all these people* → definite description −→ referential


### Pronominal Adverbs

Depending on context, some words can be either referring expressions or not. This may be automatically pre-annotated, but must be marked as non-referring in their referentiality annotation (see above).

A notorious problem in German is the annotation of pronominal adverbs such as *damit* (in the sense "so that", not in the sense "with it"), if they act as a connector: 

	> (21.a) *\[Auf dem <u>Tisch</u>\]~PM~ liegt \[eine <u>Kneifzange</u>\]~SM~. \[<u>Damit</u>\]~PM~ kann man viel anfangen.* (German, referential *damit* "with it")
	> (21.b) *\[<u>Ich</u>\]~PM~ habe \[<u>dir</u>\]~PM~ \[den <u>Brief</u>\]~PM~ gezeigt, damit \[<u>du</u>\]~PM~ bescheid weißt.* (German, non-referential *damit" "so that")


### Relative Possessive Pronouns

Relative pronouns are syntactically bound and not to be annotated, but relative posessive pronouns in possessive constructions are
treated as possessive pronouns. 

> Test for German: Ein (nicht-possessives) Relativpronomen ist genau dann gegeben, wenn es durch ‚*welch*' ersetzt werden kann:

	> (x) *Und so schielten \[die Israelis\] \[nach Washington\], \[an \[dessen\]/*∗*welchem Tropf\] \[sie\] hängen.* (maz-19074)
	> (x') *Und so schielten \[die Israelis\] \[nach Washington, das/welches \[sie\]* *wirtschaftlich stützt\].*

### Cataphora

We distinguish two types of forward-referring expressions, discourse cataphora and syntactic cataphora.

#### Discourse cataphora (anaphora of anticipation)

Discourse cataphora is a label used for non-pronominal reference forward. Sometimes an author introduces a discourse referent by means of an underspecified NP, i.e. an NP that cannot be interpreted only on the basis of the reader's knowledge up to this point. This way the author tries to encourage the reader to continue reading, in order to catch up the missing information. In the example below, *die einstige
Fußball-Weltmacht* and *vor einem Winzling* should be annotated as discourse cataphors, since their referents cannot be identified until introduced explicitly in the following text (*Deutschland* and
*Ukraine* correspondingly).

(33) *Die einstige Fußball-Weltmacht zittert vor einem Winzling*
     (newspaper article title)

In case one goes on reading the text, it becomes clear that *die einstige Fußball-Weltmacht* refers to Germany, whereas *ein Winzling* refers either to the Ukraine or the 1.62 meter tall ukranian footballer who made the most impact in the match ^5^. Discourse cataphors have to be annotated as normal anaphors, i.e. in accordance with the Chain Principle (p. 12), i.e. the most recent referent mention to the left (if any) is considered to be an antecedent.

#### Syntactic cataphora

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

## NOT INTEGRATED YET

- `RELATION`

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


	Bridging relations. Bridging is the term introduced in Clark 1975, which accounts for referents of definite descriptions, which are not directly related to some previously mentioned textual entities, but are rather inferred through lexical or world-knowledge of discourse participants.



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

## Trouble-shooting

### Ambiguities

In case of ambiguities, we suggest the following preferences. Below is the example outlined in the core scheme (p. 14 considered with respect to the options supported in the extended scheme and interpreted in accordance with these preferences.

anaphoric \> generic/idiomatic/expletive \> bridging \> situational

### World knowledge and situational references

Whenever a non-generic definite description cannot be explained as contextually accessible due to anaphoric reference or bridging inference, consider it to be inferrable from world knowledge or the situational environment.

	> (65) *This publication may not be reproduced, \...* (situational reference to the reading environment)

	> (66) *Last Sunday, Ms. Johnson finally got a chance to water her plants, but stopped abruptly. "I realized I couldn't waste this water when there are people in Watsonville who don't have fresh water to drink."* (WSJ, situational reference to the reported context)^9^

> Note:
> - In (66), we seem to have a bridging reference from direct speech to the predication *to water her plants*. However, it is less likely that Ms. Johnson refers to a text which had been written after she said that. So, it seems to be appropriate to classify such cases as situational anaphora, referring to situational environment at the moment of speaking.


Note that bridging references from direct quotes to the textual level are never subject to annotation! These are prototypical candidates for situational references.

To avoid waste-baket effects for situational and world-knowledge references, we mark situational references by relations pointing to a set of situationally prominent entities that are listed after the text itself, enclosed in \<situation\>, resp. in \<universe\> tags.

