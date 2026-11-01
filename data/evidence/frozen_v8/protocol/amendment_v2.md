# Protocol amendment 2 — functional virtual-cell eligibility

Date: 27 October 2026, Asia/Shanghai. This amendment follows the author's request to narrow the v7 evidence corpus; it is not a retrospectively registered protocol. The v7 files and original retrieval counts are frozen.

## Author decisions

The author confirmed that earlier models meeting the prediction / perturbation-simulation criterion remain eligible. The Cell Perspective published on 12 December 2024 defines a temporal subgroup, not an eligibility cutoff. The author also requested completion of AI-assisted screening and appraisal followed by a blinded verification package for the research team. Human independent review has not yet occurred.

## Question and inclusion gate

Which empirically evaluated computational models predict a change in cellular molecular state, fate, or functional phenotype under a defined intervention or future condition, and what supports their use in injury repair and regeneration?

Eligible original studies must meet all three functional conditions:

1. A computational representation of a cell or cellular state is an input or explicitly modelled entity.
2. An executable model generates a cellular response to a specified genetic, chemical, environmental, or temporal condition. A learned regulatory-network model may qualify when it actually simulates interventions. A temporal model must evaluate missing-timepoint interpolation or future extrapolation against observations, rather than simply order observed cells in pseudotime. Interpolation and future-only forecasting are recorded separately.
3. Model-development reports evaluate prediction against empirical cellular observations; benchmark reports compare such predictive models, including negative results. Algorithm development is eligible without a repair application. Application reports must document an executed intervention simulation with an empirically evaluated model; their own biological validation is extracted separately, so computational-only applications are not silently treated as experimentally confirmed applications. This clarification separates functional eligibility from validation strength.

Primary evidence strata: M, predictive model / algorithm development; A, model application in a biological study; B, independent comparative evaluation of predictive models. H is a separate historical/mechanistic virtual-cell model stratum: explicit VCell / whole-cell simulators with empirical evaluation. H is never pooled with AI-model performance or counted as modern AI applications. Repair relevance is recorded separately: direct injury/repair, enabling lineage/reprogramming, general transferable method, or historical model foundation. Cancer-derived training or benchmark data do not exclude a general model, but cancer-specific clinical classifiers are outside scope.

Historical mechanistic VCell / whole-cell simulation papers are assessed separately for H; tutorials and reviews remain background. They are not combined with the AI or data-trained cell-state prediction evidence denominator. The 1997 Schaff et al. paper is an early verified VCell landmark, not asserted to be the first use of the term anywhere. The 2024 Bunne et al. Perspective (preprint 18 September; Cell issue 12 December) is the prespecified modern-framework temporal anchor, not the first predictive algorithm.

## Exclusions from the primary evidence denominator

E1: review, perspective, news, teaching material, protocol without new evaluative results, correction, or other non-original report.
E2: atlas, experimental resource, lineage description, or mechanism experiment without executed cell-response prediction.
E3: annotation, integration, imputation, deconvolution, embeddings, regulatory association, or pseudotime only; no tested response / future-state prediction.
E4: bulk biomarker, clinical risk / treatment-response classifier, docking, network pharmacology, or disease diagnostic model without a cellular response simulator.
E5: generic mechanistic modelling, tissue/organ physics, whole-organ agent simulation, or non-cellular computation without an explicit virtual-cell/whole-cell platform or data-trained cellular prediction task.
E6: non-vertebrate biological application without a model-development or benchmark contribution and without injury/repair relevance. Non-vertebrate model foundations can enter H, or M/B if they meet the predictive-model criteria; species applicability is recorded separately.
E7: retracted or withdrawn report; retained in the audit, not in positive synthesis.
E8: superseded version of the same study, linked to its report family.
U1: insufficient abstract or source access to determine eligibility; retain for retrieval, never infer exclusion from missing text.

A model name or the words 'virtual cell' are neither necessary nor sufficient. Relevance is determined from the actual input, simulated condition, output, and evaluation. Earlier foundation-model papers remain background if their evaluated tasks only concern annotation or embedding quality. The 20 author-designated historical CNS papers retain their citation role even if they no longer count as primary included predictive studies.

Oncology-only applications are assigned to contextual stratum C rather than the primary repair application denominator. This application boundary was made explicit during source appraisal on 27 October 2026; general transferable method and benchmark studies remain eligible regardless of the training tissue. C is distinct from the biological-reference category used in v7. Application relevance includes injury, maladaptive remodeling, and enabling lineage control; it is not synonymous with demonstrated regeneration.

## Screening and provenance

Reassess all 4,885 v7 report-family representatives, including the 182 provisional inclusions. Preserve stable R identifiers. Record the source actually inspected, decision, reason, functional evidence, assessor, and review date. Software routing is distinct from AI title/abstract assessment and full-text appraisal. No record becomes eligible solely through a keyword match. Missing full text remains an access status, not an adverse quality score. New searches, if executed, have separate identifiers and raw-response logs.

## Appraisal

Use the DOME data, optimisation, model and evaluation recommendations for model reporting and validation, with an explicitly review-specific reproducibility field. These are domain judgments, not a validated numerical risk-of-bias scale. Extract the independent sampling unit, split unit, held-out condition, comparator, metric, uncertainty, code/data source and applicability to repair. Do not use DOME to award GRADE certainty or declare 150 studies high quality. Evaluate animal intervention components with SYRCLE where applicable; clinical prediction with PROBAST+AI, trials with RoB 2, and non-randomized clinical interventions with an appropriate design-specific tool only if such studies are included.

Report source-supported strengths and concerns per domain. Absence from a targeted extraction is 'not established from inspected source', not proof that the study omitted it. For overall synthesis use descriptive validation profiles, kept distinct from risk of bias: within-dataset prediction; held-out condition/context; external dataset; prospective experimental test. Multiple profiles may apply. Clinical GRADE is reserved for comparable clinical outcome evidence bodies.

## Independent verification and reporting

Deliver a blinded worksheet without the first assessor's decisions and an adjudication template. The author team will complete independent verification. Until then describe the workflow exactly as single-AI-assisted screening/appraisal awaiting author verification. Report screening outcomes and functional boundaries in Methods / Results; discuss their implications once in Discussion Limitations. Preserve the title, approved outline and ten tissue scope. An empty organ-specific predictive evidence cell is an informative finding, not a reason to broaden eligibility.

## Primary methodological sources

- Schaff et al. 1997. https://pubmed.ncbi.nlm.nih.gov/9284281/ ; doi:10.1016/S0006-3495(97)78146-3.
- Bunne et al. 2024. https://pubmed.ncbi.nlm.nih.gov/39672099/ ; doi:10.1016/j.cell.2024.11.015. Preprint: https://arxiv.org/abs/2409.11654.
- DOME. https://doi.org/10.1038/s41592-021-01205-4.
- PRISMA 2020 explanation, selection process / automation. https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/.
- Cochrane Handbook, chapter 4, section 4.6.4. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04.
