source: 
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale Koreferenz, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.71-85
- automatically translated using www.onlinedoctranslator.com and converted to Markdown using PanDoc

# Nominal referential expressions {#nominal-referential-expressions .unnumbered}

> Christian Chiarcos, Manfred Stede, and Saskia Warzecha
>
> Hints:

-   These guidelines are based on the core PoCoS scheme by Krasavina and
    > Chiarcos (2007); however, some of the decisions made there have
    > been modified.

-   Text examples that appear in this chapter without citing the source
    > are always fictitious.

-   These guidelines use notation as it might be used \"on paper\" or in
    > a text editor. For the practical procedure with a special
    > annotation software, separate instructions for its use are issued.

-   We would like to thank André Herzog, David Kaupat and Sara Mamprin
    > for discussing and suggesting improvements to these guidelines.

## Background: Terms

> Asreferential expressionswe denote those linguistic forms that are
> used to refer to an object, person, or state of affairs (or several
> respectively) of the \"real world\" or a \"conceptualized world\" (as
> it only exists in our imagination) in a broad sense. to refer. We also
> include \"generic terms\" (so-called generic expressions), such as in
> [The whale]{.underline} is known to be a mammalwith a. The
> representative of the object/the person/the facts is the Discourse
> speaker:an object that can then be used in formal representations of
> the discourse. That means: Linguistic expressions refer to abstract
> discourse references, which in turn correspond to an object (or
> similar) of the world.
>
> The annotation scheme presented here is limited tonominal referential
> expressions, i.e. on (in the broadest sense) noun phrases. In the
> following (following the perspective of the text annotation) the term
> desMarkableused for those referential expressions that are the subject
> of the annotation. The central topic of this chapter is the exact
> characterization of the concept of markables, as it is then based on
> the processing of coreference or information status in later
> annotation steps. (In other words, the identification of referential
> expressions is not usually "an end in itself" in text analysis.)

## Markables: types and extent

> The annotation task is to process each text in reading order and
> identify all markables. After marking a markable, it can also be
> assigned various attributes that characterize the shape of the
> markable. These are explained later in section 5.3.
>
> We distinguish between three types of markables, which are also to be
> marked as such:

-   primaryMarkables (hereinafter: PM) are such referential noun phrases
    that, due to their form, identify their discourse referent
    asidentifiableto mark. For us, this corresponds to the linguistic
    category ofdefiniteness.

-   secondaryMarkables (hereinafter: SM) are all other referential noun
    phrases - typically indefinite expressions (NP with indefinite
    article (a dog)or without article (good weather)).

-   non-referentialMarkables (hereinafter: NM) are noun phrases whose
    function is not to refer to a discourse referent. These include
    e.g. B. NP in idiomatic expressions such asto annoy someone.

> To clarify the distinction, the different types of PM are described in
> more detail in the following section, followed by a brief
> characterization of SM, and then a list of cases of NM. In the
> examples given for illustration, markables are marked in \[square
> brackets\]. The type (PM, SM, NM) is usually not specified for the
> sake of brevity. Sometimes, for the sake of clarity, not all markables
> are marked in an example, but only those whose status is currently
> being discussed.
>
> For all types of markables, the question of theirs arises in the same
> wayExpansion.This governs the following principle:
>
> As the coordination example illustrates, markables can be nested
> within each other, which is often the case due to the maximum
> principle. A fully annotated version of the first example is:
>
> \[Hans -- he always was \[a weakness \[for Susanne\]p.m\]NMhad -\]p.m
>
> was also \[there\]p.m.

#### Definition: PM

> In general: PM are such referential noun phrases that, due to their
> form, speak to their discourse referents as to the readers
> identifiableto mark. We distinguish the following categories:

a.  Pronouns

> Personal, demonstrative, possessive pronouns and pronominal adverbs
> (e.g.there, there, next to, there)as well as bothandall in nominal use
> (i.e. not as a determiner) \[I\] saw \[her\] yesterday.
>
> Reflexive pronouns are PM if they are not connected but act as clauses
> (otherwise they are NM; see below). The clause status can be
> determined by conversion test:
>
> \[I\]p.mhave \[me\]NMwondered yesterday. (then:∗I was surprised
> yesterday.)
>
> \[I\]p.mhave \[me\]p.mseen yesterday. (then:I saw me yesterday.)
>
> The demonstrative pronoun \'such\'and generically used pronounsnoPM;
> see section 5.2.3 below.

b.  Definite Descriptions

    -   With definite article: \[the house\]

    -   With determiner \'both\': \[both houses\]

    -   With quantifiers that clearly delimit the \'set of objects\'. A
        > replacement test helps with the decision: Does a definite
        > article or a

> Insert a demonstrative without changing the meaning? Example:all
> people −→all these people
>
> -- → definite description −→p.m

