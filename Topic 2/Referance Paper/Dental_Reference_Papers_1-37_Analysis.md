# Dental Reference Papers 1–37: Structured Analysis and Selection

> **Project:** *Deep Learning-Driven Radiographic Analysis for Impacted Tooth Detection and Localization*
> **Source folder:** `E:\Defense\Discuss\Topic 2\Referance Paper`
> **Review date:** 4 September 2026
> **Purpose:** A serial-preserving evidence map for the Introduction, Related Work, Methods, Discussion, and gap analysis.

### Review protocol and scope

All 37 numbered PDFs were text-extracted in full. For every unique study, the title page, abstract, dataset/reference-standard description, model and training method, quantitative results, discussion, and limitations were examined. Exact duplicates were checked with SHA-256 hashes; alternate versions were matched by title, authors, DOI, dataset, and results. Figure/table captions and reported metrics were included where they affected interpretation. This is a structured scientific-content review for manuscript writing, not a formal systematic-review risk-of-bias assessment, and it does not reproduce every item in each paper's bibliography.

## Inventory verdict

The folder contains 37 numbered PDFs plus `Paper Reference. (1 - 25).pdf`. The latter is not a research paper: it is an incomplete reference list containing placeholders such as “A. Author,” “Journal Name,” and “Year.” It must not be cited or copied into a bibliography without replacing every placeholder from the actual papers.

### Recommended final library

- **Keep:** 25 unique sources.
- **Remove or archive:** 12 files: one unrelated case report, one conference-abstract-only item, and ten duplicate/alternate copies.
- **Core direct evidence:** impacted-tooth classification, detection, segmentation, localisation, impaction classification, or surgical-difficulty prediction on panoramic/CBCT images.
- **Supporting evidence:** broader tooth segmentation, clinical CBCT context, an adjacent YOLO workflow, and CLAIM reporting guidance.

### Files recommended for removal or archival

| Serial | Reason |
|---:|---|
| 6 | Clinical aneurysmal bone cyst case report; no AI method or model evaluation |
| 9 | Alternate copy of paper 4 |
| 11 | Exact duplicate of paper 1 |
| 19 | Alternate copy of paper 15 |
| 23 | Conference abstract only; insufficient methodological detail for a primary citation |
| 26 | Pre-publication/alternate copy of paper 20 |
| 28 | Exact duplicate of paper 24 |
| 29 | Alternate copy of paper 10 |
| 30 | Alternate copy of paper 25 |
| 31 | Exact duplicate of paper 2 |
| 33 | Alternate copy of paper 10 |
| 34 | Alternate copy of paper 15 |

After removing these 12 files, the folder retains exactly **25 useful unique sources**.

## How to use the evidence

- Compare classification papers using accuracy, sensitivity, specificity, F1, AUROC, calibration, and confidence intervals.
- Compare object detectors using precision, recall, AP/mAP, IoU threshold, false positives per image, and inference time.
- Compare segmentation studies using Dice and IoU.
- Do not place classification accuracy, detection mAP, and segmentation IoU in one “best model” ranking.
- A saliency map or attention score is not equivalent to expert-annotated localisation.
- Prefer patient-level partitions and independently annotated reference standards.
- Use the term **reference standard**, following CLAIM 2024, rather than assuming any label is automatically “ground truth.”

---

## Serial paper analyses

## 1. Deep learning-based approach to third molar impaction analysis with clinical classifications

**Citation:** Balel, Y., & Sağtaş, K. (2025). *Deep learning-based approach to third molar impaction analysis with clinical classifications*. Scientific Reports, 15, 23688. DOI: 10.1038/s41598-025-93783-y.

**Study and objective:** A large retrospective study that detects impacted third molars and simultaneously assigns Pell and Gregory class, Winter angulation, and Pederson difficulty information.

**Data and reference standard:** Panoramic radiographs acquired at Sivas Cumhuriyet University from 2014–2024. CVAT bounding boxes and clinical classification labels were manually prepared. The reported partitions contained 2,300 training, 765 validation, and 765 test images, representing 7,624, 2,580, and 2,493 impacted teeth, respectively, across 98 combined labels.

**Model and method:** YOLOv11, learning rate 0.01, batch size 4, up to 1,000 epochs, with augmentation and a multi-label detection/classification design.

**Key results:** Precision 0.980, recall 0.948, F1 0.974, mAP@0.50 0.990, and mAP@0.50:0.95 0.974. Rare combinations performed less well; for example, `48-Distoangular-C-III` had F1 0.633.

**Limitations:** Single clinical source, label imbalance, absent/rare label combinations, no external device/population test, no explainable-AI mechanism, and potential usability barriers.

**Useful references/themes inside the paper:** Pell and Gregory, Winter, and Pederson clinical systems; earlier impacted-tooth detection, mandibular-canal assessment, and extraction-difficulty studies.

**Use in our paper:** This is a central state-of-the-art comparator. It proves that a localisation/classification claim is expected to use tooth-level boxes and object-detection metrics. It also provides a strong motivation for analysing rare-class failure rather than reporting only aggregate accuracy.

**Verdict:** **CORE — KEEP.**

## 2. Deep Learning Based Detection Tool for Impacted Mandibular Third Molar Teeth

**Citation:** Celik, M. E. (2022). *Deep Learning Based Detection Tool for Impacted Mandibular Third Molar Teeth*. Diagnostics, 12(4), 942. DOI: 10.3390/diagnostics12040942.

**Study and objective:** Develops a computer-aided object detector for impacted mandibular third molars on panoramic radiographs.

**Data and reference standard:** 440 panoramic radiographs from 300 patients, annotated for impacted mandibular third molars and randomly partitioned.

**Models and method:** Two-stage Faster R-CNN with ResNet50, VGG16, and AlexNet backbones; one-stage YOLOv3 comparison.

**Key results:** Faster R-CNN mAP@0.50 was 0.91 with ResNet50, 0.87 with VGG16, and 0.86 with AlexNet. YOLOv3 performed best with mAP@0.50 0.96, recall 0.93, and precision 0.88.

**Limitations:** Small dataset and only mandibular third molars; no broad tooth-type or external validation.

**Useful references/themes:** Deep learning in dental radiology, panoramic imaging limitations, Faster R-CNN, YOLO, and earlier CNN-based dental diagnosis.

