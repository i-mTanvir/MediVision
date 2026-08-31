# MedVision: 30-Reference Evidence Synthesis

**Prepared for:** *The Incoherence of Text-Debiasing in Medical Vision-Language Models: An Empirical Study of Label Circularity in MIMIC-CXR*  
**Source folder:** `E:\Defense\Discuss\Referances`  
**Scope:** The 30 PDFs in the folder were inventoried, their first pages were rendered for visual verification, and their searchable text, abstracts, methods, results, and conclusions were reviewed. The “relation to MedVision” notes below are intended to support citation selection, literature review, gap analysis, and cautious claim writing.

## How to use this file

- The numbering follows the filenames in the reference folder and is intended to match references 1-30 in the draft where possible.
- Some papers are direct medical-VLM studies; others are methodological foundations (shortcut learning, debiasing, statistics, encoders, and fusion).
- A citation should support the exact claim made. Do not cite a general architecture paper as evidence for a clinical safety claim.
- References 26-30 are statistical and reporting standards. They are summarized below because they directly support the paired inference, multiplicity control, and transparent reporting used in the MedVision audit.

---

## 1. Wang et al. (2026) — Revisiting Performance Claims for Chest X-Ray Models Using Clinical Context

- **File:** `01_Wang_2025_ChestXRay_ClinicalContext.pdf`
- **Authors:** Andrew Wang, Jiashuo Zhang, Michael Oberst
- **Date/venue:** 25 June 2026; Conference on Health, Inference, and Learning (CHIL), PMLR 333 (the PDF is an arXiv/CHIL version).
- **What the paper does:** Uses discharge summaries recorded before each chest radiograph to estimate a “pre-CXR” probability, then stratifies performance by the amount of clinical context available before the image. It also uses matching/reweighting to reduce the correlation between context and the current label.
- **Key findings:** Aggregate metrics conceal clinically important heterogeneity. Models perform worse in high pre-test-probability cases, and performance decreases when context-label correlations are controlled. High-risk cases are visually difficult, not simply statistically unusual.
- **Relevance to MedVision:** This is strong support for an evaluation that separates image evidence from contextual information. It motivates reporting results by clinical-risk strata and discussing why IID aggregate AUROC is insufficient. MedVision goes further in a different direction: it directly removes or replaces the image while keeping report text, targeting same-report label circularity rather than prior discharge-summary context.
- **Use in the paper:** Introduction/related work for context dependence; discussion for clinical heterogeneity; comparison paragraph explaining that clinical-context confounding and report-label circularity are related but distinct.
- **Gap left open:** No gray-square control, image contribution metric, labeler-specific audit, or TOST-style equivalence analysis of image versus text-only predictions.

## 2. Jin et al. (2024) — Hidden Flaws Behind Expert-Level Accuracy of Multimodal GPT-4 Vision in Medicine

- **File:** `02_Jin_2024_HiddenFlaws_MultimodalMedicalAI.pdf`
- **Authors:** Qiao Jin et al.
- **Date/venue:** 2024; *npj Digital Medicine*.
- **What the paper does:** Evaluates GPT-4 Vision on NEJM Image Challenges and compares it with physicians. It separately examines final-answer correctness and the quality of the model’s visual reasoning.
- **Key findings:** GPT-4V reached 81.6% accuracy versus 77.8% for physicians in the reported benchmark, but 35.5% of correct answers were accompanied by flawed rationales; image-comprehension errors accounted for a large share of failures.
- **Relevance to MedVision:** Establishes the “right answer for the wrong reason” problem in medical multimodal systems. It supports evaluating mechanism/grounding rather than treating accuracy as evidence of safe reasoning. MedVision operationalizes this idea with image ablation, image replacement, image-contribution metrics, and gate behavior on CXR classification.
- **Use in the paper:** Motivation and safety framing; do not use it as evidence that MIMIC-CXR models have the same error rate.
- **Gap left open:** It is a challenge-question study, not a controlled paired-image/report ablation study; it does not quantify label circularity or train-time text debiasing failure.

## 3. Lotfinia et al. (2026) — Vision-Language Models for Chest Radiography Do Not Always Need the Image

- **File:** `03_Lotfinia_2026_VLM_ChestRadiography.pdf`
- **Authors:** Mahshad Lotfinia, Sebastian Ziegelmayer, Lisa Adams, Daniel Truhn, Andreas Maier, Soroosh Tayebi Arasteh
- **Date/venue:** 2026; local preprint/manuscript.
- **What the paper does:** Performs a causal audit of chest-radiography VLMs using image-region occlusion, replacement with another patient’s image having the same label, and three behavioral metrics. It compares multimodal systems with text-only counterparts across nine systems.
- **Key findings:** Text-only models come within 5.7 accuracy points of the best multimodal systems; a 119B multimodal model is statistically indistinguishable from a 7B text-only model in one comparison. Models are categorized as ignoring, unstable, or selectively using image information. The pattern persists across dataset, resolution, and prompt changes.
- **Relevance to MedVision:** This is the closest prior work and must be acknowledged explicitly. It strongly supports causal image-grounding audits and prevents an unqualified “first” claim. MedVision’s contribution should be scoped around report-derived label circularity, gray-square training/inference controls, ICM/TOST equivalence, gate-stagnation analysis, five CADQ variants, and multi-seed statistical evaluation.
- **Use in the paper:** Related work, motivation, and direct comparison table.
- **Gap left open:** It does not test the specific train-time text-debiasing setup in the draft, nor the interaction between CheXpert-derived labels, text encoder exposure, and learned fusion gates.

## 4. Sadanandan & Behzadan (2026) — Consistent but Dangerous: Per-Sample Safety Classification Reveals False Reliability in Medical Vision-Language Models

