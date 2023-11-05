# [DRAFT] Discourse Annotation

We annotate discourse relations between sentences and thus annotate entire sentences, only. For this reason, manual discourse annotation is conducted on a different format, but using the same set of technologies (i.e., Spreadsheet Software).

Although complete sentences are the unit of annotation, the sentence may include material not relevant for the discourse relation at hand. Instead, annotators should focus on the main clause of the sentence (or, for attribution verbs, the main clause of the reported speech contained in the current sentence).

## Task and Procedure

Goal of the annotation is to annotate every sentence with at least one discourse relation. It is neither required nor expected that the annotation of discourse relations leads to a tree structure.

Tasks:

1. [to be automated] For every sentence, identify the main clause
2. [to be automated] For every sentence, identify the primary discourse marker
3. if there is a discourse marker:
	1. annotate the target of the discourse relation (i.e., the sentence it refers to), identified by its numerical ID
	2. annotate the discourse relation
4. if there is no discourse marker:
	1. the preceding target candidate is the (main clause of the) preceding sentence.
	2. check whether the preceding target candidate is the target of a discourse relation with the (main clause of the) preceding clause by asking yourself the following questions:
		1. is there a logical connection between these utterances that could be described in terms of a discourse relation?
		2. what would be an explicit discourse marker *at the current utterance* that would make this explicit?

			> Note: It seems most practical to answer these questions in tandem, i.e., to check first which discourse marker could be applied without having the text sounding unnatural and then identify the corresponding discourse relation on that basis. Inserting (or substituting) discourse markers is an established technique for checking the applicability of a discourse relation.
		3. if a discourse relation can be annotated, annotate the target, the discourse relation and the (implicit) discourse marker; continue in 5.
	3. the following target candidate is the (main clause of the) following sentence.
		- apply the procedure of 4.2 to the following target candidate
	4. if no discourse relation with either preceding nor following target candidates can be established, then
		- set the preceding target candidate to the utterance preceding it,
		- set the following target candidate to the utterance following it

		and iterate in 4.2
5. use the `COMMENT` column to provide additional comments, e.g., if no target and/or discourse relation could be established.
6. continue with the next sentence.

> Note: This section is not concerned with the annotation of centering transitions. These are part of Sect. 5 and (to be) automatically induced from (manual) CB annotations.

## 0. Centering transitions [move out of here]

Centering transitions are not to be manually annotated

TODO: extrapolate coherence relations from CB annotation:

- no CB: no-CB
- same CB, CB=SBJ: CONTINUE
- same CB, CB!=SBJ: RETAIN
- different CB, CB=SBJ: SMOOTH-SHIFT
- different CB, CB!=SBJ: ROUGH-SHIFT

possible repair technique:
- if previous sentence has no CB, resort to the last established CB, annotate relation in round brackets

this repair technique is designed to increase robustness against incorrect segmentations and textual fragments (e.g. headlines) interrupting the continuous flow of written text

## Data format

We 

## 1.1 Scope of Annotation

Discourse relations hold between discourse segments. Here, we concentrate on discourse relations between sentences, only.

TBC: We annotate the entire sentence with a discourse relation, with automated pre-annotation for discourse relations, based on discourse marker statistics.

- we could actually annotate complete sentences rather than the head word, then, we generate data for discourse annotation from the *parsed* text, so that we have identical tokenization
- we can write this into a spreadsheets, with pre-annotations going before the actual sentence, sentence number, so that we just annotate the (absolute) ID of the external argument. people could enable word wrap to actually read the text properly.

For Discourse Annotation, we adopt the role inventory of ISO 24617-8 as described by Żurowski et al. (2023) for Polish, ...

Note that we do not directly quote from the ISO-24617-8 norm, because this is available only upon payment at https://www.iso.org/obp/ui/#iso:std:iso:24617:-8:ed-1:v1:en.

## Argument roles

For every discourse relation, we distinguish the internal argument and the external argument. Annotate the (syntactic head of the?) internal argument for

- canonical form of the discourse marker
- discourse relation
- offset of the external argument (-1 for )

If the main clause of a sentence carries a discourse marker, this clause is the internal argument of this discourse marker. The sentence that the discourse marker refers to is the external argument. The external argument can precede or follow the internal argument.

If the main clause of a sentence carries no discourse marker, annotate the most suitable discourse relation based on an insertion test for different discourse markers based on the following hierarchy: ...

