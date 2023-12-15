# Y. Using the `COMMENT` column

The `COMMENT` column can (and should) be used to provide free-text information. In addition, it can also be used to provide metadata in a structured format for documenting aspects of or difficulties in the annotation. 

### Y.1 Ambiguous reference

Ambiguity is to be annotated in the `COMMENT` field, using pre-defined tags (if applicable) or plain text descriptions (otherwise). Optionally, ambiguity tags can be followed by a more detailed description in round parentheses `(...)`.

The following tags can be used to mark ambiguous 

1. `AMBIG:COREF` (ambiguous antecedent):<sup>[7](lit.md#coref7)</sup> There is uncertainty as to which is the \"right\" antecedent for an anaphor (or, controller for a cataphor). See above for antecedent selection preferences, provide referent index for all equally likely antecedents in round parentheses

	> (4) *In a letter, \[prosecutors\]<sub>p</sub> told \[Mr. Antar's lawyers\]<sub>l</sub> that because of the recent Supreme Court rulings, \[they\]<sub>p/l</sub>*<sub>?</sub> *could expect that any fees collected from Mr. Antar may be seized.*

2. `AMBIG:REL`: There is uncertainty as to whether an anaphoric relation exists or which type it is (anaphoric vs. bridging or event, i.e. contextual inference)

	This is sometimes the case with definite NPs. In the example below: If it is unclear whether the *confrontation* is identical to the *conflict*, the coreference should be annotated and the markable should be marked with this attribute. It is not necessary to provide a more detailed description.

	> (5) *This <ins>conflict</ins> is ... Therefore, the <ins>confrontation</ins> ...*

3. `AMBIG:IDIOM`: There is uncertainty as to whether a markable could be understood as a referential expression or as part of an idiom. Annotate anaphoric reading and mark the ambiguity.

4. `AMBIG:EXPL`: There is uncertainty as to whether a pronoun is an expletive (and therefore non-referring) or whether it is anaphoric. Annotate the anaphoric relations and mark the ambiguity. No description necessary.

	> (6) *At stake was an \$80,000 settlement involving who should pay what share of cleanup costs at the site of a former gas station, where underground fuel tanks had leaked and contaminated the soil. And the lawyers were just as eager as the judge to wrap \[it\] up.*

	*It* can either be interpreted as referring to *an \$80,000 settlement* or as a part of a lexicalized expression *to wrap it up* where *it* does not have any particular reference. 

	This can be made clearer with a constructed example:

	> (7.a) *She looks out of the window. <ins>It</ins><sub>EXPL</sub> is dark.* (expletive)
	
	> (7.b) *Your <ins>cat</ins><sub>1</sub> has a nice color. <ins>It</ins><sub>1</sub> is dark, much more so than mine.* (anaphoric)
	
	> (7.c) *The <ins>cat</ins><sub>1</sub> is hard to see. <ins>It</ins><sub>1,AMBIG:EXPL</sub> is dark.* (ambiguous)

5. `AMBIG:COREF_REL`: There is ambiguity with respect to both antecedent and relation

	> (8) "There seems to be a move around the world to deregulate the genera- tion of electricity," Mr. Richardson said, and Canadian Utilities hopes to capitalize on it.

	*On it* refers either to *a move around the world to deregulate the generation of electricity*, or to the whole clause beginning with
	*there* and ending with *electricity* (event anaphora).

6. `AMBIG:other`: other cases of ambiguity. Please provide a description in round parentheses.

If more than one kind of ambiguity applies, e.g., both ambiguity of antecedent and ambiguity of an anaphoric relation, then provide all of the corresponding tags (and descriptions), separated by comma.