- **File:** `04_Sadanandan_2026_ConsistentDangerous_MedVLM.pdf`
- **Authors:** Binesh Sadanandan, Vahid Behzadan
- **Date/venue:** 2026; local preprint/manuscript.
- **What the paper does:** Tests prediction consistency under text paraphrases and introduces a four-quadrant, per-sample safety taxonomy: Ideal (consistent and image-reliant), Fragile (inconsistent and image-reliant), Dangerous (consistent but not image-reliant), and Worst (inconsistent and not image-reliant).
- **Key findings:** High consistency can be produced by relying on text rather than the image. LoRA reduces flip rates but can shift samples toward the “Dangerous” quadrant. Accuracy and low entropy therefore do not guarantee safe grounding.
- **Relevance to MedVision:** Provides a useful conceptual vocabulary for explaining why consistency is not reliability. It supports reporting image reliance at the sample/model level, while MedVision uses gray-square ablations, ICM, confidence changes, and gate diagnostics instead of paraphrase-only testing.
- **Use in the paper:** Related work and discussion of false reliability; possible inspiration for a per-sample extension in future work.
- **Gap left open:** The paper does not isolate report-label circularity, labeler noise, or equivalence margins for image and text-only models.

## 5. Chiang (2026) — An Interpretable Chest X-ray Classification Framework Using Prototype Memory and Counterfactual Consistency

- **File:** `05_cureus-0018-00000103134.pdf`
- **Author:** Ling-Feng Chiang
- **Date/venue:** Published 6 February 2026; *Cureus* 18(2): e103134.
- **What the paper does:** Proposes CXR-NeXus for four-class CXR classification (COVID-19, pneumonia, tuberculosis, normal). The method combines class-specific prototype memory, Grad-CAM-guided lesion suppression, counterfactual consistency, and anatomical attention regularization.
- **Key findings:** The reported experiments improve macro-F1, AUROC, specificity, and calibration while reducing saliency on non-pulmonary regions. The central principle is that confidence should fall when clinically meaningful lesion evidence is removed.
- **Relevance to MedVision:** Supports counterfactual evidence-dependence as a clinically interpretable audit principle. MedVision applies the idea to a different failure mode: whether image information is used at all when paired reports already encode the target label.
- **Use in the paper:** Related work on causal/counterfactual interpretability; discussion of why saliency alone is not a causal proof.
- **Gap left open:** Small/four-class setting, weak supervision, and no multimodal report-ablation or text-only equivalence analysis; reported gains should not be transferred to MIMIC-CXR without independent validation.

## 6. Lakens (2017) — Equivalence Tests

- **File:** `06_lakens-2017-equivalence-tests.pdf`
- **Author:** Daniel Lakens
- **Date/venue:** 2017; *Social Psychological and Personality Science*.
- **What the paper does:** Gives a practical explanation of the two one-sided tests (TOST) procedure for testing whether an effect lies inside a pre-specified smallest effect size of interest (SESOI).
- **Key findings:** Failure to reject a null hypothesis is not evidence of equivalence. Equivalence requires both one-sided tests to reject, and the equivalence margin must be set before looking at the data and justified substantively.
- **Relevance to MedVision:** Directly supports the draft’s claim that a multimodal model is functionally equivalent to a text-only model only when the pre-defined margin is met. The ±0.01 margin must be described as an operational/statistical margin, not automatically as a clinical or regulatory threshold.
- **Use in the paper:** Methods/statistics and interpretation of ICM/TOST results.
- **Gap left open:** The paper is general statistical guidance; it does not determine an appropriate margin for CXR AUROC or accuracy. MedVision must report confidence intervals, sample size/power rationale, and the chosen SESOI transparently.

## 7. Myronenko et al. (2025) — Reasoning Visual Language Model for Chest X-Ray Analysis

- **File:** `07_Myronenko_2025_ReasoningVLM_ChestXRay.pdf`
- **Authors:** Andriy Myronenko, Dong Yang, Baris Turkbey, Mariam Aboian, Sena Azamat, Esra Akcicek, Hongxu Yin, Pavlo Molchanov, Marc Edgar, Yufan He, Pengfei Guo, Yucheng Tang, Daguang Xu
- **Date/venue:** 30 October 2025; arXiv:2510.23968v2.
- **What the paper does:** Presents NV-Reason-CXR-3B, trained with radiologist-style reasoning supervision followed by GRPO reinforcement learning with verifiable abnormality rewards. It releases code/model and reports an expert reader study.
- **Key findings:** The model generates stepwise reasoning, achieves competitive multi-label classification under OOD evaluation, and reportedly improves reader confidence, error auditing, and reporting time. Human reasoning data are collected through voice transcription/editing; approximately 100 expert-annotated cases were available at the described training stage, with roughly 100k MIMIC-CXR reports rewritten synthetically for SFT.
- **Relevance to MedVision:** Illustrates the current emphasis on reasoning traces and auditability, but also highlights a potential distinction between plausible textual reasoning and actual image grounding. MedVision can cite it to argue that reasoning output should be paired with causal image-use tests.
- **Use in the paper:** Current VLM context and discussion of explanation faithfulness.
- **Gap left open:** A generated chain of thought is not itself a causal grounding certificate; the paper is not a label-circularity or image-ablation study.

## 8. Geirhos et al. (2020) — Shortcut Learning in Deep Neural Networks

- **File:** `08_Geirhos_2020_ShortcutLearning.pdf`
- **Authors:** Robert Geirhos et al.
- **Date/venue:** 2020; *Nature Machine Intelligence*.
- **What the paper does:** Reviews how neural networks exploit predictive but unintended features (“shortcuts”) that work on benchmark distributions but fail under distribution shift or when the shortcut is removed.
- **Key findings:** High IID accuracy can coexist with reliance on non-causal or brittle cues. Robust performance requires evaluation environments and interventions that separate intended features from correlated artifacts.
- **Relevance to MedVision:** This is the theoretical foundation for describing report text as a shortcut, the image as the intended evidence source, and gray-square/image-swap tests as interventions. It also supports a careful distinction between correlation, causal evidence, and robustness.
- **Use in the paper:** Introduction, conceptual framework, and discussion.
- **Gap left open:** It is a broad review rather than a medical-VLM experiment; specific claims about MIMIC-CXR must come from the medical papers and MedVision results.