Annotate the current sentence with the implicit discourse marker [HOW?]. The current sentence is considered the internal argument. With implicit discourse relations, the external argument normally precedes the internal argument.

	(ex)
		EXTERNAL ARG (NARRATIVE) She insisted that I go to college.
		DISCOURSE MARKER: Ø
		INTERNAL ARG (EXPANDER) During the occupation, she put herself in great danger to save me ...

		(Żurowski et al. 2023, p.487, translated from Polish)

NB: maybe change terminology: instead of external argument, we speak about SOURCE and TARGET of relation? or about UTTERANCE and ANCHOR? This would make sense because we aim to annotate every utterance. 

> Note: Our approach on argument identification follows the Penn Discourse Treebank. Our internal argument corresponds to the PDTB ARG1, our external argument corresponds to the PDTB ARG0. There is no systematic relation between internal and extenal arguments and ARG0 and ARG1 as defined in ISO SemAF.

## Pre-Annotation

For every sentence, we annotate the word that expresses its core predicate. Here, we refer to this word as the (semantic) nucleus, further abbreviated as NUC. The NUC is to be automatically identified with the following rules:

1. initial NUC candidate is the syntactic head according to UD
2. if the current NUC candidate is a nominal, adjectival or adverbial predicate of a copula clause with an explicit verb, make the copular verb the NUC candidate.
3. if the current NUC candidate is an attribution verb, then
	- set the NUC candidate to the first directly dependent finite verb
	- if this is not possible, set the NUC candidate to the first direct dependent with clausal dependents
	- if this is not possible, set the NUC candidate to its first csubj, ccomp or xcomp argument
	- if this is not possible, keep the NUC candidate
4. iterate in 2. until the NUC candidate cannot be further propagated downwards
5. set the NUC to the current NUC candidate

- rule 2. is necessary because of an unfortunate design decision in UD. 
- rule 3. is designed to rule out verbs of attribution as core predicates. Traditionally, these are assigned a special status. Here, they are excluded from discourse annotation.

## Automated discourse marker identification

For every sentence, discourse markers are heuristically identified as follows:
- lexicalize the top nodes of the parse tree (skip all words with depth larger than 3)
- if that contains a candidate discourse marker known from our discourse marker lexicon, assume that this is a sentence-level discourse marker
- keep the longest candidate discourse marker found
- keep the alphabetically first candidate discourse marker found

However, not every candidate discourse marker is an actual discourse marker (e.g., the prepositions "for" and "to"), and not every discourse marker applies to the sentence level (it could also connect clauses within a sentence). Thus, automated discourse marker identification is to be taken with a grain of salt, and automatically identified discourse markers are to be verified first, before being used in annotation.


## Manual discourse marker annotation

We distinguish two primary kinds of discourse markers: 
- explicit discourse markers are stated in the text. annotators should write them as plain strings.
- implicit discourse markers are not stated in the text. annotators should write them in round brackets.

Because of the uncertainties of automated pre-annotation for discourse markers, automatically identified discourse markers are always marked by a question mark. To confirm a discourse marker, annotators should remove the question mark. Discourse markers with question marks are considered an error.

Many researchers distinguish discourse markers and alternative lexicalizations, i.e., a phrasal expression that conveys the meaning of a discourse marker that could be used in its place in a more or less equivalent way (e.g., "This observation leads us to conclude that ..." in place of "Thus, ..."). If such phrases are no longer than 5 words, annotators should annotate such phrases as explicit discourse markers. If such phrases are longer than 5 words, proceed as follows:

- provide a common discourse marker that could be used in place of the alternative lexicalization, write it in **square brackets**, add the alternative lexicalization afterwards

If the discourse marker you provided could also be used *in addition to* the alternative lexicalization, then treat this as implicit discourse marker, i.e.,

- provide the discourse marker you inferred in round brackets. 

See the list of diagnostic markers in the appendix

## Relations

> Note: ISO 24617-8 has been heavily criticized for being poorly defined (e.g., by Żurowski et al. 2023). We provide operationalizable definitions by exploiting the correspondence with established RST, SDRT and PDTB definitions as given by proponents of ISO SemAF.

For asymmetric relations, we annotate the ISO SemAF role of the internal argument. For symmetric relations, we annotate the ISO SemAF relation at the second argument.

