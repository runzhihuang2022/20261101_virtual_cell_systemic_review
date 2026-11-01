# Virtual cell review reproducibility materials

Search records, evidence-assessment data, tables and conceptual figure assets for
*Application Research Progress of Virtual Cells in Tissue and Organ Injury Repair and Regenerative Medicine*.

Repository: https://github.com/runzhihuang2022/20261101_virtual_cell_systemic_review

## Repository organization

| Directory | Contents |
|---|---|
| Figure1–Figure5 | Approved figure, legend, source citations and figure-specific runner |
| data/evidence | Frozen searches, eligibility decisions, appraisal fields and reference index |
| script, scripts | Convenience launcher and canonical replay code |
| table | Editable source tables for Tables 1–3 |
| config, environment | Figure hashes and runtime requirements |
| outputs/reference | Verified reference export checksums |
| provenance, validation | Release manifest and executed reproduction record |

## Quick start

```bash
git clone https://github.com/runzhihuang2022/20261101_virtual_cell_systemic_review.git
cd 20261101_virtual_cell_systemic_review
python scripts/reproduce.py all --out outputs/replay_01
python Figure4/run_figure.py --out outputs/figure4_replay
```

Use Python 3.10 or later. Output directories must be new. The replay uses the
standard library, exports five record-level evidence tables and the reference
index, copies the three manuscript tables and verifies the five approved figures.

## Search and assessment scope

The search was frozen on 26 October 2026, with the function-based eligibility
amendment dated 27 October and six bibliographic additions dated 31 October.
Recorded screening and appraisal states are retained. Independent human review
is pending. DOME fields describe computational reporting and evaluation; they
are not an overall certainty score. The manuscript is a Review with systematic
searches and a structured evidence map.

## Figures and data

Figures are conceptual illustrations prepared with OpenAI image generation.
Replay preserves the approved assets and does not promise deterministic image
generation. Search records, report identifiers and citations support tracing each
record to its source. Original experiments and models belong to the cited studies.
Author review comments, correspondence, private document histories and publisher
full-text files are not part of this public package.

## Citation and rights

The article title above identifies this review; a journal DOI has not yet been
assigned. Third-party resources retain their original rights. No additional
blanket licence is assigned by this packaging step.