## 9. Irvin et al. (2019) — CheXpert: A Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison

- **File:** `09_Irvin_2019_CheXpert.pdf`
- **Authors:** Jeremy Irvin et al.
- **Date/venue:** 2019; AAAI Conference on Artificial Intelligence.
- **What the paper does:** Introduces the CheXpert dataset and a rule-based report labeler for 14 observations, including explicit uncertainty labels and radiologist validation.
- **Key findings:** Report-derived labels scale chest-X-ray supervision but contain uncertainty and labeler-dependent noise. The paper compares labeler-generated targets with expert annotations and establishes a strong DenseNet baseline.
- **Relevance to MedVision:** Supports the provenance and limitations of CheXpert-style labels used in the draft. It is important for explaining why labels extracted from the same report supplied to a text encoder can create circular supervision.
- **Use in the paper:** Dataset/label construction, label noise, and baseline description.
- **Gap left open:** CheXpert is a Stanford dataset and is not identical to MIMIC-CXR. Do not write as if the CheXpert dataset itself supplied the MIMIC images; distinguish the labeler from the dataset.

## 10. Johnson et al. (2019) — MIMIC-CXR, a De-identified Publicly Available Database of Chest Radiographs with Free-Text Reports

- **File:** `10_s41597-019-0322-0.pdf`
- **Authors:** Alistair E. W. Johnson et al.
- **Date/venue:** 2019; *Scientific Data*.
- **What the paper does:** Describes the MIMIC-CXR release, including 377,110 images, free-text radiology reports, study/patient structure, de-identification, and PhysioNet access requirements.
- **Key findings:** MIMIC-CXR enables paired image-report research at scale but retains real-world heterogeneity, repeated studies, report structure, and clinically generated text that can encode the target findings.
- **Relevance to MedVision:** Primary source for dataset provenance, patient/study grouping, and the rationale for patient-level splitting. It also supports the central observation that the image and report are naturally paired—and therefore that report-derived labels may be information leakage when the report is an input modality.
- **Use in the paper:** Data section and motivation for studying paired-data circularity.
- **Gap left open:** The database paper does not evaluate multimodal leakage, text-only performance, or image contribution; those are empirical questions for MedVision.

## 11. Clark et al. (2019) — Don’t Take the Easy Way Out: Ensemble Based Methods for Avoiding Known Dataset Biases

- **File:** `11_Clark_2019_EasyWayOut_EMNLP.pdf`
- **Authors:** Christopher Clark, Mark Yatskar, Luke Zettlemoyer
- **Date/venue:** 2019; EMNLP/arXiv version.
- **What the paper does:** First trains a bias-only model that captures a known superficial pattern, then trains a robust model in an ensemble/product-of-experts configuration so that the robust model must learn information not already explained by the bias model.
- **Key findings:** Across five datasets, including VQA and language tasks, ensemble debiasing improves out-of-domain performance; the best method can dynamically decide when to trust the bias-only component.
- **Relevance to MedVision:** Provides the methodological precedent for LMH/PoE-style text-debiasing used in the draft. It also suggests a critical audit question: debiasing objectives can change training behavior without guaranteeing that the image branch becomes causally necessary.
- **Use in the paper:** Related work and CADQ/LMH motivation.
- **Gap left open:** The experiments are not medical and do not test report-derived label circularity, image ablation, or static-versus-dynamic gate behavior.

## 12. Cadene et al. (2019) — RUBi: Reducing Unimodal Biases for Visual Question Answering

- **File:** `12_Cadene_2019_Rubi_NeurIPS.pdf`
- **Authors:** Remi Cadene et al.
- **Date/venue:** 2019; NeurIPS workshop/VQA-CP line of work.
- **What the paper does:** Adds a question-only branch to identify language priors and uses it to gate or modulate the multimodal prediction, reducing reliance on unimodal question-answer correlations.
- **Key findings:** RUBi improves robustness on VQA settings with changing answer priors and demonstrates that a modality can be useful as a bias detector even when it should not determine the final answer alone.
- **Relevance to MedVision:** A direct conceptual predecessor for treating the report/text branch as a bias model. It supports the motivation for testing whether LMH/PoE-style debiasing actually makes the image branch more useful.
- **Use in the paper:** Related work; explain the adaptation from question bias to clinical report bias.
- **Gap left open:** VQA questions are not radiology reports; RUBi does not address labels extracted from the same report, clinical label noise, or causal image-use measurement.

## 13. Zhang et al. (2022) — Contrastive Learning of Medical Visual Representations from Paired Images and Text

- **File:** `13_Zhang_2022_ContrastiveLearning_Medical.pdf`
- **Authors:** Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P. Langlotz
- **Date/venue:** 2022; *Proceedings of Machine Learning Research* 182, Machine Learning for Healthcare (ConVIRT).
- **What the paper does:** Pretrains an image encoder with a bidirectional image-text contrastive objective on naturally paired medical images and reports, then transfers it to four classification and two retrieval tasks.
- **Key findings:** ConVIRT achieves better or comparable performance than ImageNet initialization using about 10% of the labeled data in the reported classification comparisons. The paper also notes that rule-based report labels are inaccurate and domain-sensitive.
- **Relevance to MedVision:** Establishes why paired image-text pretraining is attractive and why it can also transmit report-derived shortcuts. It is a key baseline/architecture citation, not evidence that contrastive pretraining guarantees causal visual reasoning.
- **Use in the paper:** Related work on medical VLP and discussion of weak supervision.
- **Gap left open:** It optimizes representation transfer and does not audit whether downstream predictions remain dependent on images when reports already contain the label.