**Use in our paper:** Foundational detector benchmark. It should be cited when explaining why true localisation requires box annotations and mAP rather than image-level classification accuracy.

**Verdict:** **CORE — KEEP.**

## 3. Canine impaction classification from panoramic dental radiographic images using deep learning models

**Citation:** Aljabri, M., Aljameel, S. S., Min-Allah, N., et al. (2022). *Canine impaction classification from panoramic dental radiographic images using deep learning models*. Informatics in Medicine Unlocked, 30, 100918. DOI: 10.1016/j.imu.2022.100918.

**Study and objective:** Classifies maxillary canine impaction into two Yamamoto-derived types using transfer learning.

**Data and reference standard:** 416 hospital panoramic radiographs from patients aged 9–12, labelled by expert dentists: 282 Type I and 134 Type II. Random undersampling produced a balanced 268-image set. Images were resized to 224×224; rescaling, flip, zoom, shear, and externally enhanced resolution were used.

**Models and method:** DenseNet121, VGG16, InceptionV3, and ResNet50.

**Key results:** InceptionV3 achieved the highest reported accuracy, 0.9259.

**Limitations:** Very small balanced sample created by discarding majority-class images, limited age range and institution, binary type formulation, possible information loss from resizing, and no external test.

**Useful references/themes:** Kuwada et al. for impacted supernumerary-tooth detection; prior radiographic and clinical predictors of canine impaction; transfer-learning foundations.

**Use in our paper:** Direct classification comparator and a good example of why class balancing strategy and data retention must be stated explicitly.

**Verdict:** **CORE — KEEP.**

## 4. Using deep learning to segment impacted molar teeth from panoramic radiographs

**Citation:** Alam, S. S., Ahad, A., Ahmed, S., Dudley, J., & Farook, T. H. (2025). *Using deep learning to segment impacted molar teeth from panoramic radiographs*. Digital Dentistry Journal, 1, 100007. DOI: 10.1016/j.ddj.2025.100007.

**Study and objective:** Evaluates classification and segmentation of impacted molars using conventional CNNs, vision models, vision-language models, and U-Net.

**Data and reference standard:** 693 panoramic radiographs, divided 80%/10%/10% into training, validation, and test sets; random oversampling addressed imbalance.

**Models and method:** CNN, CLIP, ViT, CNN with ViT embedding for classification, and U-Net for segmentation.

**Key results:** CNN+ViT embedding achieved accuracy 0.77 with precision 0.43 for impacted cases. ViT achieved the highest AUROC, 0.85. The plain CNN identified non-impacted images well (precision 0.84, recall 0.86). U-Net struggled severely; the paper reports very low impacted-tooth class IoU.

**Limitations:** Imbalance, small per-class sample, weak segmentation, no external test, and limited clinical validation. The paper itself recommends balanced data and stronger pretrained/hybrid segmentation.

**Useful references/themes:** Celik’s YOLO work, impacted supernumerary-tooth studies, U-Net, CNN/ViT/CLIP, and panoramic-radiograph error sources.

**Use in our paper:** Extremely close to our task and dataset scale. It provides a realistic comparator for classification and demonstrates that successful image-level classification does not guarantee good pixel-level segmentation.

**Verdict:** **CORE — KEEP.**

## 5. Deep learning for tooth detection and segmentation in panoramic radiographs: a systematic review and meta-analysis

**Citation:** Bonfanti-Gris, M., Herrera, A., Salido Rodríguez-Manzaneque, M. P., Martínez-Rus, F., & Pradíes, G. (2025). *Deep learning for tooth detection and segmentation in panoramic radiographs: a systematic review and meta-analysis*. BMC Oral Health, 25, 1280. DOI: 10.1186/s12903-025-06349-9.

**Study and objective:** Systematically evaluates deep-learning performance for tooth detection and segmentation in panoramic images.

**Evidence base and method:** Searches of Medline, Embase, and Cochrane through September 2023; 20 studies included. Two reviewers independently selected studies and extracted data; GRADE was used. Six mesiodens studies entered the diagnostic meta-analysis.

**Key results:** Pooled sensitivity 0.92, specificity 0.94, positive likelihood ratio 15.7, negative likelihood ratio 0.08, and diagnostic odds ratio 186. Overall evidence supported only a moderate recommendation.

**Limitations:** Heterogeneous designs, variable reference standards, limited external validation, dataset bias, and premature clinical implementation.

**Useful references/themes:** Broad tooth localisation/segmentation literature, diagnostic-test meta-analysis, GRADE, and evidence-quality assessment.

**Use in our paper:** High-value evidence for the Introduction and Discussion. It supports cautious language despite apparently high individual-study metrics.

**Verdict:** **SUPPORTING — KEEP.**

## 6. Aneurysmal Bone Cyst of the Mandible Associated with an Impacted Tooth: A Case Report

**Citation:** Karimi, A., Derakhshan, S., & Abdarjouy, F. (2025). *Aneurysmal Bone Cyst of the Mandible Associated with an Impacted Tooth; a Case Report*. Journal of Iranian Dental Association, 37(3–4). DOI: 10.34172/jida.2279.

**Study and objective:** Reports a 15-year-old patient with a mandibular aneurysmal bone cyst associated with an impacted tooth and discusses differential diagnosis.

**Method and result:** Clinical imaging, aspiration, biopsy, excision, histopathology, and seven-year follow-up. It contains no AI model, training dataset, or performance evaluation.

**Possible contextual value:** Shows that radiolucent pathology around an impacted tooth can mimic odontogenic lesions and that imaging alone may be insufficient.

**Why not retain:** It is too distant from the paper’s machine-learning objective and would not strengthen the technical or evaluation argument.

**Verdict:** **REMOVE — clinically interesting but not relevant enough.**

## 7. Cone-beam CT evaluation of orthodontic treatment outcomes for multiple impacted maxillary anterior teeth

**Citation:** Chen, L., & Mo, S. (2026). *Cone-beam CT evaluation of orthodontic treatment outcomes for multiple impacted maxillary anterior teeth*. BMC Oral Health, 26, 58. DOI: 10.1186/s12903-025-07317-z.

**Study and objective:** Evaluates root development, bone attachment, and traction success after orthodontic treatment of multiple impacted maxillary anterior teeth.

