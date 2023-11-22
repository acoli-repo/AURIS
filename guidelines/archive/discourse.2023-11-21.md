# A. Discourse Relations

The annotation of discourse relations adopts a different format and is thus described in an appendix to the AURIS guidelines.

We annotate discourse relations between sentences and thus annotate entire sentences, only. For this reason, manual discourse annotation is conducted on a different format, but using the same set of technologies (i.e., Spreadsheet Software).

Although complete sentences are the unit of annotation, the sentence may include material not relevant for the discourse relation at hand. Instead, annotators should focus on the main clause of the sentence.
There is an exception for attribution verbs, for which the main clause of the attributed statement (i.e., the reported speech) is to be annotated.

> Note that these guidelines are partially based on the Penn Discourse Treebank, which also accounts for intrasentential discourse relations. We thus still include examples of intrasentential relations in the definition of discourse relations. In the future, these are to be replaced by real-world intersentential corpus examples. 

The Goal of the annotation is to annotate every sentence with one **discourse relation**. It is neither required nor expected that the annotation of discourse relations leads to a tree structure. The refer to the sentence that is annotated as the **utterance**, the sentence that it is linked to by the discourse relation as the **(contextual) anchor**. If a discourse relation is indicated by an explicit discourse marker, this is syntactically integrated with the utterance. Accordingly, the applicability of a discourse relation can be tested by means of a paraphrase or substitution test where a diagnostic discourse marker is inserted: If the insertion of a diagnostic discourse marker does not change the meaning of the utterance in its context, the corresponding discourse relation can be annotated. A list of diagnostic markers is provided in an appendix.

The order of anchor and utterance is flexible, but in many cases, the anchor precedes the utterance. For implicit discourse markers, the anchor should generally precede the utterance, explicit discourse can be used by the speaker to underline that the anchor follows the utterance. A notable special case is the first part of a paired discourse marker, such as *On the one hand ... . On the other hand ...*. Here, the first utterance, marked with *on the one hand*, takes the second as its anchor, whereas the second takes the first as its anchor. If an utterance carries more than one explicit discourse marker, we annotate the first discourse marker, only.

> **Note**: This section is concerned with the annotation of discourse relations, i.e., semantic or functional relations between utterances. As for relations between discourse referents (coreference, Centering Transitions), this is subject to Sect. 5 of the AURIS guidelines.

## A.1 Preparation and Format

Annotation is done using Spreadsheet software such as MS Excel or LibreOffice. We provide automated pre-annotations as well as formulas to dynamically populate the spreadsheet file. For annotating a file with pre-annotations, say `doyle_bask.14.tsv`, please proceed as follows:

1. Copy `discourse-template.xlsx` to `doyle_bask.14.xlsx` (take the name of your source file as a basis)
2. Open `doyle_bask.14.tsv` in your Spreadsheet software (or, alternatively, in a text editor)
3. Select the full content of `doyle_bask.14.tsv`
	- Text editor, Windows/Linux: press `<CTRL>+A` to select all
	- Spreadsheet software, Windows/Linux: go to upper left corner (cell `A1`), press `<SHIFT>+<CTRL>+<END>` to select table data
4. Copy the content of `doyle_bask.14.tsv`
	- Windows/Linux: press `<CTRL>+C`
5. Open `doyle_bask.14.xlsx` in your Spreadsheet software
6. Go to cell `A3` (first cell, third line)
7. Paste the content of `doyle_bask.14.tsv` into `doyle_bask.14.xlsx`
	- Windows/Linux: press `<CTRL>+V`
8. Copy the formulas (colored cells) from row `3`
	- Windows/Linux: nagivate to `G3`, press `<SHIFT>+<END>` to select all formulas
9. Select from `G3` until the end of the table
	- Windows/Linux: navigate to `G3`, press `<SHIFT>+<CTRL>+<END>`
10. Paste formulas into the selected area, confirm consent to overwrite
	- Windows/Linux: press `<CTRL>+V`
11. If successful, the entire table should have the same colored columns as the template.

After preparation, your table should look as follows:

![template.png](template.png)

(Note that you can resize column width and height as needed.)

Empty cells should be filled with `_`, automated pre-annotations are marked with question marks. After annotations, no question marks should remain.

The spreadsheet file contains the following columns:

- `ID` (col A) sentence number
- `PREDICATE` (col D) main verb, automatically annotated
- `TEXT` (col E) utterance to be annotated
- `MARKER` (col G) possible discourse marker. Automatically identified discourse markers are marked by a question mark. To be replaced with actual discourse marker (without question mark).
- `TARGET` (col H) ID of the utterance that serves as anchor of the discourse relation.
- `RELATION` (col I) discourse relation
- `COMMENT` (col J) free-text comment

Note that in the template, several columns are hidden. These are auxiliary columns that annotators don't need to look into.

Also note that automated pre-annotations might be incorrect. Except for `MARKER` (whose annotations should be replaced anyway), correcting an incorrect pre-annotation requires to leave a comment, either in an accompanying text file (annotation log), with reference to the corresponding sentence ID, or in the `COMMENT` column.

## A.2 Annotation Tasks and Procedure

Annotation involves the following sub-tasks. Some of these tasks are automated, however, automated annotations, if found to be incorrect, should be corrected. In those cases, leave a comment in the `COMMENT` column.

1. For every sentence, identify the main predicate
	- Pre-annotation in `PREDICATE`. If the annotator believes the predicate to be incorrect, fix that column and leave a comment with an explanation.
2. For every sentence, identify the primary discourse marker (pre-annotation in `MARKER`)
	- Pre-annotation in `MARKER`. Should be manually confirmed or revised.
3. if there is an explicit discourse marker:
	1. annotate the anchor of the discourse relation (i.e., the sentence it refers to) in column `TARGET`, identified by its numerical ID. If there are multiple candidate anchors, annotate the closest anchor.
	2. annotate the discourse relation in `RELATION`
4. if there is no explicit discourse marker:
	1. the preceding target candidate is the (main predicate of the) preceding sentence.
	2. check whether the preceding target candidate is the target of a discourse relation with the (main predicate of the) preceding clause by asking yourself the following questions:
		1. is there a logical connection between these utterances that could be described in terms of a discourse relation?
		2. Is there an discourse marker *at the current utterance* that could be used to make this explicit? Annotate this discourse marker in `MARKER`, put it in round brackets to mark it as an implicit discourse marker.
		3. If a discourse relation (and, optionally, an implicit `MARKER`) has been confirmed, annotate the `TARGET` and the `RELATION`; continue in 5.
		4. If no discourse relation could be annotated, check the following utterance as candidate anchor, then extend further into preceding context until an anchor has been found or it can be assumed that no anchor exists. If the latter, explain why you think so in `COMMENT`.
5. use the `COMMENT` column to provide additional comments, e.g., if no target and/or discourse relation could be established.
6. continue with the next sentence.

> **Note**: For 4.2.1 and 4.2.2, it seems most practical to answer these questions in tandem, i.e., to check first which discourse marker could be applied without having the text sounding unnatural and then identify the corresponding discourse relation on that basis. Inserting (or paraphrasing with) diagnosting discourse markers is an established technique for testing the applicability of a discourse relation. See Sect. A.4.2 for more detailed instructions.

## A.3 Identifying the Main Predicate

For every sentence, we annotate the discourse relations of its core statement. Syntactically, the core statement is represented by the main predicate and its syntactic dependents. The main predicate is identified by the following rules:

1. By default, the main predicate is the syntactic head of the first main clause in the current sentence
2. If the syntactic head is a nominal, adjectival or adverbial predicate of a copula clause with an explicit verb, the predicate consists of the copula in conjunction with the predicate.
3. If the syntactic head is an attribution verb (*say*, *write*, *think*, etc.) and the current sentence contains a reported statement (direct or indirect speech), the main predicate of the sentence is the main predicate of the reported statement.

