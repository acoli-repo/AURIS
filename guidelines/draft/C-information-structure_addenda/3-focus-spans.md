# Aspects of Focus

In the context of information structure, "focus" refers to the part(s) of the sentence that comprise information that cannot be presupposed by the speaker, i.e., new information. Traditional approaches on focus annotation concentrate on a question test, i.e., the annotator needs to construct a hypothetical question that a hearer might be asking at the current point in discourse and to which the next utterance might be a possible answer. Unfortunately, annotating these questions is infeasible in terms of effort and agreement between annotators regarding those questions is low.

For this reason, we concentrate on the annotation of newsworthiness, instead. As focus is defined by being the part(s) of the sentence that contain non-presupposed information (i.e., new information), it can be largely predicted from newsworthiness. This is explored with the following line of annotations.

## Novelty (`NOVEL`)

As for novelty, or, more technically, newsworthiness, we annotate text spans, with a focus on referring expressions (anaphoric pronouns, noun phrases, proper nouns) and content words (independent nouns, proper nouns, verbs, and, under certain circumstances, adjectives and adverbs). As for function words (determiners, adpositions, conjunctions, syntactically bound pronouns, etc.) and modifiers (numerals, most adjectives and adverbs), these are included in the span of (and with the same `NOVEL` value) as their syntactic head.

> (1) *She reminded her that such hamsters were quite shy.*

In (1), the following content words are to be annotated:

- `remained` (verb)
- `hamsters` (independent noun)
- `shy` (predicative adverb -- not a syntactic modifier)

... and the following referring expressions

- `She` (anaphoric pronoun)
- `her` (anaphoric pronoun)
- `(such) hamsters` (definite noun phrase)

As a rule, relative clauses and prepositional phrases that modify noun phrases are not considered to be part of the referring expression designated by the noun phrase.

For zero anaphors, no a referring expression is only to be annotated if a token representing the zero anaphora has been created during preprocessing (e.g., tokenization or parsing). Likewise, clitics are only to be annotated as referring expressions if they are separated from the word they are attached to, either by orthographic convention or during preprocessing. Automated preprocessing may be error-prone, but annotators are advised to not correct any tokenization errors they observe, but document such errors in a separate file ("log") and to hand in that log file along with their annotation. 

In span-based annotation, we aim for the annotation of continuous spans, where function words are annotated along with their respective syntactic head, unless they have a newsworthiness value on their own:

- `such` is annotated together with `hamsters` because they form a noun phrase
- `quite` is annotated together with `shy` because it's a syntactic modifier
- `were` is annotated together with `shy` because the copula serves to mark a the adverb as a predicate adverb

Adjacent phrases with the same newsworthiness value are annotated as a single span. These may include further function words. Function words that are "stranded" between phrases with different newsworthiness values are not to be annotated.

> In (1), this may be the case for `that`. Although its syntactic head (in Universal Dependencies) is `were ... shy`, it should only be included in the span of `were ... shy` if that has the same newsworthiness value as the intermediate phrase `such hamsters`.

We distinguish two major qualities of newsworthy information:

- `KNOWN`: hearer-old information that is known to (or inferrable by) the hearer, i.e.,

    - *for referring expressions*: a referring expression that denotes an entity (person, object, place, organization, ...) that has been previously mentioned, that is generally known and unambiguously identifiable in the current context (`the pope`) or that is otherwise evoked in the discourse context (e.g., because it is part of the communication situation, e.g., `this Monday`, `you`, `I`, `here`), or because of a semantic relation (hyponymy, meronymy, etc.) connects it with a `KNOWN` referring expression in the preceding discourse. 

        > Note: For the latter case (not unambiguously identifiable, but in a semantic relation with a `KNOWN` referring expression `Y`) , annotate `KNOWN` for a referring expression `X` if and only if (a) `X` can be replaced by `Y` without a change in meaning, or (b) `X` can be paraphrased by `(the) X of Y` (or `... from Y`, or another preposition) without a change in meaning.

        > Note: Syntactically bound pronouns (e.g., relative pronouns such as `the people, **who** ...`) and attributive possessive pronouns (e.g., `**our** students`) are function words that are not to be annotated unless included in an otherwise continuous span. Nominal predicates (e.g. `Peter is **a football star**`) are to be annotated as non-referring expressions.

    - *for non-referring expressions* (e.g., verbs, predicative adverbs, predicative adjectives): a context word that has been introduced in a preceding sentence, either directly, with a morphologically related form (`America` - `American`), or means of a semantic relation (synonymy, hypernymy, hyponymy, meronymy, etc.) with a previously mentioned word.

        > Note: For the latter case (semantic relation between word `X` and a previously mentioned word `Y`), annotate `KNOWN` only `X` could be replaced by `Y` without a change in meaning.

	> Note: By definition, phrases like *the same*, *another*, etc. refer to previously introduced types, so they are `KNOWN`.

