# MedVision Notebook Knowledge Base

> এই ফাইলটি `E:\Defense\Discuss\ipynb Files` ফোল্ডারের সব ১২টি Jupyter notebook বিশ্লেষণ করে তৈরি করা হয়েছে। এটি ভবিষ্যৎ paper writing, audit এবং reproducibility planning-এর জন্য working reference।

## 1. Scope and notebook inventory

ফোল্ডারে মোট ১২টি notebook আছে। এগুলো একটি ধারাবাহিক multimodal chest-X-ray research pipeline-এর অংশ। প্রতিটি notebook Python 3 kernel ব্যবহার করে এবং সংরক্ষিত execution state-এ কোনো recorded error পাওয়া যায়নি। তবে “no recorded error” মানেই methodological validity নিশ্চিত নয়।

| Notebook group | Files | Role |
|---|---|---|
| Data preparation | `medvision-thesis-part1.ipynb` | MIMIC-CXR cohort, report processing, labels, patient-level split |
| Baseline | `medvision-thesis-part2.ipynb`, `part3.ipynb` | Multimodal baseline এবং image/text/gray-square baselines |
| LMH | `part4.ipynb`, `part5.ipynb`, `part6.ipynb` | Learned Mixin Hypothesis/LMH warm-start training |
| Noise consistency | `part7.ipynb`, `part8.ipynb`, `part9.ipynb` | Noise-Consistency variant-এর বাকি seeds |
| GACR-B ablation | `part10.ipynb` | তিনটি seed-এ ablation |
| Adaptive model | *(আগের `medvision-adaptive-cadq-train.ipynb` এখন folder-এ নেই)* | Adaptive-CADQ training-এর upstream artifacts audit notebook-এ input হিসেবে ব্যবহৃত |
| Audit (legacy) | `medvision-q1-audit-v2.ipynb` | পুরোনো cross-variant statistics ও audit |
| Audit (current) | `medvision-q1-audit-final-FIXED-MERGE-v2.ipynb` | Multi-input merge, extended statistics, fixed figures, CLAIM/TRIPOD checklist |

Parts 2–10, adaptive notebook এবং audit notebook-এর প্রথম shared code cells একই pipeline/config/model definitions পুনরায় ব্যবহার করে। ফলে notebook-গুলো আলাদা হলেও computational design মূলত একটি single research system।

### Current-folder revision

সর্বশেষ re-analysis-এ folder-এ adaptive training notebook আর নেই; তার পরিবর্তে `medvision-q1-audit-final-FIXED-MERGE-v2.ipynb` আছে। নতুন audit notebook নিজে training করে না। এটি `/kaggle/input`-এর attached upstream datasets থেকে `all_results.pkl`, `img_text_results.pkl` এবং checkpoints খুঁজে এনে merge করে। অর্থাৎ পুরোনো adaptive notebook মুছে গেলেও adaptive model-এর ফলাফল ব্যবহার করতে তার exported upstream output attach করা থাকতে হবে।

## 2. End-to-end research pipeline

```text
MIMIC-CXR metadata + JPG + CheXpert + reports
        ↓
Frontal-image filtering, report section extraction, 3-class cohort
        ↓
Patient-level train/validation/test split
        ↓
DenseNet image encoder + ClinicalBERT text encoder
        ↓
CADQ multimodal baseline
        ├─ image-only baseline
        ├─ text-only baseline
        ├─ gray-square + text control
        ├─ LMH
        ├─ Noise-Consistency
        ├─ Adaptive-CADQ
        └─ GACR-B ablation
        ↓
Macro-F1, per-class F1/recall, AUROC, ECE, Brier, confusion matrix
        ↓
Q1 audit: ICM, paired tests, gate analysis, figures and JSON artifacts
```

## 3. Dataset and cohort construction

### Source and labels

- Source: PhysioNet MIMIC-CXR 2.0.0 metadata এবং MIMIC-CXR-JPG 2.1.0 image files।
- Report archive থেকে `findings` এবং `impression` section regex/fallback parser দিয়ে আলাদা করা হয়।
- Frontal AP/PA studies রাখা হয়; lateral images বাদ দেওয়া হয়।
- CheXpert NLP labels থেকে তিনটি class তৈরি করা হয়:
  - `Normal`: `No Finding == 1.0`
  - `Pneumonia`: `Pneumonia == 1.0`
  - `Pneumothorax`: `Pneumothorax == 1.0`
  - অন্য label/ambiguous case বাদ দেওয়া হয়।