- **CAUSE**
	- **Reason**: In a `CAUSE` relation, the `Reason` provides a reason for the `Result` to come about or occur. (Bunt & Prasad 2016)
		- cf. RST Vol. cause, Non-vol. cause, Evidence, Justify
		- cf. RSTDTB Cause, Evidence, Explanation-argumentation, Reason
		- cf. SDRT Explanation (DISCOR Explanation, ANNODIS Explanation)
		- cf. PDTB Reason, Justification
	- **Result**: In a `CAUSE` relation, the `Reason` provides a reason for the `Result` to come about or occur. (Bunt & Prasad 2016)
		- cf. RST Vol. result, Non-vol. result
		- cf. RSTDTB Consequence, Result
		- cf. SDRT Result (DISCOR Result, ANNODIS Result)
		- cf. PDTB Result
- **CONDITION**
	- **Antecedent**In a `CONDITION` relation, the `Condition` is an unrealized situation which, when realized, would lead to the `Consequent`. (Bunt & Prasad 2016)
		- cf. RST Condition
		- cf. RSTDTB Condition, ?Hypothetical
		- cf. ANNODIS ?Conditional
		- cf. PDTB ?Hypothetical, ?General, UnrealPast, ?UnrealPresent, FactualPast, ?FactualPresent
	- **Consequent**: In a `CONDITION` relation, the `Condition` is an unrealized situation which, when realized, would lead to the `Consequent`.(Bunt & Prasad 2016)
		- ?cf. RSTDTB Contingency
		- cf. SDRT Consequence (DISCOR Consequence)
- **NEGATIVE_CONDITION**
	- **Negated_Condition**: In a `NEGATIVE_CONDITION` relation, the `Negated_Condition` is an unrealized situation which, when not realized, would lead to the `Consequent`. (Bunt & Prasad 2016)
		- cf. ANNODIS ?Conditional
		- cf. PDTB Condition
	- **Consequent**: In a `NEG_CONDITION` relation, the `Negated_Condition` is an unrealized situation which, when not realized, would lead to the `Consequent`. (Bunt & Prasad 2016)
		- cf. ?RST Otherwise
		- cf. ?RSTDTB Otherwise
		- cf. SDRT Consequence (DISCOR Consequence)
- **PURPOSE**, cf. RST ?Purpose, RSTDTB ?Purpose
	- **Goal**: In a `PURPOSE` relation, the `Goal` enables the `Enablement`. (Bunt & Prasad 2016)
		- cf. SDRT Explanation (DISCOR Explanation, ANNODIS Goal)
		- cf. PDTB Result
	- **Enablement**: In a `PURPOSE` relation, the `Goal` enables the `Enablement`. (Bunt & Prasad 2016)
- **MANNER**, cf. SDRT (ANNODIS, DISCOR) Elaboration
	- **Means**: In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs. (Bunt & Prasad 2016)
		- cf. RSTDTB Means, ?Manner
	- **Achievement**: In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs. (Bunt & Prasad 2016)
- **CONCESSION**, cf. SDRT (DISCOR, ANNODIS) Contrast
	- **Expectation-raiser**: `CONCESSION` is an expected causal relation between two arguments, where the `Expectation-raiser` is expected to cause the situation described in the other argument, but is cancelled or denied by the `Expecation-denier` argument. (Bunt & Prasad 2016)
		- cf. RST ?Concession
		- cf. RSTDTB ?Concession, ?Antithesis, ?Preference
		- cf. PDTB Expectation
	- **Expectation-denier**: `CONCESSION` is an expected causal relation between two arguments, where the `Expectation-raiser` is expected to cause the situation described in the other argument, but is cancelled or denied by the `Expecation-denier` argument. (Bunt & Prasad 2016)
		- cf. RST ?Concession
		- cf. RSTDTB ?Concession, ?Antithesis, ?Preference
		- cf. PDTB Contra-Expectation
- **CONTRAST**: `CONTRAST` is a symmetric relation in which one or more differences between the internal argument and the external argument are highlighted with respect to what each predicates as a whole or to some entities they mention. (Bunt & Prasad 2016)
	- cf. RST Contrast
	- cf. RSTDTB Comparison
	- cf. SDRT (DISCOR, ANNODIS) Contrast
	- cf. PDTB Justaposition, Opposition
