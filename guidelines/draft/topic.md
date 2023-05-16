## Backward-Looking Center (`CB`)

After IS annotation, CB annotation is to be done in a separate column.

In Centering Theory (Grosz et al. 1995), the "backward-looking center" is a technical term for the notion of "familiarity topic". The following criteria apply:

- Each sentence ("utterance") has at most one backward-looking center.
- The backward-looking center of the current sentence must be explicitly mentioned ("realized") in the immediately preceding sentence. That is, it must have been previously annotated as `IN FOCUS` or `ACTIVATED`.
- If there is more than one CB candidate that has been mentioned in the preceding sentence, check the properties of its antecendent. 
- Mark the expression as CB whose antecedent is highest on the following ranking ("salience ranking"):
    1. SUBJECT (of main clause, `GR`=`subj`)
    2. OBJECT (of main clause, e.g., direct or indirect object, `GR`=`obj`)
    3. OTHER  (oblique argument of main clause, e.g., prepositional phrase, `GR`=`other`), 
    4. MAIN CLAUSE (event anaphora: refer to the main clause or the full sentence, rather than any of its arguments, no `GR` annotation)
    5. SUBJECT (of dependent clause, `GR`=`subj_2`, `subj_3`, etc.)
    6. OBJECT (of dependent clause, `GR`=`obj_2`, `obj_3`, etc.)
    7. OTHER (of dependent clause, `GR`=`other_2`, `other_3`, etc.)
    8. DEPENDENT CLAUSE (event anaphora: refer to a dependent clause, no `GR` annotation)
    9. etc., for more deeply embedded dependent clauses
- If there are multiple CB candidates whose antecedent realization (according to this ranking) is identical, chose the one whose antecedent is mentioned _first_ in the preceding sentence.

CB annotation is partially pre-annotated, but has to be manually refined.

Selected CB examples:
- antecedent SUBJECT (main clause, Grosz et al. 1995, ex. 6)

    > (24)
    > a. **Susan**  gave Betsy a pet hamster.
    > b. <u>She</u> reminded her that such hamsters were quite shy.

- antecedent direct object (main clause, Grosz et al. 1995, ex. 18)

    > (25) 
    > a. I'm reading **The French Lieutenant's Woman**.
    > b. <u>The book</u>, which is Fowles's best, was a bestseller last year.

- antecedent indirect object (main clause, Grosz et al. 1995, ex. 17)

    > (25) 
    > a. My dog is getting quite obstreperous. 
    > b. I took **him** to the vet the other day.
    > c. <u>The mangy old beast</u> always hates these visits.

- antecedent clause (ex. 10 from above)

    > (10') 
    > a. **John fell off his bike**. 
    > b. <u>This/it</u> happened yesterday.

- antecedent SUBJECT (dependent clause, Grosz et al. 1995, ex. 2)
    > (26) 
    > b. It was a store **John** had frequented for many years.
    > c. <u>He</u> was excited that he could finally buy a piano.

> Notes: 
> 1. Following Grosz et al. (1995), Centering Theory was extended and parameterized. The definitions given above represent *one* specific interpretation of Grosz et al.'s criteria designed to facilitate unambiguous annotation. Other interpretations are possible.
> 2. The salience ranking has been extended to include dependent clauses and word order, following Gernsbacher (2013). Furthermore, the Centering category "OTHER" is split into "OBLIQUE ARGUMENT" and "CLAUSE". Unlike the original formulation of Centering, the Givenness Hierarchy supports event anaphora.
> 3. If an IN FOCUS expression refers to the preceding sentence or clauses within it, annotate it only as CB if no other candidate