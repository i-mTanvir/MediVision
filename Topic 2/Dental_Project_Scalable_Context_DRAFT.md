# Dental Project Scalable Research Context — Draft

> **Purpose:** This file is the reusable, evidence-controlled context for the second dental research project. It records what the executed notebook actually contains, what can safely be claimed, what remains exploratory, and which recent papers should guide the manuscript. Future writing should use this file before reopening the notebook.
>
> **Audit date:** 4 September 2026  
> **Primary source:** `E:\Defense\Discuss\Topic 2\ThesisDental_v5.ipynb`  
> **Notebook SHA-256:** `8796AFF52CD0621745922854B9D89046AA27DE88C1ECDF879C90D4FF1CC207F2`

## 1. Project identity

**Current project title**  
*Deep Learning-Driven Radiographic Analysis for Impacted Tooth Detection and Localization*

**Group members**

1. Meherajur Rahman — Student ID: 0242220005101400
2. Jannatun Nahar — Student ID: 0242220005101281

**Supervisor**  
Dr. Arif Mahmud  
Associate Professor & Associate Head

**Co-supervisor**  
Dr. Md Zahid Hasan  
Associate Professor

## 2. Executive research summary

The notebook studies impacted-tooth recognition from panoramic dental radiographs. Its strongest completed component is **image-level binary classification** of impacted versus non-impacted cases. It also explores quadrant attention, Grad-CAM++, pseudo-box generation, and YOLOv8-based object detection. Those latter components constitute **weakly supervised localization**, because their targets are generated from classification-model explanations rather than independently drawn and adjudicated expert bounding boxes.

The current v5 run does not establish a new state-of-the-art model. The best executed conventional baseline, ResNet-18, achieved a test AUROC of 0.7768 and accuracy of 0.7474, while the final OOF-selected anchor achieved AUROC 0.7417 and accuracy 0.7062 at its accuracy-oriented threshold. The work is nevertheless potentially publishable as a carefully scoped study of:

- comparative classification under a modest clinical dataset;
- calibration and sensitivity-oriented triage;
- label-review prioritisation;
- the limitations of explanation-derived pseudo-localisation;
- a transparent negative-result analysis showing that increased architectural complexity did not reliably improve discrimination.

The paper should not claim clinically validated localisation unless expert bounding boxes and an independent detection test set are added.

## 3. Notebook provenance and structure

| Item | Audited value |
|---|---:|
| Notebook format | Jupyter nbformat 4.5 |
| Kernel | Python 3 |
| Total cells | 27 |
| Code cells | 25 |
| Markdown cells | 2 |
| Executed code cells | 25 |
| Notebook size | 15,680,540 bytes |
| Main execution setting visible in outputs | Kaggle GPU workflow, primarily T4 |

### Cell-level functional map

| Cell | Main role |
|---:|---|
| 1 | Project overview and intended experimental phases |
| 2 | Environment and dependency setup |
| 3 | Configuration, paths, seeds, and hyperparameters |
| 4 | Dataset discovery and image/label mapping |
| 5 | Exploratory data analysis |
| 6 | Preprocessing, geometry handling, datasets, and multi-instance views |
| 7 | Model definitions |
| 8 | Training and evaluation engine |
| 9 | Fixed split and Phase I baselines |
| 10 | Phase II EfficientNet-B4 + CBAM |
| 11 | Threshold selection and temperature calibration |
| 12 | Phase III quadrant attention-MIL |
| 13 | Two-stage cross-validation, label-review weighting, strong and anchor families |
| 14 | Label-disagreement audit and review sheets |
| 15 | Grad-CAM++ visualisation |
| 16 | Leak-aware pseudo-box generation |
| 17 | YOLO dataset preparation and training |
| 18 | YOLO evaluation against pseudo-reference boxes |
| 19 | Calibration analysis |
| 20 | Bootstrap confidence intervals |
| 21 | Sensitivity-oriented triage thresholds |
| 22 | Model comparison and roadmap |
| 23 | DeLong and McNemar comparisons |
| 24 | Inference benchmark |
| 25 | Failure analysis |
| 26 | Artifact export |
| 27 | Draft methods skeleton |

