# AURIS annotation manual

Covers annotations for discourse, information structure and reference on two levels, provided in two parts

- [A. word-level annotations](word-level/): reference, information status (givenness), topicality, focus

- [B. sentence-level annotations](sentence-level/): coherence (discourse) relations

Both guidelines are provided in excerpt form (excluding aspects of pre-annotation) and in full form (including appendices, literature reference and metadata)

## Editing the draft

- for deleting stuff, please use XML comments (`<!-- ... -->`)
- for every example, add `<example id="some-id">...</example>` before and after
- for every sub-example within an example, add `<sub id="some-other-id">...</sub>` before and after
- when referencing an example, add `<ref id="some-ex-or-sub-id">...</ref>` around the reference, e.g.,

      <example id="nr56">
        <sub id="nr56.a">(56.a) rztfuzguh hgj jhgjkl</sub>
        ...
      </example>
  
      this is a reference to example <ref id="nr56">(1)</ref>, and its sub-item <ref id="some-sub-item">(1.a)</ref>.