**Data and method:** Sixteen patients treated from 2016–2020; 14 impacted central incisors, 13 lateral incisors, and 16 canines assessed with CBCT and 3D reconstruction, with contralateral teeth as controls.

**Key results:** Traction success was 71.43% for central incisors, 84.62% for lateral incisors, and 93.75% for canines. Several impacted-tooth groups showed reduced intraosseous root ratios or greater alveolar bone loss.

**Limitations:** Very small retrospective cohort, possible selection bias, and missing gingival and other clinical indicators.

**Useful references/themes:** Clinical consequences of impaction, CBCT measurement, orthodontic traction, and treatment outcomes.

**Use in our paper:** Only for clinical motivation and future-outcome discussion—not as an AI benchmark.

**Verdict:** **SUPPORTING CLINICAL CONTEXT — KEEP, but cite sparingly.**

## 8. Comparative Evaluation of Deep Learning Models for the Classification of Impacted Maxillary Canines on Panoramic Radiographs

**Citation:** Tokatlı, N., Erdem, B., Özcan, M., Turan Maviş, B., Şar, Ç., & Özdemir, F. (2026). *Comparative Evaluation of Deep Learning Models for the Classification of Impacted Maxillary Canines on Panoramic Radiographs*. Diagnostics, 16(2), 219. DOI: 10.3390/diagnostics16020219.

**Study and objective:** Compares transfer-learning models for binary impacted-maxillary-canine classification and demonstrates a prototype diagnostic interface.

**Data and reference standard:** Retrospective single-centre set of 694 annotated panoramic radiographs with mild class imbalance.

**Models and method:** ResNet50, Xception, InceptionV3, and VGG16.

**Key results:** VGG16 reported the best performance, with accuracy 99.28% and F1 99.43%.

**Limitations:** Single centre, no prospective clinical testing, no external device/population validation, and classification rather than anatomical localisation.

**Useful references/themes:** Transfer learning, impacted canine epidemiology, earlier canine classification, and clinical-interface implementation.

**Use in our paper:** A recent high-performing classification comparator, but its very high single-centre result should be discussed alongside potential dataset/domain effects.

**Verdict:** **CORE — KEEP.**

## 9. Using deep learning to segment impacted molar teeth from panoramic radiographs

**Identity:** Same title, authors, journal, DOI, methods, dataset, and results as paper 4. The binary files differ slightly, indicating alternate publisher/download versions rather than different studies.

**Use:** Do not count or cite twice. Retain paper 4 as the canonical copy.

**Verdict:** **DUPLICATE OF 4 — REMOVE/ARCHIVE.**

## 10. Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs

**Citation:** He, Z., Wang, Y., & Li, X. (2024). *Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs*. Biomedical Engineering and Computational Biology, 15, 11795972241288319. DOI: 10.1177/11795972241288319.

**Study and objective:** Fine-tunes MedSAM for impacted-tooth segmentation/localisation on panoramic radiographs.

**Data and reference standard:** DENTEX-derived masks. After augmentation, 1,016 images were used with a 16:3:1 training/validation/test ratio. The source annotations appear to emphasise the most prominent impacted tooth per image.

**Models and method:** A fine-tuned SAM first predicts impacted regions, a mass/centroid component generates point prompts, and SAM-family models refine the segmentation. Models include SAM-Med2D, SAM-base, SAM-large, SAM-huge, and MedSAM.

**Key results:** MedSAM was best: accuracy 86.73%, F1 0.5350, recall 0.3868, and IoU 0.3652.

**Limitations:** Small and augmented sample, modest segmentation overlap, possible incomplete labelling of multiple impacted teeth, and no broad clinical/external validation.

**Useful references/themes:** DENTEX, SAM, MedSAM, Celik, ResMIBCU-Net, and zero-shot/fine-tuned medical segmentation.

**Use in our paper:** Direct segmentation comparator and strong evidence that localisation should be measured with overlap metrics, not only image-level accuracy.

**Verdict:** **CORE — KEEP.**

## 11. Deep learning-based approach to third molar impaction analysis with clinical classifications

**Identity:** Byte-for-byte exact duplicate of paper 1, confirmed by identical SHA-256 hashes.

**Use:** Retain paper 1 only.

**Verdict:** **EXACT DUPLICATE OF 1 — REMOVE.**

## 12. Comparative Analysis of Pixel-Based Segmentation Models for Accurate Detection of Impacted Teeth on Panoramic Radiographs

**Citation:** Durmuş, M., Ergen, B., Çelebi, A., & Türkoğlu, M. (2024/2025). *Comparative Analysis of Pixel-Based Segmentation Models for Accurate Detection of Impacted Teeth on Panoramic Radiographs*. IEEE Access. DOI: 10.1109/ACCESS.2024.3523816.

**Study and objective:** Compares four segmentation architectures with ten encoder backbones for pixel-level impacted-tooth detection.

**Data and reference standard:** 407 high-resolution panoramic radiographs with expert segmentation annotations.

**Models and method:** U-Net, feature pyramid network (FPN), PSPNet, and LinkNet combined with multiple backbones including EfficientNet families.

**Key results:** U-Net with EfficientNetB7 performed best, with mean IoU 85.29%.

**Limitations:** One curated dataset, no external multicentre test, limited exploration of different morphologies/pathologies, and computational cost of large backbones.

**Useful references/themes:** Region-based versus pixel-based methods, impacted-tooth detectors, U-Net-family segmentation, and backbone comparison.

**Use in our paper:** One of the strongest direct segmentation benchmarks; essential if the manuscript retains “localization” in its title.

**Verdict:** **CORE — KEEP.**

## 13. Detection of Tooth Position by YOLOv4 and Various Dental Problems Based on CNN With Bitewing Radiograph

**Citation:** Li, K.-C., Mao, Y.-C., Lin, M.-F., et al. (2024). *Detection of Tooth Position by YOLOv4 and Various Dental Problems Based on CNN With Bitewing Radiograph*. IEEE Access. DOI: 10.1109/ACCESS.2023.3348788.

**Study and objective:** Two-stage dental analysis: YOLOv4 tooth-position detection followed by CNN-based symptom classification on bitewing radiographs.

**Models and method:** Gaussian filtering, adaptive binarisation and enhancement; YOLOv4 for tooth localisation; AlexNet/CNN models for disease recognition.