## 4. Dataset and cohort

### Audited facts

- The tracking CSV contains `Serial`, `Image Number`, `Impacted Tooth`, and `Note`.
- 1,287 images were successfully mapped to labels; two referenced images were missing.
- Class distribution: 786 non-impacted and 501 impacted images.
- Class imbalance ratio: approximately 1.57:1.
- The notebook describes anonymised public-hospital clinical panoramic radiographs from Bangladesh in JPEG/PNG form.
- Mean image dimensions reported by the notebook are approximately 1271 × 752 pixels.
- Fixed stratified split:
  - training: 900 images;
  - validation: 193 images;
  - test: 194 images;
  - development total: 1,093 images.
- No separate confirmed-label CSV was supplied in the run, so the original tracking-sheet labels were used as the reference standard.

### Critical cohort limitation

The notebook carries image identifiers but no verified patient identifiers. It therefore demonstrates an **image-level stratified split**, not a proven patient-level split. If a patient contributed multiple radiographs, subject leakage cannot currently be excluded. The manuscript must not say “patient-independent” or “patient-level split” unless patient IDs are recovered and the split is rebuilt or verified.

### Information still required from the research team

- ethics approval or waiver and approval number;
- data-use permission and institutional source wording;
- acquisition devices and exposure protocol;
- date range and inclusion/exclusion criteria;
- number of unique patients;
- number and expertise of label annotators;
- adjudication procedure and inter-rater agreement;
- definition of “impacted” and whether all tooth types or only selected teeth were included;
- whether one image can contain multiple impacted teeth.

## 5. Preprocessing and model pipeline

### Image processing

The implemented pipeline includes automatic border cropping, CLAHE enhancement, aspect-ratio-preserving letterboxing, augmentation, and horizontal-flip test-time augmentation. The standard anchor resolution is 512 pixels; the strong-model family uses 576 pixels. Coordinate transforms for Grad-CAM and pseudo-boxes are mapped back through the letterbox geometry and include an internal geometry self-test.

### Model families

1. **Phase I baselines:** ResNet-18 and EfficientNet-B0.
2. **Phase II:** EfficientNet-B4 with CBAM attention.
3. **Phase III:** quadrant attention-MIL using a bag of five views: full panorama, left-upper, left-lower, right-upper, and right-lower.
4. **Two-stage cross-validation:**
   - Stage 1: five folds, ten epochs, used to generate out-of-fold probabilities for label-review flags.
   - Stage 2 strong family: ConvNeXt-Small requested through `timm` with ImageNet-22k weights, five folds, 16 epochs, 576-pixel input.
   - Stage 2 anchor family: EfficientNet-B4 + CBAM, three folds, 20 epochs, 512-pixel input.
5. **Weak localisation:** multi-layer Grad-CAM++ → pseudo-box extraction → YOLOv8n.

### Model metadata caveat

The strong-model training output indicates that the `timm` ImageNet-22k ConvNeXt-Small weights loaded successfully. Later metadata reports `random-init (smoke)`, apparently because a test shell created with `pretrained=False` overwrote the global metadata variable. Before publication, model provenance should be stored per checkpoint rather than in mutable global state.

## 6. Executed results ledger

### 6.1 Phase I and Phase II classification

| Model / setting | Test F1 | Accuracy | AUROC | Notes |
|---|---:|---:|---:|---|
| ResNet-18 | 0.6573 | 0.7474 | 0.7768 | Best executed accuracy and AUROC among the reported full-image candidates |
| EfficientNet-B0 | 0.6108 | 0.6649 | 0.7658 | Phase I comparison |
| EfficientNet-B4 + CBAM, TTA | 0.6014 | 0.7062 | 0.7606 | Precision 0.6418; recall 0.5658; AP 0.6833 |
| EfficientNet-B4 + CBAM, no TTA | — | — | 0.7698 | Horizontal-flip TTA reduced AUROC in this run |