-   With possessive pronouns: \[\[his house\]

-   Definite genitive attributions count as definite possessive
    > descriptions when replacing the determiner: \[\[Harald\'s\]
    > house\]

c.  Proper Names and Titles

> Typical types of proper nouns are geographic locations, people,
> societies, names of newspapers and magazines, and names of various
> social, political, and financial institutions.
>
> Examples of personal names:

-   \[Bertolt Brecht\] (full name)

-   \[Bert Brecht\] (abbreviated full name)

-   \[Bertolt\] (First name)

-   \[BB\] (Abbreviation)

-   \[the famous Brecht\] (name modified via definite description)

> Complex proper names are only treated as a single markable and are not
> further divided (\[Heidelberger Druckmaschinen Vertrieb Deutschland
> GmbH\]).Titles associated with proper names are annotated as part of
> those proper names, as are suffixes (\[dr Mueller\], \[Dr. Martin
> Luther King, Jr.\]).Standalone titles are also assigned to the
> \'proper noun\' category and receive the appropriate attribute (see
> Section 5.3):\[the graduate engineer\] didn\'t like it..If a proper
> noun is not the head of an NP, then the phrase is annotated as a
> definite/indefinite NP: \[a piggy named Babe\]

d.  Times and Dates

> These relate to a point in time or a time interval
>
> and can be resumed anaphorically in the text; so we treat them as PM.
> These include date formats (\[12.3.2012\]), Weekday and month names,
> year numbers, etc.

#### Definition of terms: SM

> All referential noun phrases that do not define the object of
> discourse as a SM are to be treated as SMidentifiableto mark. These
> are in particular:

-   NP with an indefinite article, regardless of whether it is a
    specificReference acts (There runs \[a fox\]SMon the street)or about
    oneunspecified (\[A fox\]SMI last saw it three years ago!)

-   NP with a quantifier that does not uniquely delimit the \'set of
    objects\': \[some people\], \[some plants\],Etc.

-   Articleless NP, especially \"bare plurals\" (I have \[cookies\]SM
    eaten),but also singular expressions like in Today will be \[good
    weather\]SMbeand quantities such as \[thirty grams\].

#### Definition of terms: NM

> There are some types of NP that at first glance \"look\" like PM or
> SM, but do not need to be annotated as such because they are
> notreferentialexpressions. In these cases, the type NM (non-
> referential markable) is to be assigned. This includes in particular
> the following categories (which are to be given to the NM as an
> attribute, see Section 5.3).

-   Expletive expressions (it-pronouns) and pronominal adverbs that are
    regens of relative clauses

> \[It\]NMwas also considered certain that . . .

-   NP in fixed, conventionalized idioms and corresponding collocations

> He got me upNM-- \'the palm tree\' is not to be read as referential.
> Similar:And then she threw \[the shotgun\]NM
>
> \[to the grain\]NM.
>
> But: markables in productive metaphors are not annotated as NM but as
> PM:
>
> Here\'s how \[the lurching city ship\]p.mperhaps still on a promising
> course. (maz-18914)

-   NPs used predicatively, which ascribe a further "type" to a
    > discourse referent

> The chief physician was \[a real professional\]NM.
>
> Max Müller is \[the greatest center forward of all time\]NM!

-   NP in the scope of a negation that are not resumable

> I didn\'t have \[a new car\] after allNMbought. However,
> reinstatements of negated NP are possible under certain circumstances;
> if such occurs, this NP is to be marked as an SM
>
> \[I\]p.mhave \[no moose\]SMmore. \[He\]p.mran away yesterday.

-   \"Generic\" pronouns such aswe, you, they (in cases where there is
    no specific reference),man, one

> Meier said to Müller: \"\[Man\]NMit should work now.\"
>
> Meier said to Müller: \"Last year \[they\]NMdemolished a house here."

-   Reflexive pronouns as verb-bound units that have no clause status
    (see the examples above under PM)

#### No Markables

> Certain words may be confused with markables for purposes of these
> guidelines, but they are not markables
>
> and accordingly not to be annotated. This applies in particular to
> pronominal adverbs such aswith it,if they act as a connector: \[On the
> table\]p.mlies \[a pair of pliers\]SM. \[With it\]p.myou can start a
> lot.
>
> but
>
> \[I\]p.mhave \[you\]p.m\[the letter\]p.mshown so that
> \[you\]p.m\[notice\]NM
>
> know.

#### Some syntactical aspects of markables

a.  **Prepositional phrases (P + complement)**