- Class cap: Normal 2,500; Pneumonia 2,500; Pneumothorax 1,000।

প্রাথমিক cohort ছিল ৬,০০০ image এবং ৪,৬৯৩ unique patient। `subject_id` group ধরে 70/15/15 patient-level split করা হয়। প্রাথমিক split count: train 2,055, validation 450, test 457। পরে missing image এবং duplicate/fingerprint cleaning-এর পর downstream notebooks-এ ব্যবহৃত split হলো:

| Split | Images used downstream |
|---|---:|
| Train | 2,049 |
| Validation | 449 |
| Test | 455 |

Patient overlap checks (`train–val`, `train–test`, `val–test`) শূন্য ছিল। Cross-split report-fingerprint duplicate অপসারণে ৩৬টি overlap সরানো হয়।

### Model text input

Training dataset-এ model input হিসেবে `findings` text ব্যবহার করা হয়; `impression` আলাদা করা হলেও primary model input হিসেবে দেখা যায়নি। Text dropout probability 0.10 এবং text masking option আছে।

## 4. Shared configuration

- Classes: Normal, Pneumonia, Pneumothorax (৩টি)।
- Seeds: `42, 123, 456, 789, 1010, 1111, 1212, 1313`।
- Epochs: 10; batch size 8; gradient accumulation 4।
- Image size: 224; max text length: 256; projection dimension: 512; attention heads: 8।
- Image encoder: TorchXRayVision DenseNet-121 (`densenet121-res224-mimic_ch`), stem-only freezing।
- Text encoder: `emilyalsentzer/Bio_ClinicalBERT`, প্রথম ৪টি BERT layer frozen।
- Optimizer: AdamW; OneCycleLR; dropout 0.25; weight decay 1e-4।
- Loss: class-weighted cross-entropy, label smoothing 0.05, focal gamma 1.5।
- Gate bounds: alpha 0.20–0.80।
- Paths used inside notebooks: `/kaggle/input`, `/kaggle/working/images`, `/kaggle/working/checkpoints`, `/kaggle/working/results`। Local machine-এ একই inputs না থাকলে exact rerun সম্ভব নয়।
- Notebook-গুলো runtime-এ pinned dependencies install করে, যেমন `transformers==4.44.2`, `torchxrayvision`, `scikit-learn`, `statsmodels` ইত্যাদি।

### Augmentation

- Train: resize 256, random crop 224, horizontal flip, affine/rotation, color jitter, grayscale, normalization।
- Heavy augmentation: stronger affine/jitter এবং Gaussian blur।
- Pneumothorax samples পাঁচবার এবং Pneumonia তিনবার effective repetition পায়; Normal একবার থাকে।
- Weighted sampler PNX-per-batch target করার জন্য সংজ্ঞায়িত, কিন্তু image-only baseline-এ `shuffle=True` ব্যবহৃত হয়েছে; sampler ব্যবহৃত হয়নি।

## 5. Architecture summary

### Common encoders

1. XRV DenseNet image encoder → linear projection → LayerNorm → GELU → dropout → 512-dimensional image representation।
2. ClinicalBERT CLS representation → 512-dimensional text representation।

### CADQ baseline

`DualPathCADQ` image query এবং text key/value দিয়ে `MultiheadAttention` চালায়। এরপর image head এবং text head-এর logits-কে learnable per-class gate alpha দিয়ে মেশানো হয়:

`logits = alpha × image_logits + (1 − alpha) × text_logits`

### LMH

LMH baseline থেকে warm-start হয়। OOF TF-IDF logistic regression থেকে text log-prior bias তৈরি করা হয়; gate network detached joint feature থেকে `g` নির্ধারণ করে এবং entropy penalty ব্যবহার করে। Evaluation call-এ `log_p_bias=None`, তাই test evaluation bias-সহ training path-এর সঙ্গে পুরোপুরি identical নয়—paper-এ এটি পরিষ্কারভাবে লিখতে হবে।

### Noise-Consistency

Image-এ Gaussian noise যোগ করে clean/noisy prediction-এর divergence consistency term তৈরি করা হয়। বর্তমান implementation-এ `compute_consistency_loss()` negative KL ফেরত দেয় এবং training loss-এ `CE + lambda × consistency_loss` যোগ করা হয়। Minimization করলে এটি KL কমানোর বদলে KL বাড়াতে পারে—এটি severe implementation bug, correction ও rerun ছাড়া এই variant-এর ফল scientific claim হিসেবে ব্যবহার করা নিরাপদ নয়।

