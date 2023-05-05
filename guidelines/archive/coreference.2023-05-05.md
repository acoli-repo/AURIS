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
	> - Corresponds to "discourse old" according to Prince (1992) and "referring" according to Chiarcos et al. (2016).
	> - Automated pre-annotation generates the value `?OLD` for all candidate anaphors (Krasavina and Chiarcos 2007: "primary markables") and `?NEW` for all other candidate referring expressions (Krasavina and Chiarcos 2007: "secondary markables"). These values need to be manually replaced by the annotator. An annotation project that still contains `?OLD` or `?NEW` annotations will be considered incomplete and must not be further processed.

2. `NEW`: Discourse entity mentioned for the first time. This includes referents that can be inferred by the hearer. 

	> Note: Corresponds to "discourse new" according to Prince (1992).

3. `CAT`: Discourse cataphor, i.e., reference to a new entity introduced into the discourse with an underspecified nominal expression whose exact denotation becomes clear only from subsequent descriptions. This is a rhetorical device employed to engage readers in literary texts.

	When reading (8.a) in the example below, it is initially unclear what *Fußball-Weltmacht* and *Winzling* refer to. This becomes clear only in sentence (8.b), when the German team and Ukraine are mentioned.

	> Note: Syntactically bound pronominal cataphors are annotated as `BOUND`.

5. `GROUP`: Group references to previously established referents (see above).

4. `BOUND`: Pronouns that are syntactically bound, e.g. reflexive pronouns. Also, possessive pronouns governed by nominal expressions in the same sentence are annotated as `BOUND`, cf. in (8.b) below *Mit <u>seinem</u>~3,BOUND~ Tor*. 

	> Note that reflexive pronouns (which are obligatorily bound) are not annotated as markables if they can be identified on grounds of their form (e.g., English *himself*, German *sich*). Only if a form is ambiguous between a reflexive and pronominal reading (e.g., German *mich*), reflexive pronouns are annotated as `BOUND`.

5. `SIT`: situationally evoked. In written texts, this applies only to first and second person, non-reflexive pronouns and to temporal expressions. 

	> Note: `SIT` is to be annotated at the first mention, only, subsequent references to the same entity are to be annotated as `OLD`.

6. `GEN`: Generic expression, referring to a type, not an entity.

	> (7.a) *<u>Whales</u>~GEN~ are <u>mammals</u>~PRED~.*
	> (7.b) *The <u>President</u>~GEN~ has always been elected by majority <u>vote</u>~1,NEW~.*

	> Note: Generics should not be annotated with a discourse referent index -- unless they are subsequently referred to:

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
2. `AMBIG:REL`: There is uncertainty as to whether an anaphoric relation exists or not. This is sometimes the case with definite NPs. In the example below: If it is unclear whether the *confrontation* is identical to the *conflict*, the coreference should be annotated and the markable should be marked with this attribute. It is not necessary to provide a more detailed description.

	> (9.a) *This <u>conflict</u> is ... Therefore, the <u>confrontation</u> ...*

3. `AMBIG:IDIOM`: There is uncertainty as to whether a markable should be understood as a referential expression or as part of an idiom. Annotate anaphoric reading and mark the ambiguity.
4. `AMBIG:EXPL`: There is uncertainty as to whether a pronoun is an expletive and therefore not referential or whether it is anaphoric. Annotate the anaphoric relations and mark the ambiguity. No description necessary.

	> (9.b.i) *She looks out of the window. <u>It</u>~EXPL~ is dark.* (expletive)
	> (9.b.ii) *Your <u>cat</u>~1~ has a nice color. <u>It</u>~1~ is dark, much more so than mine.* (anaphoric)
	> (9.b.iii) *The <u>cat</u>~1~ is hard to see. <u>It</u>~1,AMBIG:EXPL~ is dark.* (ambiguous)

5. `AMBIG:other`: other cases of ambiguity. Please provide a description in round parentheses.

If more than one kind of ambiguity applies, e.g., both ambiguity of antecedent and ambiguity of an anaphoric relation, then provide all of the corresponding tags (and descriptions), separated by comma.

## Trouble Shooting

### Coreference Substiution Test

A replacement test can be used to check whether a referential expression e belongs to a chain k: If it is true for every noun s (noun, proper noun) in k, that the replacement of e by s changes the interpretation of the text is not changed, then e belongs to chain k and a coreference relation to the last element of the chain is to be annotated.

According to this scheme, we only annotate coreference relations that
express a real identity between discourse objects. A "semantically loose"
connection between a definite NP and another nominal is therefore not sufficient. For this purpose the following
test: Two given nominal descriptions count as co-referent if it is
possible to refer to each other through the other substitute. (Certain
transformations may be necessary, such as removing prepositions from
markables.)

German Example (many markables not of interest here are unmarked):

	> (5) *Als 1999 die im Rahmen der Dorferneuerung neu gestaltete \[Radeweger\]~PM,1~ Ablage inklusive Seebrücke mit viel Pomp eingeweiht wurde\... Doch mit der Nachrüstung tut sich \[Radewege\]~PM,2\>1~ schwer\... Zu teuer, zu hässlich sei die Anlage, sagen die Meinungsführer \[im Gemeinderat\]~PM,?~* (maz-6488)

	> Hier könnte *\[Gemeinderat\]* zwar möglicherweise als koreferent mit
	> *\[Radewege\]*~PM,2~ gelesen werden, doch obwohl beide im Sinne einer
	> Metonymie austauschbar sind, scheitert der Ersetzungstest für
	> *\[Radewege\]*~1~ -- denn *„neu gestaltete Gemeinderat Ablage"* ist in
	> diesem Kontext nicht angemessen. Daher erhält *Gemeinderat* einen
	> anderen Index.

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

Referring expressions that designate groups can serve as antecedents of nominal markables.  Here is a very compact example:

	> (4) 
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



