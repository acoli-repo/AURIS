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

> Note: Our approach on argument identification follows the Penn Discourse Treebank. Our internal argument corresponds to the PDTB ARG2, our external argument corresponds to the PDTB ARG1. There is no systematic relation between internal and extenal arguments and ARG1 and ARG2 as defined in ISO SemAF.

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

For automated discourse marker identification, we largely follow discourse marker lists provided by PDTB2.

## Manual annotation of explicit discourse markers

We distinguish two primary kinds of discourse markers: 
- explicit discourse markers are stated in the text. annotators should write them as plain strings.
- implicit discourse markers are not stated in the text. annotators should write them in round brackets.

Following Prasad et al. (2007), explicit discourse markers are drawn from the following grammatical classes:

- adverbials (ADVP and PP, e.g., however, otherwise, then, as a result, for example)

	- (12) Working Woman, with circulation near one million, and Working Mother, with 625,000 circulation, are legitimate magazine success stories. The magazine Success, **however**, was for years lackluster and unfocused. (PDTB2, 1903)

	- (13) In the past, the socialist policies of the government strictly limited the size of new steel mills, petrochemical plants, car factories and other industrial concerns to conserve resources and restrict the profits businessmen could make. As a result, industry operated out of small, expensive, highly inefficient industrial units. (PDTB2, 0629)

	- (39) Such problems will require considerable skill to resolve. **However**, neither Mr. Baum nor Mr. Harper has much international experience. (PDTB2, 0109)

	- DO NOT ANNOTATE adverbials modifying clauses other than the main predicate:

		- (33) Polyvinyl chloride capacity “has overtaken demand and we are experiencing reduced profit margins **as a result**”, ... (PDTB2, 2083)

		In line with Universal Dependency syntax, the clause connected with the conjunction _and_ is syntactically analyzed as a dependent of the first clause. It does thus not carry the main predicate.

- coordinating conjunctions (e.g., and, or, nor), but only if attached to the main predicate of an utterance.
	
	- (11) The report offered new evidence that the nation’s export growth, though still continuing, may be slowing. Only 19% of the purchasing managers reported better export orders in October, down from 27% in September. **And** 8% said export orders were down last month, compared with 6% the month before. (PDTB2, 0036)

	- (38) Metropolitan Houston’s population has held steady over the past six years. And personal income, after slumping in the mid-1980s, has returned to its 1982 level in real dollar terms. (PDTB2, 2444)

	- DO NOT ANNOTATE

		- (10) The House has voted to raise the ceiling to $3.1 trillion, **but** the Senate isn’t expected to act until next week at the earliest. (PDTB2, 0008)

		- (i) More common chrysotile fibers are curly **and** are more easily rejected by the body, Dr. Mossman explained. (PDTB2, 0003)

- subordinating conjunctions (e.g., because, when, since, although), but only if attached to the main predicate of an utterance:
		
	- (37) Why do local real-estate markets overreact to regional economic cycles? **Because** real-estate purchases and leases are such major long-term commitments that most companies and individuals make these decisions only when confident of future economic stability and growth. (PDTB2, 2444)

	- This is expected to occur rarely.

	- DO NOT ANNOTATE

		- (8) **Since** McDonald’s menu prices rose this year, the actual decline may have been more. (PDTB2, 1280)

		- (9) The federal government suspended sales of U.S. savings bonds **because** Congress hasn’t lifted the ceiling on government debt. (PDTB2, 0008)

	> Note: Differently from PDTB, annotate subordinating conjunctions only if they apply to the main predicate of the sentence.

The position of connectives in the utterance they modify is restricted to initial position for subordinating and coordinating conjunctions, but adverbials may also occur medially (or finally):

	- (31) Despite the economic slowdown, there are few clear signs that growth is coming to a halt. **As a result**, Fed officials may be divided over whether to ease credit. (PDTB2, 0072)

	- (32) The chief culprits, he says, are big companies and business groups that buy huge amounts of land “not for their corporate use, but for resale at huge profit.” . . . The Ministry of Finance, **as a result**, has proposed a series of measures that would restrict business investment in real estate . . . (PDTB2, 0761)

In line with Prasad et al. (2007), adverbials that do not denote relations between two utterances have not been annotated as discourse connectives. Interjections such as _well_ and focus markers such as _anyway_ or _now_, etc. are only to be annotated if they establish a relation between two utterances, not if they serve to indicate dialog act, organizational or focus structure of the discourse. Likewise, clausal adverbials such as _strangely_, _probably_, _frankly_, _in all likelihood_ etc. are not annotated as discourse connectives since they take a single utterance as argument.
	
	> Note: As a temporal expression, _now_ can be annotated if it serves to establish a comparison between an earlier (or a future) state and the current situation. 

Not all tokens of words and phrases that can serve as discourse markers actually do so: Some tokens can also serve other functions, e.g., _for_ can be a causal discourse marker (and then, be substituted with _because_), but also serve as a preposition indicating the beneficiary of an action. EXAMPLES. Likewise, discourse markers that serve to connect parts of the same utterance are beyond the scope of AURIS. Such expressions are not annotated as discourse connectives.

Because of the uncertainties of automated pre-annotation for discourse markers, automatically identified discourse markers are always marked by a question mark. To confirm a discourse marker, annotators should remove the question mark. Discourse markers with question marks are considered an error.

## Annotation of implicit discourse markers

If an utterance does not feature an explicit discourse marker, annotators should try to test whether an explicit discourse marker could be inserted (using a list of lexically-defined explicit connectives, following the order of discourse markers as given on that list):

1. check whether the preceding utterance could be an anchor
	1. by inserting the first discourse marker on the list, if that fails
	2. by inserting the second discourse marker, etc.
	3. if both utterances are connected by a coherence relation between two referring expressions, insert no marker, but annotate EntRel
2. if no discourse marker could be inserted, test the preceding utterance
	1. using the same procedure
3. iterate until an anchor and an implicit discourse marker have been found or no possible anchor can be expected anymore (e.g., because the text deals with different topics)

Prasad et al. 2007: "In Example (68), a causal relation is inferred between raising cash positions to record levels and high cash positions helping to buffer a fund, even though no Explicit connective appears in the text to express this relation. Similarly, in Example (69), a consequence relation is inferred between the increase in the number of rooms and the increase in the number of jobs, though no Explicit connective expresses this relation."

	- (68) Several leveraged funds don’t want to cut the amount they borrow because it would slash the income they pay shareholders, fund officials said. But a few funds have taken other defensive steps. Some have raised their cash positions to record levels. **[Implicit = because]** High cash positions help buffer a fund when the market falls. (PDTB2, 0983)

	- (69) The projects already under construction will increase Las Vegas’s supply of hotel rooms by 11,795, or nearly 20%, to 75,500. **[Implicit = so]** By a rule of thumb of 1.5 new jobs for each new hotel room, Clark County will have nearly 18,000 new jobs. (PDTB2, 0994)

> Note: Unlike PDTB2, the annotation of implicit relations is not limited to adjacent utterances.

## Alternative lexicalizations

Many researchers distinguish discourse markers and alternative lexicalizations, i.e., a phrasal expression that conveys the meaning of a discourse marker that could be used in its place in a more or less equivalent way (e.g., "This observation leads us to conclude that ..." in place of "Thus, ..."). If such phrases are no longer than 5 words, annotators should annotate such phrases as explicit discourse markers. If such phrases are longer than 5 words, proceed as follows:

- provide a common discourse marker that could be used in place of the alternative lexicalization, write it in **square brackets**, add the alternative lexicalization afterwards

If the discourse marker you provided could also be used *in addition to* the alternative lexicalization, then treat this as implicit discourse marker, i.e.,

- provide the discourse marker you inferred in round brackets. 

See the list of diagnostic markers in the appendix

> Note: We annotate at most one discourse marker per sentence. If multiple discourse markers apply, this defaults to the first discourse marker.

## Relations

> Note: ISO 24617-8 has been heavily criticized for being poorly defined (e.g., by Żurowski et al. 2023). We provide operationalizable definitions by exploiting the correspondence with established RST, SDRT and PDTB definitions as given by proponents of ISO SemAF. These definitions are primarily based on PDTB 2.0 (Prasad et al. 2007).