**Key results:** Reported classification accuracies were 92.85% for caries, 96.55% for restorations, and 91.13% for periodontal disease.

**Limitations:** Different modality (bitewing), different diseases, and not an impacted-tooth study. Its metrics are not directly comparable with our panoramic impacted-tooth task.

**Useful references/themes:** General dental object detection, preprocessing, YOLO/CNN cascades, and dental-image annotation.

**Use in our paper:** A technical supporting example of detection-then-classification architecture only.

**Verdict:** **SUPPORTING TECHNICAL SOURCE — KEEP, but not in the core comparison table.**

## 14. Impacted lower third molar classification and difficulty index assessment: comparisons among dental students, general practitioners and deep learning model assistance

**Citation:** Achararit, P., Manaspon, C., Jongwannasiri, C., et al. (2025). *Impacted lower third molar classification and difficulty index assessment: comparisons among dental students, general practitioners and deep learning model assistance*. BMC Oral Health, 25, 152. DOI: 10.1186/s12903-025-05425-4.

**Study and objective:** Tests CNN classification of lower-third-molar angulation, Pell/Gregory-style class and position, and Pederson difficulty; also evaluates whether AI assistance improves dental-student and GP performance.

**Data and reference standard:** 1,200 cropped impacted lower-third-molar panoramic images for model development. A separate 50-image set was evaluated by 35 dental students and 35 general practitioners with and without AI support.

**Models and method:** RegNetY032, DenseNet201, Xception, InceptionV3, ResNetRS101, and InceptionResNetV2; augmentation, transfer learning, Score-CAM, accuracy/AUROC, Cohen’s kappa, and timing comparisons.

**Key results:** For angulation, InceptionResNetV2 reached accuracy 0.88/AUROC 0.97; RegNetY032 reached AUROC 0.98. Xception led class prediction (accuracy 0.78/AUROC 0.87). InceptionResNetV2 led position prediction (accuracy 0.92/AUROC 0.96). AI assistance significantly improved accuracy and agreement for both clinician groups.

**Limitations:** Cropped-image task, one dataset, no broad external validation, varying class balance, and assistance-study performance may not translate to routine workflow.

**Useful references/themes:** Winter, Pell and Gregory, Pederson index, human–AI comparison, kappa, and Score-CAM.

**Use in our paper:** Excellent clinical-comparison reference and justification for reporting class-wise metrics, observer agreement, and decision-support—not replacement—language.

**Verdict:** **CORE — KEEP.**

## 15. The diagnostic performance of impacted third molars in the mandible: A review of deep learning on panoramic radiographs

**Citation:** Faadiya, A. N., Widyaningrum, R., Arindra, P. K., & Diba, S. F. (2024). *The diagnostic performance of impacted third molars in the mandible: A review of deep learning on panoramic radiographs*. The Saudi Dental Journal, 36, 404–412. DOI: 10.1016/j.sdentj.2023.11.025.

**Study and objective:** Reviews detection, impaction classification, and mandibular-third-molar/mandibular-canal relationship assessment on panoramic radiographs.

**Evidence base:** Searches PubMed, Google Scholar, and ScienceDirect; 49 articles reviewed, with 12 core studies discussed in depth.

**Key results:** Reported diagnostic accuracy for mandibular impacted-third-molar tasks ranged from 78.91% to 90.23%; accuracy for third-molar/mandibular-canal relationship tasks ranged from 72.32% to 99%.

**Limitations:** Narrative rather than formal meta-analytic synthesis, heterogeneous tasks and datasets, and limited direct evidence of clinical implementation.

**Useful references/themes:** Celik, extraction-difficulty models, canal-proximity classifiers, panoramic limitations, and clinical classification systems.

**Use in our paper:** Core source for the Introduction, landscape description, and discussion of the gap between promising internal performance and clinical validation.

**Verdict:** **CORE REVIEW — KEEP.**

## 16. Deep learning driven segmentation of maxillary impacted canine on cone beam computed tomography images

**Citation:** Swaity, A., Elgarba, B. M., Morgan, N., et al. (2023). *Deep learning driven segmentation of maxillary impacted canine on cone beam computed tomography images*. Scientific Reports. DOI: 10.1038/s41598-023-49613-0.

**Study and objective:** Evaluates automated 3D segmentation of impacted maxillary canines on CBCT using a commercial cloud platform.

**Data and reference standard:** 100 CBCT scans: 50 for training and 50 for testing. Automated masks were compared with semi-automated reference segmentations using voxel- and surface-based measures.

**Model and method:** CNN-based `Virtual patient creator` platform, with Dice and timing evaluation.

**Key results:** Dice similarity coefficient 0.99 ± 0.02; automated segmentation was 24 times faster than the semi-automated process.

**Limitations:** Small sample, 3D CBCT rather than 2D panoramic radiographs, platform-specific implementation, and no multicentre external test.

**Useful references/themes:** Digital dentistry workflows, CBCT segmentation, observer burden, Dice, and automated-versus-manual timing.

**Use in our paper:** Strong adjacent segmentation evidence. It should be used to contrast 3D CBCT localisation with the inherent depth ambiguity of 2D panoramics.

**Verdict:** **CORE/ADJACENT — KEEP.**

## 17. Artificial Intelligence for Classifying the Relationship between Impacted Third Molar and Mandibular Canal on Panoramic Radiographs

**Citation:** Lo Casto, A., Spartivento, G., Benfante, V., et al. (2023). *Artificial Intelligence for Classifying the Relationship between Impacted Third Molar and Mandibular Canal on Panoramic Radiographs*. Life, 13, 1441. DOI: 10.3390/life13071441.

**Study and objective:** Classifies contact between the lower third molar and mandibular canal on panoramic images and compares CNNs with a sixth-year dental student.

**Data and reference standard:** 142 cropped third-molar images from 83 panoramic radiographs, labelled by an experienced radiologist; 80% training/validation and 20% test with k-fold cross-validation.

**Models and method:** ResNet152 and VGG19; sensitivity, specificity, PPV, and accuracy.

**Key results:** ResNet152: sensitivity 84.09%, specificity 94.11%, PPV 92.11%, accuracy 88.86%. VGG19: 71.82%, 93.33%, 92.26%, and 85.28%. Dental student: 69.60%, 53.00%, 64.85%, and 62.53%.