- `NOVEL`: hearer-new, novel, relevant information.

    - *for referring expressions*: a referring expression that denotes an specific entity (person, object, place, organization, ...) that is neither previously mentioned, nor identifiable in the current context nor otherwise evoked in the discourse context
    - Any content word that is not `KNOWN` is to be annotated as `NOVEL`.

    > Note: In the first sentence of a text, every content word is `NOVEL` except for terms referring to the situational context (e.g., *here* , *I*, *today*, etc.) or referring expressions with an antecedent in the same sentence. Note that we exclude front matter (author, headline) from annotation.

	> Note: WH-words are `NOVEL` by definition. In a question without WH-word, the verb (which carries the interrogative mood) should be annotated as `NOVEL`. Here, the novel information lies in the modality. This supersedes the lexical criteria for `KNOWN` mentioned above.

	> Note: In imperative sentences, the verb (which carries the imperative mood) should be annotated as `NOVEL`. Here, the novel information lies in the modality. This supersedes the lexical criteria for `KNOWN` mentioned above.

	> Note: If a sentence does not contain material annotated as *NOVEL*, it is not a repetition or summarization, and it is not *COUNTER* (see below), annotate the syntactic head as `NOVEL`. Typically, this is the predicate of the (first) main clause. This can be the case for sentences with identifying or definitory copula (see ex. (4.a) below).

**After** the annotation of `KNOWN` and `NOVEL` for a sentence, annotators need to spot contrastive or counterexpected information. , so that these annotations are nested inside the span(s) of `KNOWN` and `NOVEL` annotations.

- `COUNTER`: information that conflicts or contrasts with information that can be presupposed by the hearer. 
Such information may be either `KNOWN` or `NOVEL`, it can thus be combined with both `KNOWN` and `NOVEL`.

	> Note: Annotators should first annotate all content words in the current sentence according to the `KNOWN`-`NOVEL` dichotomy. The annotation of `COUNTER` should be nested inside the annotation of earlier `KNOWN` or `NOVEL` annotations, if possible.

	> Note: Annotators should annotate `COUNTER` in a sentence if and only if either the clause contains a discourse marker such as *however*, *although*, *nevertheless* (or an equivalent, e.g., German *allerdings*, *jedoch*, *dennoch*, *trotzdem*, *nichtsdestotrotz*), or if the clause could be reformulated in a way that it contains *however* or an an equivalent and may still occur naturally at the current position in text. Note that the `COUNTER` annotation pertains to the contrasted information, not the discourse marker itself.


## Examples

For the examples quoted below, we assume that they constitute the beginning of a text or conversation (unless marked otherwise).

> (1.a)
>
    <NOVEL>Susan gave Betsy a pet hamster.</NOVEL>

> (1.b)
>
    <KNOWN>She</KNOWN> <NOVEL>reminded</NOVEL> <KNOWN>her</KNOWN> that <KNOWN>such hamsters</KNOWN> <NOVEL>were quite shy</NOVEL>.

> (2.a) 
>
    <KNOWN>I</KNOWN> <NOVEL>'m reading The French Lieutenant's Woman_N</NOVEL>.


> (2.b) 
>
    <KNOWN>The book</KNOWN>, which is <KNOWN>Fowles's</KNOWN> <NOVEL>best</NOVEL>, <NOVEL>was a bestseller</NOVEL> <KNOWN>last year</KNOWN>.