> \[The plane\] landed \[on the runway\].
>
> If an NP occurs as the complement of a PP, the entire PP must (in the
> sense of the \'maximum\' principle) be assigned the status of a
> markable and not the embedded NP alone.
>
> (Warning: Ambiguous words like \'until\'and ,as\'are only to be
> integrated into the markable if they function as prepositions and not
> as conjunctions.)
>
> Postpositions and circumpositions (like \'by profession\') are treated
> like prepositions.

#### relative pronoun

> Relative pronouns are annotated with the entire relative clause as a
> single markable, but relative pronouns in possessive constructions are
> treated as possessive pronouns. Test: A (non-possessive) relative
> pronoun is given if and only if it is replaced by \'whichcan be
> replaced:
>
> And so \[the Israelis\] glanced \[at Washington\], \[at \[its\]/∗
> which drip\] \[they\] depend on. (maz-19074)
>
> And so \[the Israelis\] looked \[to Washington, which supports
> \[them\] economically\].

#### Coordination of markables

> As mentioned in principle \'maximum\', in the case of coordinations,
> in addition to the individual NPs, the entire coordinated NP
>
> to annotate. If all of the individual NPs are each PM, the entire NP
> also forms a PM, otherwise an SM.
>
> There goes \[\[my dog\]p.mor \[a fox\]SM\]SM. \[\[Hans\]
>
> p.mand \[Mary\]p.m\]p.mhave no school today.

#### Discontinuous Markables

> Markables are not always made up of contiguous elements; this is
> primarily the case with relative clauses that are not directly next to
> the head noun. The two parts are then to be marked as belonging
> together by co-indexing with lower- case letters:I have \[the
> squirrel\]PM, aseen \[running across the garden\]PM, a.
>
> Another example aresplit NPConstructions in German: \[ Books\]SM, ahas
> Anna \[three\]SM, a.
>
> These two phenomena can also occur in combination, in which case the
> markable has three components: \[Tea\]PM, a we have \[the best\]PM,
> abought \[that we could get\]PM, a. Note that the PM property
> (identifiability) here refers to the initially unspecific (i.e.
> SM)teatransmits.

#### Elliptical markables

> An NP can be incomplete by elision and, at first glance, not meet the
> criteria of a markable:
>
> I had \[two hours\]p.mscheduled, but \[three\]p.m. Individual numerals
> are not usually PM, but in these cases we complete the elided NP and
> get a PM.

## Attributes

> The following is a listing of all the attributes and their possible
> values to annotate for markables.
>
> Attention: If markables in a coordination have different features,
> then for the higher-level markable (i.e. which includes
> \"feature-conflicting\" markables) all values of these attributes are
> asotherto annotate.
>
> NM-type (only for non-referential markables) 1.none (default)
>
> 2.expl -expletive expression, filler word 3.idiom --NP in idiomatic
> expression 4.pred -predicatively used NP 5.other --other
>
> Direct speech
>
> 1.text level (default) - reference on the text layer 2.to you
> -Reference to or within direct speech 3.in you -Reference to or within
> reported speech
>
> phrase type
>
> 1.np (default) - nominal phrase NP 2.pp -prepositional phrase PP
>
> 3.other --Phrase type that cannot be clearly classified
>
> NP form (applies to NP & PP)

1.  none (default)

2.  no --Proper names

3.  def-np --definite NP 4.indef-np --indefinite NP

> 5.per -personal pronouns (you we) 6.ppos --Possessive pronouns (his,
> mine)
>
> 7.pds --demonstrative pronoun (this, that)
>
> 8th.padv --pronominal adverbs (before that, because of that)
>
> 9.other
>
> ambiguity

1.  not ambiguous (default) - There is no uncertainty.

2.  ambiguous idiom --There is uncertainty as to whether a markable
    should be understood as a referential expression or as part of an
    idiom.

3.  ambig-expl --There is uncertainty as to whether a pronoun is an
    expletive and therefore not referential or whether it is anaphoric.

4.  Ambig-other --Other cases of ambiguity.

> Complex NP:A description is complex if it contains more than one noun
> phrase.

1.  not specified (default)

2.  yes

### no

> Relevant test: If a description consists of more than one nominal (not
> pronominal!) phrase, consider it a complex description. (Nominal
> phrases are phrases that have head nouns and can act as complements in
> sentence structures (subject, object)).
>
> his good friend and financial adviser −→typical complex NP
>
> Grammatical role:Surface-oriented definition of grammatical roles. If
> an NP is used in the predicate position, then annotate it as a
> subject.

1.  not specified (default)

2.  SBJ subject --The part of the sentence or clause about which
    something is said; usually agent of action; usually a noun or
    pronoun (nominative)

3.  DIR-OBJ direct object --A noun or pronoun (accusative) that
    experiences the action of the verb or indicates the result of the
    action. Test: direct object answers the questionsWho what?after the
    verb

4.  INDIR-OBJ indirect object --For the purposes of annotation, we
    consider the indefinite object to be one that precedes the direct
    object and tells to whom or for whom the verb\'s action is occurring
    and who receives/experiences the direct object. An indirect object
    is therefore only annotated if there is also a direct object.
    Indirect objects answer the question Whom?and are commonly found
    with verbs of communicating or giving. They are always a noun or a
    pronoun (dative) that is not part of a PP.

5.  other --PPs and embedded elements

## Analysis of a sample text

> Using an example text, we will once again illustrate the assignment of
> the different types of markables, but leave the assignment of
> attributes aside here.
>
> 1 That he\]p.m\[2011\]p.m\[in Stockholm\]p.m\[the Nobel Prize for
> Literature\]p.m
>
> 2 was not only astonished \[because of the size \[of the complete
>
> 3 works \[by Tomas Gösta Tranströmer\]p.m\]p.m\]p.m--
> \[it\]p.mcomprises
>
> 4 just \[500 pages\]SM-- but \[it\]p.malso surprised because \[man\]NM
>
> 5 \[there\]p.m\[with these pages\]p.m\[after decades\]SM
>
> 6 first time again \[lyric\]SMawarded.
>
> 7 No question, also \[\[by Günter Grass, who \[the prize\]p.m
>
> 8th \[1999\]p.mreceived\]p.m, \[Elfriede Jelinek, award winner
>
> 9 from \[2004\]p.m\]p.mor \[Harold Pinter, laureate
> \[2005\]p.m,\]p.m\]p.m
>
> 10 are there \[poems\]SM, but were honored \[these three\]p.mexplicit
>
> 11 \[\[for prosaic works\]SMor \[\[her\]p.mdramas\]p.m\]SM. However,
> \[we\]
>
> 12 canNM\[us\]NMon \[2009\]p.mfeel reminded when \[Herta Müller, \[to
>
> 13 \[their\]p.mPlant\]p.mnext to \[novels\]SMalso \[literary
> collages\]SMto
>
> 14 count\]p.m, \[according to the committee\]p.m
>
> 15 \[for this\]p.mwas honored that by means of \[compression\]SM
>
> 16 \[landscapes \[of homelessness\]p.m\]SMbe drawn.
>
> 17 Perhaps \[these two award winners\]p.mso that
>
> 18 \[Compression\]SMand \[linguistic experimentation\]SMstraight up
> \[in
>
> 19 literature class\]p.mstand. \[The\]p.mwould explain, on the one
> hand,
>
> 20 why \[\[Philip Roth\'s\]p.mnovels\]p.mwere again not acknowledged,
> on
>
> 21 the other hand, \[es\]p.m, which is why \[adhere \[to bestseller
> lists\]SM
>
> 22 orienting readers\]p.m\[up to the respective award\]p.m\[\[Tomas
>
> 23 Transtromer\]p.mand \[Herta Müller\]p.m\]p.mshould not have been a
>
> 24 concept. So congratulations \[both\]p.m\[to their\]p.mmerit\]p.m
>
> 25
>
> 26 and let\'s stay curious \[for the awards \[of the next few
> years\]p.m\]
>
> 27 p.m.
>
> In the following, we discuss some of the annotation cases, but not all
> of them - especially not when the phenomena discussed are repeated
> within the example text.
>
> (Z. 1) Years are times and therefore PM. The nounStockholmis a proper
> noun, ie also a PM, and is marked including the preposition, since
> markables of maximum size are annotated according to the \'Maximum\'
> principle.
>
> (lines 2-3)Because ofintroduces three PM embedded in each other: two
> definite descriptions and a proper noun.
>
> (lines 3-4)Itis annotated as PM because it belongs to a parenthesis
> that does not modify a head.500 pagesis not marked as PM because the
> numeral is not preceded by a determiner, as in line 10 atthese
> threethe case is. Instead, it is an SM.
>
> (line 4)Itrefers to the award ceremony and thus forms a PM.
>
> (Line 5) Thatmanis not referential as a generic pronoun, so NM.
> Thereacts as a pronominal adverb and accesses the place descriptionin
> Stockholmup again.decadesis a \'bare plural\' and together with the
> preposition forms an SM.
>
> (line 6)lyricis an SM as a generic term without an article (further
> information can be found in lines 10-11).
>
> (Lines 7-9) The three authorsGrass, Jelinek, Pintereach form a
>
> common PM on their own and additionally as a coordinated phrase. The
> individual PM are each treated according to the \'maximum\' principle
> (with relative clause or apposition).
>
> (line 11) In the coordinationfor prosaic works or their dramas the
> overall expression forms an SM, since onlytheir dramasa PM is not
> butprosaic works.
>
> (lines 12-13) Here iswegeneric to read and therefore an NM. However,
> the generic reading only prevents the PM status, the discourse
> referents, for pronounsthe Nobel Prize in Literatureand the readers
> who orientate themselves on bestseller listseach show an example of
> generic NPs in the singular/plural, which are nevertheless (here due
> to the definite determiner) primary markables. The reflexive
> pronounushas no constituent status and is therefore an NM. Herta
> Muellermust be marked as a maximum PM, i.e. including the apposition,
> which in turn contains a number of embedded markables.Asis not marked
> because it is used here as a conjunction, not as a preposition.
>
> (line 14) The PMaccording to the committeecontains both the article
> and the post position.for thisacts as a referential pronominal adverb
> and is therefore also PM.
>
> (lines 19-21)in the literature courseshould be read as a productive
> metaphor and marked PM whileon the one handandon the other hand are
> not marked in the following sentence, despite being definite, since
> the terms are lexicalized.
>
> (line 21)Itis not an expletive here, but refers tothe is Z. 19, so
> represents a PM.
>
> (lines 23-24) InTomas Transtromer and Herta Mullerboth PMs are
> coordinated to form a new PM.
>
> (line 24)to be a termis an idiomatic expression, so it doesn\'t result
> in a markable.

# Nominal coreference {#nominal-coreference .unnumbered}

> Christian Chiarcos, Manfred Stede, and Saskia Warzecha
>
> Hints:

-   These guidelines are based on the core PoCoS scheme by Krasavina and
    > Chiarcos (2007); however, some of the decisions made there have
    > been modified.

-   All uncredited examples mentioned in these guidelines are
    > fictitious.

-   These guidelines use notation as it might be used \"on paper\" or in
    > a text editor. For the practical procedure with a special
    > annotation software, separate instructions for its use are issued.

-   We would like to thank André Herzog, David Kaupat and Sara Mamprin
    > for discussing and suggesting improvements to these guidelines.

## Background: Terms

> coreferencedenotes the relation between two text elements that refer
> to the same entity (the samediscourse speakers)refer. We call the text
> elementsreferential expressions;one often speaks of resumption, when
> the same discourse referent is mentioned more than once.
>
> A common variety of coreference isanaphoric:If a referential
> expression cannot be interpreted on its own - its discourse referent
> can only be determined by resorting to a previously mentioned
> co-referential expression - it is oneanaphor. The preceding
> co-referential expression is then the corresponding one
> antecedent.Example:
>
> (6.97)Susanne likes \[gymnastics\]1not, because \[it\]2\>1is very
> hard.
>
> We mark referential expressions in square brackets; if they are in a
> coreference relation, they are given a numeric index, and the sign \>
> indicates the reference direction (anaphor to antecedent).
>
> Non-anaphoric co-reference is present when two referential expressions
> are assigned the same discourse referent, even in isolation. This is
> mainly the case with proper names or often also with definite noun
> phrases. In the example below, there are two coreference relations,
> one of which is anaphoric.
>
> (6.98)At noon \[the Federal President\] opened1\[the session\]2, and
> in the evening \[Joachim Gauck\]3\>1\[she\]4\>2closed again.
>
> We call the series of mentions of the same referent one referential
> chain.A replacement test can be used to check whether a referential
> expression e belongs to a chain k (see also Section 6.4.1): If it is
> true for every noun s (noun, proper noun) in k, that the replacement
> of e by s changes the interpretation of the text is not changed, then
> e belongs to chain k and a coreference relation to the last element of
> the chain is to be annotated.
>
> This annotation scheme is limited tonominaldiscourse speakers. That
> is, only referential chains whose components are each expressed by a
> (in the broad sense) noun phrase are treated.
>
> Relations that are established by so-called factual anaphora, in which
> the antecedent can be a verb phrase, a sentence, or an entire partial
> text, are not dealt with here.
>
> In the following (following the perspective of the text annotation)
> the term desMarkableused for referential expressions. The
> determination of the markables and their status asprimary
> sekundaryornon-referentialis subject to the annotation guidelines in
> Chapter 5; this processing step is assumed for the following
> guidelines.
>
> So now referential chains are to be established between the markables,
> on the basis of which the referential structure of a
>
> text can be determined; this makes it explicit which discourse objects
> are dealt with how often and in what form and gives indications of
> central or consistently discussed discourse speakers. This often
> allows conclusions to be drawn about the structure of the text in
> thematically related sections.

## Annotation Statement

1.  **Objective of the annotation**

> The aim of analyzing the referential structure of a text is to record
> all pairs of co-referential markables and thus to establish
> referential chains. We distinguish between three annotation
> levels:markables, relations,as well as attributes. Since the markables
> are already in place, the concrete target for the coreference analysis
> is eachprimary markable (see section 5.2.1) with regard to the
> question whether and to which antecedent markable it is assigned (see
> section 6.3 below) and thus arelation ( Section 6.4) to establish. In
> addition, it is necessary to decide which specificattributescarries
> the treated markable in terms of coreference (Section 6.5).

#### Annotation History

> Step 1: Identify the Primary Markables (PM) already marked.
>
> For each PM*a*:
>
> Step 2: Connect markables by coreference links.

a.  Check if*a*is co-referent with a PM or SM in the preceding context;
    use the replacement test described in Section 6.4.1.

b.  If coreference is found, write*a*its immediate antecedent to (last
    mention). Notation: Index for*a*

> \'\>\'Index of the antecedent. (If the antecedent does not already
> have an index, establish a new one.)