**Limitations:** Very small image/patient count, cropped images, single expert reference, and panoramic projection cannot fully establish buccolingual contact.

**Useful references/themes:** Inferior alveolar nerve risk, CBCT escalation, human–AI comparison, ResNet/VGG, and panoramic distortion.

**Use in our paper:** Useful for clinical relevance, observer comparison, and explaining why 2D localisation claims must be carefully scoped.

**Verdict:** **CORE — KEEP.**

## 18. Artificial Intelligence for 3D Reconstruction from 2D Panoramic X-rays to Assess Maxillary Impacted Canines

**Citation:** Minhas, S., Wu, T.-H., Kim, D.-G., Chen, S., Wu, Y.-C., & Ko, C.-C. (2024). *Artificial Intelligence for 3D Reconstruction from 2D Panoramic X-rays to Assess Maxillary Impacted Canines*. Diagnostics, 14, 196. DOI: 10.3390/diagnostics14020196.

**Study and objective:** Tests whether a generative reconstruction model can estimate impacted-canine position in 3D from a 2D panoramic image.

**Data and reference standard:** Paired pre-treatment CBCT and panoramic information from 123 patients; 74 had impacted canines and 49 did not. The impacted subset generated paired 2D/pseudo-3D training data.

**Model and method:** Deep generative 2D-to-3D reconstruction; SSIM and positional classification in buccolingual and mesiodistal directions.

**Key results:** Buccal/middle/lingual position accuracy 41%; mesial/distal accuracy 55%; mean SSIM 0.71 (range 0.63–0.84).

**Limitations:** Small paired set, single panoramic projection lacks depth information, modest positional accuracy, and reconstruction quality does not automatically imply clinical localisation accuracy.

**Useful references/themes:** X2CT-GAN-style reconstruction, impacted-canine diagnosis, CBCT reference imaging, and 2D projection ambiguity.

**Use in our paper:** Valuable negative/feasibility comparator demonstrating that anatomical depth localisation from a single panoramic image remains difficult.

**Verdict:** **CORE/ADJACENT — KEEP.**

## 19. The diagnostic performance of impacted third molars in the mandible: A review of deep learning on panoramic radiographs

**Identity:** Same review as paper 15; alternate downloaded version with the same DOI and scientific content.

**Use:** Retain paper 15 only.

**Verdict:** **DUPLICATE OF 15 — REMOVE/ARCHIVE.**

## 20. Dual Framework for Classification and Detection of Third Molar Impaction in Panoramic Radiographs

**Citation:** Khurshid, Z., Alsleem, M. H., Aljubairah, F. A., et al. (2026). *Dual Framework for Classification and Detection of Third Molar Impaction in Panoramic Radiographs*. International Dental Journal, 76(2), 109430. DOI: 10.1016/j.identj.2026.109430.

**Study and objective:** Builds separate classification and object-detection frameworks for multiclass third-molar impaction assessment.

**Data and reference standard:** Multinational set of 5,796 expertly annotated orthopantomograms; reported inter-rater kappa 0.92.

**Models and method:** Modified YOLOv10 and YOLOv11n with multihead self-attention for detection; ResNet50 and InceptionV3 feature extraction followed by classical classifiers; GAN augmentation and ablations.

**Key results:** Fine KNN with ResNet50 features achieved accuracy 97.56%, precision 96.07%, recall 96.21%, and F1 96.10%. YOLOv11n achieved mAP@0.50 88.9% and mAP@0.50:0.95 85.7%. Attention and GAN augmentation reportedly improved mAP by 6.4%.

**Limitations:** Remaining 2D projection ambiguity, lower precision for some angulation classes, and need for heterogeneous-protocol/multicentre confirmation despite the multinational set.

**Useful references/themes:** YOLOv10/11, ResNet/Inception deep features, traditional classifiers, GAN augmentation, attention, class imbalance, and inter-rater reliability.

**Use in our paper:** Closest current comparator for a combined classification/detection title. Its annotation scale and agreement reporting define the standard our current pseudo-box pipeline does not yet meet.

**Verdict:** **HIGHEST-PRIORITY CORE — KEEP.**

## 21. Automatic diagnosis of true proximity between the mandibular canal and the third molar on panoramic radiographs using deep learning

**Citation:** Jeon, K. J., Choi, H., Lee, C., & Han, S.-S. (2023). *Automatic diagnosis of true proximity between the mandibular canal and the third molar on panoramic radiographs using deep learning*. Scientific Reports. DOI: 10.1038/s41598-023-49512-4.

**Study and objective:** Predicts true anatomical contact between a mandibular third molar and mandibular canal from a panoramic radiograph, using CBCT to determine the reference relationship.

**Data and reference standard:** 901 third molars, balanced as 450 true-contact and 451 true-non-contact cases. Two radiologists assessed CBCT. Data came from six imaging devices across multiple institutions.

**Models and method:** RetinaNet, YOLOv3, and EfficientDet; accuracy, sensitivity, and specificity.

**Key results:** EfficientDet performed best: accuracy 78.65%, sensitivity 82.02%, and specificity 75.28%.

**Limitations:** Panoramic imaging cannot directly represent buccolingual separation; performance remains moderate; reference requires CBCT; generalisability and prospective clinical impact remain to be shown.

**Useful references/themes:** CBCT-confirmed canal proximity, panoramic warning signs, inferior alveolar nerve injury, RetinaNet/YOLO/EfficientDet, and multicentre/device variation.

**Use in our paper:** Methodologically valuable because it uses a stronger cross-modality reference standard rather than labels derived only from the same 2D image.

**Verdict:** **CORE — KEEP.**

## 22. Comparison of Faster R-CNN, YOLO, and SSD for Third Molar Angle Detection in Dental Panoramic X-rays

**Citation:** Vilcapoma, P., Parra Meléndez, D., Fernández, A., Vásconez, I. N., Hillmann, N. C., Gatica, G., & Vásconez, J. P. (2024). *Comparison of Faster R-CNN, YOLO, and SSD for Third Molar Angle Detection in Dental Panoramic X-rays*. Sensors, 24, 6053. DOI: 10.3390/s24186053.

**Study and objective:** Detects and classifies third-molar angulation according to Winter’s system and compares detector/backbone combinations.

