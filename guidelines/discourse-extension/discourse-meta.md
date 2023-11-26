# Design principles for the AURIS Discourse Guidelines

The AURIS guidelines for discourse are designed in accordance with the following priorities:
- Discourse relations must be annotatable by non-experts with off-the-shelf tools
- We aim for an annotation that is directly mappable to other schemes. We take ISO SemAF as a basis
- We focus on discourse relation annotation
- We impose no constraints on discourse structure (as in PDTB, ISO SemAF)
- We focus on intersentential relations only
- We aim for maximum coverage: every utterance must be annotated

Some features set AURIS apart from other schemas:
- We annotate discourse relations as a relation between an utterance and one contextual anchor (i.e., another utterance). The basis of discourse relations is the utterance, not the discourse marker. This allows for a more systematic annotation of explicit and implicit discourse markers.
- Within an utterance (both the utterance to be annotated and the contextual anchor), the basis of annotation is the main clause. 
- Verbs of attribution are excluded. Instead, we annotate the clausal arguments. 
- We do not annotate spans, but (the syntactic heads of) complete utterances.
- The basis of segmentation is determined by off-the-shelf sentence splitting. There is no explicit notion of discourse segments.
- Unlike PDTB, we aim to provide a complete annotation (of all utterances).
- Unlike RST, we do not expect a connected tree
- If (the main predicate of) an utterance carries a discourse marker, this determines the discourse relation to be annotated. We annotate exactly one discourse relation per utterance. This means that paired discourse markers ("either ... or ..." or "on the one hand ... on the other hand ...") yield circular annotations where the first utterance refers to the second, the second to the first.
- Unlike PDTB, we annotate at most one discourse relation (one discourse marker) per sentence. If multiple discourse markers apply, this defaults to the first discourse marker.
- There are no structural constraints as to where the anchor is located. We support unrestricted long-distance relations (unlike PDTB) and crossing edges (unlike RST), however, the schema imposes a preference for annotating the closest possible anchor. In line with human discourse processing, most anchors are expected in the previous discourse, not in the following discourse.

AURIS is unique in grounding its annotations in utterances rather than discourse markers (as PDTB, ISO SemAF) or discourse segments (as RST, SDRT). In comparison to ISO SemAF, this leads to a shift of focus, as we annotate roles for asymmetric discourse relations rather than discourse relations. However, AURIS annotations are 1:1 mappable to ISO SemAF.



The core assumption of the Penn Discourse Treebank is that discourse markers establish discourse-level predicates that
take two abstract objects such as events, states, and propositions as their arguments. This is somewhat problematic for cases in which implicit discourse markers are to be annotated or in which a discourse relation is expressed by an alternative lexicalization, because there is no structural anchor to attach discourse annotations to. in AURIS, we adopt an alternative view and interpret discourse relations along the lines of anaphoric relations. Not in the sense that entity coreference is involved (although this is likely, and sometimes, required for certain discourse relations), but in the sense that a discourse relation serves to anchor a discourse unit in the preceding context. Like a referring expressions thus calls for an antecedent to be found, we see the task of (shallow) discourse parsing as the task to identify the anchor of an utterance. And, as we aim for a complete analysis, for *every* utterance. This idea is similar to models of global coherence such as RST and SDRT, but unlike these, we posit no structural constraints on discourse relations. In particular, we do not require that discourse relations constitute a tree structure. However, _some_ limitations are posited, but not out of theoretical, but practical considerations:

- We annotate only one discourse relation per utterance. If more than one explicit discourse marker is found, this should be the meaning of the first discourse marker. If no discourse marker is found, this would be the relation that links it with the closest candidate anchor possible. 

- We rely on syntactic (orthographic) sentences to serve as discourse segments. On the theoretical side, this is because we assume that overt syntactic and morphological cues already are sufficient indicators of intrasentential discourse relations. On the practical side, this decision allows us to efficiently preprocess data and to use a simple, tabular annotation format.

- Within each utterance, we identify the main predicate. Discourse relations to be annotated, are concerned with the anchoring of that predicate (and its arguments) in discourse. The anchoring of dependent clauses that modify the predicate are beyond scope.

- For identifying the main predicate, we rely on the dependency analysis of the Universal Dependencies. That is, every conjunct is represented by (and reducible to) its first element.

- Traditionally, attribution has been modelled as an aspect of discourse stucture ... but in fact, verbs of attribution often serve to provide episthemic information, provenance or, in technical terms, metadata about the utterance rather than represent its actual content. For this reason, the main predicate of an attribution sentence is defined as the main verb, but as the reported statement, if given.