### Adaptive-CADQ

Image/text logits-এর entropy থেকে adaptive gate alpha নির্ধারিত হয়। আটটি seed-এ সম্পূর্ণ training হয়েছে।

### GACR-B

Part10-এ তিনটি seed (`42, 123, 456`) ব্যবহৃত হয়েছে। Audit v2-এর main 32-entry comparison-এ GACR-B অন্তর্ভুক্ত নয়; unequal seed count-এর কারণে একে আলাদা ablation হিসেবে report করতে হবে।

## 6. Results currently recorded in notebooks

Audit v2-এ ৩২টি result entry আছে: ৮ baseline, ৮ LMH, ৮ Noise-Consistency, ৮ Adaptive-CADQ। Mean ± SD test results:

| Variant | Macro-F1 | Pneumothorax F1 | ECE | Brier |
|---|---:|---:|---:|---:|
| Baseline | 0.9397 ± 0.0061 | 0.8810 ± 0.0174 | 0.0237 | 0.0522 |
| LMH | 0.9435 ± 0.0093 | 0.9003 ± 0.0191 | 0.0621 | 0.0685 |
| Noise-Consistency | 0.9346 ± 0.0075 | 0.8753 ± 0.0237 | 0.0347 | 0.0655 |
| Adaptive-CADQ | 0.9388 ± 0.0072 | 0.8772 ± 0.0175 | 0.0241 | 0.0527 |

Paired comparisons across eight seeds were not statistically significant:

- Baseline vs LMH: delta +0.0038; Wilcoxon exact p=0.2500; paired t-test p=0.2024।
- Baseline vs Noise-Consistency: delta −0.0051; Wilcoxon p=0.1953; t-test p=0.1928।
- Baseline vs Adaptive-CADQ: delta −0.0009; Wilcoxon p=0.8438; t-test p=0.6663।

Seed-42 AUROC permutation comparisons-ও significant নয়: baseline বনাম LMH p=0.1430, বনাম Noise p=0.9110, বনাম Adaptive p=0.9430।

### Single baselines

- Image-only Macro-F1: 0.4611
- Text-only Macro-F1: 0.8555
- Gray-square + text Macro-F1: 0.9381

Gray-square control অত্যন্ত শক্তিশালী হওয়ায় multimodal result-এ image branch-এর প্রকৃত incremental contribution প্রশ্নবিদ্ধ।

### Adaptive-CADQ individual summary

Eight-seed Macro-F1: 0.9378, 0.9333, 0.9485, 0.9388, 0.9276, 0.9342, 0.9473, 0.9431; mean 0.9388 ± 0.0072।

### GACR-B

Seed-42/123/456 Macro-F1 যথাক্রমে 0.9248, 0.9307, 0.9498; mean 0.9351 ± 0.0130। এটি তিন seed-এর ছোট ablation এবং main audit comparison-এর সঙ্গে সরাসরি pooled comparison করা উচিত নয়।

## 7. Audit findings

### ICM

Audit-এর Incremental Contribution Metric:

`ICM = (VLM F1 − Gray-Square F1) / VLM F1`

Means:

- Baseline: 0.001600 ± 0.006485
- LMH: 0.005577 ± 0.009848
- Noise-Consistency: −0.003856 ± 0.008097
- Adaptive-CADQ: 0.000681 ± 0.007660

Zero-এর বিরুদ্ধে Wilcoxon tests significant নয়। TOST equivalence ±0.01-এ baseline ও adaptive equivalent evidence পেয়েছে; LMH এবং Noise-এর ক্ষেত্রে equivalence প্রমাণিত হয়নি।

### Gate audit

Baseline gate alpha প্রায় constant:

- Normal ≈ 0.42627
- Pneumonia ≈ 0.49950
- Pneumothorax ≈ 0.57324

Mean alpha ≈ 0.4997 এবং initialization থেকে drift মাত্র ≈ 0.000254। অর্থাৎ gate collapse করে 0.20-এ যায়নি; বরং parameter প্রায় শেখেনি/স্থির ছিল। Audit markdown-এর “gate collapse” বা “image branch shut off” ধরনের wording actual numeric output-এর সঙ্গে সামঞ্জস্যপূর্ণ নয় এবং পুনর্লিখন প্রয়োজন।

## 8. High-priority validity issues

### Critical / must fix before publication

