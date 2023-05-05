# Annotation Manual (April 2023 edition)

Annotation manual for 

- the automated annotation of referring expressions, 
- the manual annotation of coreference, and
- the manual annotation information status ("Givenness")

Note that all annotations need to revised if changes to this manual occur. For this reason, annotators must **NEVER** change this document. Instead, if you encounter difficulties or problems with the annotation, document your requirements or issues in an accompanying document, along with a reference to the data where you encountered the issue and a brief statement on how you solved or marked it.

## Content

The manual consists of four separate documents:

- [terms.md](terms.md): terms file format and annotation procedure, by Christian Chiarcos (2023)
- [refexp.mp](refexp.md): guidelines for automated pre-annotation for referring expressions, originally by Chiarcos and Krasavina (2005)
- [coref.md](coreference.md): guidelines manual annotation of coreference and referentiality, originally by Chiarcos and Krasavina (2005)
- [information-status.md](information-status.md): guidelines for the manual annotation of information status ("givenness"), originally by Gundel, Hedberg and Zacharski (1993)

This document is meant to be a practical handbook, compiled and revised from earlier manuals, with a focus on examples and common problems. In some design decisions, we deviate from our sources:

- **referring expressions**: We skip the coreference annotation principles in order to provide a more minimal description. We introduced head-based annotation instead of phrase-based annotation. We skip the extended part of PoCoS. We extend the annotation to antecedents of event anaphora.
- **coreference**: We skip the coreference annotation principles in order to provide a more minimal description. Instead of anaphoric relations, we annotate coreference by coindexing. We skip the extended part of PoCoS. We skip features of referring expressions than can be derived from syntax.
- **information status**: We introduced head-based annotation. The original hierarchy is extended for backward-looking center.

Original contributions include specifics of format and annotation procedure.

## Disclaimer

The following guidelines have been developed on the basis of existing guidelines whose original creators are attributed along with the compilator. 
Note that we do not track all possible changes, but instead, we provide the modified guidelines along with the original files in the same format, so that changes can be tracked automatically (e.g., using the command line tool `diff`).

Because they can be automatically identified, we do not mark literal quotations from the original document. Note that this manual is **not to be published** unless this information is to be added to it. 

## Contributors

### Authors 

We list direct contributors as well as primary authors of sources that went, fully or partially, into this document, along with their (estimated) duration of involvement

- CC: Christian Chiarcos (coreference: since 2005, information status: since 2008), University of Augsburg, Germany
- OK: Olga Krasavina (coreference: 2005-2011), HU Berlin, Germany / Moscow State University, Russia
- MS: Manfred Stede (coreference: 2005-2015), U Potsdam, Germany
- SW: Saskia Warzecha (coreference: until 2015), U Potsdam, Germany
- JG: Jeanette Gundel (information status: 1993-2006)
- NH: Nancy Hedberg (information status: 1993-2006)
- RZ: Ron Zacharski (information status: 1993-2006)

### Other contributors

Other contributors are people who provided feedback and input, incl. annotators.

- André Herzog (coreference: before 2016), U Potsdam. Germany
- David Kaupat (coreference: before 2016), U Potsdam. Germany
- Sara Mamprin (coreference: before 2016), U Potsdam. Germany
- Ann Mulkern (information status: before 2007)
- Tonya Custis (information status: before 2007)
- Bonnie Swierzbin (information status: before 2007)
- Amel Khalfoui (information status: before 2007)
- Linda Humnick (information status: before 2007)
- Bryan Gordon (information status: before 2007)
- Mamadou Bassene (information status: before 2007)
- Shana Watters (information status: before 2007)

## History

- [terms.md](terms.md): definitions
	- [2023-04-20](../archive/terms.2023-04-20.md): extracted from refexp.md and coreference.md, see there for sources and contributors [CC]
- [format.md](format.md): file formats and annotation proceduce
	- 2023-05-04: first draft [CC]
- [refexp.md](refexp.md): guidelines for automated pre-annotation
	- **TODO**: restore and update English examples from Krasavina and Chiarcos (2007) and Chiarcos and Krasavina (2005)
	- [2023-04-20](../archive/refexp.2024-04-20.md): restructured and fully revised [CC]
	- [2015-xx-xx](../archive/coreference.2019.chiarcos-et-al.md): translation of relevant parts of Stede et al. (2015) to English
		- source: Stede, M. (Ed.). (2016). [Handbuch Textannotation: Potsdamer Kommentarkorpus 2.0](https://publishup.uni-potsdam.de/frontdoor/index/index/docId/8276) (Vol. 8). Universitätsverlag Potsdam, p.55-88
		- authors (of chapters): Christian Chiarcos, Manfred Stede, Saskia Warzecha [CC, MS, SW]
		- contributors (of chapters): André Herzog, David Kaupat and Sara Mamprin
		- excerpt and (minor) revision of the Potsdam Coreference Scheme (PoCoS), limited to German
	- [2007-06-28](../archive/coreference.2007-06-28.pdf): Krasavina, O., & Chiarcos, C. (2007, June). PoCoS-Potsdam coreference scheme. In Proceedings of the Linguistic Annotation Workshop (LAW-2007), held in conjunction with ACL-2007, Prague, Czech Republic (pp. 156-163). [OK,CC]
		- Reference publication for the Potsdam Coreference Scheme (PoCoS)
	- [2005-10-25](../archive/coreference.2005-10-25.pdf): Chiarcos, C., & Krasavina, O. (2005). Annotation Guidelines PoCoS–Potsdam Coreference Scheme. Technical Report. University of Potsdam, Germany. [CC,OK]
		- Original edition of the Potsdam Coreference Scheme (PoCoS), focusing on English, Russian and German
- [coreference.md](coreference.md)
	- **TODO**: restore and update English examples from PoCoS
	- [2023-04-20](coreference.2023-04-20.md): revision by Christian Chiarcos, fully restructured
		- The original annotation procedure was focusing on anaphoric relations. Now revised to annotate coreference sets. However, many examples are taken over.
	- [2015-xx-xx](../archive/coreference.2019.chiarcos-et-al.md): translation of relevant parts of Stede et al. (2015) to English
		- see under refexp.md (above) for sources and contributors
- [information-status.md](information-status.md)
	- [2023-04-16](../archive/information-status.2023-04-16.md): revision by Christian Chiarcos, extended for backward-looking center
	- [2006-05-xx](../archive/information-status.2006.gundel-et-al.md): revision of May 2006
		- published under http://www.sfu.ca/~hedberg/Coding_for_Cognitive_Status.pdf
		- authors: Jeanette Gundel, Nancy Hedberg, Ron Zacharski
		- contributors: Ann Mulkern, Tonya Custis, Bonnie Swierzbin, Amel Khalfoui, Linda Humnick, Bryan Gordon, Mamadou Bassene, Shana Watters
	- 2004-07-xx: preceding revision of Jeanette Gundel, Nancy Hedberg, Ron Zacharski of July 2004
	- 1993: original version by Gundel, Hedberg and Zacharski