c.  If there is no coreference in the preceding context, check if*a*
    cataphorically refers to an element in the following context (see
    Section 6.4.2); if so, annotate the relation. Notation: Index
    for*a*\'\>\' index of the following \"ante\" ceded.

d.  If there is no coreference, then gets*a*no numeric index.

> Step 3: Lay for*a*the values of the attributes.
>
> At the end, the texts then contain referential chains (the first link
> of which can be a primary or a secondary markable) as well as
> individually annotated markables (i.e. those that are not repeated in
> the text).singletons).Members of chains carry a numeric subscript,
> singletons do not. The order in which the indices are assigned (i.e.
> which numbers are assigned) is irrelevant; the co- reference
> relationships are decisive. For the sake of clarity, however, it is
> advisable to assign indices in ascending order when editing the text.
>
> The following section first explains some important aspects of this
> annotation history in more detail. Section 6.4 discusses the
> difference between anaphoric and cataphoric relations, and then gives
> hints on how to deal with ambiguity. Section 6.5 then explains the
> attributes to be set (step 3 in the process above). At the end of
> these guidelines, the annotation principles are summarized again,
> after which we illustrate the annotation decisions using a sample
> text.

## Details

#### Antecedent Decision

> The assignment of an antecedent will be fairly straightforward in most
> cases. However, if several interpretations are equally plausible, then
> principle 1 can govern the decision if there is a choice between a PM
> and an SM.