1. **Image normalization mismatch.** Dataset image-কে `[-1, 1]` range-এ পাঠানো হয়েছে, কিন্তু TorchXRayVision প্রতি run-এ warning দিয়েছে যে pretrained XRV DenseNet-এর expected heuristic range সম্ভবত `[-1024, 1024]`। Pretrained encoder-এর input convention source documentation/code দিয়ে যাচাই করে corrected preprocessing-এ সব model rerun করতে হবে।

2. **Noise-Consistency sign bug.** Negative KL term loss-এ যোগ করা হয়েছে। Correct consistency objective সাধারণত positive KL/JS/MSE term minimize করবে। Current Noise result retain না করে bug fix-এর পর rerun করা উচিত।

3. **One-token attention degeneracy.** Image query-এর key/value হিসেবে একটি মাত্র pooled text vector আছে। Sequence length 1 হলে attention weight trivially 1; ফলে এটিকে genuine token-level cross-attention/alignment বলা যাবে না। Architecture description ও claim-এ সতর্ক থাকতে হবে, অথবা full token sequence দিয়ে experiment করতে হবে।

4. **Potential label–text circularity.** CheXpert NLP-derived labels এবং একই radiology `findings` report model input হিসেবে ব্যবহার করা হয়েছে। Report text-এ রোগের নাম/অভিব্যক্তি label-এর proxy হতে পারে; gray-square + text-এর 0.9381 F1 এই ঝুঁকিকে জোরালো করে। Label source, report leakage analysis, text-only control এবং image contribution claim পুনর্মূল্যায়ন জরুরি।

### Important but secondary

5. **Image-only checkpoint bug.** Best validation F1 state সংরক্ষণ করা হলেও test evaluation-এর আগে `load_state_dict(best_img_state)` করা হয়নি। ফলে image-only test F1 final epoch-এর, অন্য baseline-এর best-checkpoint F1 নয়।

6. **Split-count discrepancy.** Part1-এর initial split 2,055/450/457 হলেও downstream cleaned split 2,049/449/455। Missing images এবং 36 fingerprint duplicate অপসারণের exact accounting Methods-এ দিন।

7. **Non-random class capping.** Class cap merge-order-এর প্রথম rows-এ প্রয়োগ হয়েছে বলে মনে হচ্ছে; random sampling/seeded selection না হলে temporal/site/reader selection bias হতে পারে।

8. **Gate audit narrative mismatch.** Numeric gate ≈0.5/stagnant, কিন্তু audit text collapse/shut-off দাবি করেছে। Claims, figure labels এবং conclusion সংশোধন করতে হবে।

9. **Unequal GACR-B evidence.** GACR-B তিন seed, অন্য variants আট seed। Main statistical table-এ সরাসরি একই confidence framing ব্যবহার করা যাবে না।

10. **Target journal mismatch.** Audit notebook-এ target হিসেবে *Journal of Biomedical Informatics* লেখা আছে, কিন্তু বর্তমান research plan-এ user target *Informatics and Health*। Final paper format, word limit, section order এবং reference style target journal অনুযায়ী আলাদা করে নিশ্চিত করতে হবে।

## 9. Reproducibility checklist

- Exact MIMIC-CXR version, download date, access conditions এবং preprocessing commit/version সংরক্ষণ করুন।
- Dependency versions, GPU/CUDA/PyTorch/TorchXRayVision versions lock করুন।
- Patient-level split file এবং cleaned image manifest immutable artifact হিসেবে রাখুন।
- প্রতিটি seed-এর best checkpoint, final checkpoint, training log এবং test prediction save করুন।
- Test set কেবল একবার final analysis-এ ব্যবহার করুন; model selection validation-এ সীমাবদ্ধ রাখুন।
- Normalization correction, Noise loss correction, image-only checkpoint correction-এর পরে সব variants পুনরায় train করুন।
- Gray-square, text-only, image-only এবং shuffled-text controls রাখুন।
- Report-derived labels ব্যবহারের কারণে external/manual label validation বা report masking sensitivity analysis করুন।
- Main paper-এ mean ± SD, per-seed values, confidence interval, paired test, effect size এবং correction for multiple comparisons দিন।

## 10. Future paper-writing guidance from these notebooks

বর্তমান codebase থেকে paper-এর Methods কাঠামো হতে পারে: Data source and cohort → label construction → patient-level split → image preprocessing → report preprocessing → encoders → fusion variants → optimization → evaluation metrics → statistical analysis → reproducibility।