> **Note 1**: For syntactic analysis, we expect pre-annotation in accordance with Universal Dependencies 2.x. See [there](https://universaldependencies.org/u/overview/syntax.html) for the definition of syntactic heads.

Rule 3 is designed to rule out verbs of attribution as main predicates. Here, we follow ISO 24617-8 in excluding them from discourse annotation (if the sentence contains a reported statement). In (1), the discourse relation doesn't hold between the communication acts (*Mr. Edelman said X. Mr. Ackerman contended Y.*) but between their respective statements (*X, [implicit:Concession] Y*). The respective main predicates are marked:

- (1) _[Mr. Edelman said]<sub>ATTRIBUTION</sub> the decision ”[**has nothing to do**]<sub>PRED</sub> with Marty Ackerman.” [Mr. Ackerman contended]<sub>ATTRIBUTION</sub> that it [**was a direct response**]<sub>PRED</sub> to his efforts to gain control of Datapoint._ (PDTB3, wsj 0333)

## A.4 Annotating Discourse Markers

Discourse markers are cues that overtly mark discourse relations. For English, this primarily includes

- adverbials (ADVP and PP, e.g., *however*, *otherwise*, *then*, *as a result*, *for example*),
- coordinating conjunctions (e.g., *and*, *or*, *nor*), and
- subordinating conjunctions (e.g., *because*, *when*, *since*, *although*).

We distinguish three kinds of discourse markers: 

- Explicit discourse markers are stated in the text. Annotators should write them as plain strings.
- Alternative lexicalizations are phrasal expressions that convey the same meaning as a discourse marker and that could be paraphrased by a discourse marker. They are, however, not grammaticalized as discourse markers. Annotators should write these phrases as plain strings, and add a discourse marker that could be used as paraphrase after that in square brackets.
- Implicit discourse markers are not stated in the text. Annotators should write them in round brackets.

### A.4.1 Annotating Explicit Discourse Markers

Explicit discourse markers are drawn from the following grammatical classes (Prasad et al. 2007):

- adverbials (ADVP and PP):

	- (2) *The magazine Success, **however**, was for years lackluster and unfocused.* (PDTB2, 1903)
	- (3) ***As a result**, industry operated out of small, expensive, highly inefficient industrial units.* (PDTB2, 0629)

	- DO NOT ANNOTATE adverbials modifying clauses other than the main predicate. In line with Universal Dependency syntax, the clause connected with the conjunction _and_ in (4) is syntactically analyzed as a dependent of the first clause. It does thus not carry the main predicate and neither _and_ nor _as a result_ should be annotated.

		- (4) *Polyvinyl chloride capacity “has overtaken demand **and** we are experiencing reduced profit margins **as a result**”, ...* (PDTB2, 2083)

- coordinating conjunctions, but only if attached to the main predicate of an utterance:
	
	- (5) *Only 19% of the purchasing managers reported better export orders in October, down from 27% in September. **And** 8% said export orders were down last month, compared with 6% the month before.* (PDTB2, 0036)

	- DO NOT ANNOTATE conjunctions not modifying the main predicate:

		- (6) *The House has voted to raise the ceiling to $3.1 trillion, **but** the Senate isn’t expected to act until next week at the earliest.* (PDTB2, 0008)
		- (7) *More common chrysotile fibers are curly **and** are more easily rejected by the body, Dr. Mossman explained.* (PDTB2, 0003)

- subordinating conjunctions, but only if attached to the main predicate of an utterance:
		
	- (8) *Why do local real-estate markets overreact to regional economic cycles? **Because** real-estate purchases and leases are such major long-term commitments that most companies and individuals make these decisions only when confident of future economic stability and growth.* (PDTB2, 2444)

	- DO NOT ANNOTATE conjunctions not modifying the main predicate:

		- (9) ***Since** McDonald’s menu prices rose this year, the actual decline may have been more.* (PDTB2, 1280, conjunction of a pre-posed dependent clause)

		- (10) *The federal government suspended sales of U.S. savings bonds **because** Congress hasn’t lifted the ceiling on government debt.* (PDTB2, 0008, conjunction of a post-posed dependent clause)

If the main predicate carries more than one discourse marker, annotate the first discourse marker, only:

- (11) *Small businesses say a recent trend is like a dream come true: more-affordable rates for employee-health insurance, initially at least. **But** then they wake up to a nightmare.* (PDTB3, wsj 0518; Webber et al. 2019b)

Here the, _but_ and _then_ encode independent discourse relations, the first indicating Concession, the second a temporal relation. However, _but then_ can also be analyzed as a single discourse marker, indicating Concession:

- (12) *To many, it was a ceremony more befitting a king than a rural judge seated in the isolated foothills of the southern Allegheny Mountains. **But then** Judge O’Kicki often behaved like a man who would be king – and, some say, an arrogant and abusive one.* (PDTB3, wsj 0267; Webber et al. 2019b)

Note that the first discourse marker may also occur at medial (or final) positions within a clause:

- (13) *The Ministry of Finance, **as a result**, has proposed a series of measures that would restrict business investment in real estate ...* (PDTB2, 0761, medial discourse marker)

Adverbials should be annotated as discourse markers only if they establish a relation between utterance and anchor. Interjections such as _well_, focus markers such as _anyway_, and clausal adverbials such as _strangely_, _probably_, _frankly_, _in all likelihood_ etc. are not annotated as discourse markers.
	
> Note that not all words and phrases that *can* serve as discourse markers actually do so under all circumstances: Some tokens can also serve other functions, e.g., _for_ can be a causal discourse marker (and then, be substituted with _because_), but it can also serve as a preposition indicating the beneficiary of an action. Likewise, discourse markers that serve to connect parts of the same utterance are beyond the scope of AURIS. Such expressions are not annotated as discourse connectives.

In the current workflow, the first candidate discourse marker is automatically annotated. However, note that this has been heuristically extracted and may include discourse markers not modifying the main predicate, or expressions that *could* serve as discourse markers but that don't in this particular context. Thus, in the column `MARKER`, these are always shown with a question mark and to be confirmed (or replaced) by manual annotation. Discourse markers with question marks are considered an error.

### A.4.2 Annotation of implicit discourse markers

If an utterance does not feature an explicit discourse marker, annotators should try to test whether an explicit discourse marker could be inserted or whether another discourse relations applies. Example (14) shows an example of an implicit *because* inserted to connect two adjacent utterances

- (14) *Some have raised their cash positions to record levels. **[Implicit = because]** High cash positions help buffer a fund when the market falls.* (PDTB2, 0983)

In discourse relations with implicit discourse markers, the anchor always precedes the utterance. In the following, it would be logically possible to annotate Reason to point from the first utterance to the second, but because of ordering preferences for implicit relations, we only annotate the inverse relation Result:

- (15) Carl is crazy. **[Implicit = this is why]** he beats his wife. (Prasad and Bunt 2015, punctuation adjusted)

For annotating implicit discourse markers, annotators should use the list of discourse relations and their diagnostic discourse markers, and check it the order specified in Sect. **BELOW**.

1. check whether the preceding sentence could be an anchor
	1. by inserting the first discourse marker on the list, if that fails
	2. by inserting the second discourse marker, etc.
	3. if both utterances are connected by a coherence relation between two referring expressions, insert no marker, but annotate EntRel
2. if no discourse marker could be inserted, test the preceding utterance
	1. using the same procedure
3. iterate until an anchor and an implicit discourse marker have been found or no possible anchor can be expected anymore (e.g., because the text deals with different topics)

> Note: Unlike PDTB2, the annotation of implicit relations is not limited to adjacent utterances.

### A.4.3 Alternative Lexicalizations

Many researchers distinguish discourse markers and alternative lexicalizations, i.e., a phrasal expression that conveys the meaning of a discourse marker that could be used in its place in a more or less equivalent way (e.g., *This observation leads us to conclude that ...* in place of *Thus, ...*). If such phrases are no longer than 5 words, annotators should annotate such phrases as explicit discourse markers. If such phrases are longer than 5 words, proceed as follows:

- provide a common discourse marker that could be used in place of the alternative lexicalization, write the alternative lexicalization and put the discourse marker in **square brackets** afterwards.

If the discourse marker you provided could also be used *in addition to* the alternative lexicalization, then treat this as implicit discourse marker, i.e.,

- provide the discourse marker you inferred in round brackets. 

## A.5 Relation Inventory

AURIS discourse relations are organized in a hierarchy that is also used to define selection preferences for annotation.

### A.5.1 Top-Level Organization

- **ADVERSATIVITY**: discourse relations concerned with highlighting prominent differences between the situations presented in utterance and anchor.
- **CONTINGENCY**: discourse relations in which one of the situations described in utterance and anchor causally influences the other, i.e., it provides a reason, explanation or justification in the other situation.
- **TEMPORAL**: the situations described in utterance and anchor are related temporally.
- **EXPANSION**: other relations which expand the discourse and move its narrative or exposition forward.
- **DIALOG**: discourse relations for turn-taking in dialog.
- **EntRel**: utterance and anchor are not related by any of the other types of discourse relations, but indirectly by addressing the same entities 

In addition to these, we use **NoRel** to mark utterances for which no anchor can be established.

### A.5.2 Annotation Principles

- if the main predicate carries more than one explicit discourse marker, annotate the first explicit discourse marker
- if there is no discourse marker or the discourse marker is ambiguous with respect to the discourse relation it encodes:

	- annotate the most specific discourse relation possible, using the following preference hierachy

		- ADVERSATIVITY > CONTINGENCY > TEMPORAL > EXPANSION > DIALOG > EntRel > NoRel

The logic behind this ranking is that it describes a spectrum from semantically highly constrained (i.e., very specific) to semantically less constrained (i.e., more generic) relation types, and that annotators should annotate the most specific discourse relation applicable.

- adversative relations can involve a causal element (especially CONCESSION), so that these are considered more specific than causal
- causal (CONTINGENCY) relations imply a temporal element (cause precedes or overlaps with result), so that these are more specific than temporal
- as a means of driving the discourse forward, TEMPORAL relations are a subset of expansion relations
- In general, dialog acts apply to all utterances, but in the context of discourse annotations, they should be limited to cases in which no other discourse relations apply. So, their annotation priority is below that of Expansion. Nevertheless, if over signals require a functional dependence or feedback dependence annotation, these should be used.
- we follow the view of PDTB that entity relations should be annotated only if no other relation applies. `EntRel` relations are a fallback to enable the annotation of discourse relations whose attachment is unclear, but still evident from coreference links.

If no relation can be established with the last preceding utterance, explore the one before, etc. Note that, as a result, the anchor of an utterance does not have to be in the preceding utterance:

- (16.1) *Kidder, Peabody & Co. is trying to struggle back.*
- (16.2) [ANCHOR:] *Only a few months ago, the 124-year-old securities firm seemed to be on the verge of a meltdown, racked by internal squabbles and defections.* 
- (16.3) *Its relationship with parent General Electric Co. had been frayed since a big Kidder insider-trading scandal two years ago.*
- (16.4) *Chief executives and presidents had come and gone.*
- (16.5) ***[Implicit Contrast = But]** Now, the firm says it’s at a turning point.* 
- (16.6) "By the end of this year, 63-year-old Chairman Silas Cathcart – the former chairman of Illinois Tool Works who was derided as a ”tool-and-die man” when GE brought him in to clean up Kidder in 1987 – retires to his Lake Forest, Ill., home, possibly to build a shopping mall on some land he owns."" (Prasad et al. 2017, p. 10)

In this example, the anchor of the implicit Contrast (16.5) is three sentences back (16.2).

- (17.1) [ANCHOR:] P1: *Is it safe to put my camera through here?*
- (17.2) P1: *It’s a very expensive camera you know.* 
- (17.3) **[Answer]** P2: *Yes, that’s perfectly safe.* (Bunt and Prasad 2016)

For (17.3), no discourse relation, nor an entity relation can be established between with (17.2), so that (17.1) has to be considered (and can be confirmed) as anchor.

- (18.1) [ANCHOR:] A: *So I can be there at 10:30.*
- (18.2) A: *I don’t know about Peterson.*
- (18.3) **[Feedback]** B: *10:30, okay.*
- (18.4) B: *We’ll start at 10:15 with the formalities.* (Bunt et al. 2012, p.433)

If an utterance can take more than one sentence as anchor, annotate the most proximate anchor, only:

- (19.1) B: *We’re gonna be selling this remote control for twenty five euro*
- (19.2) B: *and we’re aiming to make fifty million euro*
- (19.3) B: *so we’re gonna be selling this on an international scale*
- (19.4) [ANCHOR:] B: *and we don’t want it to cost more than twelve fifty euros*
- (19.5) **[Feedback]** D: *Okay*
- (19.6) [ANCHOR:] B: *So fifty percent of the selling price*
- (19.7) **[Feedback]** D: *Can we go over that again* (Bunt et al., 2012, p.432-433)

According to Bunt et al. (2012), (19.5) actually refers back to (19.1) - (19.4), but we annotate only (19.4) as anchor. (19.7), then, takes scope over (19.1) - (19.4) _and_ (19.6), but we only annotate the relation to (19.6). 

### A.5.3 Overall hierarchy

The top level of the hierarchy follows PDTB2, the middle level represents SemAF relations, the third level represents SemAF attribute roles.

- **ADVERSATIVITY**
	- `Concession` (SemAF Concession)
		- `expectation-raiser` (SemAF Concession/Expectation-raiser)
		- `contra-expectation` (SemAF Concession/Expectation-denier)
		- `concession` (SemAF Concession, PDTB: Concession with unclear directionality)
	- `Contrast` (SemAF Contrast)
- **CONTINGENCY**
	- `Causal` (SemAF Cause)
		- `reason` (SemAF Cause/Reason)
		- `result` (SemAF Cause/Result)
		- `cause`  (SemAF Cause, if directionality is unclear)
	- `Conditional` (SemAF Condition)
		- `condition` (SemAF Condition/Antecedent)
		- `consequence` (SemAF Condition/Consequent)
	- `Negative_Condition` (SemAF Negative Condition)
		- `neg_condition` (SemAF Negative Condition/Negated Antecedent)
		- `neg_consequence` (SemAF Negative Condition/Consequence)
	- `Purpose` (SemAF Purpose)
		- `goal` (SemAF Purpose/Goal)
		- `enablement` (SemAF Purpose/Enablement)
- **TEMPORAL**
	- `Synchrony` (SemAF Synchrony)
	- `Asynchrony` (SemAF Asynchrony)
		- `after` (SemAF Asynchrony/After)
		- `before` (SemAF Asynchrony/Before)
- **EXPANSION**
	- `Manner` (SemAF Manner)
		- `means` (SemAF Manner/Means)
		- `achievement` (SemAF Manner/Achievement)
	- `Exception` (SemAF Exception)
		- `regular` (SemAF Exception/regular)
		- `exception` (SemAF Exception/exception)
	- `Similarity` (SemAF Similarity)
	- `Substitution` (SemAF Substitution)
		- `disfavoured` (SemAF Substitution/Disfavoured-alternative)
		- `favoured` (SemAF Substitution/Favoured-alternative)
	- `Conjunction` (SemAF Conjunction)
	- `Disjunction` (SemAF Disjunction)
	- `Excemplification` (SemAF Excemplification)
		- `set` (SemAF Excemplification/Set)
		- `instance` (SemAF Excemplification/Instance)
	- `Elaboration` (SemAF Elaboration)
		- `broad` (SemAF Elaboration/Broad)
		- `specific` (SemAF Elaboration/Specific)
	- `Restatement` (SemAF Restatement)
	- `Hypophora` (missing in SemAF)
	- `Attribution` (missing in SemAF)
- **DIALOG**
	- `Functional-Dependence` (SemAF Functional-dependence/dependent-act)
		- `Answer` (SemAF Dialog, communicative function `Answer`
		- `Offer` (SemAF Dialog, communicative function `Offer`
		- `Address Suggest` (SemAF Dialog, communicative function `Address Suggest`
		- `Agreement` (SemAF Dialog, communicative function `Agreement`
		- `Disagreement` (SemAF Dialog, communicative function `Disagreement`
		- `dependent-act` (other)
	- `Feedback` (SemAF Feedback-dependence/feedback-act)
- **EntRel** (SemAF Expansion/Entity description)
	- coreference between a preceding utterance and the current one.

## BIS HIER

## A.6 Individual Relations

### ADVERSATORY

Discourse relations concerned with highlighting differences between the situations described in the utterance and the anchor (PDTB2 COMPARISON).

#### Concession 

`CONCESSION` is an expected causal relation between two arguments, where the `Expectation-raiser` is expected to cause the situation described in the other argument, but is cancelled or denied by the `Contra-expectation` argument. `CONCESSION` is used when an expected causal relation is cancelled or denied by the situation described in one of the arguments. At the same time, concession is related to CONTRAST in that it highlights a difference between utterance and anchor where expectations raised by one argument are then denied by the other. The connective indicates that one of the arguments describes a situation A which causes C, while the other asserts (or implies) ¬C. Alternatively, one argument denotes a fact that triggers a set of potential consequences, while the other denies one or more of them. (cf. Bunt & Prasad 2016, Prasad et al. 2007, p.32,34; Webber et al. 2019a, p.24) Diagnostic discourse markers (either at `Expectation-raiser` or `Contra-expectation`) are _although_ or _even though_, a diagnostic discourse marker at Contra-expectation is _however_.

> Note that concessive connectives can also be used in a rhetorical or pragmatic way where their semantic conditions do not hold. Such cases of "apparent Concession" are included under `CONCESSION`, as well, but MUST be documented in comments (cf. Prasad et al. 2007, p. 27). This includes cases in which the speech act associated with the `Expectation-raiser` is cancelled or denied by the `Contra-expectation` or its speech act. So far, this has only be observed for `Contra-expectation`, see there for examples (PDTB3 Comparison.Concession+SpeechAct, Webber et al. 2019a, p. 24).

Following PDTB2, CONCESSION relations are under ADVERSATIVITY (PDTB2 COMPARISON).

> Notes: cf. SDRT (DISCOR, ANNODIS) Contrast

##### Concession.expectation-raiser (`Expectation-raiser`)

The utterance creates an expectation (a situation that is expected to cause the situation described in the other argument) that is cancelled or denied by the anchor. (cf. Bunt & Prasad 2016; PDTB "expectation", Prasad et al. 2007, p.34) A diagnostic discourse marker is _although_ (Webber et al. 2019a, p.23-24)

- (119) **Although** the purchasing managers’ index continues to indicate a slowing economy, it isn’t signaling an imminent recession, said Robert Bretz, chairman of the association’s survey committee and director of materials management at Pitney Bowes Inc., Stamford, Conn. (PDTB2, 0036; INTRASENTENTIAL)

- (104) The documents also said that **although** the 64-year-old Mr. Cray has been working on the project for more than six years, the Cray-3 machine is at least another year away from a fully operational prototype. (PDTB3, wsj 0018; INTRASENTENTIAL)

- (105) It’s as if investors, the past few days, are betting that something is going to go wrong – **even if** they don’t know what. (PDTB3, wsj 0359; INTRASENTENTIAL)

- (106) **[Implicit=although]** Barely visible on Hong Kong’s property scene in 1985, by last year Japan had become the top foreign investor. (PDTB3, wsj 0524; INTRASENTENTIAL)

> Notes:
> - cf. RST ?Concession
> - cf. RSTDTB ?Concession, ?Antithesis, ?Preference
> - cf. PDTB2 Expectation, PDTB3 Concession/arg1-as-denier

##### Concession.contra-expectation (`Contra-expectation`)

The utterance cancels or denies a situation that is expected after processing the anchor. This corresponds to the "Expecation-denier" role in Bunt & Prasad (2016), clif. Prasad et al. (2007, p.34) A diagnostic discourse marker of contra-expectation is _however_. Note that _but_, taken as diagnostic discourse marker of `CONTRAST` is usually also applicable to `CONCESSION`. Annotate `CONCESSION` for cases in which `however` can be used in place of `but`.

- (120) The Texas oilman has acquired a 26.2% stake valued at more than $1.2 billion in an automotive-lighting company, Koito Manufacturing Co. **But** he has failed to gain any influence at the company. (PDTB2, 0082)

- (107) Last Friday, 96 stocks on the Big Board hit new 12-month lows. **But** by Mr. Granville’s count, 493 issues were within one point of such lows. (PDTB3, wsj 0359)

- (109) American Brands “just had a different approach,” Mr. Wathen says. **[Implicit=however]** “Their approach didn’t work.” (PDTB3, wsj 0305)

`Contra-expectation` also applies to cases in which concessive connectives are used in a rhetorical or pragmatic way where their semantic conditions do not hold (cf. Prasad et al. 2007, p. 27). Such cases of "apparent Concession" MUST be documented in comments. This includes cases in which the speech act associated with the anchor is cancelled or denied by the utterance or its speech act (PDTB3 Comparison.Concession+SpeechAct, Webber et al. 2019a, p. 24-25):

- (110) Congress closed this loophole last year, **or** thought it did. (PDTB3, wsj 1574; INTRASENTENTIAL)

This can be paraphrased as follows, with its implicit SAs made explicit: _While (Although) I say Congress closed this loophole last year, it might be more accurate to say Congress thought it closed this loophope last year_.

- (111) He lived in Peking, **or** should I say Beijing, for 20 years. (Webber et al. 2019a, p. 25; INTRASENTENTIAL)

Here, the anchor speech act is explicit, although the utterance speech act (the one that is denied) is (as required) implicit. It can be paraphrased as _While (Although) I say He lived in Peking, it might be more accurate to say he lived in Beijing_.

> Notes:
> - cf. RST ?Concession
> - cf. RSTDTB ?Concession, ?Antithesis, ?Preference
> - cf. PDTB2 Contra-Expectation, PDTB3 Concession/arg2-as-denier

##### Concession.concession (`Concession`)

Instances which are ambiguous between “expectation” and “contra-expectation”, where the context or the annotators’ world knowledge is not sufficient to specify the subtype are tagged as `CONCESSION` (Prasad et al. 2007, p.34)

- (121) Besides, to a large extent, Mr. Jones may already be getting what he wants out of the team, **even though** it keeps losing. (PDTB2, 1411)

### Contrast (`Contrast`)

`CONTRAST` is a symmetric relation in which one or more differences between the internal argument and the external argument are highlighted with respect to what each predicates as a whole or to some entities they mention. Semantically, the truth of both arguments is independent of the connective or the established relation (Bunt & Prasad 2016, Prasad et al. 2007, p.32). In `CONTRAST`, the utterance and the anchor share a predicate or property and a difference is highlighted with respect to the values assigned to the shared property. However, neither argument describes a situation that is asserted on the basis of the other one, and thus, there is no directionality in the interpretation of the arguments. This is the main difference in comparison with the otherwise similar `CONCESSION` relation. (PDTB2 Contrast, Prasad et al. 2007, p.32) A diagnostic discourse marker for contrast is _but_.

This includes cases in which the connective indicates that the values assigned to some shared property are taken to be alternatives ("juxtaposition", Prasad et al. 2007, p.32-33).

- (116) Operating revenue rose 69% to A$8.48 billion from A$5.01 billion. **But** the net interest bill jumped 85% to A$686.7 million from A$371.1 million. (PDTB2 1449)

- (113) After all, gold prices usually soar when inflation is high. Utility stocks, **on the other hand**, thrive on disinflation ... (PDTB3, wsj 0359)

- (114) Mr. Edelman said the decision ”has nothing to do with Marty Ackerman.” **[implicit=on the contrary]** Mr. Ackerman contended that it was a direct response to his efforts to gain control of Datapoint. (PDTB3, wsj 0333)

- (2) The Manhattan U.S. attorney’s office stressed criminal cases from 1980 to 1987, averaging 43 for every 100,000 adults. **But** the New Jersey U.S. attorney averaged 16. (Prasad et al. 2017, p.8)

This also includes cases in which the connective indicates that the values assigned to some shared property are the extremes of a gradable scale, e.g., _tall-short_, _accept-reject_, etc. ("opposition", Prasad et al. 2007, p.33)

- (117) Most bond prices fell on concerns about this week’s new supply and disappointment that stock prices didn’t stage a sharp decline. Junk bond prices moved higher, **however**. (PDTB2, 1464)

Note that explicit discourse markers can also be used to underline a `CONTRAST` relation that does not hold between utterance and anchor, but between one of the arguments and an inference that can be drawn from the other, in many cases at the speech act level ("pragmatic contrast", Prasad et al. 2007, p.33)

- (118) “It’s just sort of a one-upsmanship thing with some people,” added Larry Shapiro. “They like to talk about having the new Red Rock Terrace one of Diamond Creek’s Cabernets or the Dunn 1985 Cabernet, or the Petrus. Producers have seen this market opening up and they’re now creating wines that appeal to these people.” That explains why the number of these wines is expanding so rapidly. **But** consumers who buy at this level are also more knowledgeable than they were a few years ago. (PDTB2, 0071)

In accordance with PDTB2, CONTRAST falls under ADVERSATIVITY (PDTB2 COMPARISON).

> Notes:
> - cf. RST Contrast
> - cf. RSTDTB Comparison
> - cf. SDRT (DISCOR, ANNODIS) Contrast
> - cf. PDTB Justaposition, Opposition

Note that is has been observed that annotators face difficulties to distinguish CONCESSION and CONTRAST. As a diagnostic test, check by paraphrasing with _although_, whether a causal relation that is expected on the basis of one argument is denied by the other. If this is possible, annotate CONCESSION, if not, annotate CONTRAST (Webber et al. 2019a, p.23-24).

### CONTINGENCY

#### Causal

In a `CAUSAL` relation, the `Reason` provides a reason, explanation or justification for the `Result` to come about or occur, but not in a conditional relation. (cf. ISO 24617-8 CAUSE, Bunt & Prasad 2016; Webber et al. 2019a, p.19)
- subset of PDTB CONTINGENCY

##### Causal.reason (`Reason`)

The situation described in the utterance is the reason (cause, explanation or justification) for the situation described in the anchor, as typically expressed with the connective _because_ (cf. PDTB2 Reason, Prasad et al. 2007, p.26, 29; Webber et al. 2019a, p.19)

- (2) But a strong level of investor withdrawal is much more unlikely this time around, fund managers said.	**A major reason is that** investors already have sharply scaled back their purchases of stock funds since Black Monday. (Prasad and Bunt 2015, (2))

- (3) Some have raised their cash positions to record levels. **[Implicit Because]** High cash positions help buffer a fund when the market falls. (Prasad and Bunt 2015, (3))

- (x) P1: I can never find my remote control.	P2: That’s **because** they don’t have a fixed place. (Bunt and Prasad 2016)

Note that in the last example, we do not annotate `Dialog` because an overt discourse markers indicates a higher-ranking discourse relation.

- (69) But service on the line is expected to resume by noon today. **[Implicit=since]** “We had no serious damage on the railroad,” said a Southern Pacific spokesman. (PDTB3, wsj 1803)

- (70) By 11:59 p.m. tonight, President Bush must order $16 billion of automatic, across-the-board cuts in government spending to comply with the Gramm-Rudman budget law. **The cuts are necessary because** Congress and the administration have failed to reach agreement on a deficit-cutting bill. (PDTB3, wsj 2384)

- (4) When the plant was destroyed, ”I think everyone got concerned that the same thing would happen at our plant,” a KerrMcGee spokeswoman said. **That prompted** Kerr-McGee to consider moving the potentially volatile storage facilities and cross-blending operations away from town. (Prasad et al. 2017, p.8)

- (12) Although bullish dollar sentiment has fizzled, many currency analysts say a massive sell-off probably won’t occur in the near future. **[Implicit, because]** While Wall Street’s tough times and lower U.S. interest rates continue to undermine the dollar, weakness in the pound and the yen is expected to offset those factors. ”By default,” the dollar probably will be able to hold up pretty well in coming days, says Francoise Soares-Kemp, a foreign-exchange adviser at Credit Suisse. ”We’re close to the bottom” of the near-term ranges, she contends. (Prasad et al. 2017, p.12)

Note that `Reason` also includes epistemic, rhetorical or pragmatic uses of causal connectives, e.g., where the utterance provides justification for a claim expressed in the anchor, as marked, for example, with the connective _because_. Ex. (104) illustrates such a case  Here, there is no causal influence between the two situations (PDTB2 Justification/Pragmatic Cause, Prasad et al. 2007, p.29; PDTB3 CONTINGENCY/Cause+Belief/reason, Webber et al. 2019a, p.20).
				
- (104) Mrs Yeargin is lying. **[Implicit = because]** They found students in an advanced class a year earlier who said she gave them similar help. (PDTB2, 0044)

- (x) Sears is negotiating to refinance its Sears Tower for close to $850 million, sources said. **[Implicit = because]** The retailer was unable to find a buyer for the building. (Prasad and Bunt 2015)

- (77) The nations of southern Africa know a lot about managing elephants; **[Implicit=as]** their herds are thriving. (PDTB3, wsj 2047)

- (78) And until last Friday, it seemed those efforts were starting to pay off. **[Implicit=because]** “Some of those folks were coming back,” says Leslie Quick Jr., chairman, of discount brokers Quick & Reilly Group Inc. (PDTB3, wsj 1866)

Likewise, `Reason` is also used when the utterance provides a reason for the speaker uttering the speech act represented by the anchor. The speech act is implicit (PDTB3 Contingency.Cause+SpeechAct.Reason, Webber et al. 2019a, p.21)

- (81) “Maybe I’m a little stuffy, **but** I wouldn’t sell them,” sniffs Bob Machon, owner of Papa’s Sports Cards in Menlo Park, California. (PDTB3, wsj 1560, INTRASENTENTIAL)

> Notes:
> - cf. RST Vol. cause, Non-vol. cause, Evidence, Justify
> - cf. RSTDTB Cause, Evidence, Explanation-argumentation, Reason
> - cf. SDRT Explanation (DISCOR Explanation, ANNODIS Explanation)

##### Causal.result (`Result`)

The situation described in the utterance is interpreted as the result (effect) of the situation presented in the anchor. A typical discourse marker is “as a result”. (cf. PDTB Result, Prasad et al. 2007, p.26,29; Webber et al. 2019a, p.20)

- (72) Now, though, enormous costs for earthquake relief will pile on top of outstanding costs for hurricane relief. “**That obviously means that** we won’t have enough for all of the emergencies that are now facing us, and we will have to consider appropriate requests for follow-on funding,” Mr. Fitzwater said. (PDTB3, wsj 1824; Prasad and Bunt 2015)

- (73) “We are going to explode lower,” says the flamboyant market seer, . . . **[Implicit=so]** Anyone telling you to buy stocks in this market is technically irresponsible. (PDTB3, wsj 0359)

`result` also applies for episthemic uses of causal markers, when the anchor gives the evidence justifying the claim given in the utterance (PDTB3 Contingency.Cause+Belief.Result, Webber et al. 2019a, p.21)

- (80) There were no {sell} lists and the calendar is lightening up a bit. **[Implicit=so]** There’s light at the end of the tunnel for municipalities. (PDTB3, wsj 0351)

Likewise, `Result` is to be used when the anchor is the reason for the speaker to produce the (speech act represented by the) utterance. (PDTB3 Contingency.Cause+SpeechAct.Result, Webber et al. 2019a, p.21)

- (83) Surviving scandal has become a rite of political passage at a time when a glut of scandal has blunted this town’s sensibility. **[implicit=so]** Let the president demand strict new ethics rules. (PDTB3, wsj 0909)

> Notes:
> - cf. RST Vol. result, Non-vol. result
> - cf. RSTDTB Consequence, Result
> - cf. SDRT Result (DISCOR Result, ANNODIS Result)
> - PDTB3 introduced Cause/negative-result for intrasentential relations, specifically for the English construction _too X to Y_ (Webber et al. 2019a, p.18,20). This does not seem to be relevant for intersentential relations. 

##### Causal.cause (`Cause`)

For causal relations between utterance and anchor, annotators should normally apply `Reason` or `Result`. When `Cause` is used in annotation, it means that the annotators could not uniquely specify the directionality, but that they found the causal association with the anchor to be the primary discourse relation for the utterance at hand. (cf. Prasad et al. 2007, p.28)

#### Conditional 

A `CONDITIONAL` relation relates a hypothetical (unrealized) scenario with its (possible) consequence. The consequence is a situation that holds when the condition is true. This involves causal influence, but unlike `CAUSAL` relations, the truth value of the arguments of a `CONDITIONAL` relation cannot be determined independently of the connective. (PDTB Condition, Prasad et al. 2007, p.26,29; SemAF CONDITION).

##### Conditional.condition (`Condition`)

The utterance represents a `Condition`, i.e., an unrealized situation which, when realized, would lead to the `Consequence` described in the anchor. If the utterance holds true, the anchor is caused to hold true at some instant in all possible futures. This can be a generic truth about the world (PDTB Condition/generic), a statement that describes a regular outcome every time the condition holds true (PDTB Condition/generic) or a single time that this is the case (PDTB Condition/general). Following ISO 24617-8, this is independent of whether the `Consequence` is believed to be true (PDTB Condition/factual present, Condition/factual past) or not (counterfactuals, PDTB Condition/unreal present, PDTB Condition/unreal past). If the condition is not true, the anchor should express what the consequences would had been if it had. Note that it is possible that the anchor can be true in the future independently of the utterance. (PDTB Condition, Prasad et al. 2007, p.30-31; Bunt & Prasad 2016, SemAF: Condition/Antecedent)

- (108') "Orange County is taking in at least $4 billion nationwide by boiler rooms every year", Mr. McClelland says. "**Because** I've heard that there is $40 billion in total, and that's 10%." (reformulated after PDTB2, 1568, cf. 108)

`Condition` also includes rhetorical or pragmatic uses of conditional constructions whose interpretation deviates from the standard semantics described above. Specifically, these are cases of explicit _if_ tokens although utterance and anchor are not causally related, but presented as if they were. In all cases, the anchor holds true independently of the anchor, there is no causal relation between the two arguments. We distinguish two primary cases:

- _relevant context information_: The utterance provides the context in which the description of the situation in anchor is relevant. A frequently cited example for this type of conditional is (113). Note that this is an intrasentential relation in this case and not to be annotated in AURIS.

	- (113) If you are thirsty, there’s beer in the fridge. (constructed, INTRASENTENTIAL)

- _implicit assertion_: refers to a special use of if-constructions when the conditional involves an (implicit) assertion. In (115), the utterance ("O’ Connor is your man") is not a consequent state that will result if the condition expressed in the anchor holds true. Instead, the discourse marker _if_ in this case implicitly asserts that O’Connor will keep the crime rates high. Again, note that this is an intrasentential example. To be replaced by an intersentential relation. 

	- (115) In 1966, on route to a re-election rout of Democrat Frank O’Connor, GOP Gov. Nelson Rockefeller of New York appeared in person saying, “**If** you want to keep the crime rates high, O’Connor is your man.” (PDTB2, 0041)

> Notes:
> - cf. PDTB Condition/hypothetical, Condition/general, Condition/unreal present, Condition/factual present.
> - cf. RST Condition
> - cf. RSTDTB Condition, ?Hypothetical
> - cf. ANNODIS ?Conditional

##### Conditional.consequence (`Consequence`)

The anchor represents a `Condition`, i.e., an unrealized situation which, when realized, would lead to the `Consequence` described in the utterance. As for the logical relation between `Condition` and `Consquence`, the same conditions hold as described above (cf. Bunt & Prasad 2016, SemAF: Condition/Consequent).

- (108) “I’ve heard that there is $40 billion taken in nationwide by boiler rooms every year,” Mr. McClelland says. “**If that’s true**, Orange County has to be at least 10% of that.” (PDTB2, 1568)

The example shows an alternative lexicalization. A possible discourse marker would have been _So,_. 

> Notes:
> - ?cf. RSTDTB Contingency
> - cf. SDRT Consequence (DISCOR Consequence)

#### Negative Condition

In a `NEGATIVE_CONDITION` relation, the `Negated_Condition` is an unrealized situation which, if it does **not** occur, would lead to the `Consequent` (Bunt & Prasad 2016; Webber et al. 2019a, p.23)

> **Note**: In PDTB2, _unless_ would normally be annotated as EXPANSION/Alternative/disjunctive, but Bund and Prasad (2016) explicitly link it with PDTB2 Condition, instead. PDTB3 introduced CONTINGENCY/Negative Condition for intrasentential relations (Webber et al. 2019a, p.18)

##### Negative Condition.condition (`Neg_Condition`)

The utterance describes an unrealized situation which, when not realized, leads to the `Consequence` described in the anchor. A diagnostic discourse marker is _unless_.

- (100) But a Soviet bank here would be crippled **unless** Moscow found a way to settle the $188 million debt, which was lent to the country’s short-lived democratic Kerensky government before the Communists seized power in 1917. (Webber et al. 2019a, p.23, INTRASENTENTIAL)

- (101) **Unless** the Federal Reserve eases interest rates soon to stimulate the economy, profits could remain disappointing. (PDTB3, wsj 0322, INTRASENTENTIAL)

- (102) Sandoz said it expects a ”substantial increase” in consolidated profit for the full year, **barring** major currency rate change. (PDTB3, wsj 2089, INTRASENTENTIAL)

This also includes episthemic uses of conditional discourse markers, esp., when the consequent is an implicit speech act. However, there have been no annotations of this kind found in PDTB3 (PDTB3 Contingency.Negative-condition+SpeechAct in Webber et al. 2019a, p.23).

- (103) **Unless** you’re on a diet, there are some cookies in the cupboard. (Webber et al. 2019a, p.23)

> Notes:
> - cf. ANNODIS ?Conditional
> - cf. PDTB2 Condition

##### Negative Condition.consequence (`Neg_Consequence`)

The anchor describes an unrealized situation which, when not realized, leads to the `Neg_Consequence` described in the utterace. A diagnostic discourse marker is _otherwise_. (SemAF Consequence)

- (98) The National Institutes of Health policy would require researchers to cut financial ties with health-care businesses **or** lose their government money. (PDTB3, wsj 0975, INTRASENTENTIAL)

- (99) This will prevent a slide in industrial production, which will **otherwise** cause new panic buying. (PDTB3, wsj 1646, INTRASENTENTIAL)

> Notes:
> - cf. ?RST Otherwise
> - cf. ?RSTDTB Otherwise
> - cf. SDRT Consequence (DISCOR Consequence)

#### Purpose

In a `PURPOSE` relation, the `Goal` enables the `Enablement`, i.e., one utterance presents an action that an AGENT undertakes with the purpose of the GOAL conveyed by the other utterance being achieved. Usually (but not always), the agent undertaking the action is the same agent aiming to achieve the goal (Bunt & Prasad 2016; Webber et al. 2019a, p.21). This relation is similar to `CAUSAL` and `CONDITION` relations, the main difference is that the former are neutral with respect to individual engagement whereas `PURPOSE` relations presume some level of agency on behalf of the speaker, the hearer or another agent addressed or involved in the situation described. PURPOSE requires a volitional agent, a diagnostic marker for the `Goal` role is _in order to_, a diagnostic marker for the `Enablement` is _therefore_ (Webber et al. 2019b).

> **Note**: There is no clear PDTB2 counterpart. PDTB2 doesn't seem to have _in order to_, but _so that_ is annotated (2/2) as PDTB2 result. So, it seems safe to group this together with other PDTB CONTINGENCY relations.

> **Note**: PDTB3 introduced Purpose for intrasentential relations (Webber et al. 2019a, p.18)

> **Note**: **TODO** check RST/RSTDTB Purpose. 

> Notes: cf. RST ?Purpose, RSTDTB ?Purpose

##### Purpose.goal (`Goal`)

The utterance represents a goal (purpose) enabled by the situation described in the anchor, i.e., the action undertaken to achieve the goal (PDTB3 Contingency.Purpose.Arg2-as-goal. Webber et al. 2019a, p.21). All PDTB3 examples are intrasentential. This is possibly not relevant for AURIS.

- (86) Skilled ringers use their wrists to advance or retard the next swing, so that one bell can swap places with another in the following change. (PDTB3, wsj 0089)

- (87) In September, the company said it was seeking offers for its five radio stations in order to concentrate on its programming business. (PDTB3, wsj 0115)

> Notes:
> - cf. SDRT Explanation (DISCOR Explanation, ANNODIS Goal)
> - cf. PDTB2 Result
> - cf. PDTB3 CONTINGENCY.Purpose.Arg2-as-Goal

##### Purpose.enablement (`Enablement`)

The utterance describes a situation that enables the goal (purpose) described in the anchor, i.e., the action undertaken to achieve the goal (PDTB3 Contingency.Purpose.Arg1-as-goal. Webber et al. 2019a, p.21). All PDTB3 examples are intrasentential. This is possibly not relevant for AURIS.

> Note: cf. PDTB3 CONTINGENCY.Purpose.Arg1-as-Goal

- (84) There are the strict monetarists, who believe that floating exchange rates free an economy to stabilize its price level **by** stabilizing the monetary aggregate. (PDTB3, wsj 0553, INTRASENTENTIAL)

- (85) She ordered the foyer done in a different plaid planting, and **[Implicit=for that purpose]** made the landscape architects study a book on tartans. (PDTB3, wsj 0984, INTRASENTENTIAL)

### EXPANSION

#### Conjunction (`Conjunction`)

`CONJUNCTION` is a symmetric relation in which the internal and the external arguments bear the same relation to some other situation evoked in the discourse. Their conjunction indicates that they are doing the same thing with respect to that situation, or are doing it together (Bunt & Prasad 2016). The situation described in the utterance provides additional, discourse new, information that is related to the situation described in the anchor, but is not related to the anchor in any other, more specific discourse relation. The semantics are thus no more than that of a logical ∧ (and). Diagnostic connectives are _also_, _in addition_, _additionally_, _further_, etc. ("conjunction", Prasad et al. 2007, p.37; Webber et al. 2019a, p.25-26):

	- (134) Food prices are expected to be unchanged, but energy costs jumped as much as 4%, said Gary Ciminero, economist at Fleet/Norstar Financial Group. He **also** says he thinks “core inflation,” which excludes the volatile food and energy prices, was strong last month. (PDTB2 2400)

	- (118) I can adjust the amount of insurance I want against the amount going into investment; **[Implicit=Conjunction]** I can pay more or less than the so-called target premium in a given year. (PDTB3, wsj 0041)

- Bunt and Prasad (2016) and Webber et al. (2019a, p.18) also group this together with PDTB2 List: "Arg1 and Arg2 are members of a list, defined in the prior discourse. “List” does not require the situations specified in Arg1 and Arg2 to be directly related" (Prasad et al. 2007, p.37). 
			
	- (135) But other than the fact that besuboru is played with a ball and a bat, it’s unrecognizable: Fans politely return foul balls to stadium ushers; **[Implicit = and]** the strike zone expands depending on the size of the hitter; (PDTB2, 0037)

> Notes: 
> - cf. RST Joint
> - cf. RSTDTB List
> - cf. SDRT (DISCOR, ANNODIS) Continuation
> - cf. PDTB Conjunction, List

- Note: because of the largely underspecified semantics, this must be annotated after any more specific relation has been tested for. It is thus put unter EXPANSION, in accordance with the PDTB2 linking postulated by Bunt and Prasad (2016)

#### Disjunction (`Disjunction`)

`DISJUNCTION` is a symmetric relation in which the utterance and the anchor denote alternative situations (Bunt & Prasad 2016; Prasad et al. 2007, p.36). Following ISO 24617-8, we do not distinguish as to whether both situations can hold simultaneously (logical or) or they are mutually exclusive (exclusive or). A diagnostic discourse marker is _or_:

- (130) Today’s Fidelity ad goes a step further, encouraging investors to stay in the market **or** even to plunge in with Fidelity. (both alternatives [can] hold, PDTB2 conjunctive, 2201)

- (131) Those looking for real-estate bargains in distressed metropolitan areas should lock in leases or buy now. (only one alternative holds, exclusie or, PDTB2 disjunctive, 2444)

`Disjunction` is used when utterance and anchor bear the same relation to some other situation evoked in the discourse, making a similar contribution with respect to that third situation. While utterance and anchor also relate to each other as alternatives (with one or both holding), they also both relate in the same way to this other situation (Webber et al. 2019a, p.26):

- (120) If we want to support students, we might adopt the idea used in other countries of offering more scholarships
based on something called ”scholarship,” rather than on the government’s idea of ”service.” Or we might
provide a tax credit for working students. **[CONTEXT:]** If we want to support students, we might adopt the idea used in other countries of offering more scholarships based on something called “scholarship,” rather than on the government’s idea of “service.”. (PDTB3, wsj 2407)

> Notes:
> - cf. RST Joint
> - cf. RSTDTB Disjunction
> - cf. SDRT (DISCOR, ANNODIS) Alternation
> - cf. PDTB Disjunctive, Conjunctive
> - following Bunt and Prasad (2016), this is put under EXPANSION

#### Restatememt (`Restatement`)

`RESTATEMENT` is a symmetric relation in which the utterance describes the same situation as the anchor, but from different perspectives, e.g., when describing the same situation as presented before using the speaker’s own words. (Bunt & Prasad 2016; PDTB2 Restatement/equivalence, Prasad et al. 2007, p.35-36, Webber et al. 2019a, p.26). A diagnostic discourse marker is _in other words_.

- (126) Chairman Krebs says the California pension fund is getting a bargain price that wouldn’t have been offered to others. **In other words**: The real estate has a higher value than the pending deal suggests. (PDTB2, 0331)

- (129) He said the assets to be sold would be “non-insurance” assets, including a beer company and a real estate firm, and wouldn’t include any pieces of Farmers. **[Implicit = in other words]** “We won’t put any burden on Farmers,” he said. (PDTB2, 2403)

- (123) But the battle is more than Justin bargained for. **[implicit=indeed]** ”I had no idea I was getting in so deep,” says Mr. Kaye, who founded Justin in 1982. (PDTB3, wsj 2418)

- (y) When the consumer had no more money and remembered the policy, he would learn at the company’s headquarters about the so-called policy surrender value coefficient. **In other words,** he did not receive what he had paid. (Żurowski et al. 2023, p.486)

> Notes:
> - Following Bunt and Prasad (2016), this is put under EXPANSION
> - cf. RST Restatement
> - cf. RSTDTB Summary
> - cf. SDRT (DISCOR, ANNODIS) Elaboration
> - cf. PDTB2 Restatement.equivalence, PDTB3 Equivalence

#### Exception

In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't. (Bunt & Prasad 2016; Webber et al. 2019a, p.27)
	
> Note: Intutitively, this involves an element of contrast, but we follow PDTB2 in considering it a form of PDTB EXPANSION.

##### Exception.regular (`Regular`)

In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't (Bunt & Prasad 2016). Not clear whether this situation exists in AURIS, as it requires a discourse marker to mark the regular rather than the exception. It could exist in cases in which paired discourse markers (like _either ... or_ or _on the one hand ... on the other hand_) mark `EXCEPTION` relations.

- (124) Twenty-five years ago the poet Richard Wilbur modernized this 17th-century comedy merely by avoiding ”the zounds sort of thing,” as he wrote in his introduction. **Otherwise**, the scene remained Celimene’s house in 1666. (PDTB3, wsj 0936)

> Note: PDTB3 Exception.Arg1-as-excpt

##### Exception.exception (`Exception`)

The utterances specifies an exception to the generalization specified by the anchor. In other words, the situation described in the anchor is false because the sitation described in the utterance is true (but if the utterance were false, the anchor would be true). (Prasad et al. 2007, p.36) According to PDTB2, possible discourse markers are _instead_ or _rather_ -- both of these are, however, more regularly used with other discourse relations, so that they are not diagnostic discourse markers.
		
- (133) Boston Co. officials declined to comment on Moody’s action on the unit’s financial performance this year **except** to deny a published report that outside accountants had discovered evidence of significant accounting errors in the first three quarters’ results. (PDTB2, 1103, INTRASENTENTIAL)

> Note: cf. PDTB2 Exception, PDTB3 Exception.Arg2-as-excpt

#### Exemplification

In an `EXEMPLICATION` relation, the `Set` describes a set of situations; the `Instance` is an element of that set (Bunt & Prasad 2016).

##### Exemplification.set (`Set`)

The utterance describes a situation as holding in a set of circumstances, while the anchor describes one or more of those circumstances (Webber et al. 2019a, p.27). Diagnostic discourse markers include _generally_ or _in general_:

- (129) Swiveling in his chair, Mr. Straszheim replies that the new outlook, though still weak, doesn’t justify calling a recession right now. “It’s all in this handout you don’t want to look at. We could still have a recession” at some point. **[Implicit=generally]** One of Mr. Straszheim’s recurring themes is that the state of the economy isn’t a simple black or white. (PDTB3, wsj 0569)

- (8) NBC’s re-creations are produced by Cosgrove-Meurer Productions, which also makes the successful primetime NBC Entertainment series Unsolved Mysteries. **[Implicit: More generally]** The marriage of news and theater, if not exactly in evitable, has been consummated nonetheless. (Prasad et al. 2017, p. 11)

> Note: PDTB3 Instantiation.Arg1-as-instance

##### Exemplification.instance (`Instance`)

The utterance provides one or more instances of the circumstances described by the anchor. The anchor evokes a set and the utterance describes it in further detail. It may be a set of events, a set of reasons, or a generic set of events, behaviors, attitudes, etc. Diagnostic discourse markes are _for example_, _for instance_ and _specifically_ (PDTB2 Instantiation, Prasad et al. 2007, p.34; PDTB3 Instantiation.Arg2-as-instance, Webber et al. 2019a, p.27)

- (122) He says he spent $300 million on his art business this year. **[Implicit = in particular]** A week ago, his gallery racked up a $23 million tab at a Sotheby’s auction in New York buying seven works, including a Picasso. (PDTB2, 0800)

- (130) The computers were crude by today’s standards. Apple II owners, for example, had to use their television sets as screens and stored data on audiocassettes. (PDTB3, wsj 0022)

- (131) And regional offices were “egregiously overstaffed,” he claims. **[Implicit=for example]** One office had 19 people doing the work of three, ... (PDTB3, wsj 0305)

- (3) So far, the mega-issues are a hit with investors. **[Implicit, For example]** Earlier this year, Tata Iron & Steel Co.’s offer of $355 million of convertible debentures was oversubscribed. (Prasad et al. 2017, p.8)

> Notes:
> - cf. RST Elaboration (set-member)
> - cf. RSTDTB Elaboration set-member, Example
> - cf. SDRT (DISCOR, ANNODIS) Elaboration
> - cf. PDTB2 Instantiation, PDTB3 Instantiation.Arg2-as-Instance
> - Following Bunt and Prasad (2016), this is put under EXPANSION

#### Elaboration

In an `ELABORATION` relation, both arguments are the same situation, but in less or more detail (Bunt & Prasad 2016; PDTB3 Level-of-Detail in Webber et al. 2019a, p.27). 

##### Elaboration.broad (`Broad`)

The utterance describes the same situation as the anchor, but the anchor provides more detail. Typically, the utterance summarizes the anchor, or in some cases expresses a conclusion or generalization based on the anchor. Diagnostic discourse markers include _in sum_, _overall_, _finally_, etc. (Bunt & Prasad 2016; PDTB2 Restatement/generalization in Prasad et al. 2007, p.35)
		
- (125) If the contract is as successful as some expect, it may do much to restore confidence in futures trading in Hong Kong. **[Implicit = in other words,]]** “The contract is definitely important to the exchange,” says Robert Gilmore, executive director of the Securities and Futures Commission. (PDTB2, 0700)

- (132) Many modern scriptwriters seem to be incapable of writing drama, or anything else, without foul-mouthed cursing. Sex and violence are routinely included even when they are irrelevant to the script, and high-tech special effects are continually substituted for good plot and character development. **In short**, we have a movie and television industry that is either incapable or petrified of making a movie unless it carries a PG-13 or R rating. (PDTB3, wsj 0911)

> Note: cf. PDTB2 Generalization, PDTB3 Level-of-Detail/arg1-as-detail

##### Elaboration.specific (`Specific`)

The utterance describes the situation described in the anchor in more detail. Diagnostic discourse markers include _specifically_, _indeed_ and _in fact_." (PDTB Restatement/specification, Prasad et al. 2007, p.35)
		
- (123) A Lorillard spokewoman said, “This is an old story. **[Implicit = in fact]** We’re talking about years ago before anyone heard of asbestos having any questionable properties.” (PDTB2, 0003)
		
- (124) An enormous turtle has succeeded where the government has failed: **[Implicit = specifically]** He has made speaking Filipino respectable. (PDTB2, 0804)

- (14) The Treasury Department said the U.S. trade deficit may worsen next year, after two years of significant improvement. **[Implicit=Specifically]** In its report to Congress on international economic policies, the Treasury said that any improvement in the broadest measure of trade, known as the current account, ”is likely at best to be very modest,” and ”the possibility of deterioration in the current account next year cannot be excluded.” (Prasad et al. 2017, p. 12)

> Notes:
> - cf. RST Elaboration
> - cf. RSTDTB Conclusion, Elaboration general-specific, Elaboration whole-part, Elaboration process-step
> - cf. SDRT (DISCOR, ANNODIS) Elaboration
> - cf. PDTB2 Specification, PDTB3 Level-of-Detail/arg2-as-detail

#### Manner

In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs (Bunt & Prasad 2016). Manner answers “how” questions such as “How were the children playing?” (Webber et al. 2019a, p.28).

> Note: While Manner may be the only relation that holds between two arguments, it is often the case that another sense (Purpose, Result or Condition) is taken to hold as well (Webber et al. 2019a, p.28). As PDTB3 introduced Manner specifically for intrasentential relations, it is yet to be confirmed whether this is a relevant category for AURIS.

> Notes: 
> - cf. SDRT (ANNODIS, DISCOR) Elaboration
> - Missing from PDTB2, and not clear what a diagnostic discourse marker could be. PDTB2 has _similarly_ as a signal of Conjunction. In that view, MANNER would fall under PDTB EXPANSION relations
> - cf. PDTB3 EXPANSION/Manner relation, introduced for intrasentential relations in PDTB3 (Webber et al. 2019a, p.18) 

##### Manner.means (`Means`)

The utterance describes the means, i.a. a way in which the achievement presented in the anchor comes about or occurs (Bunt & Prasad 2016). For intrasentential manner relations, a diagnostic discourse marker is _by_, a diagnostic paraphrase is _the manner of/in which/by which_ (Webber et al. 2019a, p.29-30).

- (137) Taking a cue from California, more politicians will launch their campaigns **by** backing initiatives, says David Magleby of Brigham Young University. (PDTB3, wsj 0120, INTRASENTENTIAL)

Here, the utterance (_backing inititatives_) answers the question _How are politicians launching their campaigns?_.

- (138) In China, a great number of workers are engaged in pulling out the male organs of rice plants **[Implicit=by]** using tweezers. (PDTB3, wsj 0209, INTRASENTENTIAL)

Here, the utterance (_using tweezers_) answers the question _How are workers pulling out the male organs of rice plants?_.

> Notes: 
> - cf. RSTDTB Means, ?Manner
> - PDTB3 Manner.Arg2-as-Manner

##### Manner.achievement (`Achievement`)

In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs (Bunt & Prasad 2016). A diagnostic discourse marker is _thereby_.

- (135) McCaw is offering $125 a share for 22 million LIN shares, **thereby** challenging LIN’s proposal to spin off its television properties, pay shareholders a $20-a-share special dividend and combine its cellular-telephone operations with BellSouth’s cellular business. (PDTB3, wsj 2443, INTRASENTENTIAL)

Here, the anchor answers the question _How did McCaw challenge LIN’s proposal?_

- (136) Long-debated proposals to simplify the more than 150 civil penalties **[Implicit=thereby]** and make them fairer and easier to administer are in the House tax bill. (PDTB3, wsj 0293)

Here, the anchor answers the question _How do the proposals make civil penalties fairer and easier to administer?_

> Note: PDTB3 Manner.Arg1-as-Manner

#### Substitution

In `SUBSTITUTION`, two mutually exclusive alternatives are evoked in the discourse but only one is taken, the other is ruled out. A diagnostic discourse marker is the connective _instead_ (PDTB2 chosen alternative, Prasad et al. 2007, p.36; Webber et al. 2019a, p.29-30)

##### Substitution.disfavoured-alternative (`Disfavoured-alternative`)

In comparison with the favoured alternative presented in the anchor, the situation described in the utterance is disfavored or rejected alternative (Bunt & Prasad 2016).

- (145) Eliminate arbitrage and liquidity will decline **instead of** rising, creating more volatility instead of less. (PDTB3, wsj 0118, INTRASENTENTIAL)

- (146) **Rather than** sell 39-cents-a-pound Delicious, maybe we can sell 79-cents-a-pound Fujis,” says Chuck Tryon, ... (PDTB3, wsj 1128, INTRASENTENTIAL)

- (147) Intervention, he added, is useful only to smooth disorderly markets, **not** to fundamentally influence the dollar’s value. (PDTB3, wsj 0240, INTRASENTENTIAL)

> Note: 
> - cf. RST ?Antithesis
> - cf. PDTB3 Substitution.Arg1-as-Subst

##### Substitution.favoured-alternative (`Favoured-alternative`)

In comparison with the disfavoured alternative presented in the anchor, the situation described in the utterance is favored, and the alternative presented in the anchor is rules out (Bunt & Prasad 2016, Webber et al. 2019a, p.30).

- (132) Under current rules, even when a network fares well with a 100%-owned series – ABC, for example, made a killing in broadcasting its popular crime/comedy “Moonlighting” — it isn’t allowed to share in the continuing proceeds when the reruns are sold to local stations. **Instead**, ABC will have to sell off the rights for a one-time fee. (PDTB2, 2451)

- (149) Nor are any of these inefficient monoliths likely to be allowed to go bankrupt. **Rather**, the brunt of the slowdown will be felt in the fast-growing private and semi-private ”township” enterprises, ... (PDTB3, wsj 1646)

- (151) However, their search notably won’t include natural gas or pure methanol ... in tests to be completed by next summer. **Instead**, the tests will focus heavily on new blends of gasoline. (PDTB3, wsj 2030)

- (153) But Santa Fe, currently trading at 18 7/8, isn’t likely to realize private market values by selling assets, ... Its plan, **instead**, is to spin off the remainder of its real estate unit and to possibly do the same with its mining and energy assets. (PDTB3, )wsj 0331)

- (154) Two days earlier, his attorney met in a Park Avenue law office with a cartoon dealer who expected to sell 44 of the most important stolen strips to Mr. Russell for $62,800. **Instead**, New York City police seized the stolen goods, and Mr. Krisher avoided jail. (PDTB3, wsj 0450)

- (155) A Sanwa Bank spokesman denied that the finance ministry played any part in the bank’s decision. **[Implicit=instead]** “We made our own decision,” (PDTB3, wsj 1421)

> Notes:
> - cf. RST ?Antithesis
> - cf. PDTB2 Chosen Alternative
> - cf. PDTB3 Substitution.Arg2-as-subst
	
> Note: Following Bunt and Prasad (2016), this can be put under PDTB Expansion. However, RST Antithesis is much more defined along the lines of contrast, so, it might be better put there?

#### Similarity (`Similarity`)

`SIMILARITY` is a symmetric relation in which one or more similarities between the utterance and the anchor are highlighted with respect to what each predicates as a whole or to some entities they mention (Bunt & Prasad 2016; Webber et al. 2019a, p.25). Diagnostic discourse markers include _similarly_,  _like_ or _also_.

- (115) ... that even after Monday’s 10% decline, the Straits Times index is up 24% this year, so investors who bailed out generally did so profitably. **Similarly**, Kuala Lumpur’s composite index yesterday ended 27.5% above its 1988 close. (PDTB3, wsj 2230)

- (x) Cats don’t like to swim. They **also** have problems with changing their place of residence. (Żurowski et al. 2023, p.486, translated from Polish)
	
- (7) There is speculation that property/casualty firms will sell even more munis as they scramble to raise cash to pay claims related to Hurricane Hugo and the Northern California earthquake. Fundamental factors are at work **as well**. (PDTB3 Similarity, wsj 0671; Webber et al. 2019b)

- (8) “They continue to pay their bills and will do so,” says Ms. Sanger. “We’re confident we’ll be paying our bills for spring merchandise **as well**.” (PDTB3 Conjunction, wsj 1002; Webber et al. 2019b)

> **Note**: This definition recalls aspects of the definition of Contrast, so SIMILARITY can be seen as a subclass of PDTB COMPARISON. In PDTB3, Similarity was indeed introduced as a subclass of COMPARISON (Webber et al. 2019a, p.18). The PDTB2 mapping by Bunt and Prasad (2016), however, linked it with PDTB Conjunction and thus puts it under PDTB EXPANSION. We follow this approach here. Note that Webber et al. (2019b) point out that splitting PDTB2 EXPANSION.Conjunction into PDTB3 EXPANSION.Conjunction and PDTB3 COMPARISON.Similarity created novel ambiguities. In line with ISO 24617-8, these are not distinguished here.

> **Note**: PDTB2 Conjunction: Bunt & Prasad (2016) provide no other PDTB counterpart but PDTB2 conjunction. But this seems to be incorrect as it has a much looser definition closer to SDRT Narration: The situation described in the utterance provides additional, discourse new, information that is related to the situation described in the anchor, but is not related to the anchor in any other, more specific discourse relation. The semantics are thus no more than that of a logical ∧ (and). Diagnostic connectives are _also_, _in addition_, _additionally_, _further_, etc. ("conjunction", Prasad et al. 2007, p.37)

- (134) Food prices are expected to be unchanged, but energy costs jumped as much as 4%, said Gary Ciminero, economist at Fleet/Norstar Financial Group. He **also** says he thinks “core inflation,” which excludes the volatile food and energy prices, was strong last month. (PDTB2 conjunction, 2400)

> Notes:
> - cf. RSTDTB Analogy, Proportion 
> - cf. SDRT (ANNODIS, DISCOR) Parallel
> - cf. PDTB Conjunction

> Note: If the PDTB2 definition is adopted, SIMILARITY is to be annotated after anything else. In combination with the annotation preference of discourse relations, this is the primary justification for grouping `Similarity` with Expansion.

### TEMPORAL

#### Synchrony (`Synchrony`)

`SYNCHRONY` applies if the situations described in the utterance and the anchorhave some degree of temporal overlap, i.e., if the two situations started and ended at the same time, if one was temporally embedded in the other, or if the two crossed. Diagnostic connectives are _while_ and _when_ (Bunt & Prasad 2016; PDTB2 Synchronuous in Prasad et al. 2007, p.27-28). 

- (58) Then, in late-afternoon trading, hundred-thousand-share buy orders for UAL hit the market, including a 200,000-share order through Bear Stearns that seemed to spark UAL’s late price surge. **Almost simultaneously**, PaineWebber began a very visible buy program for dozens of stocks. (PDTB3, wsj 1208)

- (60) The parishioners of St. Michael and All Angels stop to chat at the church door, as members here always have. **[Implicit=while]** In the tower, five men and women pull rhythmically on ropes attached to the same five bells that first sounded here in 1614. (PDTB3, wsj 0089)

> Notes:
> - cf. RSTDTB Temporal-same-time
> - cf. PDTB Synchronous
> - Following Bunt and Prasad (2016), this is put under TEMPORAL

#### Asynchrony

The situation described in utterance stands in a temporal order with the situation described in the anchor, i.e., the role `Before` temporally precedes the `After` role. (Bunt & Prasad 2016) (cf. Prasad et al. 2007, p.27).

> Notes: cf. RST Sequence

##### Asynchrony.before (`Before`)

The situation described in the utterance temporally precedes the situation described in the anchor. A diagnostic discourse marker is _before_ (Bunt & Prasad 2016; PDTB2 precedence in Prasad et al. 2007, p.28)
		
- (66) John D. Carney, 45, was named to succeed Mr. Hatch as president of Eastern Edison. Previously he was vice president of Eastern Edison. (PDTB3, wsj 0019)

- (12) The Japanese are in the early stage right now,” said Thomas Kenney, . . . . “**Before**, they were interested in hard assets and they saw magazines as soft. (PDTB3, wsj 1650; Webber et al. 2019b)

> Notes:
> - cf. RSTDTB Temporal-before, Inverted-sequence
> - cf. DISCOR Precondition, ANNODIS Flashback
> - cf. PDTB Precedence

##### Asynchrony.after (`After`)

The situation described in the anchor temporally precedes the situation described in the utterance (Bunt & Prasad 2016; PDTB2 succession in Prasad et al. 2007, p.28). A diagnostic discourse marker is _after (that)_ or _ then_.

- (61) A buffet breakfast was held in the museum, where food and drinks are banned to everyday visitors. **Then**, in the guests’ honor, the speedway hauled out four drivers, crews and even the official Indianapolis 500 announcer for a 10-lap exhibition race. (PDTB3, wsj 0010)

- (64) The Artist has his routine. He spends his days sketching passers-by, or trying to. **[Implicit=then]** At night he returns to the condemned building he calls home. (PDTB3, wsj 0039)

- (x) The daughters will bake cakes. **Then**, it will be time for presents. (Żurowski et al. 2023, p.486, translated from Polish)

> Notes:
> - cf. RSTDTB Temporal-after, Sequence
> - cf. SDRT (DISCOR, ANNODIS) Narration
> - cf. PDTB Succession
> - Following Bunt and Prasad (2016), this is put under TEMPORAL

##### Hypophora

Hypophora is used for answers to rhetorical questions. The discourse relation that links these answers to the preceding discourse is to be annotated on the question.

- (19) If not now, when? **[HYPOPHORA]** “When the fruit is ripe, it falls from the tree by itself,” he says. (PDTB3, wsj 0300)

- (20) Of all the ethnic tensions in America, which is the most troublesome right now? **[HYPOPHORA]** A good bet would be the tension between blacks and Jews in New York City. (PDTB3, wsj 2369)

- (21) But can Mr. Hahn carry it off? **[HYPOPHORA]** In this instance, industry observers say, he is entering uncharted waters. (PDTB3, wsj 0100)

- (22) So can a magazine survive by downright thumbing its nose at major advertisers? **[HYPOPHORA]** Garbage magazine, billed as ”The Practical Journal for the Environment,” is about to find out. (PDTB3, wsj 0062)

- (23) With all this, can stock prices hold their own? **[HYPOPHORA]** ”The question is unanswerable at this point” she says. (PDTB3, wsj 0681)

- (9) How can we turn this situation around? **[HYPOPHORA]** Reform starts in the Pentagon. (Prasad et al. 2017, p. 11)

> Notes:
> - missing from PDTB2, added with PDTB3 as top-level category "Hypophora": "In HYPOPHORA relations, one argument (commonly Arg1) expresses a question and the other argument (commonly Arg2) provides an answer.""

##### Attribution

We do not consider attribution a discourse relation in its own right. However, as we perform sentence-level annotation over pre-determined sentence splits, it is possible that an attribution phrase gets detached from the reported statement. In those cases, annotate the utterance expressing the attribution with an `Attribution` relation that takes the statement (resp., its closest sentence) as anchor:

- (1.1) **[Attribution]** Now, let’s read what He said in Matthew 6:9-10:
- (1.2) [Anchor] After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name. (https://kcmcanada.ca/04-2021-partner-letter/, accessed 2023-11-16)

Note that the example in (1.1) originally had a paragraph break between the attribution sentence and the statement.

### DIALOG

Dialog relations are to be annotated if and only if turn-taking between multiple speakers applies. In this case, annotate the discourse function.

Two kinds of discourse relations which are specific to dialogue are (1) functional dependence relations, such as those between an answer and the
question that it answers, or an ‘accept apology’ and the apology which is accepted; and (2) feedback dependence relations, such as the relation between a feedback utterance like “sure” or a head nod, and the utterance that the feedback is about; or between “you see?” and the utterance that the speaker is eliciting information about (Bunt et al. 2012, p.431)

Dialog relations are defined for expressing semantic relations between dialogue acts, e.g. for indicating which question is answered by a certain answer act (functional dependence relation), or which utterance a feedback act responds to (feedback dependence relation) (Bunt et al. 2019).

In AURIS, dialog relations are only to be annotated if they occur after turn-taking and no other discourse relation applies. Dialog relations do not apply when the subsequent text relates to a question in other ways – for example, in the case of rhetorical questions that are posed for dramatic effect or to make an assertion, rather than to elicit an answer (Webber et al. 2019a, p.9). Rhetorical questions are excluded from this group and to be annoted as EXPANSION.Hypophora.
If the subsequent text is not an answer (direct or indirect) or a denial that an answer is possible, another relation should be annotated (Webber et al. 2019a, p.9):

- (25) Since chalk first touched slate, schoolchildren have wanted to know: What’s on the test? **[Implicit=however]** These days, students can often find the answer in test-coaching workbooks and worksheets their teachers give them in the weeks prior to taking standardized achievement tests. (PDTB3, wsj 0045)

#### Functional dependence

In a FUNCTIONAL_DEPENDENCE` relation, the utterance is a dialogue act that is responsive in nature and that address the information communicated in the utterances; the anchor is the dialogue act that the utterance responds to (Bunt & Prasad 2016, Bunt et al. 2019). The semantic content of these types of dialogue act depend crucially on which previous dialogue act they respond to, in many cases, they can be paraphrased by (semantically empty) responses such as “Yes”, “No thanks”, “No problem”, and “OK” (Bunt et al. 2012, p.432).

In AURIS, functional dependence relations involve the explicit elicitation of the response as an anchor -- either directly by a question, request or suggestion, or indirectly with a statement that the addressee reacts to. 

The ancedent act of a functional dependence relation always serves as an anchor and precedes the utterance, so it is not to be annotated.

> Note in ISO 24617-8, the utterance occupies the Dependent-act role, the anchor the Antecedent-act

Following ISO (2010; cf. Bunt et al. 2018, 2019), the following communicative functions are relevant and should be annotated in AURIS as sub-types of functional dependence:
- `Answer`
- `Offer`
- `Address Suggest`
- `Agreement`
- `Disagreement`

###### `Answer`

The speaker performs a dialog act in order to make the information in the utterance known to the addressee in response to the anchor that expresses an information-seeking function (i.e., a question). The speaker believes the utterance to be correct (ISO 2010, Bunt et al. 2018, 2019).

- (2.1) S: "what does the display say?"
- (2.2) H: **[ANSWER]** "send error document ready" (DIAMOND corpus, ISO 2010)

- (v) A: Is there an earlier connection? **[ANSWER]** B: No, I’m sorry, there isn’t. (Bunt et al. 2012, p.432)

- (w) P1: Is it safe to put my camera through here? It’s a very expensive camera you know. **[ANSWER]** P2: Yes, that’s perfectly safe. (Bunt and Prasad 2016)

- (x) So, are you satisfied? **[ANSWER]** Yes, we are.	(Żurowski et al. 2023, p.487, translated from Polish)

- (y) A: What newspapers do you read? **[ANSWER]** B: I read uh the local newspaper, and I also try and read one of the uh major dailies like the Chicago Tribune, or the New York Times or something like that (Prasad and Bunt 2015)

We do not differentiate types of asnwers. However, note that we distinguish answers that address an information need from responses to requests for a particular action. Both can take questions as their anchors, but a commitment (or denial) of future actions on behalf of the speaker is to be annotated as `Offer`.

> Note: Dialog act of utterance corresponds to ISO/DIS 24617-2 "Answer", dialog act of anchor corresponds to ISO/DIS 24617-2 "Question".

###### `Agreement`

The anchor describes a situation that the speaker presents as a true statement. With the utterance, the addressee confirms that he believes that this statement is indeed true (ISO 2010). Use if the utterance can be paraphrased by "Exactly!".

- (z) B: I really like NPR a lot **[Agreement]** A: Yeah that's pretty good (Prasad and Bunt 2015)

- (x) But our children are different. **[AGREEMENT]** Yes, they are different. (Żurowski et al. 2023, p.487, translated from Polish)

Agreement is related to `Answer` in that it addresses an information need of the addressee, for the case of Agreement, however, it is not solicted by a question.

###### `Disagreement`

The anchor describes a situation that the speaker presents as a true statement. With the utterance, the addresee informs the speaker that he believes that this statement is false (ISO 2010).

- (1.1) J: "do you know where to find ink saving?"
- (1.2) S: **[Answer]** "ehm.. oh I think to the left of the ink cartridge"
- (1.3) J: **[Disagreement]** "ehm... no" (DIAMOND corpus, ISO 2010)

Disagreement is is similar to Agreement in that it is addresses an information need of the addressee not solicted by a question, it differs in polarity.

###### `Offer`

With the utterance, the speaker commits himself to perform a particular action. The speaker assumes that the addressee refers the action to be performed (ISO 2010). The anchor of an `Offer` relation should be an utterance that caused the speaker to assume that the addressee wants him to perform the offered activity (ISO 2010, Bunt et al. 2018, 2019). 

- (1.1) CAMOETO: Nice runs! Are you running any supporting mods such as DP?
- (1.2) ParadigmDawg: **[Offer]** I will look that up for you since it is in the original post (https://x3.xbimmers.com/forums/showthread.php?t=1604114, accessed 2023-11-16)

We do not differentiate different kinds of offers, such as promises or accepting requests:

- (2.a) SKubrick: I've noticed the date ranges don't update very frequently and the percentages are different from what I'm calculating manually. 
- (2.b) SKubrick: Is there any way to update the date range or select a specific date range to view? ...
- (2.b) karstenkoehler: **[Offer]** Sure, happy to help, @SKubrick! 
- (2.c) karstenkoehler: I've added a short example to my previous post. (https://community.hubspot.com/t5/Email-Marketing-Tool/Email-Health-Tool/m-p/400198, accessed 2023-11-16)

Offers also includes a _negative_ response to requests:

- (3.a) Unknown ID: We'll investigate it. 
- (3.b) Unknown ID: Is it possible for us to meet in person?
- (3.c) Alibaba: **[Offer (declineRequest)]** Not now. 
- (3.d) Alibaba: Maybe in a week or two. 
- (3.e) Alibaba: I'll stay in contact. (https://forums.spacebattles.com/threads/oracle-persona-5-time-travel.1098423/, accessed 2023-11-16)

In Alibaba's response, the first statement (3.c) directly responds (3.b), but is subsequently elaborated into a refined offer. Note that this elaboration is to be modelled by EXPANSION relations that take (3.c) as their anchor, not directly as feedback responses to (3.b).

> Note: We only annotate *solicited* offers that are performed in response to a request. The dialog act of the utterance corresponds to ISO/DIS 24617-2 "Offer", dialog act of anchor corresponds to ISO/DIS 24617-2 "Request".

###### `Address Suggest`

With the utterance, the speaker commits himself (or declines) to perform an action that was suggested to him (ISO 2010). The anchor is the utterance of the addressee that made him believe that was a suggested action. The main difference to `Offer` is that the addressee is neutral about his proposal or that the speaker himself is the main beneficiary of the proposal (ISO 2010, Bunt et al. 2018, 2019).

- (4.1) Admiral James: Do you want to tour the waterfront area?
- (4.2) Congressman Norblad: **[Address Suggest]** I would like to.
- (4.3) Admiral James: Maybe, we can do it in a little less than half an hour.
- (4.4) Chairman Doyle: **[Address Suggest]** Let's do that before we come home back here. (U.S. Congress. House. Commitee on the Armed Services (1957/1958), Hearings Vol. 3. 85th Congress, 1st and 2nd Session. p. 3122)

We include both positive and negative responses to suggestions under `Address Suggest`.

> Note: The ISO/DIS 24617-2 dialog act of the utterance is "Address Suggest", the dialog act of the anchor is "Suggest".

###### `Dependent-act`

If an utterance dialog act is in response to the content of an utterance by the addressee but none of the aforementioned communicative functions applies, annotate as `Dependent-act` and leave a comment.

#### Feedback dependence: `Feedback`

In a `FEEDBACK_DEPENDENCE` relation, the feedback act (`feedback`) provides or elicits information about the understanding or evaluation by one of the dialogue participants of the feedback scope, a communicative event that occurred earlier in the discourse. As with Entity Relations, no explicit or implicit connective is identified and annotated: The only elements of the relation are the utterance and the anchor (Bunt & Prasad 2016; PDTB Hypophora in Webber et al. 2019a, p.9).

> For the AURIS `Feedback` relation, the utterance corresponds to the SemAF role "Feedback act", the anchor the SemAF roile "Feedback scope".

For feedback dependence relations the semantic content of a feedback act necessarily depends on the utterance(s) that the feedback is about. The difference to functional dependence is that the semantic content of a feedback act may be determined by what was said before rather than by the semantic content of a previous dialogue act (Bunt et al. 2012).

Feedback acts are about the processing of something that was said before. The nature of this ‘something’ depends on the kind of feedback. Feedback by means of expressions like “OK”, “Uh-huh”, or “Really?” is about one or more previous dialogue acts, while feedback by means of “Tuesday?” or “What did you say?” is about a previous utterance segment, rather than about a dialogue act (Bunt et al. 2019).

The difference between feedback dependence and functional dependence is that feedback dependence is not solicited by the speaker. We do not distinguish communicative functions of feedback relations

In a feedback depedence relation, the anchor precedes the utterance and defines the feedback scope, the utterance represents the feedback act. 

The utterance provides an answer to a question expressed in the anchor. Normally, the question should precede the answer. For a question seeking information, the response should aim to fulfill that need by addressing it explicitly, or, alternatively, indicate that the information need cannot be fulfilled, as in (23) below. 

- (8.a) A: I would like to come on Tursday. **[Feedback]** B: On Thursday? (Bunt et al. 2012, p.433)

- (8.b) A: That’s at two-thirty. **[Feedback]** B: I see. (Bunt et al. 2012, p.433)

- (x.1) A: go south and you’ll pass some cliffs on your right. **[Feedback]** B: okay
- (x.2) A: and keep going down south. **[Feedback]** B: mmhmm
- (x.3) A: we are going to go due south straight south and then we’re going to turn straight back round and head north past an old mill on the right hand side. **[Feedback]** B: due south and then back up again

### Entity relations (`EntRel`)

In an entity relation, the utterance provides further description about some entity or entities introduced in the anchor, expanding the narrative forward of which the anchor is a part, or expanding on the setting relevant for interpreting the anchor. Utterance and anchor describe distinct situations, and the anchor may seen as a "foreground" that introduces the entities elaborated in the utterance (Bunt & Prasad 2016). Entity relations are not marked by explicit discourse markers, but defined by coreference between their referrring expressions, the anchor *must* always precede the utterance.

> Note: Our naming follows PDTB2 and PDTB3. According to Bunt and Prasad (2016), entity relations are equivalent to the SemAF relation "Expansion", but here, we refrained from this name because it would create an unfortunate overlap with the top-level class `EXPANSION` which does *not* overlap with PDTB entity relations.

> Note: Żurowski et al. 2023 (p.487) report the SemAF relation "Expansion" with roles "Narrative" and "Expander". This differs from scientificially published version of ISO 24617-8. They give the following example

- (x) She insisted that I go to college. **[EntRel]** During the occupation, she put herself in great danger to save me ...	(Żurowski et al. 2023, p.487, translated from Polish)

> Note: ISO 24617-8 distinguishes two argument roles here, "foreground" and "entity description". As the foreground is always the anchor and the entity description is always the utterance, all AURIS annotations for entity relations are actually instances of SemAF entity description. Foreground is never explicitly annotated.

> Note: For cross-paragraph link annotation, Prasad et al. (2017) distinguish "semantic" entity relations (where the narrative is expanded forward) and "other" entity relations (were only coreference establishes a link). However, this division had been abandoned for PDTB3.

> Notes:
> - cf. RST Elaboration (object-attribute)
> - cf. RSTDTB Elaboration object-attribute, Elaboration additional
> - cf. SDRT Background, Elaboration (DISCOR Commentary, Attribution, Source; ANNODIS Comment, Attribution, Frame, Temporal-location)
> - cf. PDTB EntRel: "for cases where only an entity-based coherence relation could be perceived between the sentences" (Prasad et al. 2007, p.18)

- "EntRel captures cases where the implicit relation between adjacent sentences is not between their AO interpretations, but is rather a form of entity-based coherence (...) in which the same entity is realized in both sentences, either directly (...) or indirectly (...). Note that entity realization here also includes reification of an abstract object (AO) mentioned in the first sentence, such as with the demonstrative _this_ in Example (92), and the definite description _the appointments_ in Example (93). ... " (Prasad et al. 2007, p.23-25)

	- (89) Hale Milgrim, 41 years old, senior vice president, marketing at Elecktra Entertainment Inc., was named president of Capitol Records Inc., a unit of this entertainment concern. **[EntRel]** Mr. Milgrim succeeds David Berman, who resigned last month. (PDTB2 0945)

	- (90) The purchase price was disclosed in a preliminary prospectus issued in connection with MGM Grand’s planned offering of six million common shares. **[EntRel]** The luxury airline and casino company, 98.6%-owned by investor Kirk Kerkorian and his Tracinda Corp., earlier this month announced its agreements to acquire the properties, but didn’t disclose the purchase price. (PDTB2 0981)

	- (91) Last year the public was afforded a preview of Ms. Bartlett’s creation in a table-model version, at a BPC exhibition. **[EntRel]** The labels were breathy: “Within its sheltering walls is a microcosm of a thousand years in garden design ... At the core of it all is a love for plants.” (PDTB2, 0984)

	- (92) She has done little more than recycle her standard motifs – trees, water, landscape fragments, rudimentary square houses, circles, triangles, rectangles – and fit them into a grid, as if she were making one of her gridded two-dimensional works for a gallery wall. But for South Gardens, the grid was to be a 3-D network of masonry or hedge walls with real plants inside them. **[EntRel]** In a letter to the BPCA, kelly/varnell called this “arbitrary and amateurish.” (PDTB2 0984)

	- (93) Ronald J. Taylor, 48, was named chairman of this insurance firm’s reinsurance brokerage group and its major unit, G.L. Hodson & Son Inc. Robert G. Hodson, 65, retired as chairman but will remain a consultant. Stephen A. Crane, 44, senior vice president and chief financial and planning officer of the parent, was named president and chief executive of the brokerage group and the unit, succeeding Mr. Taylor. **[EntRel]** The appointments are effective Nov. 1. (PDTB2 0948)

	- (94) Proceeds from the offering are expected to be used for remodeling the company’s Desert Inn resort in Las Vegas, refurbishing certain aircraft of the MGM Grand Air unit, and to acquire the property for the new resort. **[EntRel]** The company said it estimates the Desert Inn remodeling will cost about $32 million, and the refurbishment of the three DC-8-62 aircraft, made by McDonnell Douglas Corp., will cost around $24.5 million. (PDTB2 0981)

If an entity relation holds between the utterance and several candidate anchors (as in ex. 95), annotate the relation to the closest anchor candidate:

- (95) HOLIDAY ADS: Seagram will run two interactive ads in December magazines promoting its Chivas Regal and Crown Royal brands. The Chivas ad illustrates – via a series of pullouts – the wild reactions from the pool man, gardener and others if not given Chivas for Christmas. The three-page Crown Royal ad features a black-and-white shot of a boring holiday party – and a set of colorful stickers with which readers can dress it up. **[EntRel]** Both ads were designed by Omnicom’s DDB Needham agency. (PDTB2, 0989)

## Troubleshooting

- pairwise discourse markers: Annotate independently. As both parts refer to each other, this creates a cycle in the annotation.

	- (22) **On the one hand**, Mr. Front says, it would be misguided to sell into “a classic panic.” **On the other hand**, it’s not necessarily a good time to jump in and buy. (PDTB2, 2415)

- discourse markers of attribution verbs: If a discourse marker is (correctly or not) attached to an attribution verb, but the main predicate of an utterance is a dependent of the attribution verb, this discourse marker is taken to refer to the main predicate. The primary discourse marker is identified by means of the following preferences:

	- MAIN CLAUSE > DEPENDENT CLAUSE > DEPENDENT of DEPENDENT CLAUSE
	- within a clause: first > second 

	- (22) **On the one hand**, Mr. Front says, it would be misguided to sell into “a classic panic.” 

- Apparent cases of multiple utterance. In the following example, utterances 4.-7. constitute an elaboration of 3. However, we adopt the SDRT view on such constellations, that is, if 4 elaborates 3 and 5 elaborates 3, a narration relation hold between 4 and 5. Because we annotate the closest anchor for each utterance, only the narration is to be annotated, but not the elaboration. (Note that these are SDRT relations, but the argumentation holds for ISO 24617-8 labels, as well.)

	(83) 
		1. Legal controversies in America have a way of assuming a symbolic significance far exceeding what is involved in the particular case. 
		2. They speak volumes about the state of our society at a given moment.
		3. It has always been so. 
		4. **[Implicit = for example]** In the 1920s, a young schoolteacher, John T. Scopes, volunteered to be a guinea pig in a test case sponsored by the American Civil Liberties Union to challenge a ban on the teaching of evolution imposed by the Tennessee Legislature. 
		5. The result was a world-famous trial exposing profound cultural conflicts in American life between the “smart set,” whose spokesman was H.L. Mencken, and the religious fundamentalists, whom Mencken derided as benighted primitives. 
		6. Few now recall the actual outcome:
		7. Scopes was convicted and fined $100, and his conviction was reversed on appeal because the fine was excessive under Tennessee law. (PDTB2, 0946)

- multiple clauses as anchors: In AURIS, the anchor must be a single utterance (resp., its main predicate). If a discourse connective seems to take a _sequence_ of utterances as anchors, chose the closest candidate anchor with which a relation can be established. However, plausibility overrides proximity. In the example below, the third sentence _could_ is in a contrast relation with the first as well as the second. However, the second seems to elaborate with anecdotal evidence on the first, so the main reason for surprisal in the third utterance is not the karaoke ban, but the general poor condition. So, annotate 1 as an anchor. (The situation may be different if karaoke is the main topic of the article.)

	- (56) 
		1. Here in this new center for Japanese assembly plants just across the border from San Diego, turnover is dizzying, infrastructure shoddy, bureaucracy intense. 
		2. Evn after-hours drag; “karaoke” bars, where Japanese revelers sing over recorded music, are prohibited by Mexico’s powerful musicians union.
		3. **Still**, 20 Japanese companies, including giants such as Sanyo Industries Corp., Matsushita Electronics Components Corp. and Sony Corp. have set up shop in the state of Northern Baja California. (PDTB2, 0300)

	> Note: This is different from PDTB, where, instead, a minimality principle applies.

- attribution: As defined by Prasad et al. (2007, p.40), attribution is "a relation of “ownership” between abstract objects and individuals or agents. That is, attribution has to do with ascribing beliefs and assertions expressed in text to
the agent(s) holding or making them". If a the main clause of an utterance expresses an attribution, with a statement in a dependent clause or direct speech annotated as part of the same utterance, then the main predicate of the utterance is to be taken from the statement, not the attribution verb. If an utterance consists of an attribution verb only, without including the reported statement, the main predicate is the attribution verb.

	> Note: We rely on an existing pre-annotation for sentence (utterances) here. If utterances are to be manually segmented, then attribution and statement should be put in distinct utterances if and only if the statement is a complete sentence. Normally, this occurs with direct speech only. Also, reported statements interrupted by an attribution verb should not be segmented, then.

	In the following example, the main predicate is "Judge O'Kicki unexpectedly awarded him an additional $100,000", although the syntactic head is "says" (in the attribution clause "he says"). Note that this is a relative clause. The attribution verb is likewise modified by a temporal relative clause ("When ... in June 1983"), but only amodifying adverbial clause, not part of the attribution.

	- (144) When Mr. Green won a $240,000 verdict in a land condemnation case against the state in June 1983, he says [Judge O’Kicki unexpectedly awarded him an additional $100,000]. (PDTB2, 0267)

	> Note: If an utterance with attribution carries multiple relative clauses, the comment should clarify which is considered the main predicate.

	In the following example, the main predicate is the reported statement in the first relative clause ("the 90-cent-an-hour rise ... is too small for the working poor"). In line with UD conventions, we consider the coordinated main clause ("opponents argued ...") to be subordinate to  the first main clause. 

	- _Advocates said_ the 90-cent-an-hour rise, to $4.25 an hour by April 1991, is too small for the working poor, while opponents argued that the increase will still hurt small business and cost many thousands of jobs. (PDTB2 0098) 

## Appendix: List of diagnostic discourse markers

You can use the following list to confirm whether a discourse relation holds. If you can use these discourse markers in place of the explicit discourse marker or the alternative lexicalization at hand, or insert them into a sentence without implicit discourse marker, take this as an indicator that the respective discourse relation holds.

Also, when disambiguating explicit or inserting implicit discourse markers, consult this list from top to bottom: If a discourse marker holds, do not consider other candidate markers further below. We currently provide lists for English and German. Discourse marker lists for other languages can be provided upon demand.

### English

### German


## Sources / Relations with other schemes

ISO 24617-8 has been heavily criticized for being poorly defined (e.g., by Żurowski et al. 2023). We provide operationalizable definitions by exploiting the correspondence with established RST, SDRT and PDTB definitions as given by proponents of ISO 24617-8. These definitions are primarily based on PDTB 2.0 (Prasad et al. 2007).

The AURIS Discourse schema is grounded in the role inventory of ISO 24617-8. Note that we do not directly quote from the ISO-24617-8 norm, because they do not provide the necessary level of detailed description, and they are available only upon payment from https://www.iso.org/obp/ui/#iso:std:iso:24617:-8:ed-1:v1:en. Instead, the primary basis for designing these guidelines is the Penn Discourse Treebank (PDTB), and the ISO 24617-8 mapping provided by Bunt and Prasad (2016). Unlike PDTB, AURIS does not annotate minimal spans, but complete sentences. The AURIS terms *utterance* and *anchor* correspond to `ARG2` (internal argument of a discourse marker) and `ARG1` (external argument) in the terminology of PDTB2. (Note that these terms have been partially re-defined for PDTB3, the exact correspondence is with the original PDTB2 definitions.)

The guidelines for discourse relation annotation are primarily based on those of the Penn Discourse Treebank (PDTB), using the ISO 24617-8 relation inventory as defined by Bunt and Prasad (2016). The first level is based on PDTB2 (not PDTB3), the second level is represented by ISO 24617-8 relations (discourse relations that are symmetric or underspecified in their directionality), the third level by ISO 24617-8 roles (asymmetric discourse relations.)

The top-level organization of discourse relations corresponds to PDTB2: CONTINGENCY (Prasad et al. 2007, p.28; Webber et al. 2019a, p.19), TEMPORAL (Prasad et al. 2007, p. 27; Webber et al. 2019a, p.18), EXPANSION (Prasad et al. 2007, p.34). The definition for ADVERSATIVITY is based on the PDTB2 definition of COMPARISON (Prasad et al. 2007, p.32), which (for PDTB2) included Contrast and Concession. We decided to rename it to highlight that the PDTB3 relation Similarity continues to be grouped with EXPANSION (as in PDTB2), not with Contrast and Concession (as in PDTB3). This reflects the the distribution of discourse markers, as those associated with Similarity overlap with those of Conjunction (in EXPANSION), whereas they do not overlap with the common pool of adversative discourse markers (esp., *but*). As for PDTB EntRel relations, these have unfortunately been named EXPANSION in ISO 24617-8, but we follow PDTB in considering them a separate top-level group. DIALOG was added for ISO 24617-8 dialog annotations: PDTB annotations primarily addressed monologuous data.

> Note: The top-level class ADVERSATIVITY has been introduced for PDTB2 COMPARISON, to avoid conflation with PDTB3 COMPARISON, because PDTB3 has revised the definition of COMPARISON to also include Similarity relations, which were previously grouped with EXPANSION. However, Webber et al. (2019a, p. 23-24) note that annotators had difficulties to distinguish Contrast and Concession, thus demonstrating the need for a common superclass. These difficulties do not extend, however, to SIMILARITY. As an alternative to the PDTB3 approach of extending the scope of COMPARISON, we would prefer to stay with the original definition, but use a more specific designation, say, ADVERSATIVITY.

For asymmetric relations, we annotate the ISO 24617-8 role of the internal argument. For symmetric relations, we annotate the ISO 24617-8 relation at the second argument.

In the following, we refer to the internal argument as utterance, to the external argument as (contextual) anchor. 



## References

- Harry Bunt, Jan Alexandersson, Jae-Woong Choe, Alex Chengyu Fang, Koiti Hasida, Volha Petukhova, Andrei Popescu-Belis and David Traum (2017), ISO 24617-2: A semantically-based standard for dialogue annotation. LREC 2012.

- Harry Bunt and Prasad, Rashmi (2016), ISO DR-Core (ISO 24617-8), Core concepts for the annotation of discourse relations, In: Proceedings 12th Joint ACL-ISO Workshop on Interoperable Semantic Annotation (ISA-12), p. 45-54

- Harry Bunt, Emer Gilmartin, Simon Keizer, Catherine Pelachaud, Volha Petukhova, Laurent Prévot, and Mariët Theune (2018), Downward compatible revision of dialogue annotation. In Proceedings 14th Joint ACL-ISO Workshop on Interoperable Semantic Annotation, pp. 21-34. 2018.

- Harry Bunt, Volha Petukhova, Andrei Malchanau, Alex Fang, and Kars Wijnhoven (2019), The DialogBank: dialogues with interoperable annotations. Language Resources and Evaluation 53 (2019): 213-249.

- Harry Bunt, Volha Petukhova, Emer Gilmartin, Catherine Pelachaud, Alex Fang, et al. (2020), The ISO Standard for Dialogue Act Annotation, Second Edition. Proceedings of the 12th Language Resources and Evaluation Conference, May 2020, Marseille, France.

- ISO (2010), Language resource management — Semantic annotation framework — Part 2: Dialogue acts, ISO/TC37/SC4 N723 Date: 2010-07-14, ISO/DIS 24617-2, ISO/TC 37/SC 4/WG 2, pre-publication draft from https://semantic-annotation.uvt.nl/DIS24617-2.pdf, referenced as ISO/DIS 24617-2

- Rashmi Prasad, Eleni Miltsakaki, Nikhil Dinesh, Alan Lee, Aravind Joshi, Livio Robaldo (2007), The Penn Discourse Treebank 2.0 Annotation Manual, December 17, 2007, https://www.cis.upenn.edu/~elenimi/pdtb-manual.pdf, accessed 2023-11-09

- Rashmi Prasad and Harry Bunt (2015), Semantic Relations in Discourse: The Current State of ISO 24617-8, Proceedings of the 11th Joint ACL-ISO Workshop on Interoperable Semantic Annotation (ISA-11), https://aclanthology.org/W15-0210

- Rashmi Prasad, Katherine Forbey-Riley and Alan Lee (2017), Towards Full Text Shallow Discourse Relation Annotation: Experiments with Cross-Paragraph Implicit Relations in the PDTB, Proceedings of the SIGDIAL 2017 Conference, pages 7–16, Saarbrücken, Germany, 15-17 August 2017.

- Bonnie Webber, Rashmi Prasad, Alan Lee, Aravind Joshi (2019a), The Penn Discourse Treebank 3.0 Annotation Manual, Language Data Consortium, https://catalog.ldc.upenn.edu/docs/LDC2019T05/PDTB3-Annotation-Manual.pdf, accessed 2023-11-13

- Bonnie Webber, Rashmi Prasad and Alan Lee (2019b), Ambiguity in Explicit Discourse Connectives, COLING-2019, Gothenburg, Sweden.

- Sebastian Żurowski, Daniel Ziembicki, Aleksandra Tomaszewska, Maciej Ogrodniczuk and Agata Drozd (2023), Adopting ISO 24617-8 for Discourse Relations Annotation in Polish: Challenges and Future Directions. In Proceedings of the 4th Conference on Language, Data and Knowledge (pp. 482-492).

## Possible Addenda

TED-MDB guidelines?

NB: for Dialog data, cf. https://dialogbank.lsv.uni-saarland.de/

Note that PDTB3 changed the definition of its arguments and shifted from a syntactically based identification of Arg1 (external argument) and Arg2 (internal argument) to a positional identification of Arg1 as first and Arg2 as second argument (except for subordinating conjunctions, where the old definition holds). As ISO 24617-8 was defined in relation to PDTB2, not PDTB3, our definitions are based on the older definitions. Subsequent updates to the definition of PDTB2 roles that pertain to this change in definitions have not been adopted here.

TODO: we could add attribution for cases in which sentence splitting separates the attribution phrase from the reported statement. In our attribution relation, the utterance is the attribution statement, attribution triggered by either the verb or an orthographic mark such as a colon (_:_)