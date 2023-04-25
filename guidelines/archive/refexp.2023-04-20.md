**source**: 
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- automatically translated using www.onlinedoctranslator.com and converted to Markdown using PanDoc
- revision by Christian Chiarcos
- see Readme.md for contributors and revision history

# Nominal referring expressions 

> Note: These guidelines use a notation as it might be used \"on paper\" or in a text editor. For the practical procedure with a special annotation software, separate instructions for its use are issued.

> Note: Text examples that appear in this chapter without citing the source are always fictitious.

## Background: Terms

As referring expressions, we denote those linguistic forms that are used to refer to an object, person, or state of affairs (or several respectively) of the \"real world\" or a \"conceptualized world\" (as it only exists in our imagination) in a broad sense. to refer. We also include \"generic terms\" (so-called generic expressions), such as in 

> (1) \[The <u>whale</u>\] is known to be a mammal

The representative of the object/the person/the facts is the discourse referent: an object that can then be used in formal representations of the discourse. That means: Linguistic expressions refer to abstract discourse referents, which in turn correspond to an object of the world (or the imagination).

The annotation scheme presented here is limited to nominal referring expressions, i.e. on (in the broadest sense) noun phrases. In the following (following the perspective of the text annotation) the term "Markable" is used for those referring expressions that are subject of the annotation. The central topic of this chapter is the exact characterization of the concept of markables, as it is then based on the annotation of coreference or information status in later annotation steps. (In other words, the identification of referring expressions is not usually "an end in itself" in text analysis.)

## Markables: types and extent

> Note: In the original PoCoS/PCC guidelines, markables were defined as phrasal expressions. Here, we annotate syntactic heads, instead.

The annotation task is to process each text in reading order and identify all markables. After marking a markable, it can also be
assigned various attributes that characterize the type of the markable. 

We distinguish between two types of markables, which are also to be marked as such:

-   **primary markable** (PM) are candidate anaphors, i.e., noun phrases whose grammatical features suggest that their discourse referent is or could be identifiable by the hearer. For German and English, these are definite NPs and pronouns. For languages without grammatical marking of definiteness, these are all nominals and pronouns. 

	Primary markables are automatically extracted. The task of annotation is to assign every primary markable either an antecedent or a flag that marks them as new or non-referential.

	> Note: This definition follows Krasavina and Chiarcos (2007). Chiarcos et al. (2016) singled out non-referential markables (NM)  from primary markables as they do not rely on automated pre-annotation.

-   **secondary markables** (SM) are antecedents for anaphoric expressions which have not been detected as primary markable.

	Typical secondary markables are  indefinite expressions (NP with indefinite article, *a dog*) or without article (*good weather*). Secondary markables are not automatically annotated.

	> Note: In Chiarcos et al. (2016), this is restricted to noun phrases. Here,  it is extended to all words, so that we cover event anaphora.

Non-referring markables (NM) are primary markables whose function is *not* to refer to a discourse referent. These include e.g. definite NPs in idiomatic expressions such as German *jemandem auf <u>die Nerven</u> gehen* "to annoy someone".

In the examples given for illustration, markables are marked under <u>underscores<u>. The type (PM, SM, NM) is usually not specified for the sake of brevity. Sometimes, for the sake of clarity, not all markables are marked in an example, but only those whose status is currently being discussed.

We only annotate the syntactic heads of markables. Thus, markables must never overlap. For clarifying the boundaries of markable *phrases*, we use \[square brackets\] instead or in addition to underscores:

> (2.a) English: *\[<u>Hans</u> -- who always had \[a soft <u>spot</u>\] \[for <u>Susanne</u>\]  -- \]  was also there.*
> (2.b) German: *\[<u>Hans</u> -- der immer schon \[eine <u>Schwäche</u>\] \[für <u>Susanne</u>\] hatte -- \] war auch da.*

> Notes: 
> - Head-based annotation sets these guidelines apart from Krasavina and Chiarcos (2007) and Chiarcos et al. (2016) who annotated phrases, not heads.

TODO 
- eliminate secondary and primary markable and replace it by referring expression and candidate anaphor

move to referring expressions 

##### e. Stranded Quantifiers

An NP can be incomplete by elision and, at first glance, not meet the criteria of a markable.  For example, individual numerals are not usually PM, but íf their head noun is elided, they serve as heads of NPs, they can be.