**Data and reference standard:** 644 panoramic radiographs with four target classes: distoangular, vertical, mesioangular, and horizontal.

**Models and method:** Faster R-CNN, YOLOv2, and SSD using ResNet18, ResNet50, and ResNet101 feature extractors. The workflow includes training, calibration, validation, and testing.

**Key results:** The best configurations reported approximately 99% mean average accuracy, with YOLOv2 providing the strongest overall effectiveness for this dataset.

**Limitations:** Modest single dataset, class-distribution dependence, no broad external test, and “mean average accuracy” should not be confused with standard COCO mAP unless its definition and IoU thresholds are reproduced exactly.

**Useful references/themes:** Winter classification, object detector comparison, ResNet backbones, dataset bias/variance, and dental object detection.

**Use in our paper:** Direct reference for third-molar angle localisation/classification and for designing a fair multi-detector comparison.

**Verdict:** **CORE — KEEP.**

## 23. Deep-learning model for assessing difficulty in localizing impacted canines

**Citation:** Özcan, M., Erdem, B., Turan, B., Tokatlı, N., Şar, Ç., & Özdemir, F. (2024). *Deep-learning model for assessing difficulty in localizing impacted canines*. Oral abstract, FDI World Dental Congress; International Dental Journal supplement. DOI: 10.1016/j.identj.2024.07.578.

**Study and objective:** Conference abstract evaluating buccal/middle/palatal position prediction for impacted maxillary canines from panoramic radiographs.

**Data and method:** 810 panoramic radiographs with clinical positional information; TensorFlow CNN classifier.

**Key result:** Reported positional classification accuracy was 68%.

**Limitations:** Only a short congress abstract is present. Model architecture, partition design, annotation process, confidence intervals, and complete results are not reported sufficiently for reproducibility or risk-of-bias assessment.

**Use in our paper:** At most, a brief indication that 2D buccopalatal localisation is difficult. Stronger full-length papers 17, 18, and 21 already support that argument.

**Verdict:** **REMOVE/ARCHIVE — relevant topic but insufficient full-paper evidence.**

## 24. Hybrid CNN-Transformer Model for Accurate Impacted Tooth Detection in Panoramic Radiographs

**Citation:** Küçük, D. B., Imak, A., Özçelik, S. T. A., Çelebi, A., Türkoğlu, M., Şengür, A., & Koundal, D. (2025). *Hybrid CNN-Transformer Model for Accurate Impacted Tooth Detection in Panoramic Radiographs*. Diagnostics, 15(3), 244. DOI: 10.3390/diagnostics15030244.

**Study and objective:** Combines real-time CNN detection and transformer detection, then fuses their boxes for impacted-tooth localisation.

**Data and reference standard:** 407 labelled panoramics pooled from three datasets/resolutions: 304 PNG images at 540×380, 53 JPG images at 2041×1024, and 50 PNG images at 3100×1300. Expert boxes were converted to YOLO format. Split: 325 training, 21 validation, and 61 test images.

**Models and method:** Super-resolution with GFP-GAN, YOLO, RT-DETR, Weighted Boxes Fusion, and Bayesian optimisation. Images were standardised to 640×640; training ran up to 500 epochs.

**Key results:** Reported mAP 98.3% and F1 96%, exceeding individual models and simpler fusion combinations.

**Limitations:** Small test set, pooled source domains, possible source-specific leakage if splits were not grouped by source/patient, heavy pipeline complexity, and no independent clinical external test.

**Useful references/themes:** YOLO, RT-DETR, transformer detection, WBF, Bayesian optimisation, super-resolution, and pixel-based impacted-tooth studies.

**Use in our paper:** A major state-of-the-art detection comparator and a model for describing bounding-box fusion. It also motivates strict source/patient-aware splitting when multiple datasets are pooled.

**Verdict:** **HIGHEST-PRIORITY CORE — KEEP.**

## 25. Deep Learning for Predicting the Difficulty Level of Removing the Impacted Mandibular Third Molar

**Citation:** Trachoo, V., Taetragool, U., Pianchoopat, P., Sukitporn-udom, C., Morakrant, N., & Warin, K. (2025). *Deep Learning for Predicting the Difficulty Level of Removing the Impacted Mandibular Third Molar*. International Dental Journal, 75, 144–150. DOI: 10.1016/j.identj.2024.06.021.

**Study and objective:** Creates a three-stage system that confirms impacted-molar presence, localises the tooth, and predicts surgical removal difficulty.

**Data and reference standard:** 1,367 impacted mandibular third molars from 784 patients collected between 2021 and 2023. Four experts (three oral/maxillofacial surgeons and one oral radiologist) reached consensus on Pederson difficulty; intrarater Cohen kappa ranged 0.82–0.94 and inter-rater Fleiss kappa was 0.84. Expert bounding boxes were prepared in LabelMe.

**Models and method:** ResNet101V2 for binary presence, RetinaNet for localisation, and ViT for three-level extraction difficulty.

**Key results:** ResNet accuracy 0.8671; RetinaNet mAP 0.9928; ViT average difficulty-classification accuracy 0.7899.

**Limitations:** Class imbalance, rare expert-difficulty cases, retrospective single-centre data, limited clinical variables, and no external device/institution test.

**Useful references/themes:** Pederson difficulty, expert agreement, ResNet, RetinaNet, ViT, staged clinical decision support, and surgical complications.

**Use in our paper:** One of the best methodological templates because it reports patients, multiple experts, agreement, boxes, and distinct metrics for each stage.

**Verdict:** **HIGHEST-PRIORITY CORE — KEEP.**

## 26. Dual Framework for Classification and Detection of Third Molar Impaction in Panoramic Radiographs

**Identity:** Pre-publication/early-layout copy of paper 20. It contains the same authors, dataset, methods, and results; the publication-status line is less final.

**Use:** Retain paper 20 as the canonical published copy.

**Verdict:** **DUPLICATE/OLDER VERSION OF 20 — REMOVE/ARCHIVE.**

## 27. Application of Convolutional Neural Networks in an Automatic Judgment System for Tooth Impaction Based on Dental Panoramic Radiography

**Citation:** Huang, Y.-Y., Mao, Y.-C., Chen, T.-Y., et al. (2025). *Application of Convolutional Neural Networks in an Automatic Judgment System for Tooth Impaction Based on Dental Panoramic Radiography*. Diagnostics, 15(11), 1363. DOI: 10.3390/diagnostics15111363.

