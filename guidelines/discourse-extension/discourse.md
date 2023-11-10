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
	- **Conjunction**
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
		- **chosen alternative**
	- **Exception**
	- **List**
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

> Note: The relation definitions follow Prasad and Bunt (2016). RST, RSTDTB, SDRT and PDTB mapping follows Prasad and Bunt (2016).

> Note: Role labels are taken from ISO SemAF. The `Condition` relation corresponds to ISO SemAF CONDITION with internal argument role "Antecedent". The `Negated_Condition` relation corresponds to ISO SemAF NEGATIVE CONDITION with internal argument role "Negated_Antecedent". 

> Note: For `Feedback-act`, annotate if and only if turn-taking or interruptions occurred  

> Note: Consider replacing `Feedback-act` and `Dependent-act` annotations by dialogue act annotations.

> Note: Annotate Dependence relations only in the absence of explicit discourse markers, example:

	- P1: I can never find my remote control.	P2: That’s [because] they don’t have a fixed place.		(Reason, not Inform, from Butt & Prasad 2016)

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