> 	(2.c) *Ich hatte \[zwei Stunden\]~PM~ eingeplant, aber es wurden letzlich \[drei\]~SM~.* (German)
>	(2.c') *I had planned for \[two hours\], but in the end, it was \[three\]~SM~* (English)




#### Definition: PM

Primary markables are automatically extracted from a syntactic analysis. The following criteria define the algorithm. Normally, annotators do not have to annotate PMs and they can skip this section. However, if you feel there may be an anaphoric expression that was missed in automated extraction, please resort to these definitions. 

> Notes: 
> - Incorrect PM prediction can result from parser errors. Annotators should mark manually introduced PMs with the comment `manual PM`.
> - Annotators must never delete an incorrectly extracted PM annotation, but you can mark it as non-referential and add the comment `parser error` to the annotation.

##### a.  Pronouns

Personal, demonstrative, possessive pronouns and pronominal adverbs (e.g. German *da* "there, then", *dort* "there", *daneben* "next to it", *dahin* "(towards) there") as well as *both* and *all* in nominal use (i.e. not as a determiner) 

> (3) *\[I\] saw \[her\] yesterday.*

Reflexive pronouns (English *herself*, etc.) are not PM. Pronouns that are formally ambiguous as to whether they are reflexive or personal pronouns (e.g., German *mich* "me; myself"), are PM, and should be marked as `bound` in the annotation. Analoguously for other non-referring pronouns (e.g., expletive *it* or generic *you* in the sense of "anyone").

The demonstrative pronoun *such* (German *solch*) is considered as indefinite. Refererring expressions with *such* should not be annotated as primary markables.

##### b.  Definite Descriptions

-   With definite article: 

	> (4) *\[the <u>house</u>\]*

-   With determiner \'both\': 

	> (5) *\[both <u>houses</u>\]*

-   With possessive pronouns: 
	
	> (6) *\[\[his house\]*

- With potentially anaphoric genitive or possessibe modifier

	> (7) 
	> a. *\[Harald\'s <u>house</u>\]*
	> b. *\[the <u>house</u> of Harald\]*
	> c. *\[the other man's <u>house</u>\]*
	> d. *\[this man's <u>house</u>\]*
	> **but not** e. *\[a man's house\]*

##### c.  Proper Names and Titles

Typical types of proper nouns are geographic locations, people, societies, names of newspapers and magazines, and names of various social, political, and financial institutions.

Examples of personal names:

> (8)
	> a.   \[Bertolt Brecht\] (full name)
	> b.  \[Bert Brecht\] (abbreviated full name)
	> c. \[Bertolt\] (first name)
	> d.   \[BB\] (abbreviation)
	> d.   \[the famous Brecht\] (name modified via definite description)

Complex proper names are only treated as a single markable and are not further divided. If the internal dependency structure is transparent, annotate the syntactic head. For names composed of given and family names, we consider the name of the individual to be head, and the name of the family as modifier. If the structure of a name is not transparent to a common speaker of the language, annotate the first word that is not clearly recognizable as a modifier.

> (9) 
> a. \[Dr. <u>Mueller</u>\]
> b. \[Dr. <u>Martin</u> Luther King, Jr.\]
> c. \[Prince <u>Dipangkorn</u> Rasmijoti Sirivibulyarajakumar of Thailand\]
> d. \[Heidelberger <u>Druckmaschinen</u> Vertrieb Deutschland GmbH\]

Standalone titles are also assigned to the \'proper noun\' category and receive the appropriate attribute 

> (10) \[the graduate <u>engineer</u>\] didn\'t like it.

##### d.  Times and Dates

These relate to a point in time or a time interval and can be resumed anaphorically in the text; so we treat them as PM.
These include dates, days of the week and month names, year numbers, etc.

> (11.a)  \[<u>12.3.2012</u>\] (single token)

If the structure is syntactically intransparent, annotate the first word not clearly recognizable as a modifier. If the structure is semantically transparent, annotate the most specific designator as head, e.g., the day in a date (not the year). This allows to create additional anaphoric links between multiple mentions of the same year without confusing it with different dates in the same year.

> (11.b)  \[<u>12</u> . 3 . 2012\] (.-based tokenization)

#### Definition of terms: SM

When annotating the antecedents of primary markables, every antecedent that has not been previously annotated as primary markable is a secondary markable.

> Note: We may automatically pre-annotate nominale secondary markables in the future, too. However, it is not clear whether this will speed up or slow down the annotation process. For the moment, secondary markables must be manually annotated.

Common types of SMs include:

-   NP with an indefinite article (if subsequently referred to):
	
	> (12.a) *There is a \[a <u>fox</u>\] running across the street. <u>It</u>'s fast!.*
	> (12.b) *I last saw \[a <u>fox</u>\] about three years ago! <u>It</u> came from the forest.*

	Annotate the secondary markable only if you are certain about the reference. If another reading is equally possible or feels more likely, do not annotate the secondary markable. (Add a comment about your uncertainty.)

	> (12.c) *I saw \[a <u>cat</u>\] tonight in the street. <u>It(= the cat)</u> was gray.*
	> (12.d) **but not**: *I saw a cat tonight in the street. <u>It(= the night/expletive?)</u> was pitch black.*

-   NPs with indefinite quantifier

	> (13) 
	> a. \[some people\]
	> b. \[some plants\]

-   Articleless NP, especially \"bare plurals\" (I have \[cookies\]SM
    eaten),but also singular expressions like in Today will be \[good
    weather\]SMbeand quantities such as \[thirty grams\].

#### Definition of terms: NM

Some expressions that are automatically annotated as PM are not referential. We refer to these as non-referring markables (NM). This includes in particular the following categories:

-   Expletive expressions (English *it*) and pronominal adverbs that are
    controllers of relative clauses

	> (14.a) *\[ ~~~It~~~ \]~NM~ was also considered certain that . . .* (English)
	> (14.b) *\[~~~Es~~~\]~NM~ galt zudem als sicher, dass . . .* (German)

-  NPs in fixed, conventionalized idioms and corresponding collocations

	> (15.a) *Er brachte mich auf \[die Palme\]~NM~* (German)
	> (15.b) *Und dann warf sie \[die Flinte\]~NM~ \[ins Korn\]~NM~.* (German)

	Note that PMs in productive, transparent metaphors are not NMs:

	> (16) *So lässt sich \[das schlingernde City-Schiff\]~PM~ vielleicht doch noch auf einen erfolgversprechenden Kurs bringen.* (German, maz-18914)

-   Predicative NPs in copular sentences

	> (17.a) *The chief physician was \[a real professional\]~NM~.*
	> (17.b) *Max Müller is \[the greatest center forward of all time\]~NM~!*

-   NP under the scope of a negation that cannot be referred to

	> (18) *I didn\'t buy \[a new car\]~NM~ after all.*

-   \"Generic\" pronouns such as *we*, *you*, *they* (in cases where they do not carry a specific reference), *someone*, *anyone*, *one*. Cf. German *man*.


	> (19.a) *Meier said to Müller: \"\[You\]~NM~ should go now.\"*
	> (19.b) *Meier sagte zu Müller: „\[Man\]~NM~ sollte jetzt gehen."* (German)

	> (20.a) *Meier said to Müller: \"Last year, \[they\]~NM~ demolished a house here."*
	> (20.b) *Meier sagte zu Müller: „Letzes Jahr haben \[sie\]~NM~ hier ein Haus abgerissen."* (German)

#### No Markables

Certain words may be confused with markables for purposes of these
guidelines, but they are not markables and accordingly not to be annotated. This applies in particular to pronominal adverbs in German such as *damit* (in the sense "so that", not in the sense "with it"), if they act as a connector: 

	> (21.a) *\[Auf dem <u>Tisch</u>\]~PM~ liegt \[eine <u>Kneifzange</u>\]~SM~. \[<u>Damit</u>\]~PM~ kann man viel anfangen.* (German, referential *damit* "with it")
	> (21.b) *\[<u>Ich</u>\]~PM~ habe \[<u>dir</u>\]~PM~ \[den <u>Brief</u>\]~PM~ gezeigt, damit \[<u>du</u>\]~PM~ bescheid weißt.* (German, non-referential *damit" "so that")


# WHERE TO PUT THIS?

non-referential quantified 

-   With quantifiers that clearly delimit the \'set of objects\'. A substitution test helps with the decision: If we can insert a definite article or demonstrative pronoun, does that change the meaning? If not, this is referring expression.

    > (6) *people* −→ *all these people* → definite description −→ referential


newness test:

-   Definite genitive attributions count as definite possessive
    > descriptions when they can be replaced with the determiner: \[\[Harald\'s\]
    > house\]



Relative pronouns are annotated with the entire relative clause as a
single markable, but relative pronouns in possessive constructions are
treated as possessive pronouns. Test: A (non-possessive) relative
pronoun is given if and only if it is replaced by \'whichcan be
replaced:

And so \[the Israelis\] glanced \[at Washington\], \[at \[its\]/∗
which drip\] \[they\] depend on. (maz-19074)

And so \[the Israelis\] looked \[to Washington, which supports
\[them\] economically\].