#### Treatment of discontinuous markables

> If a discontinuous markable is recorded anaphorically, establish a
> relation from the anaphora to thelastmentioned part of the antecedent
> markable. On the other hand, if the anaphora is discontinuous, connect
> its former part to the antecedent.
>
> Here we mark that the Markable parts belong together with lower case
> letters and the co-reference with numbers.
>
> (6.99) \[I\]PM,1had \[of the tea\]PM, adrank \[the \[Anna\]p.m
>
> \[to me\]PM,2\>1had given\]PM,a,3. Honestly, \[he\] tasted
>
> PM,4\>3awful.

#### Recursive Embedding

> Due to the principle of maximum extension of markables (see Chapter
> 5), recursively embedded references can occur. Although relative
> pronouns are not markables, in the case of a possessive construction
> occurring in the relative clause or in the apposition, the possessive
> pronoun refers to the entire surrounding NP.
>
> (6,100)And so \[the Israelis\] squintedPM,1\[to Washington, \[at
>
> \[whose\]PM,4\>3Drip\]PM,5\[she\]PM,2\>1hang\]PM,3. (maz-19074)

#### Group Reference

> With plural NPs (also quantifying NPs) and with plural pronouns ( you,
> youetc.) one can refer to groups of antecedents:
>
> (6.101) \[Germany\]p.m\[vs Argentina\]p.m- \[both\]p.mwin with help
> \[referee\]p.m.
>
> Here refersbothonGermanyandArgentina,however, there has not been a
> phrase in the text that specifically designates this group, so there
> is no markable either. Therefore, another type of markables must be
> created in this annotation step: Group markables (GM).
>
> The notation is based on that for discontinuous markables. The members
> of the group receive an index made up of \'G\' and a number. For the
> latter member of the group, the coreference with the anaphora is
> notated by numerical index as usual:
>
> (6.102) \[Germany\]PM,G1\[vs Argentina\]PM,G1- \[both\]PM,1\>G1
>
> win with the help of \[the referee\]p.m.
>
> If a markable contained in a group also stands as singleMarkable in a
> coreference relation (in example 6.102 this could be done by
> mentioning againArgentina happens in the following sentence), then in
> addition to the group index, another index is assigned to it, to which
> the corresponding anaphor can then refer.
>
> GMs can serve as antecedents of nominal markables (but not as
> anaphora). Such groups can include markables that differ in their
> grammatical role, the type of referential expression, and other
> features. Therefore, a group as a whole is not further annotated with
> attributes.
>
> If groups and their members are mentioned repeatedly, the situation
> can be unclear for the annotation. Here is a very compact example:
>
> (6.103)Peter and Malte went for a walk. Both wore a hat.
>
> Peter was out and about in his coat, Malte in his rain jacket. They
> reached\...
>
> When annotatingShethere is a temptation to use the chain principle
> (Principle 3, see below) to follow the immediately preceding mentions
> ofMalteandPetergroup again and mark as an antecedent. Exactly this
> group was however already before by the anapherbothestablished. We
> state that in this situation coreference betweenshe andbothis to be
> annotated to make the identity of the group references transparent.
>
> This question of the primacy of the identity of groups over the chain
> principle explained below (Principle 3) governs Principle 2 (an
> extension of Principle 1):
>
> Further comments on the priority of each principle follow at the end
> of these guidelines.