## 14. Huang et al. (2021) — GLoRIA: A Multimodal Global-Local Representation Learning Framework for Label-Efficient Medical Image Recognition

- **File:** `14_Huang_GLoRIA_A_Multimodal_Global-Local_Representation_Learning_Framework_for_Label-Efficient_Medical_ICCV_2021_paper.pdf`
- **Authors:** Shih-Cheng Huang, Shunxing Shen et al.
- **Date/venue:** 2021; ICCV.
- **What the paper does:** Learns global image-text alignment and local word-region alignment for medical images, aiming to improve label-efficient recognition and localization.
- **Key findings:** Multimodal global/local alignment improves transfer and localization performance on medical imaging benchmarks relative to the reported baselines.
- **Relevance to MedVision:** Represents the class of sophisticated multimodal systems whose high performance should not automatically be interpreted as evidence of image grounding. It is useful for positioning MedVision as an audit of multimodal behavior rather than another representation-learning proposal.
- **Use in the paper:** Related work and architectural background.
- **Gap left open:** The paper does not perform gray-square controls, report-preserving image swaps, text-only equivalence, or gate-stagnation analysis.

## 15. Boecking et al. (2022) — Making the Most of Text Semantics to Improve Biomedical Vision–Language Processing

- **File:** `15_Boecking_2022_TextSemantics_Biomedical.pdf`
- **Authors:** Benedikt Boecking, Naoto Usuyama, Shruthi Bannur, Daniel C. Castro, Anton Schwaighofer, Stephanie Hyland, Maria Wetscherek, Tristan Naumann, Aditya Nori, Javier Alvarez-Valle, Hoifung Poon, Ozan Oktay
- **Date/venue:** 2022; biomedical VLP work (arXiv:2204.09817; published version associated with EACL-era biomedical NLP/VLP work).
- **What the paper does:** Improves biomedical VLP by modeling radiology-text semantics, negation, uncertainty, discourse, and domain vocabulary; it also releases a language model and locally aligned phrase-grounding data.
- **Key findings:** Better domain-specific text modeling improves contrastive learning and downstream recognition/segmentation benchmarks. The paper explicitly notes that random negatives and imbalance can cause models to memorize irrelevant text/image aspects.
- **Relevance to MedVision:** Supports the importance of clinical-language pretraining and, simultaneously, the risk that a highly capable text encoder can dominate the fused predictor. It is especially useful when discussing ClinicalBERT-style text branches and semantic label leakage.
- **Use in the paper:** Related work, text encoder rationale, and discussion of text-dominant fusion.
- **Gap left open:** Performance gains do not establish that the model uses the image causally; no report-preserving image ablation or label-circularity audit is performed.

## 16. Sabottke et al. (2024) — Text Report Analysis to Identify Opportunities for Optimizing Target Selection for Chest Radiograph Artificial Intelligence Models

- **File:** `16_10278_2023_Article_927.pdf`
- **Authors:** Carl Sabottke, Jason Lee, Alan Chiang, Bradley Spieler, Raza Mushtaq
- **Date/venue:** Published online 12 January 2024; *Journal of Imaging Informatics in Medicine* 37:402–411 (received/revised/accepted in 2023).
- **What the paper does:** Analyzes 210,025 MIMIC-CXR reports and 168,949 local reports. NLP extracts 59 imaging-finding categories; linear and LASSO regression estimate which findings drive report length and complexity.
- **Key findings:** Imaging-finding keywords explain substantially more report-length variance than perception terms alone. In MIMIC-CXR, masses, nodules, cavitary and cystic lesions receive high coefficients; device findings are important in local data.
- **Relevance to MedVision:** Demonstrates that report text contains structured, clinically meaningful information about CXR findings and can be used to select targets. This supports the plausibility of a strong text-only baseline and the need to distinguish efficiency-oriented report mining from causal multimodal diagnosis.
- **Use in the paper:** MIMIC-CXR/report-text context, target selection, and label circularity motivation.
- **Gap left open:** It studies report complexity, not predictive leakage or image contribution; it does not compare text-only and image-text classifiers.

## 17. Agrawal et al. (2018) — Don’t Just Assume; Look and Answer: Overcoming Priors for Visual Question Answering

- **File:** `17_Agrawal_2018_DontAssume_CVPR.pdf`
- **Authors:** Aishwarya Agrawal, Dhruv Batra, Devi Parikh, Aniruddha Kembhavi
- **Date/venue:** 2018; CVPR.
- **What the paper does:** Introduces VQA-CP splits whose answer priors differ between train and test, then proposes GVQA to separate visual concept recognition from answer-space prediction.
- **Key findings:** Existing VQA models degrade sharply when answer priors change, showing that IID test performance can reward language shortcuts. GVQA improves robustness by explicitly grounding visual concepts and offers more interpretable intermediate outputs.
- **Relevance to MedVision:** Provides the clearest conceptual precedent for changing-prior evaluation and “look versus assume.” In MedVision, the report is a stronger source of the prior because it may contain the label itself; gray-square and image-swap tests are the medical analogue of breaking answer priors.
- **Use in the paper:** Introduction, shortcut-learning related work, and justification for modality-specific controls.
- **Gap left open:** VQA prior shifts are synthetic/rebalanced and not the same as clinical label circularity; the paper does not address radiology reports or weak labels.

## 18. Cohen et al. (2022) — TorchXRayVision: A Library of Chest X-ray Datasets and Models