Beyond that, the AURIS annotation scheme is based on ISO SemAF, because that claims to be theory-neutral. However, as the full specification is not publicly available (unless being paid for), and too massively underspecified to be of practical use (Żurowski et al. 2023), practical definitions and examples are largely drawn from the second edition of the Penn Discourse Treebank (PDTB2) in its ISO SemAF interpretation as given by Bunt and Prasad (2016). 


Note that unlike any other scheme we are aware of, we formulate the task of shallow discourse parsing from an utterance-centric position. By comparison, ISO SemAF and PDTB are formulated from a marker-centric perspective. The advantage is that this approach allows to more easily compare with RST and SDRT annotations, because these typically lack explicit annotations of discourse markers.




## Sources / Relations with other schemes

ISO 24617-8 has been heavily criticized for being poorly defined (e.g., by Żurowski et al. 2023). We provide operationalizable definitions by exploiting the correspondence with established RST, SDRT and PDTB definitions as given by proponents of ISO 24617-8. These definitions are primarily based on PDTB 2.0 (Prasad et al. 2007).

The AURIS Discourse schema is grounded in the role inventory of ISO 24617-8. Note that we do not directly quote from the ISO-24617-8 norm, because they do not provide the necessary level of detailed description, and they are available only upon payment from https://www.iso.org/obp/ui/#iso:std:iso:24617:-8:ed-1:v1:en. Instead, the primary basis for designing these guidelines is the Penn Discourse Treebank (PDTB), and the ISO 24617-8 mapping provided by Bunt and Prasad (2016). Unlike PDTB, AURIS does not annotate minimal spans, but complete sentences. The AURIS terms *utterance* and *anchor* correspond to `ARG2` (internal argument of a discourse marker) and `ARG1` (external argument) in the terminology of PDTB2. (Note that these terms have been partially re-defined for PDTB3, the exact correspondence is with the original PDTB2 definitions.)

The guidelines for discourse relation annotation are primarily based on those of the Penn Discourse Treebank (PDTB), using the ISO 24617-8 relation inventory as defined by Bunt and Prasad (2016). The first level is based on PDTB2 (not PDTB3), the second level is represented by ISO 24617-8 relations (discourse relations that are symmetric or underspecified in their directionality), the third level by ISO 24617-8 roles (asymmetric discourse relations.)

The top-level organization of discourse relations corresponds to PDTB2: CONTINGENCY (Prasad et al. 2007, p.28; Webber et al. 2019a, p.19), TEMPORAL (Prasad et al. 2007, p. 27; Webber et al. 2019a, p.18), EXPANSION (Prasad et al. 2007, p.34). The definition for ADVERSATIVITY is based on the PDTB2 definition of COMPARISON (Prasad et al. 2007, p.32), which (for PDTB2) included Contrast and Concession. We decided to rename it to highlight that the PDTB3 relation Similarity continues to be grouped with EXPANSION (as in PDTB2), not with Contrast and Concession (as in PDTB3). This reflects the the distribution of discourse markers, as those associated with Similarity overlap with those of Conjunction (in EXPANSION), whereas they do not overlap with the common pool of adversative discourse markers (esp., *but*). As for PDTB EntRel relations, these have unfortunately been named EXPANSION in ISO 24617-8, but we follow PDTB in considering them a separate top-level group. DIALOG was added for ISO 24617-8 dialog annotations: PDTB annotations primarily addressed monologuous data.

> Note: The top-level class ADVERSATIVITY has been introduced for PDTB2 COMPARISON, to avoid conflation with PDTB3 COMPARISON, because PDTB3 has revised the definition of COMPARISON to also include Similarity relations, which were previously grouped with EXPANSION. However, Webber et al. (2019a, p. 23-24) note that annotators had difficulties to distinguish Contrast and Concession, thus demonstrating the need for a common superclass. These difficulties do not extend, however, to SIMILARITY. As an alternative to the PDTB3 approach of extending the scope of COMPARISON, we would prefer to stay with the original definition, but use a more specific designation, say, ADVERSATIVITY.

For asymmetric relations, we annotate the ISO 24617-8 role of the internal argument. For symmetric relations, we annotate the ISO 24617-8 relation at the second argument.

In the following, we refer to the internal argument as utterance, to the external argument as (contextual) anchor. 