## Relations

> The following statements concern the relations to be annotated between
> markables. We do not differentiate here between anaphoric and
> non-anaphoric coreference relations.
>
> For the annotation of the relation in this section we therefore use
> \'anaphoric\' in a broad sense that includes any resumption.

#### Anaphoric Relations

> According to this scheme, we only annotate coreference relations that
> express a real identity between discourse objects. A "loose"
> connection is therefore not sufficient. For this purpose the following
> test: Two given nominal descriptions count as co- referent if it is
> possible to refer to each other through the other substitute. (Certain
> transformations may be necessary, such as removing prepositions from
> markables.)
>
> Example (many markables not of interest here are unmarked):
>
> (6.104)When 1999 redesigned as part of the village renewal
> \[Radeweger\]PM,1Storage including the pier was inaugurated with a lot
> of pomp\... But the retrofitting is happening \[Radewege\]PM,2\>1
> difficult\... The system is too expensive, too ugly, say the opinion
> leaders \[in the municipal council\]PM,?(maz-6488)
>
> Here could \[council\]although possibly as co-speaker with \[bike
> paths\]PM,2can be read, but although both are interchangeable in terms
> of metonymy, the replacement test for \[bike paths\]1- then \" newly
> designed municipal council filingis not appropriate in this context.
> Therefore receivescouncilanother index.
>
> For the annotation of the antecedent, the following priority rule must
> be observed according to principle 3:
>
> As explained at the beginning, so-called factual anaphora are marked
> (it is PM), but no antecedent is assigned to them if this is
> non-nominal. However, if the factual anaphor itself occurs repeatedly,
> an anaphoric relation should be marked between them. Example:
>
> (6.105)Bayern Munich won again yesterday.
>
> \[The\]PM,1really bothered Jan. Marianne, on the other hand, was
> \[of\]PM,2\>1enthused.
>
> i.e.,Thegets no antecedent while betweenof thatand Thea relation is
> marked.

#### Cataphors

> There are two types of forward expressions: discourse cataphores and
> syntactic cataphors.

1.  Discourse cataphores

> Discourse cataphores are those forward-looking expressions that are
> not realized pronominal, but, for example, by an underspecified NP
> that cannot be interpreted at the time of their occurrence in the
> text. In this way, the author may encourage the reader to read further
> in order to obtain the missing information. Example:
>
> (6.106) \[The former football world power\]p.mtrembles \[in front of a
>
> midget\]SM. With his goal to make it 1-0 for Ukraine, he fell
>
> 1.62 meters tall Gennady Zubov temporarily traumatized the German
> national team. The smaller the kickers come along, the bigger the
> opponent is talked about\... (maz-10374)
>
> Only one PM is identified when processing the first record. Only when
> the text is read further does it become clear that the former world
> football poweronthe German national teamrefers, and beyondin front of
> a tiny (as SM) depending on the interpretation eitherUkraineor onthe
> 1.62 meter tall Gennady Zubov. (Similar are then in the next sentence
> forthe kickers several interpretations possible.)
>
> Discourse cataphores are annotated like normal anaphora, i.e. in
> accordance with the chain principle (principle 3): Always choose the
> most recent previous referent mention (if there is one) as the
> antecedent. For the attributereferentiality becomes the value
> discourse cataphoraspecified.

2.  Syntactic cataphores