For asymmetric relations, we annotate the ISO SemAF role of the internal argument. For symmetric relations, we annotate the ISO SemAF relation at the second argument.

### PDTB

- **CONTINGENCY**
	- "the connective indicates that one of the situations described in Arg1 and Arg2 causally influences the other" (Prasad et al. 2007, p.28)
	- **Cause** 
		- "relating two situations via a direct cause-effect relation" (Prasad et al. 2007, p.26)
		- "the situations described in Arg1 and Arg2 are causally influenced and the two are not in a conditional relation. The directionality of causality is not specified at this level: when “Cause” is used in annotation, it means that the annotators could not uniquely specify its directionality." (Prasad et al. 2007, p.28)
		- **reason**
			- "the situation specified in Arg2 is interpreted as the cause of the situation specified in Arg1, as often with the connective _because_" (Prasad et al. 2007, p.26)
			- "the situation described in Arg2 is the cause and the situation described in Arg1 is the effect" (Prasad et al. 2007, p.29)
				- (102) Use of dispersants was approved **when** a test on the third day showed some positive results, officials said. (CONTINGENCY:Cause:reason) (PDTB2, 1347)
		- **result**
			- "the situation described in Arg2 is interpreted as the result of the situation presented in Arg1. A connective typically tagged as “result” is “as a result”." (Prasad et al. 2007, p.26)
			- "the situation in Arg2 is the effect brought about by the situation described in Arg1" (Prasad et al. 2007, p.29)
				- (103) In addition, its machines are typically easier to operate, so customers require less assistance from software. (CONTINGENCY:Cause:result) (PDTB2, 1887)
	- **Pragmatic Cause**
		- "Connectives can also be used to relate the use of the arguments of a connective to one another or the use of one argument with the sense of the other. For these rhetorical or pragmatic uses of connectives, we have defined pragmatic sense tags – specifically, “Pragmatic Cause”, “Pragmatic Condition”, “Pragmatic Contrast” and “Pragmatic Concession”." (Prasad et al. 2007, p. 27)
		- "no semantic distinction is made between the type “Pragmatic” and the subtype “justification”." (Prasad et al. 2007, p.29)
		- **justification**
			- "Arg1 expresses a claim and Arg2 provides justification for this claim, as shown in the use of ’because’ in (104). There is no causal influence between the two situations. ... Epistemic uses of the connective “because” are labelled as “Pragmatic cause:justification”. " (Prasad et al. 2007, p.29)
				- (104) Mrs Yeargin is lying. Implicit = because They found students in an advanced class a year earlier who said she gave them similar help. (CONTINGENCY:Pragmatic Cause:justification) (PDTB2, 0044)
	- **Condition**
		- "relating a hypothetical scenario with its (possible) consequence" (Prasad et al. 2007, p.26)
		- "“Condition” is used to describe all subtypes of conditional relations. In addition to causal influence, “Condition” allows some basic inferences about the semantic contribution of the arguments. Specifically, the situation in Arg2 is taken to be the condition and the situation described in Arg1 is taken to be the consequence, i.e., the situation that holds when the condition is true. Unlike “Cause”, however, the truth value of the arguments of a “Condition” relation cannot be determined independently of the connective." (Prasad et al. 2007, p.29)
		- **hypothetical**
			- "if Arg2 holds true, Arg1 is caused to hold at some instant in all possible futures. However, Arg1 can be true in the future independently of Arg2 ... The main difference between “hypothetical” and “general” is that, in the former, the causal relation is taken to hold at a single time." (Prasad et al. 2007, p.30)
				- (105) Both sides have agreed that the talks will be most successful if negotiators start by focusing on the areas that can be most easily changed. (CONTINGENCY:Condition:hypothetical) (PDTB2, 0082)
				- (106) In addition, Black & Decker had said it would sell two other undisclosed Emhart operations if it received the right price. (CONTINGENCY:Condition:hypothetical) (PDTB2, 0807)
		- **general**
			- "every time that ||Arg2|| holds true , ||Arg1|| is also caused to be true. Typically, “general” describes either a generic truth about the world or a statement that describes a regular outcome every time the condition holds true. ... in all possible futures, it is always the case that ||Arg2|| causes ||Arg1||. ... The main difference between “hypothetical” and “general” is that, in the former, the causal relation is taken to hold at a single time." (Prasad et al. 2007, p.30)
				- (107) That explains why the number of these wines is expanding so rapidly. But consumers who buy at this level are also more knowledgeable than they were a few years ago. “They won’t buy **if** the quality is not there,” said Cedric Martin of Martin Wine Cellar in New Orleans. (CONTINGENCY:Condition:general) (PDTB2, 0071)
		- **unreal present**
			- "Arg2 describes a condition that either does not hold at present (...) or is considered unlikely to hold (...) Arg1 describes what would also hold if Arg2 were true. The tag “unreal present” represents the semantics of conditional relations also known in the lingustic literature as present counterfactuals (...). The semantics for “unreal present” is a special case of the semantics for hypothetical." (Prasad et al. 2007, p.31)
				- (110) Of course, **if** the film contained dialogue, Mr. Lane’s Artist would be called a homeless person. (CONTINGENCY:Condition:unreal present) (PDTB2, 0039)
				- (111) I’m not saying advertising revenue isn’t important,” she says, “but I couldn’t sleep at night” if the magazine bowed to a company because they once took out an ad. (CONTINGENCY:Condition:unreal present) (PDTB2, 0062)
		- **unreal past**
			- "Arg2 describes a situation that did not occur in the past and Arg1 expresses what the consequence would have been if it had ... the situations described in Arg1 and Arg2 did not hold." (Prasad et al. 2007, p.31)
				- (112) “If I had come into Friday on margin or with very little cash in the portfolios, I would not do any buying. (CONTINGENCY:Condition:unreal past) (PDTB2, 2376)
		- **factual present**
			- "Arg2 is a situation that has either been presented as a fact in the prior discourse or is believed by somebody other than the speaker/writer. “Factual present” is really a special case of the subtype “hypothetical”. ... it also asserts that ||Arg2|| holds true or is believed by someone to hold true. (If ||Arg2|| indeed holds true, then ||Arg1|| is caused to be true.)" (Prasad et al. 2007, p.30-31)
				- (108) “I’ve heard that there is $40 billion taken in nationwide by boiler rooms every year,” Mr. McClelland says. “If that’s true, Orange County has to be at least 10% of that.” (CONTINGENCY:Condition:factual present) (PDTB2, 1568)
		- **factual past**
			- "“factual past” is similar to “factual present” except that in this case Arg2 describes a situation that is assumed to have taken place at a time in the past." (Prasad et al. 2007, p.31)
				- "In (109), for example, the speaker expresses in Arg2 what in the prior discourse is asssumed to have taken place, and in Arg1, a consequence that may subsequently occur assuming Arg2 holds." (Prasad et al. 2007, p.31)
					- (109) “If they had this much trouble with Chicago & North Western, they are going to have an awful time with the rest.” (CONTINGENCY:Condition:factual past) (PDTB2, 1464)
	- **Pragmatic Condition**
		- "Connectives can also be used to relate the use of the arguments of a connective to one another or the use of one argument with the sense of the other. For these rhetorical or pragmatic uses of connectives, we have defined pragmatic sense tags – specifically, “Pragmatic Cause”, “Pragmatic Condition”, “Pragmatic Contrast” and “Pragmatic Concession”." (Prasad et al. 2007, p. 27)
		- "instances of conditional constructions whose interpretation deviates from that of the semantics of “Condition”. Specifically, these are cases of Explicit _if_ tokens with Arg1 and Arg2 not being causally related. In all cases, Arg1 holds true independently of Arg2" (Prasad et al. 2007, p.31)
		- **relevance**
			- "The conditional clause in the “relevance” conditional (Arg2) provides the context in which the description of the situation in Arg1 is relevant. A frequently cited example for this type of conditional is (113) and a corpus example is given in (114). There is no causal relation between the two arguments." (Prasad et al. 2007, p.32)
				- (113) If you are thirsty, there’s beer in the fridge.
				- (114) If anyone has difficulty imagining a world in which history went merrily on without us, Mr. Gould sketches several. (CONTINGENCY:Pragmatic condition:relevance) (PDTB2, 1158)

		- **implicit assertion**
			- "special rhetorical uses of if-constructions when the intepretation of the conditional construction is an implicit assertion. In (115), for example, Arg1, O’ Connor is your man is not a consequent state that will result if the condition expressed in Arg2 holds true. Instead, the conditional construction in this case implicitly asserts that O’Connor will keep the crime rates high." (Prasad et al. 2007, p.32)
				- (115) In 1966, on route to a re-election rout of Democrat Frank O’Connor, GOP Gov. Nelson Rockefeller of New York appeared in person saying, “If you want to keep the crime rates high, O’Connor is your man.” (CONTINGENCY:Pragmatic Condition:implicit assertion) (PDTB2, 0041)

