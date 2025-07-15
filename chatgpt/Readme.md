# Perform coreference and IS annotations with ChatGPT

## Using ChatGPT

- https://openai.com/de-DE/policies/terms-of-use/
- https://platform.openai.com/settings/organization: organization ACoLi, project AURIS Givenness Hierarchy
- models and parameters: https://openai.com/de-DE/api/
- GPT-4.1 mini: https://platform.openai.com/docs/models/gpt-4.1-mini, we work with gpt-4.1-mini-2025-04-14 
- limits (free tier): https://platform.openai.com/settings/organization/limits
- programmatically handling limits
	- https://cookbook.openai.com/examples/how_to_handle_rate_limits
	- python: `RateLimitError` => cascade the models down?
- for estimating token length: https://github.com/openai/tiktoken, https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken, I guess r50k_base is a good upper bound for the length of all later models
- https://openai.com/index/introducing-structured-outputs-in-the-api/

## Initial experiment

ChatGPT, online version 2025-07-09

You are a cognitive linguist annotating coreference and givenness as described below. Do not perform web search. All information is provided in the prompt. Do not return explanations, but only the desired output in JSONL as described below. Annotate the text in chunks of 15 sentences.

Coreference annotaton: Given a text in English, you give a unique identifier to every entity (person, object, organization, living thing, etc.) mentioned with a noun phrase in the text. For every noun phrase, annotate the syntactic head (e.g., the last nominal in a noun phrase) with the identifier of the entity it refers to or with "_" if there is none. Subsequent mentions to the same entity should use the same identifier. If a noun refers to an event introduced in a previous utterance, annotate the syntactic head (i.e., the main predicate) of the antecedent utterance with the same identifier as used for the noun. In the following, we use the term "referent" for this identifier, and "referring expression" for the word (phrase) that is annotated with the referent.

Givenness annotation: Annotate every noun phrase and predicate annotated with a referent in coreference annotation. 
If the referent is the main subject of the preceding sentence, annotate FOCUS. If the referent is previously mentioned in the same sentence, annotate FOCUS. If the referent occurs in the last two utterances, annotate FOCUS. If the referent refers to the main event described in the preceding utterance, annotate FOCUS. 
If it is not annotated as FOCUS: If the referent is mentioned in one of the two preceding utterances, annotate ACTIVATED. If the referent is an event that is part of the event or situation described in the preceding utterance, annotate ACTIVATED.
If it is not annotated as FOCUS or ACTIVATED: If the referent is previously mentioned, annotate FAMILIAR. If the referent is a specific entity that is commonly known, annotate FAMILIAR.
If it is not annotated as FOCUS or ACTIVATED or FAMILIAR: If the referent is not previously mentioned, but the referring expression provides enough descriptive content to identify or describe the referent as a unique entity (e.g., by its proper name, or by an association with another, uniquely identifiable entity), annotate it as UNIQUE.
If it is not annotated as FOCUS or ACTIVATED or FAMILIAR or UNIQUE: If the referent is mentioned later in discourse, annotate  REFERENTIAL. If it is clear that the speaker intents to refer to a specific entity, but does not provide sufficient information to describe it as a unique entity, annotate REFERENTIAL.
If it is not annotated as FOCUS or ACTIVATED or FAMILIAR or UNIQUE or REFERENTIAL: If the referring expression refers to a specific entity, annotate NEW.

The input (text to be annotated) is provided with one utterance per line. Every utterance is preceded by its number (sentence id). The sentence id is not part of the text.

The output (annotation) should be provided in the JSONL format, with one array per sentence. The first element in the array is the sentence id provided in the input. This is followed by one dict per word. This dict contains the word form as "form". If the word is not head of a referring expression or its antecedent no further information is to be added. If the word is annotated with a referent, provide its id as value of the key "coref". The id should be a short, unambigous mnenonic. If the word is annotated with a referent, provide its givenness annotation as the value of "givenness". Possible values for "givenness" are only "FOCUS", "ACTIVATED", "FAMILIAR", "UNIQUE", "REFERENTIAL" and "NEW".

During annotation, treat interpunctuation as separate words.

Example input:

1. Peter called Jim a Republican.
2. He insulted him.

Example output:

