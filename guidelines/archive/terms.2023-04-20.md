**source**: Partially based on excerpts from

- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale Koreferenz, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.71-85

> Note: Text examples that appear in this document without citing the source are always fictitious.

# Background

> Note: These guidelines use a notation as it might be used \"on paper\" or in a text editor. For the practical procedure with a special annotation software, separate instructions for its use are issued.

## Terms

- **Coreference**: the relation between two expressions that refer to the same discourse referent (entity) in a text. We call these expressions **referential expressions**. 
- **Anaphor**: an anaphor is a referring expression that can only be interpreted by resorting to a previously mentioned co-referential expression. The preceding co-referential expression is then referred to as **antecedent**.
- **Referential chain**: We call the series of mentions of the same referent one referential chain.
- **Markable**: A (potential) referential expression that is to be annotated. 

This annotation scheme is focusing on the annotation of nominal and pronominal anaphors. However, verbs may be annotated as *antecedents* of pronouns if these refer to the corresponding clause.

## Markables

> Note: In the original PoCoS/PCC guidelines, markables were defined as phrasal expressions. Here, we annotate syntactic heads, instead.

Markables represent spans in a text that carry one or more possible annotations, e.g., various attributes that characterize the type of the markable. 

The annotation task is to process each text in reading order and identify all markables. After marking a markable, it can also be
assigned various attributes that characterize the type of the markable. 

## Referring Expression

As referring expressions, we denote those linguistic forms that are used to refer to an object, person, or state of affairs (or several respectively) of the \"real world\" or a \"conceptualized world\" (as it only exists in our imagination) in a broad sense. to refer. We also include \"generic terms\" (so-called generic expressions), such as in 

> (1) \[The <u>whale</u>\] is known to be a mammal

The representative of the object/the person/the facts is the discourse referent: an object that can then be used in formal representations of the discourse. That means: Linguistic expressions refer to abstract discourse referents, which in turn correspond to an object of the world (or the imagination).

The annotation scheme presented here is limited to nominal referring expressions, i.e. on (in the broadest sense) noun phrases. In the following (following the perspective of the text annotation) the term "Markable" is used for those referring expressions that are subject of the annotation. The central topic of this chapter is the exact characterization of the concept of markables, as it is then based on the annotation of coreference or information status in later annotation steps. (In other words, the identification of referring expressions is not usually "an end in itself" in text analysis.)

In this document, we mark referential expressions in square brackets; if they are in a
coreference relation, they are given a numeric index that indicates the referent they refer to. In practical annotation, annotators should not use numbers, bus a meaningful, short and unambiguous abbreviation of their own choice. 

## Referential Chains

We call the series of mentions of the same referent one referential chain. As result of the annotation, all elements of a referential chain must carry the same index.

> (1) *Susanne doesn't like \[gymnastics\]~1~, because \[it\]~1~ is very hard.*

> (2) *At noon, \[the Federal President\]~1~ opened \[the session\]~2~, and
in the evening, \[Joachim Gauck\]~1~ closed \[it\]~2~\> again.*

## Formatting Conventions in this Document

In the examples given for illustration, markables are marked under <u>underscores<u>. The type (PM, SM, NM) is usually not specified for the sake of brevity. Sometimes, for the sake of clarity, not all markables are marked in an example, but only those whose status is currently being discussed.

For clarifying the boundaries of markable *phrases*, we use \[square brackets\] instead or in addition to underscores.

## Head-based Annotation

We only annotate the syntactic heads of markables. Thus, markables must never overlap.

> (2.a) English: *\[<u>Hans</u> -- who always had \[a soft <u>spot</u>\] \[for <u>Susanne</u>\]  -- \]  was also there.*
> (2.b) German: *\[<u>Hans</u> -- der immer schon \[eine <u>Schwäche</u>\] \[für <u>Susanne</u>\] hatte -- \] war auch da.*

> Notes: 
> - Head-based annotation sets these guidelines apart from Krasavina and Chiarcos (2007) and Chiarcos et al. (2016) who annotated phrases, not heads.