Results-এ প্রথমে cohort/accounting, তারপর baseline/control, তারপর four main variants, শেষে ablation ও error analysis দিন। Gray-square এবং text-only controls লুকিয়ে না রেখে স্পষ্টভাবে report করতে হবে, কারণ এগুলো image contribution-এর মূল interpretation বদলে দেয়।

Discussion-এ statistical non-significance, text-label circularity, gate stagnation এবং corrected-vs-original implementation-এর পার্থক্য আলাদা করে লিখতে হবে। Code output থেকে সরাসরি “Q1-ready” বা causal image contribution claim করা যাবে না যতক্ষণ critical issues resolve এবং experiments rerun না হয়।

## 11. Memory/status note

এই জ্ঞান বর্তমান conversation-এর working context-এ ব্যবহার করা হবে এবং এই Markdown ফাইলটি local persistent reference হিসেবে রাখা হলো। নতুন conversation-এ স্বয়ংক্রিয় স্থায়ী memory-এর নিশ্চয়তা নেই; তাই ভবিষ্যতে এই ফাইলটি reference হিসেবে খুলে নিলে একই analysis দ্রুত পুনরুদ্ধার করা যাবে।

## 12. Re-analysis of `medvision-q1-audit-final-FIXED-MERGE-v2.ipynb`

### What the replacement notebook adds

নতুন notebook-এর একটি patch cell ৪৭টি audit defect address করার দাবি করছে এবং নিচের সুবিধাগুলো যোগ করেছে:

- তিনটি upstream `all_results.pkl` merge: Part 10, Adaptive-CADQ training output এবং Part 9 output।
- পাঁচটি condition-এর জন্য ৪০টি unique result: baseline, LMH, Noise-Consistency, GACR-B এবং Adaptive-CADQ—প্রতিটিতে ৮টি seed।
- McNemar test, DeLong-style paired AUC test, Wilson 95% CI, bootstrap CI, Cohen's d, Shapiro precheck, BH-FDR adjustment, TOST equivalence এবং multi-seed permutation AUC।
- Per-class ROC CI band, row-normalised confusion matrix, strip-overlay boxplot, reliability diagram, circularity bar এবং gate-stagnation figure।
- Full CLAIM 2024 (27 items) এবং TRIPOD+AI (41 items) checklist।
- `q1_fix_results.json`, `q1_fix_compliance_checklist_full.json`, `requirements.txt` এবং `figures_fixed/` outputs।

### Updated five-variant results

Current merged output-এর mean ± sample SD:

| Variant | Macro-F1 | Pneumothorax F1 | ECE | Brier |
|---|---:|---:|---:|---:|
| Baseline | 0.9397 ± 0.0061 | 0.8810 ± 0.0174 | 0.0237 | 0.0522 |
| LMH | 0.9435 ± 0.0093 | 0.9003 ± 0.0191 | 0.0621 | 0.0685 |
| Noise-Consistency | 0.9346 ± 0.0075 | 0.8753 ± 0.0237 | 0.0347 | 0.0655 |
| GACR-B | 0.9417 ± 0.0059 | 0.8880 ± 0.0167 | 0.0245 | 0.0540 |
| Adaptive-CADQ | 0.9388 ± 0.0072 | 0.8772 ± 0.0175 | 0.0241 | 0.0527 |

Seed-level paired Macro-F1 outcomes remain mostly non-significant. Baseline বনাম GACR-B-এ paired t-test p=0.0441 হলেও exact Wilcoxon p=0.0547; ২৮টি Wilcoxon comparison-এ BH-FDR করার পরে significant result শূন্য। তাই GACR-B-কে “statistically superior” বলা যাবে না।

Patch-এর PNX one-vs-rest AUC output-এ LMH baseline-এর চেয়ে খারাপ দেখায় (Wilcoxon p=0.0078; BH-adjusted p=0.2188), কিন্তু এটিও multiplicity correction-এর পরে significant নয়।

### New audit limitations discovered during code review

1. **Pooled-seed dependence invalidates several tests.** DeLong, McNemar এবং multi-seed permutation AUC-এ আট seed-এর একই 455 test subject বারবার concatenate করা হয়েছে। এগুলো independent observations নয়; ফলে nominal sample size 8×455 এবং p-value অতিরিক্ত optimistic/invalid হতে পারে। সঠিক পদ্ধতি হবে per-seed statistic হিসাব করে seed-level paired analysis, অথবা clustered/bootstrap procedure।