{"id":"1", {"form":"Peter", "coref":"peter", "givenness":"UNIQUE"}, {"form": "called"}, {"form":"Jim", "coref":"jim", "givenness":"UNIQUE"}, {"form":"a"}, {"form":"Republican"}, {"form":"."}}
{"id":"2", {"form":"He", "coref":"peter", "givenness":"FOCUS"}, {"form":"insulted"}, {"form":"him", "coref":"jim", "givenness":"ACTIVATED", {"form":"."}}}

Annotate the following text:

1 Seeking refuge: Every refugee woman has dealt with sexual violence
2 For women fleeing a country on their own, sexual violence is almost part of daily life.
3 When they arrive in Germany, they are often traumatised.
4 One house offers refuge.
5 Four women are sitting in a large kitchen.
6 Every one of them has a baby with them, the oldest of which is one year old.
7 One woman holds her little son in her arms.
8 He looks around the room inquisitively, his eyes wide.
9 His mother stares at the tabletop.
10 Until she realises she's being watched.
11 She smiles briefly and kisses the child.
12 The scene looks normal.
13 Until you start talking to Katrin Bahr.
14 She is the field manager for Condrobs, a provider of social assistance within Bavaria. One of the issues she deals with is refugee women.
15 The four women in the kitchen are refugees.
16 They live in the north of Munich, in one of the few decentralised accommodation centres in Bavaria for refugee women and their children who have made the journey alone.
17 Condrobs opened the centre in January, in collaboration with Pro Familia and the Munich Women's Help organisation.
18 It recently had its official opening.
19 60 people live there - around 40 women and 20 children.
20 There are no men - not even male visitors.
21 The exception is a bodyguard on the door.
22 I'm not exaggerating when I say that every woman who arrives here has dealt with sexual violence on her way to find refuge, said Bahr.
23 Men flee because of war, because they are politically persecuted, because they are threatened with torture or death, or because their families pin their hopes on them and send them to Europe, she explains.
24 When women flee, other reasons are in the foreground: "Many women sneak away secretly, because they see no other way out".
25 In their home countries, they experienced sexual violence, forced marriage, honour killings, slavery or forced prostitution.
26 That propels them forward.
27 And it continues even while they're on the run.
28 It is not a rare occurrence that traffickers request a sexual act in exchange for a bottle of water, for example, says Bahr.
29 And the woman are alone, unprotected by their families.
30 If you think that this stops as soon as they arrive in Germany, you'd be wrong, says Bahr.
31 Even in Germany, lone women are often seen as inferior in refugee accommodation, and, in the worst cases, they are abused.
32 As a result, around 90 percent of the women living in accommodation in the north of Munich are traumatised, she estimates.
33 "Some of the children were certainly not conceived with the woman's consent".
34 Many women are so used to it that they do not say anything, she says.
35 "Or they can't bring themselves to talk about what they experienced because they are too ashamed".
36 Because they often don't know how to get help, there needs to be more accommodation just for them, says Bahr.
37 In Bavaria, the seven district governments are responsible for providing accommodation for refugees.
38 When asked if they knew of projects like the one in Munich operating within the areas they covered, some answered with "no".
39 In Upper Palatinate and Upper Franconia regions, for example, there is no similar accommodation offered by the government.
40 Even in Swabia, women who come as lone refugees are not given separate accommodation, says Karl-Heinz Meyer, press spokesperson for the region.
41 In Upper Bavaria, Lower Franconia and Middle Franconia, floors, or individual houses, are set aside in some shared accommodation for lone women and their children.
42 The exception is Lower Bavaria: there, there are two central accommodation centres exclusively for women.
43 Even the European Parliament's Committee on Women's Rights and Gender Equality stresses that women must be provided with accommodation separate from that of the men.
44 In a study published on behalf of the Committee, it was stated that it is very important that men and women are given separate accommodation.
45 "If there is a lack of private space, or if men and women are provided with accommodation together, this can result in (perpetual) violence against women".
46 Washing facilities, above all, should be separate, and easily accessible for women, according to the study.
47 The extent to which women need this protection can be seen in the sheer number of people interested in the house in Munich.
48 Since word has got around that we exist, we have developed a long waiting list, says Bahr.
49 It would be easy to open a second house.


## Output