- **TEMPORAL**
	- "the connective indicates that the situations described in the arguments are related temporally. The class level tag “TEMPORAL” does not specify if the situations are temporally ordered or overlapping." (Prasad et al. 2007, p. 27)
	- **Asynchronous**
		- "the situations described in the arguments are ... temporally ordered" (Prasad et al. 2007, p.27)
		- **precedence**
			- "the situation in Arg1 precedes the situation described in Arg2, as _before_ does in (99)." (Prasad et al. 2007, p.28)
				- (99) But a Soviet bank here would be crippled unless Moscow found a way to settle the $188 million debt, which was lent to the country’s short-lived democratic Kerensky government **before** the Communists seized power in 1917. (TEMPORAL:Asynchronous:precedence) (PDTB2, 0035)

		- **succession**
			- "the situation described in Arg1 follows the situation described in Arg2, as _after_ does in (100)." (Prasad et al. 2007, p.28)
				- (100) No matter who owns PS of New Hampshire, **after** it emerges from bankruptcy proceedings its rates will be among the highest in the nation, he said. (TEMPORAL:Asynchronous:succession) (PDTB2, 0013)

	- **Synchronous**
		- "the situations described in the arguments are ... temporally overlapping ... The type “Synchronous” does not specify the form of overlap, i.e., whether the two situations started and ended at the same time, whether one was temporally embedded in the other, or whether the two crossed. Typical connectives tagged as “Synchronous” are while and when," (Prasad et al. 2007, p.27-28)
			- (101) Knowing a tasty – and free – meal when they eat one, the executives gave the chefs a standing ovation. (TEMPORAL:Synchrony) (PDTB2, 0010)

- **COMPARISON**
	- "the connective indicates that a discourse relation is established between Arg1 and Arg2 in order to highlight prominent differences between the two situations. Semantically, the truth of both arguments is independent of the connective or the established relation." (Prasad et al. 2007, p.32)
	- **Contrast**
		- "Arg1 and Arg2 share a predicate or property and a difference is highlighted with respect to the values assigned to the shared property. ...  neither argument describes a situation that is asserted on the basis of the other one. In this sense, there is no directionality in the interpretation of the arguments. This is an important difference between the interpretation of “Contrast” and “Concession”." (Prasad et al. 2007, p.32)
		- **juxtaposition**
			- "the connective indicates that the values assigned to some shared property are taken to be alternatives ... When the intended juxtaposition is not clear, the higher level tag “Contrast” is annotated." (Prasad et al. 2007, p.32-33)

				- (116) Operating revenue rose 69% to A$8.48 billion from A$5.01 billion. But the net interest bill jumped 85% to A$686.7 million from A$371.1 million. (COMPARISON:Contrast:juxtaposition) (PDTB2, 1449)

		- **opposition**
			- "the connective indicates that the values assigned to some shared property are the extremes of a gradable scale, e.g., tall-short, accept-reject etc. Note that the notion of gradable scale used in distinguishing “opposition” from “juxtaposition” strongly depends on the context where the sentence is uttered." (Prasad et al. 2007, p.33)

				- (117) Most bond prices fell on concerns about this week’s new supply and disappointment that stock prices didn’t stage a sharp decline. Junk bond prices moved higher, however. (COMPARISON:Contrast:opposition) (PDTB2, 1464)

	- **Pragmatic Contrast**
		- "Connectives can also be used to relate the use of the arguments of a connective to one another or the use of one argument with the sense of the other. For these rhetorical or pragmatic uses of connectives, we have defined pragmatic sense tags – specifically, “Pragmatic Cause”, “Pragmatic Condition”, “Pragmatic Contrast” and “Pragmatic Concession”." (Prasad et al. 2007, p. 27)
		- "the connective indicates a contrast between one of the arguments and an inference that can be drawn from the other, in many cases at the speech act level: The contrast is not between the situations described in Arg1 and Arg2." (Prasad et al. 2007, p.33)
			- (118) “It’s just sort of a one-upsmanship thing with some people,” added Larry Shapiro. “They like to talk about having the new Red Rock Terrace one of Diamond Creek’s Cabernets or the Dunn 1985 Cabernet, or the Petrus. Producers have seen this market opening up and they’re now creating wines that appeal to these people.” That explains why the number of these wines is expanding so rapidly. But consumers who buy at this level are also more knowledgeable than they were a few years ago. (COMPARISON:Pragmatic Contrast) (PDTB2, 0071)
	- **Concession**
		- "the difference [between Arg1 and Arg2 that -- CC] is highlighted ... are related to expectations raised by one argument which are then denied by the other." (Prasad et al. 2007, p.32)
		- "the connective indicates that one of the arguments describes a situation A which causes C, while the other asserts (or implies) ¬C. Alternatively, one argument denotes a fact that triggers a set of potential consequences, while the other denies one or more of them." (Prasad et al. 2007, p.34)
		- Instances have been found in the PDTB which are ambiguous between “expectation” and “contra-expectation”, where the context or the annotators’ world knowledge is not sufficient to specify the subtype, as in (121). Such cases are tagged as “Concession”.
			- (121) Besides, to a large extent, Mr. Jones may already be getting what he wants out of the team, even though it keeps losing. (COMPARISON:Concession) (PDTB2, 1411)
		- **expectation**
			- "Arg2 creates an expectation that Arg1 denies" (Prasad et al. 2007, p.34)
				- (119) Although the purchasing managers’ index continues to indicate a slowing economy, it isn’t signaling an imminent recession, said Robert Bretz, chairman of the association’s survey committee and director of materials management at Pitney Bowes Inc., Stamford, Conn. (COMPARISON:Concession:expectation) (PDTB2, 0036)
		- **contra-expectation**
			- "Arg1 creates an expectation that Arg2 denies" (Prasad et al. 2007, p.34)
				- (120) The Texas oilman has acquired a 26.2% stake valued at more than $1.2 billion in an automotive-lighting company, Koito Manufacturing Co. But he has failed to gain any influence at the company. (COMPARISON:Concession:contra-expectation) (PDTB2, 0082)
	- **Pragmatic Concession**
		- "Connectives can also be used to relate the use of the arguments of a connective to one another or the use of one argument with the sense of the other. For these rhetorical or pragmatic uses of connectives, we have defined pragmatic sense tags – specifically, “Pragmatic Cause”, “Pragmatic Condition”, “Pragmatic Contrast” and “Pragmatic Concession”." (Prasad et al. 2007, p. 27)