2. **ECE/Brier are not actually populated in the fixed patch's metric table.** `metric_fns` upstream `test['ece']` এবং `test['brier']` খোঁজে; training results-এ এগুলো না থাকলে default 0.0 ফেরে। Output-এ সব ECE/Brier Wilcoxon p=1.0 এবং t-test `nan`, যা প্রমাণ করে এই patch-এর multi-metric ECE/Brier inference বাস্তবে শূন্য placeholder-এর উপর চলছে। ECE/Brier অবশ্যই `all_probs` ও `all_labels` থেকে প্রতি seed পুনরায় compute করে তারপর test করতে হবে।

3. **Shapiro precheck is applied to baseline values, not paired differences.** Paired t-test-এর normality assumption যাচাই করতে `variant − baseline` differences পরীক্ষা করা উচিত; শুধু baseline metric distribution নয়।

4. **Gate figure uses hard-coded alpha values.** Fixed patch-এ checkpoint থেকে প্রতি seed gate পুনরায় extract না করে `0.426270`, `0.499512`, `0.573242` values আট seed-এ copy করা হয়েছে। ফলে plotted standard deviation ও individual dots independent evidence নয়; gate-stagnation conclusion-এর জন্য raw checkpoint extraction দরকার।

5. **Patch/legacy execution order is confusing.** Notebook-এর patch cell নিজেকে “after original audit cell” বলে, কিন্তু cell order-এ patch original audit cell-এর আগে চলে। বর্তমান outputs সঠিকভাবে তৈরি হলেও future rerun-এ explicit execution order এবং dependency comments ঠিক করা উচিত।

6. **Merge is first-seen wins.** Duplicate key conflict হলে প্রথম file-এর value রেখে দেয়। Source order filesystem traversal-এর উপর নির্ভরশীল; provenance/hash manifest না থাকলে একই `variant_seed`-এর conflicting result silently select হতে পারে। Merge-এর আগে source priority এবং conflict report স্থিরভাবে সংজ্ঞায়িত করা দরকার।

7. **Claims remain partly post-hoc.** Checklist নিজেই স্বীকার করছে যে Adaptive-CADQ-এর ৮ seed extension post-hoc এবং pre-registration আংশিক। এটি Methods/Limitations-এ লিখতে হবে; “pre-registered eight-seed study” বলা যাবে না।

8. **No external validation or external SOTA.** নতুন audit reporting rigor বাড়িয়েছে, কিন্তু single MIMIC-CXR dataset, no external cohort, no K-fold/nested CV, no external SOTA baseline এবং MIMIC-pretrained image encoder overlap সমস্যাগুলো সমাধান করেনি। Notebook নিজেই এগুলো ৩২টি unresolved defect হিসেবে তালিকাভুক্ত করেছে।

9. **Original severe model issues remain unchanged.** XRV normalization mismatch, Noise-Consistency negative-KL sign, one-token attention degeneracy, CheXpert-label/report circularity এবং image-only best-checkpoint bug নতুন audit notebook fix করেনি। এগুলো training notebooks-এ fix করে complete rerun ছাড়া final paper conclusion নিরাপদ নয়।

### Updated interpretation

নতুন notebook আগের audit-এর তুলনায় reporting এবং figure generation অনেক উন্নত করেছে, বিশেষ করে GACR-B merge এবং transparent compliance checklist-এর কারণে। কিন্তু এটি মূল model-training validity issue ঠিক করেনি; কিছু নতুন statistical test-এ repeated-test-subject pooling এবং zero-placeholder ECE/Brier-এর মতো implementation সমস্যা আছে। তাই বর্তমান audit-কে “fixed reporting audit” বলা যায়, কিন্তু “fully validated final audit” বলা যাবে না।

সম্পূর্ণ artifact-level inventory, pickle/JSON structure এবং figure review আলাদা ফাইলে রাখা হয়েছে: [new_added_analysis.md](E:/Defense/Discuss/new_added_analysis.md)।

PDF guide এবং primary manuscript draft-এর deep review: [medvision_source_documents_analysis.md](E:/Defense/Discuss/medvision_source_documents_analysis.md)। `MedVision_Q1_Paper_FINAL_v9.docx`-কে writing base/high-priority reference হিসেবে ধরা হবে, কিন্তু factual claims executed code ও exported results দিয়ে যাচাই করে তবেই ব্যবহার করতে হবে।