Prasad and Bunt's (2016) definition of `Similarity` recalls aspects of the definition of Contrast, so SIMILARITY can be seen as a subclass of PDTB COMPARISON. In PDTB3, Similarity was indeed introduced as a subclass of COMPARISON (Webber et al. 2019a, p.18). The PDTB2 mapping by Bunt and Prasad (2016), however, linked it with PDTB Conjunction and thus puts it under PDTB EXPANSION. We follow this approach here. Note that Webber et al. (2019b) point out that splitting PDTB2 EXPANSION.Conjunction into PDTB3 EXPANSION.Conjunction and PDTB3 COMPARISON.Similarity created novel ambiguities. In line with ISO 24617-8, these are not distinguished here.

> Notes:
> - `Hypophora` is missing from both PDTB2 and ISO SemAF, added here with PDTB3 as top-level category "Hypophora": "In HYPOPHORA relations, one argument (commonly Arg1) expresses a question and the other argument (commonly Arg2) provides an answer.""

Functional dependence: Note in ISO 24617-8, the utterance occupies the Dependent-act role, the anchor the Antecedent-act. The ancedent act of a functional dependence relation always serves as an anchor and precedes the utterance, so it is not to be annotated.

For turn-taking relations, the scheme has been extended with a subset of ISO/DIS 24617-2 communicative functions. This is, however, limited to top-level categories, at the moment.

> Note: For Answer, the sDialog act of utterance corresponds to ISO/DIS 24617-2 "Answer", dialog act of anchor corresponds to ISO/DIS 24617-2 "Question".

In offer relations, The dialog act of the utterance corresponds to ISO/DIS 24617-2 "Offer", dialog act of anchor corresponds to ISO/DIS 24617-2 "Request".

> Note: for `address-suggest`, the ISO/DIS 24617-2 dialog act of the utterance is "Address Suggest", the dialog act of the anchor is "Suggest".

> For the AURIS `Feedback` relation, the utterance corresponds to the SemAF role "Feedback act", the anchor the SemAF roile "Feedback scope".


Expansion/Expander
Expansion/Entity Description

On EntRel:

	- Note: Our naming follows PDTB2 and PDTB3. According to Bunt and Prasad (2016), entity relations are equivalent to the SemAF relation "Expansion", but here, we refrained from this name because it would create an unfortunate overlap with the top-level class `EXPANSION` which does *not* overlap with PDTB entity relations.

	- Note: Żurowski et al. 2023 (p.487) report the SemAF relation "Expansion" with roles "Narrative" and "Expander". This differs from scientificially published version of ISO 24617-8. They give the following example

	- Note: ISO 24617-8 distinguishes two argument roles here, "foreground" and "entity description". As the foreground is always the anchor and the entity description is always the utterance, all AURIS annotations for entity relations are actually instances of SemAF entity description. Foreground is never explicitly annotated.

	- Note: For cross-paragraph link annotation, Prasad et al. (2017) distinguish "semantic" entity relations (where the narrative is expanded forward) and "other" entity relations (were only coreference establishes a link). However, this division had been abandoned for PDTB3.



## Possible Addenda

TED-MDB guidelines? (no)

NB: for Dialog data, cf. https://dialogbank.lsv.uni-saarland.de/

Note that PDTB3 changed the definition of its arguments and shifted from a syntactically based identification of Arg1 (external argument) and Arg2 (internal argument) to a positional identification of Arg1 as first and Arg2 as second argument (except for subordinating conjunctions, where the old definition holds). As ISO 24617-8 was defined in relation to PDTB2, not PDTB3, our definitions are based on the older definitions. Subsequent updates to the definition of PDTB2 roles that pertain to this change in definitions have not been adopted here.

TODO: we could add attribution for cases in which sentence splitting separates the attribution phrase from the reported statement. In our attribution relation, the utterance is the attribution statement, attribution triggered by either the verb or an orthographic mark such as a colon (_:_)

## Appendix: List of diagnostic discourse markers

You can use the following list to confirm whether a discourse relation holds. If you can use these discourse markers in place of the explicit discourse marker or the alternative lexicalization at hand, or insert them into a sentence without implicit discourse marker, take this as an indicator that the respective discourse relation holds.

Also, when disambiguating explicit or inserting implicit discourse markers, consult this list from top to bottom: If a discourse marker holds, do not consider other candidate markers further below. We currently provide lists for English and German. Discourse marker lists for other languages can be provided upon demand.



- English and German diagnostic discourse markers

