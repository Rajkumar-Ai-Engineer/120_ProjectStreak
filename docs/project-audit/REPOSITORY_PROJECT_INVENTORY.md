# Repository Project Inventory

Snapshot date: 2026-11-05. This report describes what is present in the repository, not what an external project catalogue expects.

## Repository structure

Default branch: master. The recursive Git tree contains 59,407 entries (251 tree entries and 59,156 blob entries at the inspected revision); the very large blob count is dominated by datasets, images, notebooks, model artifacts and other project assets. It must not be interpreted as a project count.

Top-level content includes: DeepLearning/, GenerativeAI/, Machine_Learning/, computer vision/, computervision/, da/, genai/, nlp/, README.md, PROJECT_INVENTORY.md, documentation_inventory.json, domain audit files and DOCUMENTATION_COVERAGE.md.

## Formal project register

The canonical project list contains 62 indexed entries. Full per-project file, entrypoint and import evidence is in [MASTER_PROJECT_INVENTORY.md](MASTER_PROJECT_INVENTORY.md).

| Domain | Indexed projects |
|---|---:|
| DeepLearning | 10 |
| GenerativeAI | 19 |
| Machine_Learning | 19 |
| computer vision | 14 |
| **Total** | **62** |

## Additional source-bearing project candidates

27 additional folders contain code or notebooks outside the 62-entry canonical register:

- DeepLearning: 9 additional directories.
- NLP: 15 source-bearing project directories (13 unnumbered and 2 explicitly labelled 067 and 068).
- computervision: 3 code-bearing project directories.

These are candidates pending catalogue reconciliation. They are not automatically added to the canonical count because duplicates, alternate experiments and overlapping IDs remain possible.

## Documentation evidence

- Canonical 62: listed in PROJECT_INVENTORY.md and documentation_inventory.json.
- DeepLearning: 19 project-like folders documented in DeepLearning/README.md; 10 indexed and 9 candidates.
- GenerativeAI: 19 projects indexed in GenerativeAI/README.md.
- Computer Vision: 14 numbered entries in computer vision/README.md; 3 additional code-bearing entries in computervision/README.md.
- NLP: 15 source-bearing folders documented in nlp/README.md.
- Data Analytics: 5 PDFs and 16 screenshots indexed in da/README.md; no executable source files were identified in da/.

## Implementation evidence classifications

| Evidence class | Meaning |
|---|---|
| Source-bearing | Python, notebook, web source or another implementation artifact is present |
| Documentation-only | README or notes exist but no implementation evidence is established |
| Image-only | A screenshot or PNG illustrates a project but does not prove source code exists |
| Data/model asset | Dataset, checkpoint, model, weights or output; not an independent project |
| Unverified | Retrieval or content limitations prevent a confident technical conclusion |

## Important limitations

- No external authoritative 120-project source catalogue was attached for this audit.
- A recursive tree is useful for inventory but does not expose binary content or prove runtime behavior.
- Several large notebooks and PDFs have documented retrieval or extraction limitations.
- Static inspection does not prove that dependencies install, applications start, APIs work, models train, or predictions are correct.
- See PARTIAL_AND_INCOMPLETE_PROJECTS.md for known code-review findings and verification boundaries.