Additional Phase II results at the selected accuracy-oriented threshold:

- balanced accuracy: 0.6812;
- Cohen's kappa: 0.3702;
- Matthews correlation coefficient: 0.3720;
- validation-fitted temperature: 0.90.

### 6.2 Quadrant attention-MIL

| Setting | Test F1 | Accuracy | AUROC |
|---|---:|---:|---:|
| Horizontal-flip TTA | 0.4078 | 0.6856 | 0.7646 |
| No TTA | 0.3846 | — | 0.7822 |

Mean attention weights were approximately full view 0.590, left-upper 0.051, left-lower 0.119, right-upper 0.062, and right-lower 0.178. In impacted cases, the full view remained the most-attended instance in 57 of 76 positive bags. Thus, this experiment does not demonstrate posterior-quadrant localisation. Attention weights should be described as exploratory model behaviour, not anatomical evidence.

### 6.3 Cross-validated families and selected model

| Development OOF candidate | AUROC | Accuracy / related value |
|---|---:|---:|
| Strong ConvNeXt family | 0.7298 | — |
| Anchor EfficientNet-B4 + CBAM family | 0.7426 | 0.6999 at accuracy-oriented threshold |
| Logistic stacker | 0.7423 | — |
| Rank average | 0.7413 | — |

The OOF selector chose the anchor family. Consequently, the final “selected fusion” is not a multimodel ensemble; it is the anchor model family. Manuscript wording should call it the **OOF-selected anchor**, not an ensemble or fusion.

| Final test operating point | Threshold | F1 | Accuracy | Balanced accuracy | AUROC |
|---|---:|---:|---:|---:|---:|
| OOF accuracy-oriented | 0.705 | 0.5289 | 0.7062 | 0.6554 | 0.7417 |
| OOF F1-oriented | 0.480 | 0.6258 | 0.6856 | 0.6830 | 0.7417 |

The strong-family test AUROC was 0.7452; the anchor-family test AUROC was 0.7417. The majority-class baseline accuracy was 0.6082.

### 6.4 Calibration

- raw expected calibration error (ECE): 0.1258;
- temperature-scaled ECE: 0.1058;
- fitted temperature: 0.90.

Temperature scaling improved calibration modestly but did not make it strong. The paper should show a reliability diagram, ECE, and preferably Brier score with confidence intervals.

### 6.5 Bootstrap uncertainty on the 194-image test set

| Metric | Bootstrap mean | SD | 95% percentile CI |
|---|---:|---:|---:|
| F1 | 0.5260 | 0.0530 | [0.4190, 0.6230] |
| AUROC | 0.7431 | 0.0348 | [0.6714, 0.8089] |
| Precision | 0.7106 | — | [0.5854, 0.8367] |
| Recall | 0.4201 | — | [0.3117, 0.5278] |
| Accuracy | 0.7064 | — | [0.6443, 0.7680] |

These intervals quantify sampling uncertainty only for the internal test set. They do not establish external generalisability.

### 6.6 Sensitivity-oriented triage analysis

| OOF target | Threshold | Test sensitivity | Specificity | PPV | NPV | Referral rate | Accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|
| ≥90% sensitivity | 0.344 | 0.921 | 0.297 | 0.458 | 0.854 | 0.789 | 0.541 |
| ≥95% sensitivity | 0.291 | 0.961 | 0.237 | 0.448 | 0.903 | 0.840 | 0.521 |

For the ≥90% setting, the confusion counts are TP 70, FP 83, FN 6, TN 35. For the ≥95% setting, they are TP 73, FP 90, FN 3, TN 28. The high referral burden means this is an exploratory rule-out/triage analysis, not a deployable clinical operating point.

### 6.7 Label-disagreement audit

- OOF review candidates in development data: 60 of 1,093 (5.5%).
- Composition: 11 positive labels with probability below 0.25 and 49 negative labels with probability above 0.75.
- Test review candidates: 10 of 194 (5.2%).
- Automatic label flips in the executed run: zero.
- Tier-2 examples downweighted to 0.2 during Stage 2: 25.