> (6.107)Through his\]PM,1\>2Lawyer has \[Mr. Antar\]PM,2the dismiss
> allegations.
>
> Syntactic cataphores (usually realized pronominal) are to be annotated
> like anaphoric, directed compounds, butin reverse direction (pointing
> from left to right). The two elements usually appear in the same
> sentence. For the attribute referentialityis, as in anaphoric
> relations, the value referringto specify.
>
> Another example can also be found above in 6.106, wherehis a
> cataphorical reference toGennady Zubovis.
>
> If it is not possible to clearly decide between a syntactic cataphor
> and an anaphor, principle 4 applies:
>
> If the cataphoric relation in question does not cross the sentence
> boundary, then this interpretation is preferable to making an
> anaphoric relation to the next preceding referent, as Principle 3
> would require. (Principle 4 thus ranks higher than principle 3.)
>
> (6.108)Cannes honors another grand master of film. For
> \[his\]PM,1\>2gets new film \[Michael Haneke\]PM,2the Golden Palm for
> the second time.
>
> Here arehisandMichael Hanekein one sentence, which is why, according
> to Principle 4, this (forward) connection ofhison Michael Hanekethe
> backward, anaphoric ofhis ona grandmaster of cinemais preferable. The
> coreference chain is fully annotated by the reference ofMichael
> Hanekeona grand master of film:
>
> be→Michael Haneke (syntactic cataphor within the sentence) Michael
> Haneke→a grand master of film (chain principle)

#### Ambiguous Antecedents

> If there is any doubt as to whether something is either connected to
> an item from the previous discourse via an anaphoric relation, or
> whether a markable may not have an antecedent at all (expletive,
> idiomatic, or generic reading), then proceed as follows:
>
> If it is clear that the relation is anaphoric, but the antecedent
> cannot be identified unequivocally or with a clear preference, an
> anaphoric relation is established for each candidate in the sense of a
> disjunction. At the
>
> Anaphorically, ambiguity is marked by an attribute (see Section
> 6.5.2).
>
> Attention: Markables with ambiguous tendencies should not be used as
> antecedents. (This is an exception to the chain principle.)

## Attributes

> All attributes for the annotation are listed below. The one with
> one∗provided categories are intended for SM alone, all others equally
> for PM and SM. NM are not annotated with attributes here.
>
> Caution: If markables in a coordination have different values, then
> for the parent markable all values of these characteristics are
> asotherto annotate.

#### Referentiality

1.  not specified (default) - No decision was made as part of the
    annotation.

2.  referring --A unit of discourse that can be interpreted based on the
    preceding context.

3.  discourse-new --Discourse entity mentioned for the first time.

4.  discourse-cataphora --Reference to a new entity introduced into the
    discourse about the meaning of an expression with an underspecified
    denotation.

5.  other --A decision between (1)-(4) is not possible; this concerns
    above all

    -   generic descriptions (Whales are mammals./The President has
        > always been elected by majority vote);

        -   predicative descriptions (It wasn\'t that both were looking
            > for a majority for their coalition \[the annoying thing
            > over the past few days\]\...);

        -   Groups whose members carry different referentiality
            > features.

> Caution: If a markable refers to an entity in the text that cannot be
> unequivocally declared as PM or SM, then the attribute \'
> referentiality\'the value \'referring\'to choose, but to attribute no
> antecedent. This exception particularly concerns discourse-deictic
> references to VPs and other non-nominal antecedents.

#### Ambiguity

> 1.not ambiguous (default) - There is no uncertainty. 2.ambiguous ante
> --There is uncertainty as to which is the
>
> \"right\" antecedent for an anaphora, so relations to multiple
> candidates are established.

3.  ambig-rel --There is uncertainty as to whether an anaphoric relation
    exists or not. This is sometimes the case with definite NPs, for
    example: (\...)This conflict is (\...) Therefore the confrontation
    is (\...)If it is unclear whether the dispute is identical to the
    conflict, the relation should be established and the anaphora should
    be marked with this attribute.

4.  ambig ante rel --There is uncertaintyas well asregarding the
    existence of a relationas well asregarding the possible antecedent.
    Then the possible relations have to be established and this
    attribute has to be chosen.

5.  ambig - other -Other cases of ambiguity.

#### Anaphora type

> 1.none (default) - First mention of a referrer 2.anaphoric --anaphoric
> relations

## Principles at a glance

> Here we give a summary of the principles mentioned and then record
> them in a ranking.
>
> **PRINCIPLE 1 (follows from Axiom (D))**
>
> \[PM \> SM\]
>
> If there are PMs that can be antecedents of a markable, then a
> connection must always be made between them, rather than declaring,
> for example, a possible SM - even in cases where, for example, a PM is
> located much further to the left of the anaphora than the possible SM
> is.
>
> **PRINCIPLE 2**
>
> \[PM \> SM \> groups\]
>
> If a PM or SM can be an antecedent of a markable, establish that
> connection rather than, say, declaring a group markable---even if the
> PM or SM is located much further to the left of the anaphora compared
> to the potential group markable.
>
> **PRINCIPLE 3**
>
> \[Right Previous \> Left Previous\] (chain principle)
>
> Every anaphoric markable has exactly one antecedent. Always mark the
> most recent, \'right-most\' previous speaker mention as antecedent.
> All the mentions of the same referent thus form an ordered chain.
>
> **PRINCIPLE 4**
>
> \[Reference to the right in the same sentence \> chain principle\]
>
> For a markable that can be read as both a cataphoric and an anaphoric
> pronoun: Can be used in the same sentence
>
> If a markable is found later that syntactically binds the pronoun, a
> cataphoric relation is to be annotated, even if a preceding utterance
> contains an anaphoric antecedent.
>
> **PRINCIPLE 5**
>
> \[anaphoric relation \> other (generic, predictive, etc)/idiomatic/
> expletive\] The anaphoric reference is preferable and to create a
> connection to a corresponding antecedent.

#### RANKING {#ranking .unnumbered}

