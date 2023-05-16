# 1. Background and Terminology

A coherent, meaningful text can be characterized by three conditions, (semantic) consistency, (pragmatic) relevance, and cohesion (or, "connectedness"). In this manual, we focus on the annotation and subsequent analysis of the latter condition, i.e., we aim to elucidate **cohesion**, or connectedness, i.e., how each sentence is linked to an adjacent sentence in the text by means of

1. anaphoric (referring) expressions,
2. a linguistic marker for the introduction of a new topic, or
3. a semantic sentence connector ("cues").

This definition (loosely following Reinhart 1980, p.168) involves three types of analysis, i.e., 

1. the annotation of (co-)reference (what are referring expressions in the text, which entities do they refer to), 
2. the annotation of topichood (what is the entity the current sentence is about), and
3. shallow discourse annotation (what are the discourse markers used, which relations do they indicate, and which utterances do they refer to)

We further limit ourselves on the first and second aspect, i.e., referring expressions and the annotation of topic continuity. Shallow discourse annotation is to be done independently, e.g., according to the schema of the Penn Discourse Treebank (Webber et al. 2019).

Coherent texts thus involve repeated mentions of the same entity as well as references to objects related in various ways to what has already been discussed, and moreover, the utterances within a coherent text are construed *about* these referents. Annotating corpora with information about such relations between elements of a text is useful both from a linguistic point of view and for applications such as information extraction.

Subsequent mentions of an entity can have the same surface form - as when the expression *the Lord Provost* is encountered twice in a text - or different ones. Anaphoric expressions are used to indicate that elements of a text are correlated. The simplest forms of anaphoric expression are used to indicate a subsequent mention of an object already introduced: typical examples of this type of anaphoric expression are pronouns such as *he* in the text *John arrived. [He] looked tired.* In the preferred reading of this text, the pronoun *he* is interpreted as an 'abbreviated reference,' to the individual John which is denoted by the expression *John*. 

Besides coreference annotation itself, we include a set of linguistic features, in particular, those pertaining to information status ("givenness"), information status (here: backward-looking centers, "sentence topics") and auxiliary linguistic features (e.g., grammatical role and type of expression).

## 1.1 Terms

