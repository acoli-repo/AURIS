# Addenda / Future Extensions

## To refexp.md

The following features of the original PoCoS scheme are currently not annotated:

- column/feature `DIRECT_SPEECH`

	- default (`_`): reference on the text level, i.e. reference NOT into or within the quoted material
	- `DIR`: reference into or within direct speech
	- `INDIR`: reference into or within indirect speech

- column/feature `COMPLEX_NP`: A description is complex if it contains more than one noun phrase
	- `_` (default)
	- `yes`
	- `no`

- column/feature `SEMANTIC_ROLE`: ag, ben/dat, pat, loc, instr, other, unspec

- `ANIMACY`: 
	- animate i.e. lexical animacy, with the following sub-types
	- human
	- non-human
	- inaminate i.e. lexical inanimacy or abstract
	Note that abstract entities are always regarded as being inanimate.

- semantic class: abstract, person, physical object, action/event, collective, other, unspec

	Note that there exist subtle dependencies between semantic class and animacy. However, critical cases such as collectives (e.g. *a group of people* vs. *a group of hills*) and certain physical objects (e.g. *tree* vs. *stone*) could be either animate or inanimate. While semantic class has to do with the perception of an entity, animacy is primary a lexical feature. However, default values semantic class and animacy can be derived from WordNet resp. GermaNet for a majority of cases.

## To coreference.md

### Bridging

This is not to be annotated at the moment. In the future, these annotations may be merged with those currently in `REF`