- **File:** `18_cohen22a.pdf`
- **Authors:** Joseph Paul Cohen, Joseph D. Viviano, Paul Bertin, Paul Morrison, Parsa Torabian, Matteo Guarrera, Matthew P. Lungren, Akshay Chaudhari, Rupert Brooks, Mohammad Hashir, Hadrien Bertrand et al.
- **Date/venue:** 2022; MIDL, PMLR 172.
- **What the paper does:** Releases a common interface for many CXR datasets, preprocessing pipelines, pretrained models, feature extraction, and cross-dataset robustness experiments.
- **Key findings:** Standardized loading/preprocessing and interchangeable pretrained models make reproducible comparison and distribution-shift testing easier. The library explicitly supports studying model failures, saliency limitations, and covariate shifts.
- **Relevance to MedVision:** Supports implementation provenance for a DenseNet/CXR backbone and reproducible preprocessing. It also warns that pretrained weights and dataset combinations can introduce hidden overlap or shortcut structure.
- **Use in the paper:** Implementation details, reproducibility, and limitations around pretrained models.
- **Gap left open:** It is infrastructure, not a causal grounding evaluation. MedVision must document exact weights, pretraining datasets, and whether any report-derived supervision overlaps with the evaluated cohort.

## 19. Gichoya et al. (2023) — “Shortcuts” Causing Bias in Radiology Artificial Intelligence: Causes, Evaluation, and Mitigation

- **File:** `19_nihms-1999605.pdf`
- **Authors:** Judy W. Gichoya et al.
- **Date/venue:** 2023; *Journal of the American College of Radiology* review (the local NIH manuscript copy may display a later repository date).
- **What the paper does:** Reviews shortcut sources in radiology AI, including acquisition/device artifacts, demographic/protected-attribute leakage, prevalence shifts, annotation practices, and deployment context. It organizes evaluation and mitigation strategies.
- **Key findings:** Shortcuts can arise at data, model, and inference stages; they may produce high benchmark scores and still fail clinically or unfairly across subgroups. Robust evaluation needs targeted stress tests and external/stratified analysis.
- **Relevance to MedVision:** Broadly supports the safety and fairness rationale for auditing non-causal cues. The paper helps frame report-text dominance as one shortcut class among many and supports adding subgroup/setting limitations to the discussion.
- **Use in the paper:** Introduction, limitations, and clinical translation discussion.
- **Gap left open:** It is a review rather than a controlled paired-report experiment; it does not quantify label circularity in MIMIC-CXR VLMs.

## 20. Santomartino et al. (2024) — Evaluating the Performance and Bias of Natural Language Processing Tools in Labeling Chest Radiograph Reports

- **File:** `20_radiol.232746.pdf`
- **Authors:** Samantha M. Santomartino, John R. Zech, Kent Hall, Jean Jeudy, Vishwa Parekh, Paul H. Yi
- **Date/venue:** 2024; *Radiology*.
- **What the paper does:** Compares four report-labeling systems (CheXpert rule-based, RadReportAnnotator, GPT-4, and a cTAKES hybrid) against radiologist annotations on balanced MIMIC-CXR and IU datasets, including subgroup analyses.
- **Key findings:** Aggregate labeling performance can hide demographic differences; performance is poorer in some older-patient groups, and labeler errors can propagate into downstream AI training/evaluation.
- **Relevance to MedVision:** Directly supports auditing the label-generation mechanism before interpreting multimodal performance. If the same report produces both the target and the text input, labeler errors and circularity can be amplified rather than averaged away.
- **Use in the paper:** Label provenance, bias, limitations, and the need for expert-adjudicated validation.
- **Gap left open:** It evaluates report labelers, not image-text model causality; it does not test gray-square or report-preserving image swaps.

## 21. Alsentzer et al. (2019) — Publicly Available Clinical BERT Embeddings

- **File:** `21_Alsentzer_2019_ClinicalBERT.pdf`
- **Authors:** Emily Alsentzer et al.
- **Date/venue:** 2019; clinical NLP workshop/arXiv release.
- **What the paper does:** Releases BERT and BioBERT models further pre-trained on MIMIC clinical notes and evaluates them on clinical NLP tasks.
- **Key findings:** Domain-adapted models improve clinical language representation relative to general-domain baselines on several tasks, although gains depend on task and pretraining/data mismatch.
- **Relevance to MedVision:** Justifies the use of Bio_ClinicalBERT-like text encoding and makes pretraining provenance explicit. Because the encoder learned from MIMIC notes, the paper also motivates a careful overlap/leakage statement when MIMIC-derived reports are used in evaluation.
- **Use in the paper:** Methods/text encoder and data-governance limitations.
- **Gap left open:** ClinicalBERT is not a grounding method; better clinical text understanding can increase, rather than reduce, report shortcut strength.

## 22. Lin et al. (2017) — Focal Loss for Dense Object Detection

- **File:** `22_Lin_2017_FocalLoss_ICCV.pdf`
- **Authors:** Tsung-Yi Lin et al.
- **Date/venue:** 2017; ICCV.
- **What the paper does:** Introduces focal loss, which downweights well-classified/easy examples so training focuses on hard examples and rare positives.
- **Key findings:** Focal loss addresses extreme foreground/background imbalance in dense detection and improves one-stage detector performance by preventing easy negatives from dominating the gradient.
- **Relevance to MedVision:** Can justify focal-loss use for imbalanced CXR labels (for example rare pneumothorax) if the implementation actually uses it. The citation should be limited to optimization/class-imbalance rationale.
- **Use in the paper:** Methods, loss function, and ablation explanation.
- **Gap left open:** The original task is object detection, not multimodal CXR classification. Focal loss does not solve report leakage, calibration, or grounding.

## 23. Huang et al. (2017) — Densely Connected Convolutional Networks