The projected OOF accuracy 0.7548 and AUROC 0.8304 after hypothetically confirming all 60 disagreements are **counterfactual rescoring estimates**, not observed trained-model performance. Model–label disagreement must not be called proven label error without independent expert review.

### 6.8 Weak localisation and YOLO

- Images with generated pseudo-boxes: 299.
- Generated boxes: 416 (mean 1.39 per boxed image).
- Background images: 403.
- Disputed/excluded images: 585.
- Box-area mean: 9.2%; median: 10.2%; 10th–90th percentile: 3.0%–13.6%.
- YOLO validation set: 133 images with 70 pseudo-reference instances.
- YOLO precision: 0.0040.
- YOLO recall: 0.8000.
- mAP@0.50: 0.0782.
- mAP@0.50:0.95: 0.0208.

These metrics compare YOLO predictions with pseudo-boxes, not expert boxes. They measure weak-supervision consistency rather than clinical localisation accuracy. Moreover, the YOLO validation configuration uses the classification test set for checkpoint selection/early stopping. Therefore, the current localisation evaluation is not an untouched final test.

### 6.9 Statistical comparisons and failure analysis

- Strong vs anchor OOF AUROC: 0.7298 vs 0.7426; DeLong p = 0.1194.
- Phase II vs selected anchor test AUROC: 0.7606 vs 0.7417; DeLong p = 0.1520.
- Phase II vs anchor test accuracy: both 0.7062; McNemar p = 1.000 with discordant counts b = 11 and c = 11.
- `p = 1.000` here means balanced discordance, not identical predictions.
- Selected-vs-anchor p = 1 is tautological because the selector chose the anchor itself.
- Final-model test failures at the accuracy-oriented threshold: 44 false negatives and 13 false positives.

### 6.10 Inference speed

- Phase II single-view model: approximately 57.8 images/s; 17.3 ms/image.
- Quadrant MIL: approximately 21.7 images/s; 46.06 ms/image.

## 7. Claims that are safe, conditional, or unsafe

### Safe from the present notebook

- A deep-learning comparison was conducted on 1,287 labelled panoramic images.
- ResNet-18 provided the strongest reported internal test discrimination among the executed candidates.
- More complex attention, MIL, and stacking strategies did not clearly outperform the simple baseline.
- Calibration remained imperfect after temperature scaling.
- High-sensitivity thresholds reduced missed impacted cases but generated high referral rates.
- Grad-CAM-derived pseudo-boxes can support an exploratory weak-localisation pipeline.
- The notebook provides uncertainty estimates and transparent negative-result analyses.

### Conditional—requires explicit caveat

- “Label-noise candidates” means cases prioritised for expert review, not confirmed errors.
- “Localisation” must be qualified as weakly supervised or explanation-derived.
- Internal generalisation applies only to the current image-level split.
- Attention and Grad-CAM are qualitative interpretability tools, not causal localisation evidence.

### Unsafe until additional work is completed

- patient-independent performance;
- clinically validated object localisation;
- state-of-the-art performance;
- automatic correction of annotation errors;
- external generalisability;
- clinical deployment readiness;
- a measured 94.8% accuracy ceiling;
- superiority of the final v5 model over the ResNet-18 baseline or the historical v4 result.

## 8. Major design risks and required fixes

