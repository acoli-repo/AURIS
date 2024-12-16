# Future extensions: Aspects of Focus

In the context of information structure, "focus" refers to the part(s) of the sentence that comprise information that cannot be presupposed by the speaker, i.e., new information. Approaches on focus annotation concentrate on a question test, i.e., the annotator needs to construct a hypothetical question that a hearer might be asking at the current point in discourse and to which the next utterance might be a possible answer. Unfortunately, annotating these questions is infeasible in terms of effort and agreement between annotators regarding those questions is low.

For this reason, we concentrate on the annotation of newsworthiness, instead. As focus is defined by being the part(s) of the sentence that contain non-presupposed information (i.e., new information), it can be largely predicted from newsworthiness.

## Novelty (`NOVEL`)

As for novelty, or, more technically, newsworthiness, we only consider the annotation of content words (not function words), i.e., verbs, nouns, and, under certain circumstances, adjectives and adverbs. We distinguish three qualities of presupposed information:

- `KNOWN`: hearer-old information that is known (or inferrable) to the hearer. For markables with `REF` annotation, we assume that this is entailed by `REF=OLD`, `SIT`, `BOUND`, `GROUP`, `EXPL`, `IDIOM` (note that we exclude `GEN` and `PRED`, because these could provide novel lexical material). For markables with `IS` annotation, this is entailed by `IS>=UNIQUE`. For non-referring expressions, annotation is to be based on *lexical cohesion*, i.e., whether or not a word has been mentioned before.

	> Note: For non-referring expressions, annotators should annotate `KNOWN` on a lexical basis, i.e., either if the current word has been mentioned before. For a previously , or, if the lexeme could be replaced with a related word mentioned before without any change in meaning.

	> Note: By definition, phrases like *the same*, *another*, etc. refer to previously introduced types, so they are `KNOWN`. Likewise, *before* is `KNOWN` as it refers to a previous point in time, which must be identifiable to the hearer at the time of utterance.

- `NOVEL`: hearer-new, novel, relevant information. For referring expressions, this is everything with `IS=TYPE` or `IS=REFERENTIAL`. For non-referring expressions, automated pre-annotation can exploit as to whether a word, its hyponyms or synonyms has been mentioned before. In information-structural terms, `H_NEW` is a characteristic of new information focus.

	> Note: In the first sentence of a text, every content word is `NOVEL` except for terms referring to the situational context (e.g., *here* , *I*, *today*, etc.). Note that we exclude front matter (author, headline) from annotation.

	> Note: Any content word that is not `KNOWN` is to be annotated as `NOVEL`.

	> Note: WH-words are `NOVEL` by definition. In a question without WH-word, the syntactic head (which carries the interrogative mood) should be annotated as `NOVEL`. Here, the novel information lies in the modality. This supersedes the lexical criteria for `KNOWN` mentioned above.

	> Note: In imperative sentences, the syntactic head (which carries the imperative mood) should be annotated as `NOVEL`. Here, the novel information lies in the modality. This supersedes the lexical criteria for `KNOWN` mentioned above.

	> Note: If a sentence does not contain material annotated as *NOVEL*, it is not a repetition or summarization, and it is not *COUNTER* (see below), annotate the syntactic head as `NOVEL`. This can be the case for sentences with identifying or definitory copula (see ex. (4.a) below).

