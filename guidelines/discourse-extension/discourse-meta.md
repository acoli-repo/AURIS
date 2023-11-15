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