| Priority | Risk | Why it matters | Recommended correction |
|---:|---|---|---|
| 1 | No patient identifiers in the split | Multiple images from one person may cross partitions | Recover subject IDs and rebuild GroupShuffleSplit/StratifiedGroupKFold partitions |
| 1 | Classification test reused during model development | Repeated Phase I–III and historical comparisons weaken the “untouched test” claim | Freeze a new final test set or use nested CV and reserve a truly locked external set |
| 1 | YOLO uses the classification test as validation | Early stopping selects on the supposed test | Create YOLO train/validation subsets only within development data; evaluate once on locked expert-box test data |
| 1 | No expert localisation reference standard | Pseudo-box mAP is not clinical localisation accuracy | Obtain radiologist/dentist boxes with independent review and adjudication |
| 1 | Unverified clinical labels | Model disagreement can be model error or label error | Dual expert review, adjudication, and agreement statistics |
| 2 | Candidate selection and threshold fitting share OOF predictions | Creates selection optimism | Nested CV or a separate calibration/selection subset |
| 2 | Final selected model underperforms ResNet-18 | Weakens an “enhanced model” narrative | Make ResNet-18 the primary baseline/model unless a clean rerun justifies another choice |
| 2 | `STRONG_META` can be overwritten | Breaks reproducibility claims about pretraining | Store immutable per-run metadata beside each checkpoint |
| 2 | Historical v4 and current v5 figures coexist | Can produce inconsistent manuscript numbers | Use a versioned results registry and cite only one locked analysis set |
| 2 | Horizontal-flip TTA reduced AUROC in several models | TTA is not automatically beneficial | Pre-specify and validate TTA; report both or omit if not beneficial |
| 3 | Calibration remains moderate | Limits probability-based decisions | Add Brier score, calibration slope/intercept, and decision-curve analysis |
| 3 | No external cohort | Limits transportability | External test on DENTEX or a second institution/device |

## 9. Title assessment and recommended positioning

### Does title-aligned prior work exist?

Yes. Directly aligned studies already cover impacted-tooth classification, object detection, segmentation, and localisation using Faster R-CNN, YOLO, MedSAM, CNN–Transformer hybrids, and multi-stage systems. Therefore, “using deep learning to detect and localise impacted teeth” alone is not a sufficient novelty claim.

### Current title risk

The current title suggests validated detection and localisation. The notebook currently demonstrates binary image classification plus weakly supervised pseudo-localisation. Unless expert bounding boxes are added, the title is broader than the available evidence.

### Safer title for the present evidence

**Deep Learning-Based Classification and Weakly Supervised Localization of Impacted Teeth on Panoramic Radiographs**

### Stronger title after expert-box validation

The original title can be retained after all of the following are available:

- expert-drawn and adjudicated tooth-level boxes or masks;
- patient-independent development and test partitions;
- a detection validation set drawn only from development data;
- a locked internal or external detection test;
- object-level AP/mAP, sensitivity, false positives per image, and localisation error with confidence intervals.

### Realistic novelty directions

1. A Bangladesh clinical OPG cohort with explicit acquisition and annotation provenance.
2. Patient-independent evaluation with an external DENTEX test.
3. Calibration-aware, sensitivity-oriented triage with decision-curve analysis.
4. A formal comparison of classification saliency, pseudo-box detection, and expert localisation.
5. A transparent negative-result study showing that model complexity does not guarantee improvement on modest dental datasets.

## 10. Recommended manuscript blueprint

### Introduction

1. Clinical importance of impacted teeth and panoramic radiography.
2. Existing AI work in classification, detection, segmentation, and surgical-difficulty prediction.
3. Problem: limited annotated datasets, unclear patient-level separation, weak external validation, and confusion between saliency and localisation.
4. Study objective stated without claiming clinical deployment.
5. Contributions limited to what the locked analysis demonstrates.

### Materials and methods

1. Study design, institution, dates, ethics, and data permission.
2. Eligibility criteria, patient/image flow, and missing images.
3. Reference-standard construction and reader agreement.
4. Patient-level split and locked evaluation protocol.
5. Preprocessing and augmentation.
6. Baselines and candidate models.
7. Cross-validation, model selection, and threshold fitting.
8. Calibration and triage evaluation.
9. Weak localisation and, if added, expert-box detection evaluation.
10. Statistical analysis and confidence intervals.
11. Reproducibility: code, versions, hardware, seeds, and checkpoint rules.

### Results

1. Cohort flow and class distribution.
2. Primary classification results with 95% CIs.
3. Pairwise model comparisons.
4. Calibration and clinical operating points.
5. Weak-localisation results clearly separated from expert-reference detection.
6. Failure analysis and reviewed disagreement cases.

### Discussion