- `RELATION`

	nominal anaphora Nominal anaphora as a type of anaphoric relations was introduced on (p. 12). Here annotation of subtypes of nominal anaphors is enabled as well:

	modification : new lexical material has been added within the NP

	45. .*.. federal prosecutors have warned lawyers for \[Eddie Antar\] that if \[the founder and former chairman of Crazy Eddie Inc.\] is indicted,* \...

	synonymy (52) *the agreement* - *the pact*

	repetition a *lexical* repetition of a whole NP or parts of it

	(53) *der Kanzler* \... *der Kanzler*

	(54) *der Bundeskanzler* \... *der Kanzler*

	BUT: *der Kanzler* \... *der hoch gesch¨atzte Kanzler* (here, we find a modification

	since new lexical material is added)

	pronominal (55) *If the government succeeds in seizing \[Antar's\] assets, \[he\] could be left without top-flight legal representation, \...*

	unspec unspecified (as default value)

	Note that these features are set not only with respect to the last mention of the referent, but to all previous references to it as well.
	So, if a particular form appeared already, we compare it to this one, not the direct antecedent. The underlying intuition is that a referent accumulates semantic information as the discourse unfolds and thus, the comparison is not between surface forms, but between the anaphor and the whole bunch of representations the referent has been associated with. In case of uncertainties, use the following preferences:

	synonymy \> modification

	non-nominal anaphor We distinguish the following types of non-nominal anaphors:

	event references to events reported in text spans, sentences, clauses or nominalized clauses

	\(56\) *\[She spent a month at an Aetna school in Gettysburg, Pa., learning all about the construction trade, including masonry, plumbing and electrical wiring.\] \[That\] was followed by three months at the
	Aetna Institute in Hartford ..*.

	spatio-temporal ^8^

	The anaphor has to be a prepositional phrase or a cue phrase replaceable by a prepositional phrase.

	This category is primarily intended for German spatio-temporal pronominal adverbs (*danach* "thereafter", *davor* "in front of this"), and locative and temporal prepositional phrases (*behind the door*, *after the WW-II*).

	anaphoric NPs (but not idenitity of reference): *fu¨nf Jahre sp¨ater*

	Antecedents of event anaphors Antecedents of an event anaphors can be clauses only. As a convention, we exclude non-finite clauses and sub-clausal phrases from the scope of potential antecedents for event anaphors.


	Bridging relations. Bridging is the term introduced in Clark 1975, which accounts for referents of definite descriptions, which are not directly related to some previously mentioned textual entities, but are rather inferred through lexical or world-knowledge of discourse participants.



	Do NOT annotate as bridging:

	-   If the relation between the definite NP bridging anaphor and preceding context has been made explicit by means additional linguistic information (possessive pronouns, attributes, etc.), this relation has not been evoked from the text, but rather from the world-knowledge of the hearer. Such definite NPs should NOT be considered as bridging anaphors. Cf.:

	\(58\) *\[Ein neues Bildbearbeitungsprogramm\]B ist auf \[den Markt\]M gekommen. \[Die Fehlermeldungen\]F, \[die\]F \[es\]B ausgibt, bringen
	\[\[seine\]B Benutzer\]U zur Verzweiflung. '\[A new graphic*

	*editor\] appeared \[in the market\]. \[The error messages\] that
	\[it\] produces bring its users in despair.'*

	In this example, *Die Fehlermeldungen 'the error messages'* is not a bridging anaphor, since the relation of these *error messages* to the context is clarified by the following relative clause. In the same way, the relation between *Bilderbearbeitungsprogramm 'the graphic editor'* and *seine Benutzer 'its users'* is not a case of bridging, being explained through a possessive pronoun *seine 'its'*.

	-   Indefinites and pronouns can NEVER be considered as bridging anaphors. Only full definite descriptions fall under the definition of bridging anaphora. We explicitly exclude examples like the following ones:

	(59.a) *Westinghouse Electric Corp. said it will buy Shaw - Walker Co.
	\[Terms\] weren't disclosed.* similar-NPs

	(59.b) *the pact\... the accord\... \[a similar alliance\]\...* i.e. similar to the pact in question

	special cases Consider the following example. Here, part-whole bridging takes place, rather than a spatio-temporal anaphoric relation. The deictic point is the moment outlined in the previous discourse, but the terms have been lexicalized in political discourse.

	(60) *im Osten\... im Westen* (in reference to Deutschland - discourse referent introduced before)

	Whenever you find a definite NP that can not be explained as anaphoric reference, consider if it can be the case of *bridging* relation.
	Bridging is a relation other than identity between markables established by inference.

	(61) *John ate pizza. There was nothing else in* the fridge*.*

	Here *the fridge* is inferred by mentioning a pizza.

	Important note: antecedent can be only one markable, choose the most recent one, but mark it as ambig-ante (if the same bridging relation could point to another trigger) resp. ambig-rel (if different bridging relations could point to several different triggers), if unsure about ambig-ante or ambig-rel, choose ambig-other and write a comment.

	Never allow bridging references from direct quotes to the textual level!

	Following Gardent et al. \[GMK03\], we interpret the following examples as bridging: examples:

	(62) T*oni Johnson pulls a tape measure across the front of \[what was once a stately Victorian home\]H. \[The chimney\]<sub>part</sub>*<sub>o*f*(*H*)</sub>
	     *is a pile of bricks on the front lawn.*

	(63.a) *A deep trench now runs along its north wall, exposed when the house lurched two feet off its foundation during last week's
	\[earthquake\]e.*

	(63.b) *The petite, 29-year-old Ms. Johnson \... has been on the move almost incessantly since last Thursday, when an army of adjusters, employed by major insurers, invaded the San Francisco area to help policyholders sift through \[the rubble\]<sub>effect</sub> <sub>of</sub>*<sub>(*e*)</sub> *and restore some order to their lives.*

	(64.a) *\[The Victorian house\]<sub>h</sub> that Ms. Johnson is inspecting has been deemed unsafe by town officials. \...*

	(64.b) *\[The owners\]<sub>property</sub> <sub>of</sub>*<sub>(*h*)</sub>*, William and Margie
	Hammack, are luckier than many others.*

	Trigger (antecedent)of bridging relations Antecedents, or triggers are sometimes difficult to be assigned to just one markable. It can be the whole context that evokes the information necessary for the interpretation of a bridging anaphor. If a single markable cannot be specified, choose the left-most one and mark it as "ambig-ante".


### Bridging: Ambiguities

In case of ambiguities, we suggest the following preferences. Below is the example outlined in the core scheme (p. 14 considered with respect to the options supported in the extended scheme and interpreted in accordance with these preferences.

anaphoric \> generic/idiomatic/expletive \> bridging \> situational

### Bridging: World knowledge and situational references

Whenever a non-generic definite description cannot be explained as contextually accessible due to anaphoric reference or bridging inference, consider it to be inferrable from world knowledge or the situational environment.

	> (65) *This publication may not be reproduced, \...* (situational reference to the reading environment)

	> (66) *Last Sunday, Ms. Johnson finally got a chance to water her plants, but stopped abruptly. "I realized I couldn't waste this water when there are people in Watsonville who don't have fresh water to drink."* (WSJ, situational reference to the reported context)^9^

> Note:
> - In (66), we seem to have a bridging reference from direct speech to the predication *to water her plants*. However, it is less likely that Ms. Johnson refers to a text which had been written after she said that. So, it seems to be appropriate to classify such cases as situational anaphora, referring to situational environment at the moment of speaking.


Note that bridging references from direct quotes to the textual level are never subject to annotation! These are prototypical candidates for situational references.

To avoid waste-baket effects for situational and world-knowledge references, we mark situational references by relations pointing to a set of situationally prominent entities that are listed after the text itself, enclosed in \<situation\>, resp. in \<universe\> tags.
