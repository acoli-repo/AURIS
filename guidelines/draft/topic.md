## 6. Information Structure

We provide a partial annotation of information structure, only, by focusing on information status and familiarity topics. As for the latter, we adopt the approach and the terminology of Centering Theory, and thus speak of "backward-looking center" (CB)

The topic of an utterance is defined the entity (referent) that the utterance is construed about. Traditionally, two cases are distinguished:
- **aboutness topic**: an entity in the current utterance about which the speaker wanted to provide more information.
- **familiarity topic**: the entity of the current utterance that is closest to the focus (or center) of attention (in the sense of Gundel et al. 1993), thus most likely to be the entity that the current sentence is about

The direct annotation of aboutness topics is notoriously difficult, so that we resort to the annotation of (a specific operationalization of) familiarity topics, instead.

### 6.1 Familiarity Topic: Backward-Looking Center (`CB`)

After IS annotation, CB annotation is to be done in the `CB` column.

In Centering Theory (Grosz et al. 1995), the "backward-looking center" is a technical term for the notion of "familiarity topic". The following criteria apply:<sup>[1](lit.md#topic1)</sup>

- Each sentence ("utterance") has at most one backward-looking center.
- The backward-looking center of the current sentence must be explicitly mentioned ("realized") in the immediately preceding sentence. That is, it must have been previously annotated as `IN FOCUS` or `ACTIVATED`.
- If there is more than one CB candidate that has been mentioned in the preceding sentence, check the properties of its antecendent. If an IN FOCUS expression refers to the preceding sentence or clauses within it, annotate it only as CB if no other candidate an be found. 
- Mark the expression as CB whose antecedent is highest on the following ranking ("salience ranking"):<sup>[2](lit.md#topic2)</sup>
    1. SUBJECT (of main clause, `GR`=`SBJ`)
    2. OBJECT (of main clause, e.g., direct or indirect object, `GR`=`OBJ`)
    3. OTHER  (oblique argument of main clause, e.g., prepositional phrase, `GR`=`other`), 
    4. MAIN CLAUSE (event anaphora: refer to the main clause or the full sentence, rather than any of its arguments, no `GR` annotation)
    5. SUBJECT (of dependent clause, `GR`=`SBJ_2`, `SBJ_3`, etc.)
    6. OBJECT (of dependent clause, `GR`=`OBJ_2`, `OBJ_3`, etc.)
    7. OTHER (of dependent clause, `GR`=`other_2`, `other_3`, etc.)
    8. DEPENDENT CLAUSE (event anaphora: refer to a dependent clause, no `GR` annotation)
    9. etc., for more deeply embedded dependent clauses
- If there are multiple CB candidates whose antecedent realization (according to this ranking) is identical, chose the one whose antecedent is mentioned _first_ in the preceding sentence.

CB annotation is partially pre-annotated, but has to be manually refined.

Selected CB examples:
- antecedent SUBJECT (main clause, Grosz et al. 1995, ex. 6)

    > (1.a) * **Susan**  gave Betsy a pet hamster.*

    > (1.b) <ins>She</ins> reminded her that such hamsters were quite shy.

- antecedent direct object (main clause, Grosz et al. 1995, ex. 18)

    > (2.a) *I'm reading **The French Lieutenant's Woman**.*
    
    > (2.b) *<ins>The book</ins>, which is Fowles's best, was a bestseller last year.*

- antecedent indirect object (main clause, Grosz et al. 1995, ex. 17)

    > (3.a) *My dog is getting quite obstreperous.*

    > (3.b) *I took **him** to the vet the other day.*

    > (3.c) *<ins>The mangy old beast</ins> always hates these visits.*

- antecedent clause

    > (4.a) * **John fell off his bike**.*
    
    > (4.b) *<ins>This/it</ins> happened yesterday.*

- antecedent SUBJECT (dependent clause, Grosz et al. 1995, ex. 2)
    
    > (5.a) *It was a store **John** had frequented for many years.*
    
    > (5.b) *<ins>He</ins> was excited that he could finally buy a piano.*

# 6.2 Topic Continuity: Centering Transitions (`Centering`)

Centering defines coherence relations that hold between utterance *U_i* and the preceding utterance *U_i-1*, resp., their backward-looking centers *CB(U_i)* and *CB(U_i-1)*.
Based on the identification of the backward-looking center, Centering Theory distinguishes four primary types of transitions between utterances:

- If the current utterance has no backward-looking center, annotate `NO-CB`
- If the backward-looking center of the preceding utterance is the same as the backward-looking center of the current utterance
    - If the backward-looking center is the subject of the main clause of *U_i*, then annotate `CONTINUE`
    - It the backward-looking center is not the subject of the main clause of *U_i*, then annotate `RETAIN`
- If the backward-looking center of the preceding utterance is not the same as the backward-looking center of the current utterance
    - Annotate `SHIFT`

Centering Theory then predicts that `CONTINUE` relations are more coherence than `RETAIN` than `SHIFT`.

Our texts are most written language, and sometimes the flow of utterances is interrupted by comments (e.g., "(Laughter.)", written as a sentence in a transcript) or metadata (e.g., headlines). Therefore, in cases in which the preceding utterance does not carry `CB` annotation, we consider the latest preceding utterance with a `CB`, instead. However, the centering transition is to be annotated in round brackets, then.

> Note: In our framework, Centering transitions are automatically induced from `CB` annotation. So, this is not to be manually annotated. 7