1. Principal findings.
2. Why ResNet-18 may outperform more complex models at this sample size.
3. Comparison with Celik, DENTEX, YOLOv8, MedSAM, CNN–Transformer, and recent dual-framework studies.
4. Clinical meaning of high sensitivity and high referral burden.
5. Limits of saliency/pseudo-box localisation.
6. Patient leakage, test reuse, label quality, calibration, and single-centre limitations.
7. Concrete external-validation plan.

### Conclusion

State that the study supports internal image-level classification and exploratory weak localisation. Do not claim autonomous diagnosis, deployment readiness, or validated anatomical localisation.

## 11. Figures and tables worth retaining

### Main figures

1. Cohort flow diagram.
2. End-to-end pipeline diagram separating classification, explanation-derived pseudo-boxes, and YOLO.
3. ROC and precision–recall curves with confidence intervals.
4. Calibration/reliability plot.
5. Triage sensitivity–specificity/referral-rate plot.
6. Expert-reviewed examples of true positive, false positive, false negative, and uncertain labels.
7. If expert boxes become available: ground-truth/prediction overlays and localisation error distribution.

### Main tables

1. Cohort characteristics and class distribution.
2. Model performance with 95% CIs.
3. Pairwise statistical comparison.
4. Calibration and operating points.
5. Literature comparison, with columns that distinguish classification from object detection or segmentation.

Do not compare classification accuracy directly with detection mAP or segmentation IoU. They are different endpoints.

## 12. Recent and foundational literature shortlist

The priority labels below reflect usefulness for this exact project, not journal rank. Links were checked on 4 September 2026. “PDF” denotes an openly downloadable copy; “full text” denotes a browser-readable open article that normally exposes its PDF link.

### A. Highest-priority exact-topic papers