- **EXCEPTION**
	- **Regular**: In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't. (Bunt & Prasad 2016)
	- **Exception**: In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't. (Bunt & Prasad 2016)
		- cf. PDTB Exception
- **SIMILARITY**: `SIMILARITY` is a symmetric relation in which one or more similarities between the internal and the external argument are highlighted with respect to what each predicates as a whole or to some entities they mention. (Bunt & Prasad 2016)
	- cf. RSTDTB Analogy, Proportion 
	- cf. SDRT (ANNODIS, DISCOR) Parallel
	- cf. PDTB Conjunction
- **SUBSTITUTION**
	- **Disfavoured-alternative**: In a `SUBSTITUTION` relation, both arguments describe alternative situations, with `Disfavoured-alternative` being the disfavored or rejected alternative. (Bunt & Prasad 2016)
		- cf. RST ?Antithesis
	- **Favoured-alternative**: In a `SUBSTITUTION` relation, both arguments describe alternative situations, with `Favoured-alternative` being the favored or chosen alternative. (Bunt & Prasad 2016)
		- cf. RST ?Antithesis
		- cf. PDTB Chosen Alternative
- **CONJUNCTION**: `CONJUNCTION` is a symmetric relation in which the internal and the external arguments bear the same relation to some other situation evoked in the discourse. Their conjunction indicates that they are doing the same thing with respect to that situation, or are doing it together. (Bunt & Prasad 2016)
	- cf. RST Joint
	- cf. RSTDTB List
	- cf. SDRT (DISCOR, ANNODIS) Continuation
	- cf. PDTB Conjunction, List
- **DISJUNCTION**: `DISJUNCTION` is a symmetric relation in which the internal and the external arguments are alternatives, with either one or both holding (Bunt & Prasad 2016)
	- cf. RST Joint
	- cf. RSTDTB Disjunction
	- cf. SDRT (DISCOR, ANNODIS) Alternation
	- cf. PDTB Disjunctive, Conjunctive
- **EXEMPLIFICATION**
	- **Set**: In an `EXEMPLICATION` relation, the `Set` describes a set of situations; the `Instance` is an element of that set. (Bunt & Prasad 2016)
	- **Instance**:	In an `EXEMPLICATION` relation, the `Set` describes a set of situations; the `Instance` is an element of that set. (Bunt & Prasad 2016)
		- cf. RST Elaboration (set-member)
		- cf. RSTDTB Elaboration set-member, Example
		- cf. SDRT (DISCOR, ANNODIS) Elaboration
		- cf. PDTB Instantiation
- **ELABORATION**
	- **Broad**: In an `ELABORATION` relation, both arguments are the same situation, but the `Specific` argument contains more detail than the `Broad` argument. (Bunt & Prasad 2016)
		- cf. PDTB Generalization
	- **Specific**: In an `ELABORATION` relation, both arguments are the same situation, but the `Specific` argument contains more detail than the `Broad` argument. (Bunt & Prasad 2016)
		- cf. RST Elaboration
		- cf. RSTDTB Conclusion, Elaboration general-specific, Elaboration whole-part, Elaboration process-step
		- cf. SDRT (DISCOR, ANNODIS) Elaboration
		- cf. PDTB Specification
- **RESTATEMENT**: `RESTATEMENT` is a symmetric relation in which the internal argument describes the same situation as the external argument, but from different perspectives. (Bunt & Prasad 2016)
	- cf. RST Restatement
	- cf. RSTDTB Summary
	- cf. SDRT (DISCOR, ANNODIS) Elaboration
	- cf. PDTB Equivalence
- **SYNCHRONY**: `SYNCHRONY` is a symmetric relation where some degree of temporal overlap exists between the internal argument and the external argument. All forms of overlap are included. (Bunt & Prasad 2016)
	- cf. RSTDTB Temporal-same-time
	- cf. PDTB Synchronous
- **ASYNCHRONY**, cf. RST Sequence
	- **Before**: In an `ASYNCHRONY` relation, the argument `Before` temporally precedes the `After` argument. (Bunt & Prasad 2016)
		- cf. RSTDTB Temporal-before, Inverted-sequence
		- cf. DISCOR Precondition, ANNODIS Flashback
		- cf. PDTB Precedence
	- **After**: In an `ASYNCHRONY` relation, the argument `Before` temporally precedes the `After` argument. (Bunt & Prasad 2016)
		- cf. RSTDTB Temporal-after, Sequence
		- cf. SDRT (DISCOR, ANNODIS) Narration
		- cf. PDTB Succession