- `COUNTER` (`KNOWN-COUNTER`, `NOVEL-COUNTER`): information that conflicts with information that can be presupposed by the hearer. In information-structural terms, `COUNTER` is a characteristic of contrastive focus (`NEWS=COUNTER`, no `IS` or `IS<=UNIQUE`) or contrastive topics (`NEWS=COUNTER`, `IS>=FAMILIAR`. Note that counterexpected information cannot be automatically spotted, because in the prototypical cases, it is the unexpected way of combining aspects of information elicited in the preceding discourse. In discourse-structural terms, counterexpected information is expected to occur in and only in concessions.

	> Note: Annotators should first annotate all content words in the current sentence according to the `KNOWN`-`NOVEL` dichotomy. The annotation of `COUNTER` should combine with earlier `KNOWN` or `NOVEL` annotations, if possible.

	> Note: Annotators should annotate `COUNTER` to the syntactic head of a contrastive clause, not at a clausal constituent.

	> Note: Annotators should annotate `COUNTER` if and only if either the clause contains the discourse marker *however* (or an equivalent), or if the clause could be reformulated in a way that it contains *however* and could still occur naturally at the current position in text.

As for content words, we focus on NOUN, PROPN, and VERB (excl. auxiliaries). adnominal adjectives, adverbs, pronouns and non-referring nouns or proper names are to be annotated only if no NOUN, PROPN or VERB carries any `NOVEL` or `COUNTER` information.

## Examples

For the examples quoted below, we assume that they constitute the beginning of a text or conversation (unless marked otherwise).

> (1.a) *Susan_N gave_N Betsy_N a pet hamster_N.*
> (1.b) *She_K reminded_N her_K that such hamsters_K were quite shy_N.* (from topic section)

We don't annotate *quite* because *shy* already introduces a novel element. We don't annotate *pet* because it is a non-referring noun in a sentence that provides other novel elements.

> (2.a) *I_K 'm reading_N The French Lieutenant's Woman_N.*
> (2.b) *The book_K, which is Fowles_K 's best_N, was a bestseller_N last year_K.* (from topic section)

The first person pronoun always refers to a known (`IS>=FAMILIAR`) entity. In its current form, we assume that *John Fowles* is identifiable (`IS>=UNIQUE`) to the hearer -- at least in the context of the book -- because he is referred to with the surname, only. On the other hand, there is no previous mention of (the adjective) *best*. As this is not adnominal, it is subject to annotation, and thus taken to be novel, here. (Note that this is not a referring expression -- although an indefinite NP -- because it is predicative.) Neither was the word *bestseller* mentioned before, nor a synonym or hypernym (something akin to *book* would change the sentence meaning), so this is novel, as well. Finally, *last year* is a referring expression that is, however, part of the shared personal experience of hearer and speaker (`IS>=FAMILIAR`), so it is `KNOWN`.

> Note: *The French Lieutenant's Woman* is a proper name, so none of its constituents represent an independent referring expression. Here, annotate the syntactic head only.

> (3.a) *My_K dog_N is getting_N quite obstreperous_N.*
> (3.b) *I_K took_N him_K to the vet_N the other day_N.*
> (3.c) *The mangy old beast_K always hates_N these visits_K.* (from topic section)

In (3.a), everything is `NOVEL` except for the first-person pronoun. In (3.b), the vet is `NOVEL` (cannot be inferred from *obstreperous* -- this might be different if a sickness would have been mentioned, then, *the vet* might be considered `IS=FAMILIAR`). We assume that *the other day* points to a specific day which is, however, not revealed to the hearer, so that it is not uniquely identifiable, so it is `NOVEL`. Example (3.c) contains *hates* as a lexically novel word. The *visits*, are lexically novel, as well, but are, in fact in focus (`IS=FOCUS`), as this is the event denoted by the immediately preceding sentence. As a test, they can be replaced with pronominal *it* or *that*. The adjectives *many* and *old* are lexically novel, but they are adnominal modifiers in a sentence that contains another `NOVEL` element, so, they are not to be annotated.

> (4.a) *So the patient_K's life_K is restored_N.*
> (4.b) *That_K's the good_K news_N.*
> (4.c) *However, his_K chin_K skin_K doesn't look_KNOWN-COUNTER the same_K as it_K did before_K.*
(TED talk 1003)

This excerpt does not start with the first sentence, previously mentioned phrases include *so*, *the patient* (known because of referentiality, though), *skin* (*the skin drape*), *good* (*very good looking*), *look*, *before*, as well as *life* (indirectly, via the phrase *their lives*). Here, *the good news* is not a referring expression (but `REF=IDIOM`), so, it is to be annotated as `KNOWN`. The word *restored* is a near-synonym of previously mentioned *reconstruct*.

In (4.a), there is no lexically novel material in content words. The sentence is not a repetition, so, annotate the syntactic head as `NOVEL`. Here, that is the (lexically known) verb *restored*.
In (4.b), the lexically novel material is an idiomatic expression and thus should be annotated as `KNOWN`. As no otherwise `NOVEL` material is found, the adjective *good* is to be annotated, as well, but it is lexically `KNOWN`, too. Yet, as the sentence lacks otherwise novel material and is not `COUNTER`, we annotate the syntactic head (*news*) as `NOVEL`.

> Note: In the definition of the syntactic head, we follow the Universal Dependencies. That is, in a copular sentence, the predicative argument should be marked as head, not the copula.

In (4.c), there is no lexically or referentially novel materials. The discourse marker *however* indicates a concession, so we annotate the syntactic head of the containing clause as `KNOWN-COUNTER`. As this sentence is marked with `COUNTER`, DO NOT annotate the syntactic head as `NOVEL`.

## Automated pre-annotation (`NOVEL_AUTO`)

1. remove function words (excl. copula), reduce content phrases to their syntactic head (in terms of UD)
- for interrogative sentences: 
	1. mark WH-words as `NOVEL`
	2. if none is found, mark the syntactic root as `NOVEL`, because it carries the question (for yes-no-questions)
	3. everything else as `KNOWN`
- for declarative sentences: 
	1. `KNOWN`: for everything with `REF_AUTO=?OLD`, `UPOS=PRON` or whose `LEMMA` occurs in preceding text
	2. `NOVEL`: for every other content word.
	3. if a sentence does not contain a `NOVEL` element, and it is not a fully repeated sentence, mark its syntactic head as `KNOWN-COUNTER`. Here, we would expect that the combination of different known aspects is counterexpected.
- for exclamative sentences:
	1. mark syntactic head as `NOVEL` (because it is its mood that is exclamative)
	2. mark everything else as `KNOWN`
- for any sentence that contains *however*, *yet* or an equivalent discourse marker, mark the syntactic head of the clause that contains the discourse marker as `COUNTER`.

## Annotation procedure

Novelty annotation involves two columns: `NOVEL_AUTO` and `NOVEL`. 

- `NOVEL_AUTO` is pre-populated in static pre-annotation
- `NOVEL` is dynamically populated on the basis of `NOVEL_AUTO` and earlier, manual annotation

Annotators should operate on the `NOVEL` column only. Any automated annotation in the `NOVEL` column left untouched after annotation is considered approved. If you feel the `NOVEL_AUTO` annotation is incorrect, please leave a comment in the `COMMENT` column.