1. **Khurshid Z, Alsleem MH, Aljubairah FA, et al. (2026). Dual Framework for Classification and Detection of Third Molar Impaction in Panoramic Radiographs. International Dental Journal, 76(2), 109430.**  
   Relevance: a recent large expert-annotated study separating classification and YOLO detection. It is the closest recent comparator for the project’s dual-purpose title.  
   [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12907845/) · [DOI](https://doi.org/10.1016/j.identj.2026.109430)

2. **Huang YY, Mao YC, Chen TY, et al. (2025). Application of Convolutional Neural Networks in an Automatic Judgment System for Tooth Impaction Based on Dental Panoramic Radiography. Diagnostics, 15(11), 1363.**  
   Relevance: a clinically sourced workflow combining preprocessing, tooth-region localisation, enhancement, and CNN classification. Useful for methods structure and workflow comparison.  
   [Article](https://doi.org/10.3390/diagnostics15111363) · [PDF](https://www.mdpi.com/2075-4418/15/11/1363/pdf)

3. **Küçük DB, Imak A, Özçelik STA, et al. (2025). Hybrid CNN-Transformer Model for Accurate Impacted Tooth Detection in Panoramic Radiographs. Diagnostics, 15(3), 244.**  
   Relevance: CNN/transformer detection, super-resolution, model fusion, and bounding-box evaluation. Use it to show that true detection studies require spatial annotations and object-level metrics.  
   [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11817329/) · [PDF](https://www.mdpi.com/2075-4418/15/3/244/pdf) · [DOI](https://doi.org/10.3390/diagnostics15030244)

4. **Zirek T, Özic MU, Tassoker M, et al. (2024). AI-Driven Localization of All Impacted Teeth and Prediction of Winter Angulation for Third Molars on Panoramic Radiographs: Clinical User Interface Design. Computers in Biology and Medicine, 178, 108755.**  
   Relevance: YOLOv8 localisation of all impacted teeth plus Winter classification and a clinical interface; a direct benchmark for the original title.  
   [Article/DOI](https://doi.org/10.1016/j.compbiomed.2024.108755) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38897151/)

5. **He Z, Wang Y, Li X. (2024). Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs. Biomedical Engineering and Computational Biology, 15, 11795972241288319.**  
   Relevance: DENTEX-derived impacted-tooth segmentation with MedSAM; reports F1 0.5350 and IoU 0.3652, making it a useful realistic segmentation comparator.  
   [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11456186/) · [PDF](https://journals.sagepub.com/doi/pdf/10.1177/11795972241288319) · [DOI](https://doi.org/10.1177/11795972241288319)

6. **Trachoo V, Taetragool U, Pianchoopat P, et al. (2024/2025). Deep Learning for Predicting the Difficulty Level of Removing the Impacted Mandibular Third Molar. International Dental Journal, 75(1), 144–150.**  
   Relevance: a patient-based, expert-consensus, three-stage ResNet–RetinaNet–ViT study. It demonstrates the annotation and inter-rater reporting expected in clinically credible work.  
   [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11806308/) · [DOI](https://doi.org/10.1016/j.identj.2024.06.021)

7. **Celik ME. (2022). Deep Learning Based Detection Tool for Impacted Mandibular Third Molar Teeth. Diagnostics, 12(4), 942.**  
   Relevance: foundational panoramic impacted-third-molar detection benchmark comparing Faster R-CNN and YOLOv3 on 440 radiographs from 300 patients.  
   [Article](https://www.mdpi.com/2075-4418/12/4/942) · [PDF](https://www.mdpi.com/2075-4418/12/4/942/pdf) · [DOI](https://doi.org/10.3390/diagnostics12040942)

### B. Dataset, segmentation, and broader evidence

8. **Hamamci IE, Er S, Simsar E, et al. (2023). DENTEX: An Abnormal Tooth Detection with Dental Enumeration and Diagnosis Benchmark for Panoramic X-rays.**  
   Relevance: the most useful public benchmark for external testing and expert spatial annotations. It includes multi-institution panoramic radiographs and impacted-tooth diagnosis labels.  
   [Paper](https://arxiv.org/abs/2305.19112) · [PDF](https://arxiv.org/pdf/2305.19112) · [Dataset](https://dentex.grand-challenge.org/data/) · [Code/data repository](https://github.com/ibrahimethemhamamci/DENTEX)

9. **Imak A, Çelebi A, Polat O, Türkoğlu M, Şengür A. (2023). ResMIBCU-Net: An Encoder–Decoder Network … for Impacted Tooth Segmentation in Panoramic X-ray Images. Oral Radiology, 39, 614–628.**  
   Relevance: a direct segmentation comparator and useful source for mask-level metrics and architecture choices.  
   [Publication record](https://avesis.gazi.edu.tr/yayin/19f102a9-1a50-4729-b99a-5a076a3b4807/resmibcu-net-an-encoderdecoder-network-with-residual-blocks-modified-inverted-residual-block-and-bi-directional-convlstm-for-impacted-tooth-segmentation-in-panoramic-x-ray-images)

10. **Faadiya AN, Widyaningrum R, Arindra PK. (2023/2024). The Diagnostic Performance of Impacted Third Molars in the Mandible: A Review of Deep Learning on Panoramic Radiographs. Saudi Dental Journal, 36(3), 404–412.**  
    Relevance: concise review for the introduction, comparison table, and limitations of the field.  
    [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10960107/) · [DOI](https://doi.org/10.1016/j.sdentj.2023.11.025)

11. **Kuwada C, Ariji Y, Fukuda M, et al. (2020). Deep Learning Systems for Detecting and Classifying the Presence of Impacted Supernumerary Teeth in the Maxillary Incisor Region on Panoramic Radiographs.**  
    Relevance: earlier clinically annotated detection/classification work; helpful for historical framing.  
    [PubMed](https://pubmed.ncbi.nlm.nih.gov/32507560/) · [DOI](https://doi.org/10.1016/j.oooo.2020.04.813)

12. **Yoo JH, Yeom HG, Shin W, et al. (2021). Deep Learning Based Prediction of Extraction Difficulty for Mandibular Third Molars. Scientific Reports, 11, 1954.**  
    Relevance: consensus-labelled, patient-based study using panoramic radiographs and explicit clinical difficulty criteria.  
    [Open article](https://www.nature.com/articles/s41598-021-81449-4) · [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820274/) · [PDF](https://www.nature.com/articles/s41598-021-81449-4.pdf)

### C. Reporting and review guidance

13. **Tejani AS, Klontzas ME, Gatti AA, et al. (2024). Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update. Radiology: Artificial Intelligence, 6(4), e240300.**  
    Use this checklist for title/abstract, cohort flow, acquisition, reference standard, partitions, external testing, uncertainty, failure analysis, and code/model availability. CLAIM recommends “reference standard” rather than “ground truth” and distinguishes internal from external testing.  
    [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11304031/) · [PDF](https://pubs.rsna.org/doi/pdf/10.1148/ryai.240300) · [Checklist page](https://pubs.rsna.org/page/ai/claim)

14. **Predicting Alveolar Nerve Injury and the Difficulty Level of Extraction of Impacted Third Molars: A Systematic Review of Deep Learning Approaches (2025).**  
    Relevance: current synthesis of datasets, model families, clinical endpoints, and generalisability limits in impacted-third-molar AI.  
    [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12129997/) · [PDF](https://public-pages-files-2025.frontiersin.org/journals/dental-medicine/articles/10.3389/fdmed.2025.1534406/pdf)

## 13. Immediate download order

Download these first because they most directly determine how the new paper should be positioned:

1. Khurshid et al. 2026 — dual classification/detection comparator.
2. Küçük et al. 2025 — recent true detection and model-fusion comparator.
3. Huang et al. 2025 — clinically structured end-to-end workflow.
4. Zirek et al. 2024 — all-impacted-tooth localisation and Winter classification.
5. He et al. 2024 — MedSAM segmentation on DENTEX.
6. DENTEX 2023 — dataset/benchmark paper and external-validation resource.
7. Celik 2022 — core YOLO/Faster R-CNN benchmark.
8. CLAIM 2024 — reporting checklist.

Suggested storage folder: `E:\Defense\Discuss\Topic 2\Referance Paper\`.

## 14. Proposed clean next experiment

1. Recover patient IDs and rebuild patient-grouped train/validation/test partitions.
2. Freeze the test set before any new model choice.
3. Have at least two dental experts annotate a representative tooth-level box subset; adjudicate disagreements and report agreement.
4. Use ResNet-18 as the transparent primary classification baseline.
5. Compare one justified stronger classifier without a large architecture search.
6. Fit thresholds and calibration only on development data.
7. Train the detector using expert boxes, with its validation set wholly inside development data.
8. Test detection once on locked expert-box cases and report AP50, AP50–95, sensitivity, false positives/image, and confidence intervals.
9. Externally test on DENTEX or a second institutional cohort.
10. Publish a model/data provenance manifest, exact seeds, checkpoint-selection rules, and code.

## 15. Reusable writing rules

- Use only metrics present in the executed v5 outputs unless a later locked-results file supersedes them.
- Keep v4 historical values separate from v5 results.
- Identify the unit of analysis as an image unless unique patient IDs are verified.
- Use “reference standard,” not “ground truth,” following CLAIM 2024.
- Use “internal test” for the current held-out subset and reserve “external test” for a different institution or dataset.
- Never convert p = 1 into “identical predictions” without checking discordant-pair counts.
- Never call pseudo-box evaluation clinical localisation accuracy.
- Never report counterfactual label-rescoring results as achieved model performance.
- Report discrimination, calibration, uncertainty, and clinical operating characteristics together.
- Explain negative findings. Do not hide the fact that the simplest baseline currently performs best.

## 16. Context update protocol

When a new notebook version is produced:

1. record filename, execution date, Git commit, and SHA-256;
2. save cohort IDs and partition manifest;
3. save immutable per-run model metadata;
4. add a new results ledger rather than overwriting v5 values;
5. state whether the run changes classification, localisation, calibration, or triage claims;
6. run a manuscript-wide consistency check before citing new numbers.

This document is a draft research context, not a submission-ready manuscript. Unknown clinical and ethical details remain intentionally unfilled rather than guessed.
