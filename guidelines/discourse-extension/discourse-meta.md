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