**Study and objective:** Fully automated preprocessing, double-tooth cropping, symptom enhancement, and CNN classification for impacted teeth.

**Data and reference standard:** De-identified clinical panoramics from Chang Gung Memorial Hospital, selected and annotated by a dentist. Original tooth-crop counts were approximately 2,000 “other” and 139 impacted examples. Augmentation increased impacted crops to 1,000; a balanced training selection was then created. Crops were 200×300.

**Models and method:** Position/frame/light adjustment, Sobel/Canny and other enhancement methods; AlexNet, VGG19, GoogLeNet, SqueezeNet, and Xception with transfer learning and hyperparameter tuning.

**Key results:** Accuracy was 84.48% without enhancement and 98.66% after the selected preprocessing/enhancement workflow. End-to-end processing took 4.4 seconds.

**Limitations:** Very large synthetic augmentation relative to only 139 original impacted samples, unclear patient-level partitioning, reported validation set used during “testing,” limited radiographic-format adaptability, and focus on one condition. The dataset description is internally inconsistent: the prose says 1,000 “Other” samples were selected for balance, while Table 1 lists 2,000 “Other” and 1,000 impacted samples after selection.

**Useful references/themes:** Dental preprocessing, impacted-tooth localisation, CNN transfer learning, class imbalance, and edge enhancement.

**Use in our paper:** Useful for preprocessing discussion, but its high accuracy must be interpreted cautiously because of sample construction and evaluation wording.

**Verdict:** **CORE — KEEP.**

## 28. Hybrid CNN-Transformer Model for Accurate Impacted Tooth Detection in Panoramic Radiographs

**Identity:** Byte-for-byte exact duplicate of paper 24, confirmed by identical SHA-256 hashes.

**Use:** Retain paper 24 only.

**Verdict:** **EXACT DUPLICATE OF 24 — REMOVE.**

## 29. Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs

**Identity:** Alternate publisher copy of paper 10 with the same authors, DOI, dataset, methods, and results.

**Use:** Retain paper 10 only.

**Verdict:** **DUPLICATE OF 10 — REMOVE/ARCHIVE.**

## 30. Deep Learning for Predicting the Difficulty Level of Removing the Impacted Mandibular Third Molar

**Identity:** Alternate/earlier-layout copy of paper 25 with the same DOI, methods, and results.

**Use:** Retain paper 25 only.

**Verdict:** **DUPLICATE OF 25 — REMOVE/ARCHIVE.**

## 31. Deep Learning Based Detection Tool for Impacted Mandibular Third Molar Teeth

**Identity:** Byte-for-byte exact duplicate of paper 2, confirmed by identical SHA-256 hashes.

**Use:** Retain paper 2 only.

**Verdict:** **EXACT DUPLICATE OF 2 — REMOVE.**

## 32. DENTEX: An Abnormal Tooth Detection with Dental Enumeration and Diagnosis Benchmark for Panoramic X-rays

**Citation:** Hamamci, I. E., Er, S., Simsar, E., et al. (2023). *DENTEX: An Abnormal Tooth Detection with Dental Enumeration and Diagnosis Benchmark for Panoramic X-rays*. MICCAI 2023 challenge paper; arXiv:2305.19112.

**Study and objective:** Defines a hierarchical multi-institution benchmark for quadrant detection, tooth enumeration, and abnormal-tooth diagnosis, including impacted teeth.

**Data and reference standard:** Three institutions and varied devices/protocols. The resource includes 693 quadrant-labelled panoramics, 634 quadrant/enumeration-labelled images, 1,005 fully labelled quadrant/enumeration/diagnosis images, and 1,571 unlabelled pretraining images. Fully labelled data are partitioned into 705 training, 50 validation, and 250 hidden test images. Final-year dental students annotated images; one of three dentists with more than 15 years of experience verified/corrected them.

**Task and metrics:** Four diagnoses—caries, deep caries, periapical lesions, and impacted teeth—with AP50, AP75, AP, and average recall.

**Key contribution:** A public, heterogeneous benchmark with expert-verified spatial labels and hidden test evaluation rather than a single-model result.

**Limitations:** Hierarchical/partial labels, class imbalance, metric sensitivity, and the original paper notes limitations of AP/AR interpretation.

**Useful references/themes:** FDI numbering, dental enumeration, abnormal-tooth detection, hierarchical labels, multi-institution data, and hidden test protocols.

**Use in our paper:** Essential dataset and external-testing reference. It is the best available route for replacing pseudo-box-only localisation with expert spatial annotations.

**Verdict:** **HIGHEST-PRIORITY CORE — KEEP.**

## 33. Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs

**Identity:** Alternate downloaded copy of paper 10. Same title, authors, DOI, dataset, MedSAM method, and performance.

**Use:** Retain paper 10 only.

**Verdict:** **DUPLICATE OF 10 — REMOVE/ARCHIVE.**

## 34. The diagnostic performance of impacted third molars in the mandible: A review of deep learning on panoramic radiographs

**Identity:** Third copy/version of paper 15 with the same authors, journal, DOI, methods, and conclusions.

**Use:** Retain paper 15 only.

**Verdict:** **DUPLICATE OF 15 — REMOVE/ARCHIVE.**

## 35. Deep learning based prediction of extraction difficulty for mandibular third molars

**Citation:** Yoo, J.-H., Yeom, H.-G., Shin, W., et al. (2021). *Deep learning based prediction of extraction difficulty for mandibular third molars*. Scientific Reports, 11, 1954. DOI: 10.1038/s41598-021-81449-4.

**Study and objective:** Predicts the three components of the Pederson difficulty score from preoperative panoramic radiographs.

**Data and reference standard:** 1,053 mandibular third molars from 600 panoramic images. Three human observers reached consensus on Pederson criteria.

**Model and method:** ImageNet-pretrained ResNet34. Separate predictions for depth (C1), ramal relationship (C2), and angulation (C3); RMSE and Cohen kappa were also reported.

**Key results:** Accuracy: C1 78.91%, C2 82.03%, C3 90.23%. Expected-vs-observed Pederson score RMSE was 0.6738. Cohen kappa was 70.88%, 65.23%, and 85.54% for C1–C3.

