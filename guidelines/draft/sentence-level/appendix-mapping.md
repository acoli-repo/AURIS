## A Technical Appendix

The following addenda are not relevant for annotation, but for conversion of data between different schemas.

### A.1 Relation Mapping

The following table provides a mapping between AURIS relations and other schemas, based on Bunt and Prasad (2016). AURIS definitions are primarily based on (descriptions and applications of) ISO 24617-8 and guidelines for PDTB1, PDTB2 and PDTB3.

| AURIS                         | ISO 24617-8                   | PDTB2 (PDTB3)                          | SDRT       | RST (RSTDTB)                         | 
| ----------------------------- | ----------------------------- | ---------------------------------------| ---------- | ------------------------------------ |
| `ADVERSATIVITY`               |                               | COMPARISON                             |            |                                      |
| - `Concession`                | Concession                    | Concession                             | (Contrast) | Concession (Antithesis, Preference)  |
| &nbsp; - `expectation-raiser` | Concession/Expectation-raiser | Expectation (Concession.arg1-as-denier)|            |                                      |
| &nbsp; - `contra-expectation` | Concession/Expectation-denier | Contra-Expectation (Concession.arg2-as-denier) |    |                                      |
| &nbsp; - `concession` 		| Concession                    | Concession                             |            |                                      |
| - `Contrast`                  | Contrast                      | Contrast, juxtaposition, opposition    | Contrast   | Contrast (Comparison)                |
| `CONTINGENCY`                 |                               | CONTINGENCY                            |            |                                      |
| - `Causal`                    | Cause                         | Cause                                  |            |                                      | 
| &nbsp; - `reason`             | Cause/Reason                  | Cause.reason, justification, explanation | Explanation | Vol./Non-vol. Cause, Evidence, Justify (Explanation-argumentation, Reason) | 
| &nbsp; - `result`             | Cause/Result                  | Cause.result                           | Result     | Vol./Non-vol. Result                 |
| &nbsp; - `cause`              | Cause                         | Cause                                  |            |                                      |
| - `Conditional`               | Condition                     |                                        |            |                                      |
| &nbsp; - `condition`          | Condition/Antecedent          | Condition                              | (Conditional) | Condition (Hypothetical)          |
| &nbsp; - `consequence`        | Condition/Consequent          | (inverse of Condition)                 | Consequence | (Contingency)                       |
| - `Negative_Condition`        | Negative Condition            |                                        |             |                                     |
| &nbsp; - `neg_condition` | Negative Condition/Negated Antecedent | Condition (Negative Condition)      | (Conditional) |                                   |
| &nbsp; - `neg_consequence`    | Negative Condition/Consequent | (inverse of Condition)                 | Consequence | Otherwise                           |
| - `Purpose`                   | Purpose                       | (Purpose)                              |             | Purpose                             |
| &nbsp; - `goal`               | Purpose/Goal                  | Result (Purpose.Arg2-as-goal)          | (Explanation, Goal) |                             |
| &nbsp; - `enablement`         | Purpose/Enablement            | (Purpose.Arg1-as-goal)                 |             |                                     |
| `TEMPORAL`                    |                               | TEMPORAL                               |             |                                     |
| - `Synchrony`                 | Synchrony                     | Synchronuous                           |             | (Temporal-same-time)                |
| - `Asynchrony`                | Asynchrony                    |                                        |             | Sequence                            | 
| &nbsp; - `before`             | Asynchrony/Before             | precedence               | (Precondition, Flashback) | (Temporal-before, Inverted-sequence) |
| &nbsp; - `after`              | Asynchrony/After              | succession                             | Narration   | (Temporal-after, Sequence)          |
| `EXPANSION`                   |                               | EXPANSION                              |             |                                     |
| - `Exception`                 | Exception                     | Exception                              |             |                                     |
| &nbsp; - `regular`            | Exception/Regular             | (Exception.Arg1-as-excpt)              |             |                                     |
| &nbsp; - `exception`          | Exception/Exception           | Exception (Arg2-as-excpt)              |             |                                     |
| - `Substitution`              | Substitution                  |                                        |             | Antithesis                          |
| &nbsp; - `disfavoured`        | Substitution/Disfavoured-alternative | (Substitution.Arg1-as-Subst)    |             |                                     |
| &nbsp; - `favoured`           | Substitution/Favoured-alternative | Chosen-alternative (Substitution.Arg2-as-Subst) | |                                    | 
| - `Exemplification`           | Exemplification               |                                       |              |                                     |
| &nbsp; - `set`                | Exemplification/Set           | (Instantiation.Arg1-as-instance)      |              |                                     |
| &nbsp; - `instance`           | Exemplification/Instance      | Instantiation (Arg2-as-instance)      | Elaboration  | Elaboration (set-member, Example)   |
| - `Elaboration`               | Elaboration                   | (Level-of-detail)                     |              |                                     |
| &nbsp; - `broad`              | Elaboration/Broad             | Generalization (Level-of-detail.Arg1-as-detail) |    |                                     | 
| &nbsp; - `specific`           | Elaboration/Specific          | Restatement.specification (Level-of-detail.Arg2-as-detail) | Elaboration  | Elaboration (general-specific, whole-part, process-step; Conclusion) |
| - `Manner`                    | Manner                        | (Manner)                               | Elaboration |                                     |
| &nbsp; - `means`              | Manner/Means                  | (Manner.Arg2-as-manner)                |             | (Means, Manner)                     |
| &nbsp; - `achievement`        | Manner/Achievement            | (Manner.Arg1-as-manner)                |             |                                     |
| - `Restatement`               | Restatement                   | Restatement.equivalence (Equivalence) | Elaboration  | Restatement (Summary)               |
| - `Disjunction`               | Disjunction                   | conjunctive, disjunctive              | Alternation  | Joint (Disjunction)                 |
| - `Conjunction`               | Conjunction                   | Conjunction, List                     | Continuation | Joint (List)                        |
| - `Similarity`                | Conjunction (Similarity)      |                                       | Parallel     | (Analogy, Proportion)               |
| - `Hypophora`                 | n/a                           | n/a (Hypophora)                       |              |                                     |
| - `Attribution`               | n/a                           | (Attribution)                         |              |                                     |
| `DIALOG`               | ISO 24617-2, communicative functions |                                       |              |                                     |
| - `Functional-Dependence`     | Functional-dependence/dependent-act |                                 |              |                                     |
| &nbsp; - `answer`             | ISO 24617-2: `Answer`         |                                       |              |                                     |
| &nbsp; - `offer`              | ISO 24617-2: `Offer`          |                                       |              |                                     |
| &nbsp; - `address suggest`   | ISO 24617-2: `Address Suggest` |                                       |              |                                     |
| &nbsp; - `agreement`          | ISO 24617-2: `Agreement`      |                                       |              |                                     |
| &nbsp; - `disagreement`       | ISO 24617-2: `Disagreement`   |                                       |              |                                     |
| &nbsp; - `dependent-act`      | other dialog act)             |                                       |              |                                     |
| - `Feedback`               | Feedback-dependence/feedback-act |                                       |              |                                     |
| **EntRel**                    | Expansion/Entity description  | EntRel                                | Background, Elaboration | Elaboration (object-attribute, additional) |

