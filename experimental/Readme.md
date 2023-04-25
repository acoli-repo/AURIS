# Experimental annotations

Experimental annotations are conducted without proper annotations guidelines and in ad hoc formats.
Make sure to use only material that has copyright clearance.

In every file, the first line must contain metadata, i.e., date of retrieval/annotation, source URL/annotator

Except for `src/` (which permits Markdown), all other files must be txt files with one sentence per line and paragraph boundaries marked by an empty line. Every sentence can be preceded by comments (line[s] starting with `#`) that can contain auxiliary annotation, if tagged as such, e.g., `Q:...` for question under discussion. Plain comments should not have a tag.

For the annotation of spans, use square brackets. For labelled spans, use `_Label`. If the Label is a single letter, say, `F`, then write `_F`. If it has several letters, e.g., `FOC`, use curly brackets, e.g., `_{FOC}`.

- `src/`: unformatted source file should be \*.txt, optionally, an accompanying Markdown file can be provided
- `topic/`: annotated for topic with (unlabelled) spans using "as for"/"aboutness" te
- `focus/`: annotated for focus with (unlabelled) spans and accompanying question under discussion (QUD)

Annotations should use the original file name, and add tags to identify annotators and date of annotation.