- **File:** `23_Huang_2017_DenseNet_CVPR.pdf`
- **Authors:** Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger
- **Date/venue:** 2017; CVPR.
- **What the paper does:** Introduces DenseNet, connecting each layer to every later layer in a feed-forward block to improve feature reuse and gradient flow.
- **Key findings:** Dense connectivity yields competitive ImageNet/CIFAR results with fewer parameters in the reported settings and became a common medical-image backbone.
- **Relevance to MedVision:** This is the architectural citation for DenseNet-121/image encoding, not evidence for a clinical or multimodal claim.
- **Use in the paper:** Methods/backbone description.
- **Gap left open:** Image-backbone quality does not establish that the fused model uses image evidence when report text is predictive.

## 24. Devlin et al. (2019) — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- **File:** `24_Devlin_2019_BERT_NAACL.pdf`
- **Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **Date/venue:** 2019; NAACL.
- **What the paper does:** Introduces bidirectional Transformer pretraining with masked-language modeling and next-sentence prediction, followed by task-specific fine-tuning.
- **Key findings:** BERT substantially improves a wide range of language-understanding benchmarks and establishes the pretrain-then-finetune paradigm used by domain-adapted clinical encoders.
- **Relevance to MedVision:** Provides the foundational citation for the report encoder and helps explain why a strong language branch may recover labels from radiology prose.
- **Use in the paper:** Methods/text encoder and background.
- **Gap left open:** General-domain BERT does not establish clinical validity or image grounding; ClinicalBERT/biomedical-specific sources should be cited for domain adaptation.

## 25. Arevalo et al. (2017) — Gated Multimodal Units for Information Fusion

- **File:** `25_Arevalo_2017_GatedMultimodalUnits.pdf`
- **Authors:** John Arevalo, Thamar Solorio, Manuel Montes-y-Gómez, Fabio A. González
- **Date/venue:** 2017; ICLR workshop track/arXiv:1702.01992.
- **What the paper does:** Introduces the Gated Multimodal Unit (GMU), where multiplicative gates learn how much each modality contributes to an intermediate representation. It evaluates plot-plus-poster movie-genre classification on MM-IMDb.
- **Key findings:** Learned gates improve macro-F1 over unimodal and several fixed-fusion baselines; the gate is intended to be input-dependent rather than manually tuned.
- **Relevance to MedVision:** Supplies the conceptual precedent for a learned image/text gate and for asking whether gate values reflect meaningful modality use. MedVision’s CADQ gate analysis is a medical, label-circularity-focused audit rather than a direct replication of GMU.
- **Use in the paper:** Architecture motivation, gate interpretation, and comparison with static/dynamic fusion.
- **Gap left open:** Gate values are not automatically causal attribution; a gate can look balanced while both branches encode the same report-derived shortcut. The gray-square, image-swap, and performance-equivalence tests are therefore necessary.

---

## 26. DeLong et al. (1988) — Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonparametric Approach

- **File:** `26_2531595.pdf`
- **Authors:** Elizabeth R. DeLong, David M. DeLong, Daniel L. Clarke-Pearson
- **Date/venue:** 1988; *Biometrics* 44(3):837-845.
- **What the paper does:** Develops a nonparametric method for comparing two or more empirical ROC curves when the tests are applied to the same individuals. The method treats AUC as a Mann-Whitney-type U-statistic and estimates the covariance between correlated AUCs using generalized U-statistics and structural components.
- **Key findings:** AUC differences cannot be tested as if the curves came from independent samples when each model is evaluated on the same cases. The covariance term is essential for a valid standard error and significance test; the method avoids requiring a binormal distributional assumption.
- **Relevance to MedVision:** This is the primary statistical justification for paired/per-seed DeLong comparisons of multimodal, text-only, image-only, and ablated predictions on the same test subjects. Predictions from separate random seeds must first be reduced to independent seed-level comparisons; concatenating repeated predictions across seeds would violate the independent-observation structure assumed by the test.
- **Use in the paper:** Methods/statistical analysis and results tables reporting paired AUC comparisons with confidence intervals and adjusted P values.
- **Gap left open:** DeLong addresses correlation between tests on the same subjects, not clustering caused by repeated training seeds. MedVision should therefore report the per-seed analysis unit and avoid pooled subject-level inference across seeds.

## 27. McNemar (1947) — Note on the Sampling Error of the Difference between Correlated Proportions or Percentages

- **File:** `27_bf02295996.pdf`
- **Author:** Quinn McNemar
- **Date/venue:** 1947; *Psychometrika* 12(2):153-157.
- **What the paper does:** Derives the sampling error and chi-square-equivalent test for comparing two proportions measured on paired or matched individuals. The key calculation is based on the discordant cells of the 2 x 2 table; concordant pairs do not contribute evidence for a difference.
- **Key findings:** Independent-sample proportion tests are inappropriate when the same individuals receive both classifications. The variance must include the correlation between paired responses, and the difference is driven by cases classified differently by the two methods.
- **Relevance to MedVision:** Supports paired McNemar testing of binary predictions from two model conditions on the identical held-out subjects. It is appropriate for asking whether gray-square, text-only, image-only, or debiased predictions change the error pattern relative to the reference condition.
- **Use in the paper:** Methods and paired classification results; report the discordant-pair counts, test version (asymptotic or exact), and the comparison family used for multiplicity correction.
- **Gap left open:** The original derivation is asymptotic and does not by itself solve repeated-seed dependence, sparse discordant cells, or multi-class extensions. These issues require explicit implementation choices and sensitivity checks in MedVision.

## 28. Benjamini and Hochberg (1995) — Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing

- **File:** `28_j.2517-6161.1995.tb02031.x.pdf`
- **Authors:** Yoav Benjamini, Yosef Hochberg
- **Date/venue:** 1995; *Journal of the Royal Statistical Society: Series B (Methodological)* 57(1):289-300.
- **What the paper does:** Introduces the step-up Benjamini-Hochberg procedure for controlling the expected proportion of false rejections among all rejected hypotheses, the false discovery rate (FDR). The paper contrasts FDR with the more conservative familywise error rate (FWER) and proves control under independent test statistics, with simulation evidence for power gains.
- **Key findings:** When many related hypotheses are tested, unadjusted P values inflate false-positive claims. FDR control can retain more power than FWER control while limiting the expected false-discovery proportion, particularly when some hypotheses are genuinely non-null.
- **Relevance to MedVision:** Provides the basis for adjusting the multiple paired comparisons across model variants, endpoints, or audit metrics. The paper supports reporting raw and BH-adjusted P values together, but only after defining the hypothesis family in advance (for example, the primary image-contribution family versus exploratory robustness analyses).
- **Use in the paper:** Statistical analysis, tables of corrected significance results, and the discussion of exploratory versus confirmatory findings.
- **Gap left open:** The original guarantee is stated for independent test statistics (and later work extends it to positive dependence). BH does not correct a flawed sampling unit, pooled repeated seeds, selective reporting, or a post-hoc family definition. Those design decisions remain MedVision responsibilities.

## 29. Tejani et al. (2024) — Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update

- **File:** `29_checklist-for-artificial-intelligence-in-medical-imaging-(claim)-2024-update.pdf`
- **Authors:** Ali S. Tejani, Michail E. Klontzas, Anthony A. Gatti, John T. Mongan, Linda Moy, Seong Ho Park, Charles E. Kahn Jr, for the CLAIM 2024 Update Panel
- **Date/venue:** 2024; *Radiology: Artificial Intelligence* 6(4):e240300. DOI: 10.1148/ryai.240300.
- **What the paper does:** Updates the CLAIM reporting guideline through a formal Delphi process involving physicians, AI scientists, editors, and statisticians. The 2024 version is an educational transparency checklist, not a scoring or risk-of-bias instrument.
- **Key findings:** The update contains 44 items with Yes, No, and Not Applicable options. It adds or clarifies image acquisition, reference-standard provenance, data partitioning, software versions, initialization, training and final-model selection, statistical uncertainty, robustness, explainability, internal/external testing, failure analysis, protocol/technical details, software-data availability, and funding. It recommends “reference standard” instead of ambiguous “ground truth,” and “internal testing”/“external testing” instead of using “validation” loosely.
- **Relevance to MedVision:** CLAIM provides the reporting checklist for making the audit reproducible and reviewer-verifiable. It maps directly to the draft’s MIMIC-CXR cohort flow, patient-level split, CheXpert-derived reference standard, five CADQ variants, learned-gate extraction, multi-seed inference, uncertainty and multiplicity reporting, failure analysis, code/data availability statement, funding, and limitations. It also supports describing this work as a retrospective empirical audit rather than implying prospective clinical validation.
- **Use in the paper:** Methods reporting, Results completeness, Discussion limitations, supplementary checklist, and the final declarations (data/code, funding, conflicts, and author roles).
- **Gap left open:** CLAIM improves reporting but cannot establish that the reference standard is clinically correct, remove report-label circularity, or prove causal image use. The MedVision audit still needs its intervention logic and statistical assumptions to be justified independently.
- **Metadata note for the draft:** The local PDF is the 2024 Update by Tejani et al. and should not be cited as “Mongan et al. (2024), e230120.” Mongan, Moy, and Kahn’s original “A Guide for Authors and Reviewers” is a separate 2020 publication.

## 30. Collins et al. (2024) — TRIPOD+AI Statement: Updated Guidance for Reporting Clinical Prediction Models That Use Regression or Machine Learning Methods

- **File:** `30_bmj-2023-078378.full.pdf`
- **Authors:** Gary S. Collins, Karel G. M. Moons, Paula Dhiman, Richard D. Riley, Andrew L. Beam, Ben Van Calster, Marzyeh Ghassemi, Xiaoxuan Liu, Johannes B. Reitsma, Maarten van Smeden, Anne-Laure Boulesteix, and collaborators (TRIPOD+AI group)
- **Date/venue:** 2024; *The BMJ* 385:e078378. DOI: 10.1136/bmj-2023-078378.
- **What the paper does:** Replaces the 2015 TRIPOD checklist with harmonized reporting guidance for studies that develop or evaluate clinical prediction models using regression or machine learning. The authors use a structured consensus process and distinguish development, evaluation, and open-science reporting needs.
- **Key findings:** TRIPOD+AI provides 27 main checklist items, expanded explanations totaling 52 subitems, and a 13-item checklist for abstracts. It covers study objectives, data sources and eligibility, predictors/outcomes, sample size, missing data, model specification, analytical methods, performance and calibration, evaluation data, limitations, funding, conflicts, protocol registration, data sharing, and code sharing.
- **Relevance to MedVision:** The evaluation-oriented items help structure the manuscript’s dataset description, partitioning, prediction-generation procedure, performance uncertainty, failure analysis, and reproducibility declarations. The open-science items directly support the planned repository placeholder and explicit self-funding/conflict statements. Because MedVision is primarily a retrospective audit of existing models and modality dependence, development-only items should be marked Not Applicable or explained rather than implying that the study is a new clinical deployment model.
- **Use in the paper:** Reporting checklist, Methods/Results organization, abstract completeness, and declarations about protocol, code, data access, funding, and conflicts.
- **Gap left open:** TRIPOD+AI is a reporting guideline, not a substitute for CLAIM, a risk-of-bias tool, or an external clinical validation study. It does not prescribe the correct causal intervention for label circularity and does not make non-significant performance differences clinically equivalent.
- **Metadata note for the draft:** The correct checklist count is 27 main items and 52 subitems (with a separate 13-item abstract checklist), not 41 items.

---

## Cross-paper synthesis for the MedVision literature review

### Theme A — Why aggregate performance is not enough