> Principle 4 (the exception to Principle 3) has more weight than
> Principle 2, which in turn has more weight than Principle 3: 4 \> 2 \>
> 3
>
> (P1 is included in P2. P5 does not conflict with any of the other
> principles and is mandatory.)

## Analysis of a sample text

> In the following we show the analysis of a sample text; the assignment
> of the markables was done (for this example) in Chapter 5.
> Explanations of the co-reference decisions then follow.
>
> 1 That he\]PM,1\>2\[2011\]p.m\[in Stockholm\]PM,6\[the Nobel Prize for
>
> 2 Literature\]PM,10received, surprised not only \[because of the size
>
> 3 \[of the complete works \[of Tomas Gösta Tran-
>
> 4 stromer\]PM,2,G1\]PM,3\]p.m-- \[it\]PM,4\>3comprises just \[500
> pages\]SM,8--
>
> 5
>
> 6
>
> 7
>
> 8th 9
>
> 10
>
> 11
>
> 12
>
> but \[it\]p.malso surprised because \[man\]NM
>
> \[there\]PM,5\>6\[with these pages\]PM,7\>8\[after decades\]SMfirst
> time again \[lyric\]SMawarded.
>
> No question, also \[\[by Günter Grass, who \[the prize\]PM,9\>10
> \[1999\]p.mreceived\]p.m, \[Elfriede Jelinek, winner of
> \[2004\]p.m\]p.mor \[Harold Pinter, laureate \[2005\]p.m\]p.m\]PM,12is
> there\]NM\[poems\]SM, but were honored \[these
> three\]PM,11\>12explicitly for \[prosaic works\]SMor
> \[\[her\]PM,13\>11dramas\]p.m.
>
> 13 However, \[we\] canNM\[us\]NMon \[2009\]p.mfeel reminded when
>
> 14 \[Herta Müller, \[to \[their\]PM,15\>14Plant\]p.mnext to
> \[novels\]SM
>
> 15 also \[literary collages\]SMto count\]PM,14,G1, \[according to the
> committee\]
>
> 16 p.m\[for this\]p.mwas honored that by means of \[compression\]SM
>
> 17 \[landscapes \[of homelessness\]p.m\]SMbe drawn. Perhaps \[these
>
> 18 two award winners\]PM,15\>G1so that \[compression\]SMand
> \[linguistic
>
> 19 experimentation\]SMstraight up \[in literature class\]p.mstand.
> \[The\]
>
> 20 PM,17would explain, on the one hand, why \[\[Philip Roth\'s\]p.m
>
> 21 novels\]p.mwere again not acknowledged, on the other hand, \[es\]
>
> 22 PM,16\>17, which is why \[adhere \[to bestseller lists\]SMorienting
>
> 23 readers\]p.m\[up to the respective award\]p.m\[\[Tomas
> Transtromer\]
>
> 24 PM,18\>2and \[Herta Müller\]PM,19\>14\]PM,21should not have been a
>
> 25 concept.
>
> 26 So congratulations \[both\]PM,20\>21\[to their\]PM,22\>20
>
> 27 merit\]p.mand let\'s stay curious \[for the awards \[of the next
> few
>
> 28 years\]p.m\]p.m.
>
> (Z. 1) Withhethere is a syntactic cataphor which is based on Tomas
> Gosta Transtromerreferenced, which is why the relation marking must be
> forward-directed here. We assign the index 1 to the pronoun and 2 to
> the proper noun (which, as mentioned above, is an arbitrary decision).
>
> (line 4)Itrefers to that herecomplete work (not on theScope of the
> complete work!);the index 3 must therefore be assigned carefully to
> the correct closing bracket.
>
> (Z. 5) Here is also aitbefore, which does not refer to the work, but
> to the award of the prize, which was described in lines 1-2 as a fact
> by a VP; there is therefore no nominal coreference.
>
> (line 6)Thererefers toStockholm,which now also receives an index (6).
> Andthese pagesis here as co-speaker to the500 pages read in lines 4-5.
>
> (line 8)The pricewe read as referring to the Nobel Prize in Literature
> as a \'concept\' and thus as a co-referee with the one in lines 1-2.
> (Another reading isolates the concrete instances (Tranströmers
>
> Prize, Grass\' Prize), which would then not be co-referent; but this
> seems less plausible here.)
>
> (lines 11-12)These threeobviously refers to the set of prizewinners
> that has already been established as coordination and that now
> receives an index;heris then again anaphoric.
>
> (line 14)Whoseis an example of embedding a pronoun in an NP Hertha . .
> . to count,to which it relates as a whole.
>
> (line 18)These two award winnersmust be interpreted in context; the
> most obvious reading is a reference totranstromer ( lines 3-4)
> andmiller.These two thus receive a group index G1.
>
> (line 22)Itis an anaphora of facts, but co-referent withThein line 20
> (itself an anaphora of facts); the relation must therefore be marked.
>
> (Lines 24-25) The resumption of the author\'s name is to be marked in
> each case.
>
> (lines 26-27)Bothrefers to Transstromer and Müller. For these, a
> reference to the corresponding group has already been annotated in
> line 18; however, according to Principle 3, we choose the most recent
> mention as the antecedent, and that is the coordinated NP in lines
> 24-25, which is now given the index 21.
>
> Then canher as co-speaker withbothbe annotated. Themeritis a typical
> case of ambiguity regarding the question of whether there is
> co-reference in the sense of identity or not: Is the merit identical
> to the award in line 24? We decided against it here, since a merit is
> more of an evaluation of a process and therefore not identical to the
> process itself. Therefore, no ambiguity is annotated.