- **EXPANSION**
	- "relations which expand the discourse and move its narrative or exposition forward." (Prasad et al. 2007, p.34)
	- **Instantiation**
		- "the connective indicates that Arg1 evokes a set and Arg2 describes it in further detail. It may be a set of events (122), a set of reasons, or a generic set of events, behaviors, attitudes, etc. Typical connectives often tagged as “Instantiation” are _for example_, _for instance_ and _specifically_." (Prasad et al. 2007, p.34)
			- (122) He says he spent $300 million on his art business this year. **[Implicit = in particular]** A week ago, his gallery racked up a $23 million tab at a Sotheby’s auction in New York buying seven works, including a Picasso. (EXPANSION:Instantiation) (PDTB2, 0800)
	- **Restatement**
		- "the semantics of Arg2 restates the semantics of Arg1. It is inferred that the situations described in Arg1 and Arg2 hold true at the same time." (Prasad et al. 2007, p.35)
		- "The Type level tag “Restatement” is used when more than on subtype interpretation is possible, as in (129), where Arg2 can be interpreted as denoting what he said, or it can be interepreted as providing the same information from a different point of view, namely the speaker’s own words." (Prasad et al. 2007, p.36)
			- (129) He said the assets to be sold would be “non-insurance” assets, including a beer company and a real estate firm, and wouldn’t include any pieces of Farmers. Implicit = in other words “We won’t put any burden on Farmers,” he said. (EXPANSION:Restatement) (PDTB2, 2403)
		- **specification**
			- "Arg2 describes the situation described in Arg1 in more detail ... Typical connectives for “specification” are _specifically_, _indeed_ and _in fact_." (Prasad et al. 2007, p.35)
				- (123) A Lorillard spokewoman said, “This is an old story. **[Implicit = in fact]** We’re talking about years ago before anyone heard of asbestos having any questionable properties.” (EXPANSION:Restatement:specification) (PDTB2, 0003)
				- (124) An enormous turtle has succeeded where the government has failed: **[Implicit = specifically]** He has made speaking Filipino respectable. (EXPANSION:Restatement:specification) (PDTB2, 0804)
		- **equivalence**
			- "the connective indicates that Arg1 and Arg2 describe the same situation from different perspectives" (Prasad et al. 2007, p.35)
				- (126) Chairman Krebs says the California pension fund is getting a bargain price that wouldn’t have been offered to others. **In other words**: The real estate has a higher value than the pending deal suggests. (EXPANSION:Restatement:equivalence) (PDTB2, 	0331)
		- **generalization**
			- "the connective indicates that Arg2 summarizes Arg1, or in some cases expresses a conclusion based on Arg1. ... Typical connectives for “generalization” are _in sum_, _overall_, _finally_, etc." (Prasad et al. 2007, p.35)
				- (125) If the contract is as successful as some expect, it may do much to restore confidence in futures trading in Hong Kong. **[Implicit = in other words,]]** “The contract is definitely important to the exchange,” says Robert Gilmore, executive director of the Securities and Futures Commission. (EXPANSION:Restatement:generalization) (PDTB2, 0700)
	- **Alternative**
		- "the connective indicates that its two arguments denote alternative situations." (Prasad et al. 2007, p.36)
		- **conjunctive**
			- "the connective indicates that both alternatives hold or are possible" (Prasad et al. 2007, p.36)
				- (130) Today’s Fidelity ad goes a step further, encouraging investors to stay in the market **or** even to plunge in with Fidelity. (EXPANSION:Alternative:conjunctive) (PDTB2, 2201)
		- **disjunctive**
			- "two situations are evoked in the discourse but only one of them holds" (Prasad et al. 2007, p.36)
				- (131) Those looking for real-estate bargains in distressed metropolitan areas should lock in leases or buy now. (EXPANSION:Alternative:disjunctive) (PDTB2, 2444)
		- **chosen alternative**
			- "two alternatives are evoked in the discourse but only one is taken, as with the connective _instead_" (Prasad et al. 2007, p.36)
				- (132) Under current rules, even when a network fares well with a 100%-owned series – ABC, for example, made a killing in broadcasting its popular crime/comedy “Moonlighting” — it isn’t allowed to share in the continuing proceeds when the reruns are sold to local stations. **Instead**, ABC will have to sell off the rights for a one-time fee. (EXPANSION:Alternative:chosen alternative) (PDTB2, 2451)
	- **Exception**
		- "Arg2 specifies an exception to the generalization specified by Arg1 (...). In other words, Arg1 is false because Arg2 is true, but if Arg2 were false, Arg1 would be true." (Prasad et al. 2007, p.36)
			- (133) Boston Co. officials declined to comment on Moody’s action on the unit’s financial performance this year except to deny a published report that outside accountants had discovered evidence of significant accounting errors in the first three quarters’ results. (EXPANSION:Exception) (PDTB2, 1103)
	- **Conjunction**
		- "the situation described in Arg2 provides additional, discourse new, information that is related to the situation described in Arg1, but is not related to Arg1 in any of the ways described for other types of “EXPANSION”. (That is, the rough semantics of “Conjunction” is simply ||Arg1|| ∧ ||Arg2||.) ... Typical connectives for “Conjunction” are _also_, _in addition_, _additionally_, _further_, etc." (Prasad et al. 2007, p.37)
			- (134)Food prices are expected to be unchanged, but energy costs jumped as much as 4%, said Gary Ciminero, economist at Fleet/Norstar Financial Group. He also says he thinks “core inflation,” which excludes the volatile food and energy prices, was strong last month. (EXPANSION:Conjunction) (PDTB2, 2400)
	- **List**
		- "Arg1 and Arg2 are members of a list, defined in the prior discourse. “List” does not require the situations specified in Arg1 and Arg2 to be directly related." (Prasad et al. 2007, p.37)
			- (135)But other than the fact that besuboru is played with a ball and a bat, it’s unrecognizable: Fans politely return foul balls to stadium ushers; **[Implicit = and]** the strike zone expands depending on the size of the hitter; (EXPANSION:List) (PDTB2, 0037)
- **EntRel**

### SemAF

- **CAUSE**
	- **Reason**: In a `CAUSE` relation, the `Reason` provides a reason for the `Result` to come about or occur. (Bunt & Prasad 2016)
		- cf. PDTB Reason
		- cf. PDTB Justification
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

> Note: The relation definitions follow Prasad and Bunt (2015) and Bunt and Prasad (2016). RST, RSTDTB, SDRT and PDTB mapping follows Bunt and Prasad (2016).

> Note: Role labels are taken from ISO SemAF. The `Condition` relation corresponds to ISO SemAF CONDITION with internal argument role "Antecedent". The `Negated_Condition` relation corresponds to ISO SemAF NEGATIVE CONDITION with internal argument role "Negated_Antecedent". 

> Note: For `Feedback-act`, annotate if and only if turn-taking or interruptions occurred  

> Note: Consider replacing `Feedback-act` and `Dependent-act` annotations by dialogue act annotations.

> Note: Annotate Dependence relations only in the absence of explicit discourse markers, example:

	- P1: I can never find my remote control.	P2: That’s [because] they don’t have a fixed place.		(Reason, not Inform, from Butt & Prasad 2016)

### SemAF+PDTB

PDTB: Arg2 is internal argument, Arg1 is external

In the following, we refer to the internal argument as utterance, to the external argument as (contextual) anchor. The order of anchor and utterance is flexible. For implicit discourse markers, the anchor should generally precede the utterance, explicit discourse can be used by the speaker to underline that the anchor follows the utterance.

- **CAUSAL**: In a `CAUSAL` relation, the `Reason` provides a reason or justification for the `Result` to come about or occur. (cf. ISO SemAF CAUSE, Bunt & Prasad 2016)
	- **Reason**: 
		- the situation described in the utterance is the reason (cause or justification) for the situation described in the anchor, as typically expressed with the connective _because_ (cf. PDTB Reason, Prasad et al. 2007, p.26, 29)
			
			- (102) Use of dispersants was approved **when** a test on the third day showed some positive results, officials said. (CONTINGENCY:Cause:reason) (PDTB2, 1347)

		- Note that `Reason` also includes epistemic, rhetorical or pragmatic uses of causal connectives, esp. where the utterance provides justification for a claim expressed in the anchor, as marked, for example, with the connective _because_. Ex. (104) illustrates such a case  Here, there is no causal influence between the two situations. ... Epistemic uses of the connective “because” are labelled as “Pragmatic cause:justification”. " (PDTB Justification/Pragmatic Cause, Prasad et al. 2007, p.29)
				- (104) Mrs Yeargin is lying. [Implicit = because] They found students in an advanced class a year earlier who said she gave them similar help. (CONTINGENCY:Pragmatic Cause:justification) (PDTB2, 0044)

		- cf. RST Vol. cause, Non-vol. cause, Evidence, Justify
		- cf. RSTDTB Cause, Evidence, Explanation-argumentation, Reason
		- cf. SDRT Explanation (DISCOR Explanation, ANNODIS Explanation)
	- **Result**: The situation described in the utterance is interpreted as the result (effect) of the situation presented in the anchor. A typical discourse marker is “as a result”. (cf. PDTB Result, Prasad et al. 2007, p.26,29)
		- (103) In addition, its machines are typically easier to operate, **so** customers require less assistance from software. (PDTB2, 1887)
		- cf. RST Vol. result, Non-vol. result
		- cf. RSTDTB Consequence, Result
		- cf. SDRT Result (DISCOR Result, ANNODIS Result)
	- **Cause**: For causal relations between utterance and anchor, annotators should normally apply `Reason` or `Result`. When `Cause` is used in annotation, it means that the annotators could not uniquely specify the directionality, but that they found the causal association with the anchor to be the primary discourse relation for the utterance at hand. (cf. Prasad et al. 2007, p.28)