Wang, Jin, Geirhos, Gichoya, Sadanandan, and Lotfinia converge on one point: a high IID score can coexist with clinically unsafe or non-causal behavior. The most defensible wording for the draft is that MedVision evaluates *evidence dependence* and *modality contribution*, not merely predictive accuracy.

### Theme B — Reports are both valuable supervision and a leakage channel

Johnson establishes the paired image-report structure of MIMIC-CXR. Irvin and Santomartino show that report-derived labels are useful but uncertain and biased. Zhang, Huang, and Boecking show why paired text improves representation learning. Sabottke demonstrates how much structured finding information is present in reports. Together, these papers make the circularity hypothesis plausible: when a label is extracted from a report that is also supplied to the model, the text branch can solve the task without image evidence.

### Theme C — Prior debiasing does not prove visual grounding

Agrawal, Cadene, and Clark motivate changing-prior tests, bias-only models, and product-of-experts/ensemble debiasing. Lotfinia and Sadanandan show why those interventions must be followed by image-ablation or per-sample safety tests. The specific gap for MedVision is the interaction of train-time text debiasing with report-derived label circularity and learned gates.

### Theme D — What the foundational citations do (and do not) establish

DenseNet, BERT, ClinicalBERT, focal loss, GMU, GLoRIA, ConVIRT, and TorchXRayVision justify the selected backbone, text encoder, loss, fusion family, and reproducible implementation. None of them, alone, proves causal image use. Lakens supplies the statistical logic for equivalence claims.

### Theme E — Paired inference and transparent reporting

DeLong and McNemar provide the appropriate paired tests when competing model conditions are evaluated on the same held-out subjects. Benjamini-Hochberg controls the expected false-discovery proportion across a pre-defined family of related hypotheses. These methods are complementary: neither can repair an invalid sampling unit or post-hoc selection of tests. CLAIM 2024 and TRIPOD+AI then supply reporting structures for the cohort flow, reference standard, partitions, model details, uncertainty, failure analysis, code/data availability, funding, and conflicts. Together, these references strengthen the audit's reproducibility without turning a reporting checklist into evidence of clinical validity.

## Suggested citation map for the draft

| Draft section | Best-supported references | Claim to make |
|---|---|---|
| Introduction/problem | 1, 2, 3, 4, 8, 19 | Accuracy/consistency can conceal non-causal or unsafe behavior. |
| MIMIC-CXR and labels | 9, 10, 16, 20 | Paired reports and automated labels are scalable but noisy, structured, and potentially circular. |
| Shortcut/unimodal bias | 8, 11, 12, 17 | Dataset priors and unimodal branches can solve multimodal tasks without the intended evidence. |
| Medical VLP background | 13, 14, 15, 18 | Image-text pretraining and multimodal fusion are effective, but effectiveness is not grounding. |
| Model implementation | 21, 22, 23, 24, 25 | Clinical text encoder, focal loss, DenseNet, BERT, and gated fusion have established methodological precedent. |
| Statistical analysis | 6, 26, 27, 28 | TOST requires a pre-specified SESOI and two one-sided rejections; DeLong and McNemar handle paired AUC and classification comparisons; BH controls FDR across a defined test family. |
| Reporting and reproducibility | 29, 30 | CLAIM 2024 and TRIPOD+AI guide transparent reporting of data, models, uncertainty, limitations, open science, funding, and conflicts. |
| Discussion/limitations | 1, 2, 3, 4, 19, 20 | Clinical context, explanation quality, shortcut bias, consistency, and labeler bias limit interpretation. |

## Claims to avoid or qualify

1. Avoid saying MedVision is the first study to show that medical VLMs ignore images; Lotfinia (2026) is a close prior. Use a scoped claim such as “we provide a controlled audit of report-label circularity under train-time text debiasing.”
2. Do not equate “text-only accuracy is close to multimodal accuracy” with clinical equivalence unless the pre-specified TOST margin and confidence interval support it.
3. Do not interpret a learned gate value as causal modality attribution without the gray-square and image-swap interventions.
4. Do not describe CheXpert as the MIMIC-CXR dataset. Cite Irvin for the CheXpert labeler/uncertainty framework and Johnson for MIMIC-CXR provenance.
5. Do not claim that a plausible reasoning trace is faithful visual reasoning; Myronenko and Jin motivate the distinction, while MedVision’s ablations provide the relevant test.

## High-priority gap statement for MedVision

Existing work separately documents clinical-context heterogeneity, report-label noise, multimodal representation learning, unimodal shortcut bias, and causal/behavioral audits. DeLong, McNemar, and Benjamini-Hochberg clarify how paired and multiple comparisons should be analyzed, while CLAIM 2024 and TRIPOD+AI clarify what must be reported for reproducibility. The unresolved intersection is whether a medical VLM trained with report-derived labels can remain image-dependent after text-debiasing objectives are introduced. MedVision addresses this intersection by combining report-preserving image controls (gray square and image swap), text-only and image-only comparisons, image-contribution metrics, a pre-specified equivalence margin, gate-behavior analysis, and multi-seed evaluation on MIMIC-CXR.

## Bibliographic and checklist corrections to apply in the manuscript

- Reference 29 should cite Tejani et al. (2024), *Radiology: Artificial Intelligence* 6(4):e240300, DOI 10.1148/ryai.240300. The original Mongan, Moy, and Kahn CLAIM guide is a separate 2020 paper (e200029).
- CLAIM 2024 contains 44 main items. TRIPOD+AI contains 27 main items, 52 expanded subitems, and a separate 13-item abstract checklist. Any draft text that says “27-item CLAIM” or “41-item TRIPOD+AI” should be corrected.
- For the MedVision study, use the reporting guidance selectively: mark development-only or clinical-trial items as Not Applicable when justified, and retain the audit-specific causal and paired-inference procedures as the substantive evidence for label circularity.