**Limitations:** Panoramic distortion and no transverse information, rare high-difficulty scores, and omission of age, sex, root morphology, bone density, and canal proximity.

**Useful references/themes:** Pederson scoring, extraction complications, ResNet, observer consensus, and clinically meaningful multi-output evaluation.

**Use in our paper:** Foundational classification/difficulty source and an example of reporting more than raw accuracy.

**Verdict:** **CORE — KEEP.**

## 36. Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update

**Citation:** Tejani, A. S., Klontzas, M. E., Gatti, A. A., Mongan, J. T., Moy, L., Park, S. H., & Kahn, C. E. Jr. (2024). *Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update*. Radiology: Artificial Intelligence, 6(4), e240300. DOI: 10.1148/ryai.240300.

**Type and objective:** Expert-consensus reporting guideline, not an impacted-tooth experiment. It updates the best-practice checklist for medical-imaging AI manuscripts.

**Method:** Formal Delphi consensus with a multidisciplinary panel. The update contains 44 reporting items.

**Key guidance:** Identify the AI technology in the title/abstract; report study design, data source, patient/examination numbers, partition level, acquisition, reference standard, model/threshold selection, internal/external testing, uncertainty, failures, limitations, code/model/data availability, and a cohort flowchart. It recommends “reference standard” instead of “ground truth” and distinguishes internal from external testing.

**Limitations:** It is a reporting framework, not a quality score and not evidence of model effectiveness.

**Useful references/themes:** STARD, EQUATOR reporting guidance, reproducibility, AI study design, and clinical translation.

**Use in our paper:** Mandatory methodological checklist for writing and peer-reviewing the final manuscript. It directly exposes current gaps in patient-level separation, reference-standard documentation, and external testing.

**Verdict:** **ESSENTIAL REPORTING SOURCE — KEEP.**

## 37. Predicting alveolar nerve injury and the difficulty level of extraction impacted third molars: a systematic review of deep learning approaches

**Citation:** Al Salieti, H., Qasem, H. M., Alshwayyat, S., et al. (2025). *Predicting alveolar nerve injury and the difficulty level of extraction impacted third molars: a systematic review of deep learning approaches*. Frontiers in Dental Medicine, 6, 1534406. DOI: 10.3389/fdmed.2025.1534406.

**Study and objective:** Systematically reviews deep-learning models for predicting extraction difficulty and inferior alveolar nerve injury involving impacted third molars.

**Evidence base and method:** Six studies from 2021–2024 were included, covering 12,419 panoramic images and 11,190 assessed third molars. QUADAS-2 was used for risk-of-bias evaluation.

**Key findings:** Four studies evaluated extraction difficulty, two evaluated nerve injury, and one covered both categories. The review found promising performance but major variation in definitions, model architectures, imaging protocols, and reporting.

**Limitations:** Only six eligible studies, potential publication bias, inconsistent outcome definitions, inability to conduct a meaningful meta-analysis, incomplete demographic reporting, and limited geographical diversity.

**Useful references/themes:** Yoo, Trachoo and related difficulty models, nerve-risk studies, QUADAS-2, generalisability, and clinical-outcome definition.

**Use in our paper:** Strong source for the research gap, risk-of-bias discussion, and argument for standardised endpoints and external testing.

**Verdict:** **CORE SYSTEMATIC REVIEW — KEEP.**

---

## Recommended 25-paper retained set

Retain these serials as the working literature library:

**1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27, 32, 35, 36, 37**

### Priority for the Related Work section

**Primary direct comparators:** 1, 2, 4, 8, 10, 12, 14, 20, 21, 22, 24, 25, 27, 32, 35.
**Clinical/adjacent context:** 3, 7, 16, 17, 18.
**Reviews and reporting:** 5, 15, 36, 37.
**General technical architecture only:** 13.

## Cross-paper synthesis for the manuscript

### What the literature already establishes

1. Impacted-tooth classification from panoramics is well studied with CNNs and transfer learning.
2. True localisation studies use expert boxes/masks and report mAP, Dice, or IoU.
3. Third-molar work increasingly predicts Winter angle, Pell and Gregory class, Pederson difficulty, canal proximity, or surgical risk—not merely impacted/non-impacted status.
4. Recent high-performing studies often use large expert-annotated datasets, explicit observer agreement, and separate classification/detection pipelines.
5. Single-centre internal accuracy is common, while external and prospective testing remain limited.

### Defensible gap for our project

The novelty cannot be simply “using deep learning to detect impacted teeth.” A stronger gap would combine:

- a clearly described Bangladesh clinical panoramic cohort;
- verified patient-level separation;
- a rigorous comparison of simple and complex classifiers;
- calibration and sensitivity-oriented triage;
- expert-reviewed label-disagreement analysis;
- a formal comparison between saliency-derived weak localisation and expert-box localisation;
- external testing on DENTEX or a second institution.

### Most important warning for writing

The current notebook’s Grad-CAM-derived pseudo-boxes support **weakly supervised localisation only**. Papers 1, 2, 10, 12, 20, 24, 25, and 32 show the evidentiary standard for genuine localisation: independent tooth-level boxes/masks, clear patient/data partitions, and object- or pixel-level metrics. Until that standard is met, the manuscript title and conclusions must qualify localisation accordingly.

## Suggested citation routing

| Manuscript location | Best serials |
|---|---|
| Clinical importance of impaction | 7, 14, 17, 21, 25, 35, 37 |
| Existing panoramic classification | 3, 8, 14, 20, 27, 35 |
| Object detection/localisation | 1, 2, 20, 22, 24, 25, 32 |
| Segmentation | 4, 10, 12, 16 |
| 2D panoramic limitations / CBCT | 16, 17, 18, 21 |
| Dataset and external benchmark | 32 |
| Clinical AI assistance | 14, 17, 25 |
| Reviews and research gap | 5, 15, 37 |
| Reporting and reproducibility | 36 |
| Preprocessing/detection cascade | 13, 27 |

## Final recommendation

Use 25 unique sources, not all 37 files. Keep the serial numbers in this document for traceability, but create the final bibliography from DOI/title identity so duplicate copies never become duplicate references. For the first manuscript draft, approximately 18–22 of these 25 sources will probably be enough; the remaining sources can support Methods choices, supplementary comparisons, and reviewer responses.