- **CONDITION**
	- a `CONDITION` relation a hypothetical (unrealized) scenario with its (possible) consequence. The consequence is a situation that holds when the condition is true. This involves causal influence, but unlike `CAUSAL` relations, the truth value of the arguments of a `CONDITION` relation cannot be determined independently of the connective. (PDTB Condition, Prasad et al. 2007, p.26,29). 
	- **Condition** 
		- the utterance represents a `Condition`, i.e., an unrealized situation which, when realized, would lead to the `Consequence` described in the anchor. If the utterance holds true, the anchor is caused to hold true at some instant in all possible futures. This can be a generic truth about the world (PDTB Condition/generic), a statement that describes a regular outcome every time the condition holds true (PDTB Condition/generic) or a single time that this is the case (PDTB Condition/general). Following ISO SemAF, this is independent of whether the `Consequence` is believed to be true (PDTB Condition/factual present, Condition/factual past) or not (counterfactuals, PDTB Condition/unreal present, PDTB Condition/unreal past). If the condition is not true, the anchor should express what the consequences would had been if it had. Note that it is possible that the anchor can be true in the future independently of the utterance. (PDTB Condition, Prasad et al. 2007, p.30-31; Bunt & Prasad 2016, SemAF: Condition/Antecedent)

			- (108') "Orange County is taking in at least $4 billion nationwide by boiler rooms every year", Mr. McClelland says. "**Because** I've heard that there is $40 billion in total, and that's 10%." (reformulated after PDTB2, 1568, cf. 108)

		- `Condition` also includes rhetorical or pragmatic uses of conditional constructions whose interpretation deviates from the standard semantics described above. Specifically, these are cases of explicit _if_ tokens although utterance and anchor are not causally related, but presented as if they were. In all cases, the anchor holds true independently of the anchor, there is no causal relation between the two arguments. We distinguish two primary cases:
			- _relevant context information_: The utterance provides the context in which the description of the situation in anchor is relevant. A frequently cited example for this type of conditional is (113). Note that this is an intrasentential relation in this case and not to be annotated in AURIS.
				- (113) If you are thirsty, there’s beer in the fridge. (constructed)
			- _implicit assertion_: refers to a special use of if-constructions when the conditional involves an (implicit) assertion. In (115), the utterance ("O’ Connor is your man") is not a consequent state that will result if the condition expressed in the anchor holds true. Instead, the discourse marker _if_ in this case implicitly asserts that O’Connor will keep the crime rates high. Again, note that this is an intrasentential example. To be replaced by an intersentential relation. 
				- (115) In 1966, on route to a re-election rout of Democrat Frank O’Connor, GOP Gov. Nelson Rockefeller of New York appeared in person saying, “**If** you want to keep the crime rates high, O’Connor is your man.” (PDTB2, 0041)

			(PDTB Condition, Pragmatic Condition, Prasad et al. 2007, p.27,31-32)

		- cf. PDTB Condition/hypothetical, Condition/general, Condition/unreal present, Condition/factual present.
		- cf. RST Condition
		- cf. RSTDTB Condition, ?Hypothetical
		- cf. ANNODIS ?Conditional

	- **Consequence**
		- The anchor represents a `Condition`, i.e., an unrealized situation which, when realized, would lead to the `Consequence` described in the utterance. As for the logical relation between `Condition` and `Consquence`, the same conditions hold as described above (cf. Bunt & Prasad 2016, SemAF: Condition/Consequent).

			- (108) “I’ve heard that there is $40 billion taken in nationwide by boiler rooms every year,” Mr. McClelland says. “**If that’s true**, Orange County has to be at least 10% of that.” (PDTB2, 1568)

			The example shows an alternative lexicalization. A possible discourse marker would have been _So,_. 

		- ?cf. RSTDTB Contingency
		- cf. SDRT Consequence (DISCOR Consequence)
- **NEGATIVE_CONDITION**: In a `NEGATIVE_CONDITION` relation, the `Negated_Condition` is an unrealized situation which, when **not** realized, would lead to the `Consequent`. (Bunt & Prasad 2016)
	- **Negated_Condition**: The utterance describes an unrealized situation which, when not realized, leads to the `Consequence` described in the anchor. A diagnostic discourse marker is _unless_.
		- cf. ANNODIS ?Conditional
		- cf. PDTB Condition
	- **Consequence**: The anchor describes an unrealized situation which, when not realized, leads to the `Consequence` described in the utterace. A diagnostic discourse marker is _otherwise_.
		- cf. ?RST Otherwise
		- cf. ?RSTDTB Otherwise
		- cf. SDRT Consequence (DISCOR Consequence)
- **PURPOSE** In a `PURPOSE` relation, the `Goal` enables the `Enablement`. (Bunt & Prasad 2016) This relation is similar to `CAUSAL` and `CONDITION` relations, the main difference is that the former are neutral with respect to individual engagement whereas `PURPOSE` relations presume some level of agency on behalf of the speaker, the hearer or another agent addressed or involved in the situation described.
	- Note: There is no clear PDTB2 counterpart. **TODO** check RST/RSTDTB Purpose
	- cf. RST ?Purpose, RSTDTB ?Purpose
	- **Goal**: The utterance represents a goal (purpose) enabled by the anchor.
		- cf. SDRT Explanation (DISCOR Explanation, ANNODIS Goal)
		- cf. PDTB Result
	- **Enablement**: The utterance describes a situation that enables the goal (purpose) described in the anchor.

- **MANNER**, cf. SDRT (ANNODIS, DISCOR) Elaboration
	- **Means**: In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs. (Bunt & Prasad 2016)
		- cf. RSTDTB Means, ?Manner
	- **Achievement**: In a `MANNER` relation, the `Means` argument describes a way in which the `Achievement` comes about or occurs. (Bunt & Prasad 2016)

- **CONCESSION**
	- `CONCESSION` is an expected causal relation between two arguments, where the `Expectation-raiser` is expected to cause the situation described in the other argument, but is cancelled or denied by the `Contra-expectation` argument. Concession highlights a difference between utterance and anchor where expectations raised by one argument are then denied by the other. The connective indicates that one of the arguments describes a situation A which causes C, while the other asserts (or implies) ¬C. Alternatively, one argument denotes a fact that triggers a set of potential consequences, while the other denies one or more of them. (cf. Bunt & Prasad 2016, Prasad et al. 2007, p.32,34) A diagnostic discourse marker (either at `Expectation-raiser` or `Contra-expectation`) is _although_, a diagnostic discourse marker at Contra-expectation is _however_.

	Note that concessive connectives can also be used in a rhetorical or pragmatic way where their semantic conditions do not hold. Such cases of "apparent Concession" are included under `CONCESSION`, as well, but MUST be documented in comments (cf. Prasad et al. 2007, p. 27)	

	- cf. SDRT (DISCOR, ANNODIS) Contrast
	- **Expectation-raiser**: The utterance creates an expectation (a situation that is expected to cause the situation described in the other argument) that is cancelled or denied by the anchor. (cf. Bunt & Prasad 2016; PDTB "expectation", Prasad et al. 2007, p.34)

		- (119) **Although** the purchasing managers’ index continues to indicate a slowing economy, it isn’t signaling an imminent recession, said Robert Bretz, chairman of the association’s survey committee and director of materials management at Pitney Bowes Inc., Stamford, Conn. (PDTB2, 0036; INTRASENTENTIAL)

		- cf. RST ?Concession
		- cf. RSTDTB ?Concession, ?Antithesis, ?Preference
		- cf. PDTB Expectation

	- **Contra-expectation**: The utterance cancels or denies a situation that is expected after processing the anchor. This corresponds to the "Expecation-denier" role in Bunt & Prasad (2016), clif. Prasad et al. (2007, p.34) A diagnostic discourse marker of contra-expectation is _however_. Note that _but_, taken as diagnostic discourse marker of `CONTRAST` is usually also applicable to `CONCESSION`. Annotate `CONCESSION` for cases in which `however` can be used in place of `but`.

		- (120) The Texas oilman has acquired a 26.2% stake valued at more than $1.2 billion in an automotive-lighting company, Koito Manufacturing Co. **But** he has failed to gain any influence at the company. (PDTB2, 0082)

		- cf. RST ?Concession
		- cf. RSTDTB ?Concession, ?Antithesis, ?Preference
		- cf. PDTB Contra-Expectation

	- **Concession**: Instances which are ambiguous between “expectation” and “contra-expectation”, where the context or the annotators’ world knowledge is not sufficient to specify the subtype are tagged as `CONCESSION` (Prasad et al. 2007, p.34)

		- (121) Besides, to a large extent, Mr. Jones may already be getting what he wants out of the team, **even though** it keeps losing. (COMPARISON:Concession) (PDTB2, 1411)

- **CONTRAST**: `CONTRAST` is a symmetric relation in which one or more differences between the internal argument and the external argument are highlighted with respect to what each predicates as a whole or to some entities they mention. Semantically, the truth of both arguments is independent of the connective or the established relation (Bunt & Prasad 2016, Prasad et al. 2007, p.32). In `CONTRAST`, the utterance and the anchor share a predicate or property and a difference is highlighted with respect to the values assigned to the shared property. However, neither argument describes a situation that is asserted on the basis of the other one, and thus, there is no directionality in the interpretation of the arguments. This is the main difference in comparison with the otherwise similar `CONCESSION` relation. (PDTB2 Contrast, Prasad et al. 2007, p.32) A diagnostic discourse marker for contrast is _but_.
	- This includes cases in which the connective indicates that the values assigned to some shared property are taken to be alternatives ("juxtaposition", Prasad et al. 2007, p.32-33).

		- (116) Operating revenue rose 69% to A$8.48 billion from A$5.01 billion. **But** the net interest bill jumped 85% to A$686.7 million from A$371.1 million. (PDTB2 1449)

	- This also includes cases in which the connective indicates that the values assigned to some shared property are the extremes of a gradable scale, e.g., _tall-short_, _accept-reject_, etc. ("opposition", Prasad et al. 2007, p.33)

		- (117) Most bond prices fell on concerns about this week’s new supply and disappointment that stock prices didn’t stage a sharp decline. Junk bond prices moved higher, **however**. (PDTB2, 1464)

	- Note that explicit discourse markers can also be used to underline a `CONTRAST` relation that does not hold between utterance and anchor, but between one of the arguments and an inference that can be drawn from the other, in many cases at the speech act level ("pragmatic contrast", Prasad et al. 2007, p.33)

		- (118) “It’s just sort of a one-upsmanship thing with some people,” added Larry Shapiro. “They like to talk about having the new Red Rock Terrace one of Diamond Creek’s Cabernets or the Dunn 1985 Cabernet, or the Petrus. Producers have seen this market opening up and they’re now creating wines that appeal to these people.” That explains why the number of these wines is expanding so rapidly. **But** consumers who buy at this level are also more knowledgeable than they were a few years ago. (PDTB2, 0071)

	- cf. RST Contrast
	- cf. RSTDTB Comparison
	- cf. SDRT (DISCOR, ANNODIS) Contrast
	- cf. PDTB Justaposition, Opposition

- **EXCEPTION**: In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't. (Bunt & Prasad 2016)
	
	- **Regular**: In an `EXCEPTION` relation, the `Regular` argument evokes a set of circumstances in which the described situation holds, while the `Exception` argument indicates one or more instances where it doesn't (Bunt & Prasad 2016). Not clear whether this situation exists in AURIS, as it requires a discourse marker to mark the regular rather than the exception. It could exist in cases in which paired discourse markers (like _either ... or_ or _on the one hand ... on the other hand_) mark `EXCEPTION` relations.

	- **Exception**: The utterances specifies an exception to the generalization specified by the anchor. In other words, the situation described in the anchor is false because the sitation described in the utterance is true (but if the utterance were false, the anchor would be true). (Prasad et al. 2007, p.36)
		
		- (133) Boston Co. officials declined to comment on Moody’s action on the unit’s financial performance this year **except** to deny a published report that outside accountants had discovered evidence of significant accounting errors in the first three quarters’ results. (PDTB2, 1103)

		- cf. PDTB Exception

- **SIMILARITY**: `SIMILARITY` is a symmetric relation in which one or more similarities between the utterance and the anchor are highlighted with respect to what each predicates as a whole or to some entities they mention (Bunt & Prasad 2016). 

	- PDTB2 Conjunction: Bunt & Prasad (2016) provide no other PDTB counterpart but PDTB2 conjunction. But this seems to be incorrect as it has a much looser definition closer to SDRT Narration: The situation described in the utterance provides additional, discourse new, information that is related to the situation described in the anchor, but is not related to the anchor in any other, more specific discourse relation. The semantics are thus no more than that of a logical ∧ (and). Diagnostic connectives are _also_, _in addition_, _additionally_, _further_, etc. ("conjunction", Prasad et al. 2007, p.37)

		- (134) Food prices are expected to be unchanged, but energy costs jumped as much as 4%, said Gary Ciminero, economist at Fleet/Norstar Financial Group. He **also** says he thinks “core inflation,” which excludes the volatile food and energy prices, was strong last month. (PDTB2 conjunction, 2400)

	- cf. RSTDTB Analogy, Proportion 
	- cf. SDRT (ANNODIS, DISCOR) Parallel
	- cf. PDTB Conjunction
	- Note: If the PDTB2 definition is adopted, SIMILARITY is to be annotated after anything else.

- **SUBSTITUTION**: In `SUBSTITUTION`, two alternatives are evoked in the discourse but only one is taken, as with the connective _instead_" (PDTB2 chosen alternative, Prasad et al. 2007, p.36)
	- **Disfavoured-alternative**: In a `SUBSTITUTION` relation, both arguments describe alternative situations, with `Disfavoured-alternative` being the disfavored or rejected alternative. (Bunt & Prasad 2016)
		- cf. RST ?Antithesis
	- **Favoured-alternative**: In a `SUBSTITUTION` relation, both arguments describe alternative situations, with `Favoured-alternative` being the favored or chosen alternative. (Bunt & Prasad 2016)

		- (132) Under current rules, even when a network fares well with a 100%-owned series – ABC, for example, made a killing in broadcasting its popular crime/comedy “Moonlighting” — it isn’t allowed to share in the continuing proceeds when the reruns are sold to local stations. **Instead**, ABC will have to sell off the rights for a one-time fee. (PDTB2, 2451)

		- cf. RST ?Antithesis
		- cf. PDTB Chosen Alternative
- **CONJUNCTION**: `CONJUNCTION` is a symmetric relation in which the internal and the external arguments bear the same relation to some other situation evoked in the discourse. Their conjunction indicates that they are doing the same thing with respect to that situation, or are doing it together. (Bunt & Prasad 2016)
	- Bunt and Prasad (2016) put PDTB List here:

		- "Arg1 and Arg2 are members of a list, defined in the prior discourse. “List” does not require the situations specified in Arg1 and Arg2 to be directly related." (Prasad et al. 2007, p.37)
			
			- (135) But other than the fact that besuboru is played with a ball and a bat, it’s unrecognizable: Fans politely return foul balls to stadium ushers; **[Implicit = and]** the strike zone expands depending on the size of the hitter; (EXPANSION:List) (PDTB2, 0037)

	- Bunt & Prasad (2016) also put PDTB2 conjunction here. But this seems to be incorrect as it has a much looser definition closer to SDRT Narration: The situation described in the utterance provides additional, discourse new, information that is related to the situation described in the anchor, but is not related to the anchor in any other, more specific discourse relation. The semantics are thus no more than that of a logical ∧ (and). Diagnostic connectives are _also_, _in addition_, _additionally_, _further_, etc. ("conjunction", Prasad et al. 2007, p.37)

		- (134) Food prices are expected to be unchanged, but energy costs jumped as much as 4%, said Gary Ciminero, economist at Fleet/Norstar Financial Group. He **also** says he thinks “core inflation,” which excludes the volatile food and energy prices, was strong last month. (PDTB2 conjunction, 2400)

	- cf. RST Joint
	- cf. RSTDTB List
	- cf. SDRT (DISCOR, ANNODIS) Continuation
	- cf. PDTB Conjunction, List

	- Note: because of the largely underspecified semantics (if the PDTB definition is adopted), this must be annotated after anything else (except for SIMILARITY, maybe).

- **DISJUNCTION**: `DISJUNCTION` is a symmetric relation in which the utterance and the anchor denote alternative situations (Bunt & Prasad 2016; Prasad et al. 2007, p.36). Following ISO SemAF, we do not distinguish as to whether both situations can hold simultaneously (logical or) or they are mutually exclusive (exclusive or). A diagnostic discourse marker is _or_:

	- (130) Today’s Fidelity ad goes a step further, encouraging investors to stay in the market **or** even to plunge in with Fidelity. (both alternatives [can] hold, PDTB2 conjunctive, 2201)

	- (131) Those looking for real-estate bargains in distressed metropolitan areas should lock in leases or buy now. (only one alternative holds, exclusie or, PDTB2 disjunctive, 2444)

	- cf. RST Joint
	- cf. RSTDTB Disjunction
	- cf. SDRT (DISCOR, ANNODIS) Alternation
	- cf. PDTB Disjunctive, Conjunctive
- **EXEMPLIFICATION**: In an `EXEMPLICATION` relation, the `Set` describes a set of situations; the `Instance` is an element of that set (Bunt & Prasad 2016).

	- **Set**: In an `EXEMPLICATION` relation, the `Set` describes a set of situations; the `Instance` is an element of that set (Bunt & Prasad 2016). It is not clear wether this relation exists in AURIS, because PDTB2 does not provide designated discourse markers for this constellation. It might be relevant for paired discourse markers.

	- **Instance**:	The anchor evokes a set and the utterance describes it in further detail. It may be a set of events, a set of reasons, or a generic set of events, behaviors, attitudes, etc. Diagnostic discourse markes are _for example_, _for instance_ and _specifically_. (PDTB2 Instantiation, Prasad et al. 2007, p.34)

		- (122) He says he spent $300 million on his art business this year. **[Implicit = in particular]** A week ago, his gallery racked up a $23 million tab at a Sotheby’s auction in New York buying seven works, including a Picasso. (PDTB2, 0800)

		- cf. RST Elaboration (set-member)
		- cf. RSTDTB Elaboration set-member, Example
		- cf. SDRT (DISCOR, ANNODIS) Elaboration
		- cf. PDTB Instantiation

- **ELABORATION**: In an `ELABORATION` relation, both arguments are the same situation, but the `Specific` argument contains more detail than the `Broad` argument. (Bunt & Prasad 2016)
	- **Broad**: The utterance describes the same situation as the anchor, but the anchor provides more detail. Typically, the utterance summarizes the anchor, or in some cases expresses a conclusion or generalization based on the anchor. Diagnostic discourse markers include _in sum_, _overall_, _finally_, etc. (Bunt & Prasad 2016; PDTB2 Restatement/generalization in Prasad et al. 2007, p.35)
		
		- (125) If the contract is as successful as some expect, it may do much to restore confidence in futures trading in Hong Kong. **[Implicit = in other words,]]** “The contract is definitely important to the exchange,” says Robert Gilmore, executive director of the Securities and Futures Commission. (PDTB2, 0700)

		- cf. PDTB Generalization

	- **Specific**: The utterance describes the situation described in the anchor in more detail. Diagnostic discourse markers include _specifically_, _indeed_ and _in fact_." (PDTB Restatement/specification, Prasad et al. 2007, p.35)
		
		- (123) A Lorillard spokewoman said, “This is an old story. **[Implicit = in fact]** We’re talking about years ago before anyone heard of asbestos having any questionable properties.” (PDTB2, 0003)
		
		- (124) An enormous turtle has succeeded where the government has failed: **[Implicit = specifically]** He has made speaking Filipino respectable. (PDTB2, 0804)

		- cf. RST Elaboration
		- cf. RSTDTB Conclusion, Elaboration general-specific, Elaboration whole-part, Elaboration process-step
		- cf. SDRT (DISCOR, ANNODIS) Elaboration
		- cf. PDTB Specification