{"id":"1", "tokens":[{"form":"Seeking"},{"form":"refuge"},{"form":": "},{"form":"Every"},{"form":"refugee","coref":"refugee_woman","givenness":"UNIQUE"},{"form":"woman","coref":"refugee_woman","givenness":"UNIQUE"},{"form":"has"},{"form":"dealt"},{"form":"with"},{"form":"sexual"},{"form":"violence","coref":"sexual_violence","givenness":"UNIQUE"}]}
{"id":"2", "tokens":[{"form":"For"},{"form":"women","coref":"refugee_woman","givenness":"FAMILIAR"},{"form":"fleeing"},{"form":"a"},{"form":"country","coref":"country","givenness":"UNIQUE"},{"form":"on"},{"form":"their","coref":"refugee_woman","givenness":"FOCUS"},{"form":"own,"},{"form":"sexual","coref":"sexual_violence","givenness":"ACTIVATED"},{"form":"violence","coref":"sexual_violence","givenness":"FOCUS"},{"form":"is"},{"form":"almost"},{"form":"part"},{"form":"of"},{"form":"daily"},{"form":"life","coref":"daily_life","givenness":"UNIQUE"},{"form":"."}]}
{"id":"3", "tokens":[{"form":"When"},{"form":"they","coref":"refugee_woman","givenness":"FOCUS"},{"form":"arrive"},{"form":"in"},{"form":"Germany","coref":"Germany","givenness":"UNIQUE"},{"form":","},{"form":"they","coref":"refugee_woman","givenness":"FOCUS"},{"form":"are"},{"form":"often"},{"form":"traumatised","coref":"trauma_event","givenness":"NEW"},{"form":"."}]}
{"id":"4", "tokens":[{"form":"One"},{"form":"house","coref":"house","givenness":"UNIQUE"},{"form":"offers"},{"form":"refuge","coref":"refuge_event","givenness":"NEW"},{"form":"."}]}
{"id":"5", "tokens":[{"form":"Four"},{"form":"women","coref":"refugee_woman","givenness":"ACTIVATED"},{"form":"are"},{"form":"sitting"},{"form":"in"},{"form":"a"},{"form":"large"},{"form":"kitchen","coref":"kitchen","givenness":"UNIQUE"},{"form":"."}]}
{"id":"6", "tokens":[{"form":"Every"},{"form":"one","coref":"refugee_woman","givenness":"ACTIVATED"},{"form":"of"},{"form":"them","coref":"refugee_woman","givenness":"ACTIVATED"},{"form":"has"},{"form":"a"},{"form":"baby","coref":"baby","givenness":"UNIQUE"},{"form":"with"},{"form":"them","coref":"refugee_woman","givenness":"FOCUS"},{"form":","},{"form":"the"},{"form":"oldest","coref":"oldest_baby","givenness":"UNIQUE"},{"form":"of"},{"form":"which"},{"form":"is"},{"form":"one"},{"form":"year"},{"form":"old","coref":"age","givenness":"UNIQUE"},{"form":"."}]}
{"id":"7", "tokens":[{"form":"One"},{"form":"woman","coref":"refugee_woman","givenness":"ACTIVATED"},{"form":"holds"},{"form":"her","coref":"refugee_woman","givenness":"FOCUS"},{"form":"little"},{"form":"son","coref":"child_son","givenness":"UNIQUE"},{"form":"in"},{"form":"her","coref":"refugee_woman","givenness":"FOCUS"},{"form":"arms","coref":"arms","givenness":"UNIQUE"},{"form":"."}]}
{"id":"8", "tokens":[{"form":"He","coref":"child_son","givenness":"FOCUS"},{"form":"looks"},{"form":"around"},{"form":"the"},{"form":"room","coref":"room","givenness":"UNIQUE"},{"form":"inquisitively","coref":"inquiry_event","givenness":"NEW"},{"form":","},{"form":"his","coref":"child_son","givenness":"FOCUS"},{"form":"eyes","coref":"eyes","givenness":"UNIQUE"},{"form":"wide","coref":"expression_wide","givenness":"NEW"},{"form":"."}]}
{"id":"9", "tokens":[{"form":"His","coref":"child_son","givenness":"FOCUS"},{"form":"mother","coref":"mother","givenness":"UNIQUE"},{"form":"stares"},{"form":"at"},{"form":"the"},{"form":"tabletop","coref":"tabletop","givenness":"UNIQUE"},{"form":"."}]}
{"id":"10", "tokens":[{"form":"Until"},{"form":"she","coref":"mother","givenness":"FOCUS"},{"form":"realises"},{"form":"she's"},{"form":"being"},{"form":"watched","coref":"watch_event","givenness":"NEW"},{"form":"."}]}
