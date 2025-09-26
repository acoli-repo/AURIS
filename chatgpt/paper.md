# Can ChatGPT do discourse annotation? A case study in coreference and information status

Zero-shot prompting against Large Language Models (LLMs) has proven to be invaluable for a number of tasks that were previously thought to require human expertise. However, especially for the realm of discourse, some reservations are justified, because the large success of machine learning -- from its very nature -- results from the generalization of regularities observed in its training data. This leads to a natural tendency to over-generalize. This is not only a problem for the amplification of biases found in the training data [REFS: bias in LLMs], but also to for the language itself. As such, linguistic phenomena that cannot be accounted for on grounds of grammar and semantics, alone, -- and that are thus to be explained by their discourse functions -- are characteristically less frequent that ``canonical constructions''. While these are or central importance to discourse analysis, the applicability of LLMs to their automated annotation is yet to be evaluated.

We understand ``discourse phenomena'' in a broad sense to encompass all communication strategies that relate to or are determined by the discourse context. In that regard, we focus on a pervasive, and thus comparably simple phenomenon, the annotation of information status [REFS]. We adopt the compact annotation scheme of Gundel et al. (1993). In order to guide the model towards well-defined, transparent decisions, this is conducted in conjunction with coreference annotation, because the definitions of Gundel et al. (1993) are based on the identification of previous and subsequent mentions of referents.

Gundel et al.'s Givenness Hierarchy is relatively widely used and has been applied to large number of typologically diverse languages [REFS]. It has also been discussed in NLP [REFS], but its uptake is somewhat limited as corpora with annotations according to this schema do not seem to be publicly available. Here, we operate with the Augsburg Corpus of Reference and Information Structure (AURIS), a corpus project under development at the University of Augsburg, Germany.

AURIS aims to provide annotations for aspects of reference, information structure and discourse structure in a multilingual and cross-theoretically interpretable manner. At its core, it is a parallel corpus, so that annotations can be compared across different languages. As we consider the underlying, cognitive aspects of information structure and discourse structure to be universals of human communication, AURIS also allows to project discourse and information structure annotations across languages, and to study their relation with surface phenomena often associated with discourse. In our experiment, AURIS is used to 

To some extent, AURIS builds on earlier annotation projects, and annotations converted from these are used for evaluating AURIS guidelines and to train annotations. In fact, the availability of related annotations has guided the selection of texts at the early stages of corpus development. At the moment, AURIS includes TED talks (cf. MDTB and Coref), two chapters of Sherlock Holmes stories by Arthur Conan Doyle (cf. FrameNet iSRL annotations), Lewis Carroll's Alice in Wonderland (cf. Emotion annotations), sections of the Bible (cf. OntoNotes coreference), selected fairy tales (cf. emotion annotation) and news articles (cf. Coref). The idea of this collection is to successively complete the annotations to construct a manually annotated core corpus and then subsequently expand it as part and in conjunction with the training of students of different language sciences at the Faculty of Philology and History at the University of Augsburg, Germany.

...



Prompt engineering: 

The prompt is constructed 

Discussion