- **RESTATEMENT**: `RESTATEMENT` is a symmetric relation in which the utterance describes the same situation as the anchor, but from different perspectives, e.g., when describing the same situation as presented before using the speaker’s own words. It is inferred that the situations described in anchor and utterance hold true at the same time. (Bunt & Prasad 2016; PDTB2 Restatement/equivalence, Prasad et al. 2007, p.35-36). A diagnostic discourse marker is _in other words_.

	- (126) Chairman Krebs says the California pension fund is getting a bargain price that wouldn’t have been offered to others. **In other words**: The real estate has a higher value than the pending deal suggests. (PDTB2, 0331)

	- (129) He said the assets to be sold would be “non-insurance” assets, including a beer company and a real estate firm, and wouldn’t include any pieces of Farmers. **[Implicit = in other words]** “We won’t put any burden on Farmers,” he said. (PDTB2, 2403)

	- cf. RST Restatement
	- cf. RSTDTB Summary
	- cf. SDRT (DISCOR, ANNODIS) Elaboration
	- cf. PDTB Equivalence

- **SYNCHRONY**: `SYNCHRONY` applies if the situations described in the utterance and the anchorhave some degree of temporal overlap, i.e., if the two situations started and ended at the same time, if one was temporally embedded in the other, or if the two crossed. Diagnostic connectives are _while_ and _when_ (Bunt & Prasad 2016; PDTB2 Synchronuous in Prasad et al. 2007, p.27-28). 

	- (101) Knowing a tasty – and free – meal **when** they eat one, the executives gave the chefs a standing ovation. (PDTB2, 0010, INTRASENTENTIAL)

	- cf. RSTDTB Temporal-same-time
	- cf. PDTB Synchronous