- **EXPANSION**
	- **Foreground**: In an `EXPANSION` relation, the `Entity-description` argument provides further description about some entity or entities in the `Foreground`, expanding the narrative forward of which `Foreground` is a part, or expanding on the setting relevant for interpreting the `Foreground`. The internal and external arguments describe distinct situations. (Bunt & Prasad 2016)
		- tbc: should never be annotated
	- **Entity-description**: In an `EXPANSION` relation, the `Entity-description` argument provides further description about some entity or entities in the `Foreground`, expanding the narrative forward of which `Foreground` is a part, or expanding on the setting relevant for interpreting the `Foreground`. The internal and external arguments describe distinct situations. (Bunt & Prasad 2016)
		- cf. RST Elaboration (object-attribute)
		- cf. RSTDTB Elaboration object-attribute, Elaboration additional
		- cf. SDRT Background, Elaboration (DISCOR Commentary, Attribution, Source; ANNODIS Comment, Attribution, Frame, Temporal-location)
		- cf. PDTB EntRel
- **FUNCTIONAL_DEPENDENCE**
	- **Antecedent-act**: External argument of a functional dependence, precedes the internal argument. (Not to be annotated.) (Bunt & Prasad 2016)
	- **Dependent-act**: In a `FUNCTIONAL_DEPENDENCE` relation, the `Dependent-act` is a dialogue act with a responsive communicative function; the `Antecedent-act` is the dialogue act(s) that the `Dependent-act` responds to. (Bunt & Prasad 2016)
- **FEEDBACK_DEPENDENCE**
	- **Feedback-scope**: External argument of a feedback dependence, precedes the internal argument. (Not to be annotated.) (Bunt & Prasad 2016)
	- **Feedback-act**:	In a `FEEDBACK_DEPENDENCE` relation, the `Feedback-act` that provides or elicits information about the understanding or evaluation by one of the dialogue participants of the `Feedback-scope` argument, a communicative event that occurred earlier in the discourse. (Bunt & Prasad 2016)

> Note: The relation definitions follow Prasad and Bunt (2016). RST, RSTDTB, SDRT and PDTB mapping follows Prasad and Bunt (2016).

> Note: Role labels are taken from ISO SemAF. The `Condition` relation corresponds to ISO SemAF CONDITION with internal argument role "Antecedent". The `Negated_Condition` relation corresponds to ISO SemAF NEGATIVE CONDITION with internal argument role "Negated_Antecedent". 

> Note: For `Feedback-act`, annotate if and only if turn-taking or interruptions occurred  

> Note: Consider replacing `Feedback-act` and `Dependent-act` annotations by dialogue act annotations.

> Note: Annotate Dependence relations only in the absence of explicit discourse markers, example:

	- P1: I can never find my remote control.	P2: That’s [because] they don’t have a fixed place.		(Reason, not Inform, from Butt & Prasad 2016)

## Appendix: List of diagnostic discourse markers

You can use the following list to confirm whether a discourse relation holds. If you can use these discourse markers in place of the explicit discourse marker or the alternative lexicalization at hand, or insert them into a sentence without implicit discourse marker, take this as an indicator that the respective discourse relation holds.

Also, when disambiguating explicit or inserting implicit discourse markers, consult this list from top to bottom: If a discourse marker holds, do not consider other candidate markers further below. We currently provide lists for English and German. Discourse marker lists for other languages can be provided upon demand.

### English

### German


## References

- Sebastian Żurowski, Daniel Ziembicki, Aleksandra Tomaszewska, Maciej Ogrodniczuk and Agata Drozd (2023), Adopting ISO 24617-8 for Discourse Relations Annotation in Polish: Challenges and Future Directions. In Proceedings of the 4th Conference on Language, Data and Knowledge (pp. 482-492).

- Bunt, Harry and Prasad, Rashmi (2016), ISO DR-Core (ISO 24617-8): Core concepts for the annotation of discourse relations, In: Proceedings 12th joint ACL-ISO workshop on interoperable semantic annotation (ISA-12), p. 45-54


NB: for Dialog data, cf. https://dialogbank.lsv.uni-saarland.de/