# A. Supplemental

## A.1 Notes

1. [Background and Terminology](terms.md)

	- <a name="terms1">1</a>: In the original PoCoS/PCC guidelines, markables were defined as phrasal expressions. Here, we annotate syntactic heads, instead.

	- <a name="terms2">2</a>: The head-based annotation adopted in these guidelines is an innovation to facilitate interoperability with Universal Dependency annotations. Krasavina and Chiarcos (2007) and Chiarcos et al. (2016) focused on the annotation of phrases, instead.

2. [File Format ands Editing](format.md)

3. [Automated Pre-Annotation of Markables](refexp.md)

	- <a name="refexp1">1</a>: The definition of primary markables follows Krasavina and Chiarcos (2007). Chiarcos et al. (2016) singled out non-referential markables  from primary markables as they do not rely on automated pre-annotation.

	- <a name="refexp2">2</a>: From UD annotation, we cannot extract times and dates reliably. So, these receive no special handling as primary markables (different from Stede et al. 2015).

	- <a name="refexp3">3</a>: Chiarcos and Krasavina (2005) also include zero (pro-drop) pronouns under pronouns. Here, we follow token-based annotation, so that zeros should not be annotated.

		> (43) *John<sub>j</sub> stepped in the kitchen,* Ø*<sub>j</sub> opened the fridge and* Ø*<sub>j</sub> decided NO-ZERO to take a pizza.*

		Here, that John is the (implicit) subject of the clause *to take a pizza*. However, this is not an instance of ∅-pronoun, since the insertion of *John* (no matter at which position within the phrase) would make the utterance ungrammatical. If not sure whether to annotate a ZERO or not, try to insert a full description of the corresponding referent. Note that zeros have to be sentential arguments, no adjuncts.

4. [Nominal coreference](coreference.md)

	- <a name="coref1">1</a>: Our annotation of anaphora as coreference differs from Chiarcos et al. (2016) who annotated anaphoric relations between anaphors and their antecedents, instead. Note that this means that we do not distinguish anaphoric (pronominal) and non-anaphoric (nominal) coreference, here.
	- <a name="coref2">2</a>: `REF=OLD` corresponds to "discourse old" according to Prince (1992). Originally abbreviated as `referring` (Chiarcos and Krasavina 2005).
	- <a name="coref3">3</a>: `REF=NEW` corresponds to "discourse new" according to Prince (1992). Originally abbreviated as `discourse-new` (Chiarcos and Krasavina 2005).
	- <a name="coref4">4</a>: `REF=CAT`, originally abbreviated as `discourse-cataphora` by Chiarcos and Krasavina (2005).
	- <a name="coref5">5</a>: Groups and situational references were originally subsumed under `other` in the PoCoS core scheme (Chiarcos and Krasavina 2005)
	- <a name="coref6">6</a>: Bound pronouns were part of the PoCoS extended scheme, not the core scheme (Chiarcos and Krasavina 2005)
	- <a name="coref7">7</a>: Abbreviated `ambig-ante` in Chiarcos and Krasavina (2005)

5. [Information status](information-status.md)

	- <a name="is1">1</a> In the context of information structure, the naming "in focus" or "focus" for the state with maximum givenness is very unfortunately. We stick with Gundel et al.'s terminology, but keep in mind that we are talking about the focus of attention here, not focus in the information-structural sense.

6. [Topic](topic.md)

	- <a name="topic1">1</a>: Following Grosz et al. (1995), Centering Theory was extended and parameterized. The definitions given above represent *one* specific interpretation of Grosz et al.'s criteria designed to facilitate unambiguous annotation. Other interpretations are possible.
	- <a name="topic2">2</a>: The salience ranking has been extended to include dependent clauses and word order, following Gernsbacher (2013). Furthermore, the Centering category "OTHER" is split into "OBLIQUE ARGUMENT" and "CLAUSE". Unlike the original formulation of Centering, the Givenness Hierarchy supports event anaphora.

## A.2 Sources

 The current manual has been compiled by Christian Chiarcos, University of Augsburg, in spring 2023. See [accompanying readme](Readme.md) for authors, contributors and revision history.

Sections 3 and 4 and parts of Sect. 1 are based on

- Christian Chiarcos and Olga Krasavina (2005), PoCoS. Potsdam Coreference Scheme, Tech. Rep., University of Potsdam, Germany
- Olga Krasavina and Christian Chiarcos (2007), PoCoS. Potsdam Coreference Scheme, First Linguistic Annotation Workshop (LAW-2007), held in conjunction with ACL-2007, Prague, Czech Republic, June 2007
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale referentielle Ausdrücke, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.55-70
- Christian Chiarcos, Manfred Stede, Saskia Warzecha (2019), Nominale Koreferenz, In: Stede, M. (Ed.). (2016). Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0 (Vol. 8). Universitätsverlag Potsdam, p.71-85

Whenever we draw from these texts, this is not specifically marked. These texts and the current manual represent different developmental stages and instantiations of the PoCoS core scheme (Chiarcos and Krasavina 2005),

Section 5 is based on Gundel et al.'s Coding Protocol for Statuses on the Givenness Hierarchy (2006, http://www.sfu.ca/~hedberg/Coding_for_Cognitive_Status.pdf, accessed 2023-04-16). Except for editorial updates, this document is largely unchanged. Changes are not explicitly marked, but are documented in Git history.

Sections 2 and 6 have been written from scratch for this manual by Christian Chiarcos, Spring 2023.

## A.3 Literature References (Selection)

Biber, Douglas et al.. *Longman Grammar of Spoken and Written
English*. Longman, 1999.

De Marneffe, M. C., Manning, C. D., Nivre, J., & Zeman, D. (2021). Universal dependencies. Computational linguistics, 47(2), 255-308.

Gernsbacher, M. A. (2013). _Language comprehension as structure building_. Psychology Press.

Gibbs, R.W. *The poetics of mind*. Cambridge University, Cambridge, 1994. Gardent, Claire, H´el\`ene Manu´elian, and Eric Kow. Which bridges for bridging descriptions. In *EACL Workshop on Linguistically Interpreted Corpora proceedings.*, 2003\.

Grosz, B. J., Joshi, A. K., & Weinstein, S. (1995). Centering: A Framework for Modeling the Local Coherence of Discourse. _Computational Linguistics_, _21_, 203-225.

Gundel, J. K., Hedberg, N., & Zacharski, R. (1993). Cognitive status and the form of referring expressions in discourse. _Language_, 274-307.

Lambrecht, K. (1996). _Information structure and sentence form: Topic, focus, and the mental representations of discourse referents_ (Vol. 71). Cambridge university press.

Mitkov, R. et al.. Coreference and anaphora: Developing annotating tools, annotating resources and annotations strategies. In *Proc. DAARC 2000*, pages 49--58, Lancaster, UK, 2000.

Reinhart, T. (1980). Conditions for Text Coherence. Poetics Today, 1(4), 161–180. https://doi.org/10.2307/1771893

Webber, B., Prasad, R., Lee, A., & Joshi, A. (2019). The Penn Discourse Treebank 3.0 Annotation Manual. Philadelphia, University of Pennsylvania, 35, 108.