- **ASYNCHRONY**: the situation described in utterance stands in a temporal order with the situation described in the anchor, i.e., the role `Before` temporally precedes the `After` role. (Bunt & Prasad 2016) (cf. Prasad et al. 2007, p.27).

	- cf. RST Sequence
	- **Before**: The situation described in the utterance temporally precedes the situation described in the anchor. A diagnostic discourse marker is _before_ (Bunt & Prasad 2016; PDTB2 precedence in Prasad et al. 2007, p.28)
		
		- (99) But a Soviet bank here would be crippled unless Moscow found a way to settle the $188 million debt, which was lent to the country’s short-lived democratic Kerensky government **before** the Communists seized power in 1917. (PDTB2, 0035, INTRASENTENTIAL)

		- cf. RSTDTB Temporal-before, Inverted-sequence
		- cf. DISCOR Precondition, ANNODIS Flashback
		- cf. PDTB Precedence

	- **After**: The situation described in the anchor temporally precedes the situation described in the utterance (Bunt & Prasad 2016; PDTB2 succession in Prasad et al. 2007, p.28). A diagnostic discourse marker is _after_.

		- (100) No matter who owns PS of New Hampshire, **after** it emerges from bankruptcy proceedings its rates will be among the highest in the nation, he said. (PDTB2, 0013, INTRASENTENTIAL)

		- cf. RSTDTB Temporal-after, Sequence
		- cf. SDRT (DISCOR, ANNODIS) Narration
		- cf. PDTB Succession
- **EXPANSION**: In an `EXPANSION` relation, the `Entity-description` argument provides further description about some entity or entities in the `Foreground`, expanding the narrative forward of which `Foreground` is a part, or expanding on the setting relevant for interpreting the `Foreground`. Utterance and anchor describe distinct situations (Bunt & Prasad 2016).
	- **Foreground**: The utterance introduces the entity or entities that are elaborated in the anchor. In AURIS, this role probably does not exist as a discourse marker, unless a dedicated discourse marker can be found that marks the `Foreground` rather than (or in addition to) the `Entity-description`. 
	- **Entity-description**: The utterance argument provides further description about some entity or entities in the anchor, expanding the narrative forward of which anchor is a part, or expanding on the setting relevant for interpreting the anchor. Utterance and anchor describe different situations (Bunt & Prasad 2016).
		- cf. RST Elaboration (object-attribute)
		- cf. RSTDTB Elaboration object-attribute, Elaboration additional
		- cf. SDRT Background, Elaboration (DISCOR Commentary, Attribution, Source; ANNODIS Comment, Attribution, Frame, Temporal-location)
		- cf. PDTB EntRel: "for cases where only an
