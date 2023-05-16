## 6. Information Structure

We provide a partial annotation of information structure, only, by focusing on information status and familiarity topics. As for the latter, we adopt the approach and the terminology of Centering Theory, and thus speak of "backward-looking center" (CB)


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