The first person pronoun always refers to a known entity. In its current form, we assume that *John Fowles* is identifiable to the hearer -- at least in the context of the book -- because he is referred to with the surname, only. On the other hand, there is no previous mention of (the adjective) *best*. As this is not adnominal, it is subject to annotation, and thus taken to be novel, here. (Note that this is not a referring expression -- although an indefinite NP -- because it is predicative.) Neither was the word *bestseller* mentioned before, nor a synonym or hypernym (something akin to *book* would change the sentence meaning), so this is novel, as well. Finally, *last year* is a referring expression that is, however, part of the shared personal experience of hearer and speaker, so it is `KNOWN`.

> Note: *The French Lieutenant's Woman* is a proper name, so none of its constituents represent an independent referring expression.

> (3.a) 
>
    <KNOWN>My</KNOWN> <NOVEL>dog is getting quite obstreperous</NOVEL>.*

> (3.b) 
>
    <KNOWN>I</KNOWN> <NOVEL>took</NOVEL> <KNOWN>him</KNOWN> <NOVEL>to the vet the other day</NOVEL>.

> (3.c) 
>
    <KNOWN>The mangy old beast</KNOWN> <NOVEL>always hates</NOVEL> <KNOWN>these visits</KNOWN>.

In (3.a), everything is `NOVEL` except for the first-person pronoun. In (3.b), the vet is `NOVEL` (cannot be inferred from *obstreperous* -- this might be different if a sickness would have been mentioned, then, *the vet* might be considered familiar. We assume that *the other day* points to a specific day which is, however, not revealed to the hearer, so that it is not uniquely identifiable, so it is `NOVEL`. Example (3.c) contains *hates* as a lexically novel word. The *visits*, are lexically novel, as well, but are, in fact evoked by `took him to the vet`, i.e., the event denoted by the immediately preceding sentence. As a test, they can be replaced with pronominal *it* or *that*, or, here, with *being taken to the vet*. The adjectives *mangy* and *old* are lexically novel, but they are part of a `KNOWN` referring expression in a sentence that contains another `NOVEL` element, so, they are not to be annotated.

> (4.a) 
>
    So <KNOWN>the patient's life</KNOWN> <NOVEL>is restored</NOVEL>.

> (4.b) 
>
    <KNOWN>That</KNOWN> <NOVEL>'s the good news</NOVEL>.

> (4.c) 
>
    However, <KNOWN>his chin skin <COUNTER>doesn't look the same</COUNTER> as it did before</KNOWN>. (TED talk 1003)

This excerpt does not start with the first sentence, previously mentioned phrases include *so*, *the patient* (known because of referentiality, though), *skin* (*the skin drape*), *good* (*very good looking*), *look*, *before*, as well as *life* (indirectly, via the phrase *their lives*). Here, *the good news* is not a referring expression, but an idiomatic phrase. 

In (4.a), there is no lexically novel material in content words. The sentence is not a repetition, so, annotate the syntactic head as `NOVEL`. Here, that is the (lexically known) verb *restored*.
In (4.b), the lexically novel material is an idiomatic, non-referring expression and thus should be annotated as `KNOWN`. Yet, as the sentence lacks otherwise novel material and is not `COUNTER`, we annotate the syntactic head (*news*) as `NOVEL`.

In (4.c), there is no lexically or referentially novel materials. In particular, the negation particle is not novel, because it is a function word. The discourse marker *however* indicates a concession, so we annotate the counterexpected part of the containing clause as `(KNOWN-)COUNTER`. As this sentence is marked with `COUNTER`, it is not necessary to annotate the syntactic head as `NOVEL`.

## Technical notes

During annotation, you can use `<K>`, `<N>` and `<C>` as notational short-hands for `<KNOWN>`, `<NOVEL>` and `<COUNTER>` (and their closed counterparts), and then expand them by global replacement.

## Acknowledgements

These guidelines have been developed by Christian Chiarcos, with input by Melissa Hofmann, Tamara Kreissl, and Giulia Mantovani (in alphabetic order).