entity-based coherence relation could be perceived between the sentences" (Prasad et al. 2007, p.18)
			- "EntRel captures cases where the implicit relation between adjacent sentences is not between their AO interpretations, but is rather a form of entity-based coherence (...) in which the same entity is realized in both sentences, either directly (...) or indirectly (...). Note that entity realization here also includes reification of an abstract object (AO) mentioned in the first sentence, such as with the demonstrative _this_ in Example (92), and the definite description _the appointments_ in Example (93). ... " (Prasad et al. 2007, p.23-25)

				- (89) Hale Milgrim, 41 years old, senior vice president, marketing at Elecktra Entertainment Inc., was named president of Capitol Records Inc., a unit of this entertainment concern. **[EntRel]** Mr. Milgrim succeeds David Berman, who resigned last month. (PDTB2 0945)

				- (90) The purchase price was disclosed in a preliminary prospectus issued in connection with MGM Grand’s planned offering of six million common shares. **[EntRel]** The luxury airline and casino company, 98.6%-owned by investor Kirk Kerkorian and his Tracinda Corp., earlier this month announced its agreements to acquire the properties, but didn’t disclose the purchase price. (PDTB2 0981)

				- (91) Last year the public was afforded a preview of Ms. Bartlett’s creation in a table-model version, at a BPC exhibition. **[EntRel]** The labels were breathy: “Within its sheltering walls is a microcosm of a thousand years in garden design ... At the core of it all is a love for plants.” (PDTB2, 0984)

				- (92) She has done little more than recycle her standard motifs – trees, water, landscape fragments, rudimentary square houses, circles, triangles, rectangles – and fit them into a grid, as if she were making one of her gridded two-dimensional works for a gallery wall. But for South Gardens, the grid was to be a 3-D network of masonry or hedge walls with real plants inside them. **[EntRel]** In a letter to the BPCA, kelly/varnell called this “arbitrary and amateurish.” (PDTB2 0984)

				- (93) Ronald J. Taylor, 48, was named chairman of this insurance firm’s reinsurance brokerage group and its major unit, G.L. Hodson & Son Inc. Robert G. Hodson, 65, retired as chairman but will remain a consultant. Stephen A. Crane, 44, senior vice president and chief financial and planning officer of the parent, was named president and chief executive of the brokerage group and the unit, succeeding Mr. Taylor. **[EntRel]** The appointments are effective Nov. 1. (PDTB2 0948)

				- (94) Proceeds from the offering are expected to be used for remodeling the company’s Desert Inn resort in Las Vegas, refurbishing certain aircraft of the MGM Grand Air unit, and to acquire the property for the new resort. **[EntRel]** The company said it estimates the Desert Inn remodeling will cost about $32 million, and the refurbishment of the three DC-8-62 aircraft, made by McDonnell Douglas Corp., will cost around $24.5 million. (PDTB2 0981)

				If an entity relation holds between the utterance and several candidate anchors (as in ex. 95), annotate the relation to the closest anchor candidate:

				- (95) HOLIDAY ADS: Seagram will run two interactive ads in December magazines promoting its Chivas Regal and Crown Royal brands. The Chivas ad illustrates – via a series of pullouts – the wild reactions from the pool man, gardener and others if not given Chivas for Christmas. The three-page Crown Royal ad features a black-and-white shot of a boring holiday party – and a set of colorful stickers with which readers can dress it up. **[EntRel]** Both ads were designed by Omnicom’s DDB Needham agency. (PDTB2, 0989)

- **FUNCTIONAL_DEPENDENCE**
	- **Antecedent-act**: External argument of a functional dependence, precedes the internal argument. (Not to be annotated.) (Bunt & Prasad 2016)
	- **Dependent-act**: In a `FUNCTIONAL_DEPENDENCE` relation, the `Dependent-act` is a dialogue act with a responsive communicative function; the `Antecedent-act` is the dialogue act(s) that the `Dependent-act` responds to. (Bunt & Prasad 2016)
- **FEEDBACK_DEPENDENCE**
	- **Feedback-scope**: External argument of a feedback dependence, precedes the internal argument. (Not to be annotated.) (Bunt & Prasad 2016)
	- **Feedback-act**:	In a `FEEDBACK_DEPENDENCE` relation, the `Feedback-act` that provides or elicits information about the understanding or evaluation by one of the dialogue participants of the `Feedback-scope` argument, a communicative event that occurred earlier in the discourse. (Bunt & Prasad 2016)

The PDTB2 top-level relations have not been mapped to SemAF roles:

	- **CONTINGENCY**
		- "the connective indicates that one of the situations described in Arg1 and Arg2 causally influences the other" (Prasad et al. 2007, p.28)

	- **TEMPORAL**
		- "the connective indicates that the situations described in the arguments are related temporally. The class level tag “TEMPORAL” does not specify if the situations are temporally ordered or overlapping." (Prasad et al. 2007, p. 27)

	- **COMPARISON**
		- "the connective indicates that a discourse relation is established between Arg1 and Arg2 in order to highlight prominent differences between the two situations. Semantically, the truth of both arguments is independent of the connective or the established relation." (Prasad et al. 2007, p.32)

	- **EXPANSION**
		- "relations which expand the discourse and move its narrative or exposition forward." (Prasad et al. 2007, p.34)


## Troubleshooting

- pairwise discourse markers: Annotate independently. As both parts refer to each other, this creates a cycle in the annotation.

	- (22) **On the one hand**, Mr. Front says, it would be misguided to sell into “a classic panic.” **On the other hand**, it’s not necessarily a good time to jump in and buy. (PDTB2, 2415)

- discourse markers of attribution verbs: If a discourse marker is (correctly or not) attached to an attribution verb, but the main predicate of an utterance is a dependent of the attribution verb, this discourse marker is taken to refer to the main predicate. The primary discourse marker is identified by means of the following preferences:

	- MAIN CLAUSE > DEPENDENT CLAUSE > DEPENDENT of DEPENDENT CLAUSE
	- within a clause: first > second 

	- (22) **On the one hand**, Mr. Front says, it would be misguided to sell into “a classic panic.” 

- Apparent cases of multiple utterance. In the following example, utterances 4.-7. constitute an elaboration of 3. However, we adopt the SDRT view on such constellations, that is, if 4 elaborates 3 and 5 elaborates 3, a narration relation hold between 4 and 5. Because we annotate the closest anchor for each utterance, only the narration is to be annotated, but not the elaboration. (Note that these are SDRT relations, but the argumentation holds for ISO SemAF labels, as well.)

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


## References

- Sebastian Żurowski, Daniel Ziembicki, Aleksandra Tomaszewska, Maciej Ogrodniczuk and Agata Drozd (2023), Adopting ISO 24617-8 for Discourse Relations Annotation in Polish: Challenges and Future Directions. In Proceedings of the 4th Conference on Language, Data and Knowledge (pp. 482-492).

- Bunt, Harry and Prasad, Rashmi (2016), ISO DR-Core (ISO 24617-8), Core concepts for the annotation of discourse relations, In: Proceedings 12th Joint ACL-ISO Workshop on Interoperable Semantic Annotation (ISA-12), p. 45-54

- Rashmi Prasad and Harry Bunt (2015), Semantic Relations in Discourse: The Current State of ISO 24617-8, Proceedings of the 11th Joint ACL-ISO Workshop on Interoperable Semantic Annotation (ISA-11), https://aclanthology.org/W15-0210

- Rashmi Prasad, Eleni Miltsakaki, Nikhil Dinesh, Alan Lee, Aravind Joshi, Livio Robaldo (2007), The Penn Discourse Treebank 2.0 Annotation Manual, December 17, 2007, https://www.cis.upenn.edu/~elenimi/pdtb-manual.pdf, accessed 2023-11-09


## Possible Addenda

TED-MDB guidelines?

NB: for Dialog data, cf. https://dialogbank.lsv.uni-saarland.de/