- **Coreference** is a relation between two or more textual elements, **referring expressions**, which denote the same entity. Semantically, these entities are prototypical objects or (discourse) referents. 
- **Discourse referent**: an entity that is being referred to in the discourse. Note that this does not have to be a physical entity, but it can also be an imagined entity ("the unicorn ... it ...")
- **Anaphor**: an anaphor is a referring expression that can only be interpreted by resorting to a previously mentioned co-referential expression. The preceding co-referential expression is then referred to as **antecedent**.
- **Information Status**: The degree of prominence or familiary that a referent entertains at a certain point in discourse in the common ground (or, in the discourse model).
- **Topic**: The referent that a particular is construed about. In many cases, this is a referent that entertains a high information status, and that is repeatedly referred to, and we focus on the annotation of these "familiary topics".
- **Referential chain**: We call the series of mentions of the same referent one referential chain.
- **Information Structure**: Pragmatic structure of utterances according to the distribution of information, involving, among other aspects, information status and topichood.
- **Markable**: A (potential) referential expression that is to be annotated. Syntactically, most referring expressions are noun phrases or adpositional phrases. In the current schema, we annotate the syntactic head of the markable, only, as defined by the [Universal Dependencies guidelines](https://universaldependencies.org/u/overview/nominal-syntax.html).

This annotation scheme is focusing on the annotation of referring expressions, i.e., nominal and pronominal anaphors and their information-structural features (information status, topichood). In addition to referring expressions, verbs may be annotated as *antecedents* of pronouns if these refer to the corresponding clause. We refer to these cases as **event anaphor**.

## 1.2 Referring Expressions

A *referring expression* is any linguistic form that can be used to refer to an object, person, or state of affairs (or several respectively) of the \"real world\" or a \"conceptualized world\" (as it only exists in our imagination) in a broad sense. We also include non-referring expressions, if they meet the syntactic criteria of referring expressions, e.g., \"generic terms\" such as in 

> (1) *\[The <u>whale</u>\] is known to be a mammal*

Referring expressions designate (refer to) a particular *discourse referent*, i.e., a conceptual object that representss an entity, person, or fact in the discourse model, resp., the common ground established between speaker and hearer during the discourse. A discourse referent is an abstract, conceptual object that exists regardless of whether it corresponds to an object of the world (or just of imagination).

Whether two markables are co-referent, i.e. referring to the same discourse referent, can be determined by a
*substitution test*. If the substitution of anaphor and antecedent yield the same interpretation of the text, these are deemed coreferential.

## 1.2 Markables

Markables<sup>[1](lit.md#terms1)</sup> represent spans in a text that carry one or more possible annotations, e.g., various attributes that characterize the type of the markable. We use the term *markable* for any element of the source text that is subject to annotation. Markables represent the basis for the subsequent annotation of coreference, information status, etc. This annotation scheme is limited to referring expressions, i.e. on (in the broadest sense) noun phrases, and their antecedents. 

If markables they are in a coreference relation, they are given an index that indicates the referent they refer to. Coreference annotation thus consists of assignment of discourse referents to markables, represented by identifiers (mnemnonics, indixes, tags) in the `COREF` column. All corerent markables should carry the same `COREF` index.

> Note: In practical annotation, annotators should not use numbers, but a meaningful, short and unambiguous abbreviation of their own choice. 

> Note: As annotation is conducted here with spreadsheet software, annotators are encouraged to use the auto-complete function that such software provides. This is most effective if indexes start with different letters.

We call the series of mentions of the same referent one *referential chain*. As result of the annotation, all elements of a referential chain must carry the same index.

> (2) *Susanne doesn't like \[gymnastics\]~1~, because \[it\]~1~ is very hard.*

> (3) *At noon, \[the Federal President\]~1~ opened \[the session\]~2~, and
in the evening, \[Joachim Gauck\]~1~ closed \[it\]~2~\> again.*

The annotation task for is to process each text in reading order and identify all markables. As described below, this process is partially automated. After marking a markable, it can also be assigned various attributes that characterize the type of the markable. Here, this comprises annotations for referentiality (`REF`), coreference (`COREF`), information status (`IS`, "givenness") and backward-looking center (`CB`, "sentence topic"). 

These guidelines use a notation as it might be used \"on paper\" or in a text editor. For the practical procedure, see [Sect. 2](format.md). In the examples given for illustration in this document, markables are marked by <u>underscores<u> (for the syntactic head), or, optionally, with square brackets \[...\] to clarify the boundaries of phrasal markables. Sometimes, for the sake of clarity, not all markables are marked in an example, but only those whose status is currently being discussed.

## 1.3 Automated Pre-Annotation

In the current workflow, automated pre-annotation will create annotations for markables, for the type of referring expressions (`NP_FORM`), their grammatical roles (`GR`), and their *possible* referentiality (`REF_AUTO`, with `?OLD` as only value so far). These annotations can be corrected by the annotator, if needed.

During annotation, dynamic pre-annotation will predict possible values for `IS` and `CB`. Again, this involves auxiliary annotations used for the automated pre-annotation of `IS` and `CB` (`GR_ANTE`: grammatical role of the antecedent, `REF_DIST`: number of sentence boundaries since last mention, `REF_DIST_ANTE`: `REF_DIST` of antecedent to *its* antecedent). These auxiliary annotations should **not** be corrected by the annotator.

## 1.4 Head-based Annotation

Although this manual sometimes gives phrasal markables for illustration, we only annotate their syntactic head, as defined by the [Universal Dependencies](https://universaldependencies.org/guidelines.html) (De Marneffe et al. 2021).<sup>[2](lit.md#terms2)</sup>
 As a result, markables must never overlap.

> (4.a) English: *\[<u>Hans</u> -- who always had \[a soft <u>spot</u>\] \[for <u>Susanne</u>\]  -- \]  was also there.*
> (4.b) German: *\[<u>Hans</u> -- der immer schon \[eine <u>Schwäche</u>\] \[für <u>Susanne</u>\] hatte -- \] war auch da.*

> Note: Annotators should normally not need to decide which expression consistutes the head of a referring expression, as these are subject to automated pre-annotation.

## 1.5 About this Document

Future revisions are expected, these may include making the criteria more precise, as well as adding or amending criteria, where appropriate, or adding more examples. **However**, during an annotation campaign, these guidelines must <u>never be changed</u>. If an annotator feels the need for clarification or to document problematic cases, please create and provide an accompanying protocol describing the example, the problem, the decision taken for resolving or marking it in the annotation and a pointer to the data where this problem occurred. These protocols will guide subsequent revisions.