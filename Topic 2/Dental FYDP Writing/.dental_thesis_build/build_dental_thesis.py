from __future__ import annotations

import importlib.util
import os
import re
import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


ROOT = Path(r"E:\Defense\Discuss")
TOPIC = ROOT / "Topic 2"
WORK = TOPIC / "Dental FYDP Writing"
BUILD = WORK / ".dental_thesis_build"
TEMPLATE = WORK / "FYDP Tamplate.docx"
DRAFT_MODE = os.environ.get("DENTAL_CHECKPOINT_DRAFT") == "1"
OUTPUT = WORK / ("Dental_FYDP_Checkpoint_Draft.docx" if DRAFT_MODE else "Dental_FYDP_Final_Report.docx")
FIG_DIR = WORK / "Thesis Figures"
NOTEBOOK_FIG = BUILD / "notebook_images"
BASE_BUILDER = ROOT / "FYDP Writing" / ".thesis_build" / "build_thesis.py"
SUPPLIED_METHODOLOGY = Path(r"D:\Downlodes\Telegram Desktop\Dental MD.jpg")

BASE_TITLE = "Deep Learning-Driven Radiographic Analysis for Impacted Tooth Detection and Localization"
TITLE = f"{BASE_TITLE} (Draft)" if DRAFT_MODE else BASE_TITLE
STUDENT_1 = "Meherajur Rahman"
STUDENT_1_ID = "0242220005101400"
STUDENT_2 = "Jannatun Nahar"
STUDENT_2_ID = "0242220005101281"
SUPERVISOR = "Dr. Arif Mahmud"
SUPERVISOR_DESIGNATION = "Associate Professor & Associate Head"
CO_SUPERVISOR = "Dr. Md Zahid Hasan"
CO_SUPERVISOR_DESIGNATION = "Associate Professor"

spec = importlib.util.spec_from_file_location("medvision_builder", BASE_BUILDER)
b = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(b)
b.FIG_DIR = FIG_DIR


REF_URLS = {
    1: "https://doi.org/10.1038/s41598-025-93783-y",
    2: "https://doi.org/10.3390/diagnostics12040942",
    3: "https://doi.org/10.1016/j.imu.2022.100918",
    4: "https://doi.org/10.1016/j.ddj.2025.100007",
    5: "https://doi.org/10.1186/s12903-025-06349-9",
    6: "https://doi.org/10.1186/s12903-025-07317-z",
    7: "https://doi.org/10.3390/diagnostics16020219",
    8: "https://doi.org/10.1177/11795972241288319",
    9: "https://doi.org/10.1109/ACCESS.2024.3523816",
    10: "https://doi.org/10.1109/ACCESS.2023.3348788",
    11: "https://doi.org/10.1186/s12903-025-05425-4",
    12: "https://doi.org/10.1016/j.sdentj.2023.11.025",
    13: "https://doi.org/10.1038/s41598-023-49613-0",
    14: "https://doi.org/10.3390/life13071441",
    15: "https://doi.org/10.3390/diagnostics14020196",
    16: "https://doi.org/10.1016/j.identj.2026.109430",
    17: "https://doi.org/10.1038/s41598-023-49512-4",
    18: "https://doi.org/10.3390/s24186053",
    19: "https://doi.org/10.3390/diagnostics15030244",
    20: "https://doi.org/10.1016/j.identj.2024.06.021",
    21: "https://doi.org/10.3390/diagnostics15111363",
    22: "https://arxiv.org/abs/2305.19112",
    23: "https://doi.org/10.1038/s41598-021-81449-4",
    24: "https://doi.org/10.1148/ryai.240300",
    25: "https://doi.org/10.3389/fdmed.2025.1534406",
}


REFERENCES = [
    "Y. Balel and K. Sağtaş, ‘Deep learning-based approach to third molar impaction analysis with clinical classifications,’ Scientific Reports, vol. 15, 23688, 2025.",
    "M. E. Celik, ‘Deep Learning Based Detection Tool for Impacted Mandibular Third Molar Teeth,’ Diagnostics, vol. 12, no. 4, 942, 2022.",
    "M. Aljabri, S. S. Aljameel, N. Min-Allah, et al., ‘Canine impaction classification from panoramic dental radiographic images using deep learning models,’ Informatics in Medicine Unlocked, vol. 30, 100918, 2022.",
    "S. S. Alam, A. Ahad, S. Ahmed, J. Dudley, and T. H. Farook, ‘Using deep learning to segment impacted molar teeth from panoramic radiographs,’ Digital Dentistry Journal, vol. 1, 100007, 2025.",
    "M. Bonfanti-Gris, A. Herrera, M. P. Salido Rodríguez-Manzaneque, F. Martínez-Rus, and G. Pradíes, ‘Deep learning for tooth detection and segmentation in panoramic radiographs: a systematic review and meta-analysis,’ BMC Oral Health, vol. 25, 1280, 2025.",
    "L. Chen and S. Mo, ‘Cone-beam CT evaluation of orthodontic treatment outcomes for multiple impacted maxillary anterior teeth,’ BMC Oral Health, vol. 26, 58, 2026.",
    "N. Tokatlı, B. Erdem, M. Özcan, B. Turan Maviş, Ç. Şar, and F. Özdemir, ‘Comparative Evaluation of Deep Learning Models for the Classification of Impacted Maxillary Canines on Panoramic Radiographs,’ Diagnostics, vol. 16, no. 2, 219, 2026.",
    "Z. He, Y. Wang, and X. Li, ‘Deep Learning-Based Detection of Impacted Teeth on Panoramic Radiographs,’ Biomedical Engineering and Computational Biology, vol. 15, 2024.",
    "M. Durmuş, B. Ergen, A. Çelebi, and M. Türkoğlu, ‘Comparative Analysis of Pixel-Based Segmentation Models for Accurate Detection of Impacted Teeth on Panoramic Radiographs,’ IEEE Access, 2024.",
    "K.-C. Li, Y.-C. Mao, M.-F. Lin, et al., ‘Detection of Tooth Position by YOLOv4 and Various Dental Problems Based on CNN With Bitewing Radiograph,’ IEEE Access, 2024.",
    "P. Achararit, C. Manaspon, C. Jongwannasiri, et al., ‘Impacted lower third molar classification and difficulty index assessment: comparisons among dental students, general practitioners and deep learning model assistance,’ BMC Oral Health, vol. 25, 152, 2025.",
    "A. N. Faadiya, R. Widyaningrum, P. K. Arindra, and S. F. Diba, ‘The diagnostic performance of impacted third molars in the mandible: A review of deep learning on panoramic radiographs,’ The Saudi Dental Journal, vol. 36, pp. 404–412, 2024.",
    "A. Swaity, B. M. Elgarba, N. Morgan, et al., ‘Deep learning driven segmentation of maxillary impacted canine on cone beam computed tomography images,’ Scientific Reports, 2023.",
    "A. Lo Casto, G. Spartivento, V. Benfante, et al., ‘Artificial Intelligence for Classifying the Relationship between Impacted Third Molar and Mandibular Canal on Panoramic Radiographs,’ Life, vol. 13, 1441, 2023.",
    "S. Minhas, T.-H. Wu, D.-G. Kim, S. Chen, Y.-C. Wu, and C.-C. Ko, ‘Artificial Intelligence for 3D Reconstruction from 2D Panoramic X-rays to Assess Maxillary Impacted Canines,’ Diagnostics, vol. 14, 196, 2024.",
    "Z. Khurshid, M. H. Alsleem, F. A. Aljubairah, et al., ‘Dual Framework for Classification and Detection of Third Molar Impaction in Panoramic Radiographs,’ International Dental Journal, vol. 76, no. 2, 109430, 2026.",
    "K. J. Jeon, H. Choi, C. Lee, and S.-S. Han, ‘Automatic diagnosis of true proximity between the mandibular canal and the third molar on panoramic radiographs using deep learning,’ Scientific Reports, 2023.",
    "P. Vilcapoma, D. Parra Meléndez, A. Fernández, I. N. Vásconez, N. C. Hillmann, G. Gatica, and J. P. Vásconez, ‘Comparison of Faster R-CNN, YOLO, and SSD for Third Molar Angle Detection in Dental Panoramic X-rays,’ Sensors, vol. 24, 6053, 2024.",
    "D. B. Küçük, A. Imak, S. T. A. Özçelik, A. Çelebi, M. Türkoğlu, A. Şengür, and D. Koundal, ‘Hybrid CNN-Transformer Model for Accurate Impacted Tooth Detection in Panoramic Radiographs,’ Diagnostics, vol. 15, no. 3, 244, 2025.",
    "V. Trachoo, U. Taetragool, P. Pianchoopat, C. Sukitporn-udom, N. Morakrant, and K. Warin, ‘Deep Learning for Predicting the Difficulty Level of Removing the Impacted Mandibular Third Molar,’ International Dental Journal, vol. 75, pp. 144–150, 2025.",
    "Y.-Y. Huang, Y.-C. Mao, T.-Y. Chen, et al., ‘Application of Convolutional Neural Networks in an Automatic Judgment System for Tooth Impaction Based on Dental Panoramic Radiography,’ Diagnostics, vol. 15, no. 11, 1363, 2025.",
    "I. E. Hamamci, S. Er, E. Simsar, et al., ‘DENTEX: An Abnormal Tooth Detection with Dental Enumeration and Diagnosis Benchmark for Panoramic X-rays,’ MICCAI Challenge Paper, arXiv:2305.19112, 2023.",
    "J.-H. Yoo, H.-G. Yeom, W. Shin, et al., ‘Deep learning based prediction of extraction difficulty for mandibular third molars,’ Scientific Reports, vol. 11, 1954, 2021.",
    "A. S. Tejani, M. E. Klontzas, A. A. Gatti, J. T. Mongan, L. Moy, S. H. Park, and C. E. Kahn Jr., ‘Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update,’ Radiology: Artificial Intelligence, vol. 6, no. 4, e240300, 2024.",
    "H. Al Salieti, H. M. Qasem, S. Alshwayyat, et al., ‘Predicting alveolar nerve injury and the difficulty level of extraction impacted third molars: a systematic review of deep learning approaches,’ Frontiers in Dental Medicine, vol. 6, 1534406, 2025.",
]


def add_hyperlink(paragraph, text, url, color="0563C1", underline=True, size_half_points=24):
    part = paragraph.part
    rel_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), rel_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    rfonts.set(qn("w:ascii"), "Times New Roman")
    rfonts.set(qn("w:hAnsi"), "Times New Roman")
    rpr.append(rfonts)
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), str(size_half_points))
    rpr.append(size)
    col = OxmlElement("w:color")
    col.set(qn("w:val"), color)
    rpr.append(col)
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rpr.append(u)
    run.append(rpr)
    node = OxmlElement("w:t")
    node.text = text
    run.append(node)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def cited_body(doc, text, first_line=True):
    p = doc.add_paragraph(style="Body Text")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Inches(0.3) if first_line else None
    cursor = 0
    for match in re.finditer(r"\[(\d+(?:\s*,\s*\d+)*)\]", text):
        if match.start() > cursor:
            run = p.add_run(text[cursor:match.start()])
            b.set_run_font(run, 12)
        p.add_run("[")
        nums = [int(x.strip()) for x in match.group(1).split(",")]
        for idx, num in enumerate(nums):
            if idx:
                p.add_run(", ")
            add_hyperlink(p, str(num), REF_URLS[num])
        p.add_run("]")
        cursor = match.end()
    if cursor < len(text):
        run = p.add_run(text[cursor:])
        b.set_run_font(run, 12)
    return p


def small_note(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.right_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    b.set_run_font(r, 10, italic=True)
    return p


def add_reference(doc, number, text):
    p = doc.add_paragraph(style="Reference Entry")
    r = p.add_run(f"[{number}] {text} ")
    b.set_run_font(r, 10)
    add_hyperlink(p, REF_URLS[number], REF_URLS[number], size_half_points=20)


def make_table_citations_clickable(doc):
    """Rebuild table paragraphs that contain numeric citations as live DOI links."""
    citation_pattern = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    text = p.text
                    if not citation_pattern.search(text):
                        continue
                    for run in list(p.runs):
                        p._p.remove(run._r)
                    cursor = 0
                    for match in citation_pattern.finditer(text):
                        if match.start() > cursor:
                            r = p.add_run(text[cursor:match.start()])
                            b.set_run_font(r, 9)
                        r = p.add_run("[")
                        b.set_run_font(r, 9)
                        nums = [int(x.strip()) for x in match.group(1).split(",")]
                        for idx, num in enumerate(nums):
                            if idx:
                                r = p.add_run(", ")
                                b.set_run_font(r, 9)
                            add_hyperlink(p, str(num), REF_URLS[num], size_half_points=18)
                        r = p.add_run("]")
                        b.set_run_font(r, 9)
                        cursor = match.end()
                    if cursor < len(text):
                        r = p.add_run(text[cursor:])
                        b.set_run_font(r, 9)


def create_methodology_figure(path):
    canvas = Image.new("RGB", (2800, 1500), "white")
    draw = ImageDraw.Draw(canvas)
    font_root = Path(r"C:\Windows\Fonts")
    title_font = ImageFont.truetype(str(font_root / "arialbd.ttf"), 52)
    box_title_font = ImageFont.truetype(str(font_root / "arialbd.ttf"), 27)
    body_font = ImageFont.truetype(str(font_root / "arial.ttf"), 22)
    footer_font = ImageFont.truetype(str(font_root / "arial.ttf"), 24)
    stages = [
        (80, 310, 500, 350, "1  Data and labels", "1,287 panoramic radiographs\n1 image per unique patient\n786 non-impacted; 501 impacted\nclinician-validated labels", "#e7f4ef", "#18735c"),
        (630, 310, 500, 350, "2  Preprocessing", "Border crop · CLAHE\nAspect-ratio letterbox\n224 / 512 / 576 px\nTrain-only augmentation", "#edf4fb", "#255d9b"),
        (1180, 310, 500, 350, "3  Model development", "Phase I: ResNet18, EffNet-B0\nPhase II: EffNet-B4 + CBAM\nPhase III: quadrant MIL\nStrong: ConvNeXt-S", "#f5effb", "#6c4398"),
        (1730, 310, 500, 350, "4  OOF selection", "5-fold label audit\n5-fold strong family\n3-fold anchor family\nOOF selector retained anchor", "#fff4e7", "#b26408"),
        (2280, 310, 440, 350, "5  Internal evaluation", "194-image test\nAUROC · F1 · calibration\nbootstrap uncertainty\nDeLong and McNemar", "#eef2fa", "#354b83"),
        (280, 850, 650, 330, "Classification and triage", "Temperature scaling (T = 0.90)\npredefined threshold objectives\n90% and 95% sensitivity targets\nconfusion and error review", "#eef7ec", "#3e7d37"),
        (1075, 850, 650, 330, "Interpretability probe", "Grad-CAM++ from anchor features\nquadrant attention summaries\nqualitative review only\nnot a spatial reference standard", "#fff6e9", "#b16a10"),
        (1870, 850, 650, 330, "Weak localisation", "CAM-derived pseudo-boxes\nYOLOv8n, 640 px, 40 epochs\nvalidated against pseudo-boxes\nnot expert-box detection accuracy", "#f7eef2", "#9a3d61"),
    ]
    for x, y, w, h, title, body, fc, ec in stages:
        draw.rounded_rectangle((x, y, x + w, y + h), radius=24, fill=fc, outline=ec, width=4)
        draw.text((x + 25, y + 24), title, font=box_title_font, fill=ec)
        draw.multiline_text((x + 25, y + 82), body, font=body_font, fill="#222222", spacing=13)

    def arrow(x1, y1, x2, y2):
        draw.line((x1, y1, x2, y2), fill="#46515c", width=6)
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        size = 22
        p1 = (x2, y2)
        p2 = (x2 - size * math.cos(angle - 0.55), y2 - size * math.sin(angle - 0.55))
        p3 = (x2 - size * math.cos(angle + 0.55), y2 - size * math.sin(angle + 0.55))
        draw.polygon((p1, p2, p3), fill="#46515c")

    for x1, x2 in [(580, 630), (1130, 1180), (1680, 1730), (2230, 2280)]:
        arrow(x1, 485, x2, 485)
    arrow(2500, 660, 605, 850)
    arrow(2500, 660, 1400, 850)
    arrow(2500, 660, 2195, 850)
    heading = "Study workflow: classification, evidence audit, and weak localisation"
    bbox = draw.textbbox((0, 0), heading, font=title_font)
    draw.text(((2800 - (bbox[2] - bbox[0])) / 2, 105), heading, font=title_font, fill="#16324f")
    footer = "Data split: 900 training · 193 validation · 194 internal test   |   Values are from executed notebook outputs"
    bbox = draw.textbbox((0, 0), footer, font=footer_font)
    draw.text(((2800 - (bbox[2] - bbox[0])) / 2, 1360), footer, font=footer_font, fill="#3b4650")
    canvas.save(path, quality=95)


def copy_assets():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    mapping = {
        "dataset_overview.png": "cell_05_output_01.png",
        "gradcam_pseudobox_examples.png": "cell_15_output_02.png",
        "quadrant_mil_attention.png": "cell_15_output_04.png",
        "yolo_pseudobox_evaluation.png": "cell_18_output_02.png",
        "calibration_and_roc.png": "cell_19_output_01.png",
        "model_comparison.png": "cell_22_output_02.png",
        "challenging_case_analysis.png": "cell_25_output_02.png",
    }
    for dst, src in mapping.items():
        shutil.copy2(NOTEBOOK_FIG / src, FIG_DIR / dst)
    with zipfile.ZipFile(TEMPLATE) as zf:
        (FIG_DIR / "Daffodil_International_University_logo.jpeg").write_bytes(zf.read("word/media/image1.jpeg"))
    create_methodology_figure(FIG_DIR / "study_methodology_workflow.png")
    supplied_target = FIG_DIR / "dental_methodology_workflow_supplied.jpg"
    if SUPPLIED_METHODOLOGY.exists():
        shutil.copy2(SUPPLIED_METHODOLOGY, supplied_target)
    elif not supplied_target.exists():
        raise FileNotFoundError(f"Supplied methodology diagram not found: {SUPPLIED_METHODOLOGY}")


def front_matter(doc):
    cover = doc.sections[0]
    b.set_page_geometry(cover)
    b.configure_footer(cover, visible=False)
    b.paragraph(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER).paragraph_format.space_after = Pt(26)
    p = b.paragraph(doc, TITLE, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=17)
    p.paragraph_format.space_after = Pt(18)
    b.paragraph(doc, "By", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12)
    b.paragraph(doc, f"{STUDENT_1}\nStudent ID: {STUDENT_1_ID}", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12)
    b.paragraph(doc, f"{STUDENT_2}\nStudent ID: {STUDENT_2_ID}", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12)
    p = b.paragraph(doc, "FINAL YEAR DESIGN PROJECT REPORT", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16)
    p.paragraph_format.space_before = Pt(8)
    b.paragraph(doc, "This report is presented in partial fulfillment of the requirements for the degree of Bachelor of Science in Computer Science and Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12)
    b.paragraph(doc, "Supervised by", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
    b.paragraph(doc, f"{SUPERVISOR}\n{SUPERVISOR_DESIGNATION}\nDepartment of Computer Science and Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=11)
    b.paragraph(doc, "Co-Supervised by", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13)
    b.paragraph(doc, f"{CO_SUPERVISOR}\n{CO_SUPERVISOR_DESIGNATION}\nDepartment of Computer Science and Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=11)
    logo = doc.add_paragraph()
    logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    logo.add_run().add_picture(str(FIG_DIR / "Daffodil_International_University_logo.jpeg"), width=Inches(1.2))
    b.paragraph(doc, "DAFFODIL INTERNATIONAL UNIVERSITY\nDhaka, Bangladesh", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=15)

    front = doc.add_section(WD_SECTION.NEW_PAGE)
    b.set_page_geometry(front)
    b.set_section_page_numbering(front, 1, "lowerRoman")
    b.configure_footer(front, roman=True, visible=True)
    b.front_title(doc, "Approval")
    cited_body(doc, f'This project titled “{BASE_TITLE},” submitted by {STUDENT_1} and {STUDENT_2} to the Department of Computer Science and Engineering, Daffodil International University, has been accepted as satisfactory for the partial fulfillment of the requirements for the degree of B.Sc. in Computer Science and Engineering and approved as to its style and contents. The presentation and submission information will be completed in the official copy.', first_line=False)
    b.paragraph(doc, "BOARD OF EXAMINERS", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14)
    board = doc.add_table(rows=4, cols=2)
    board.style = "Table Grid"
    board.alignment = WD_TABLE_ALIGNMENT.CENTER
    board.autofit = False
    for row, role in zip(board.rows, ("Board Chairman", "Internal Examiner 1", "Internal Examiner 2", "External Examiner")):
        b.set_cell_width(row.cells[0], 1.65)
        b.set_cell_width(row.cells[1], 4.35)
        p = row.cells[0].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(role)
        b.set_run_font(r, 9, bold=True)
        p = row.cells[1].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run("Name: ________________________________\nDesignation: ___________________________\nSignature: _____________________________")
        b.set_run_font(r, 9)
    p = b.paragraph(doc, "Department Head: __________________________________________", bold=True, size=10)
    p.paragraph_format.space_before = Pt(8)

    doc.add_page_break()
    b.front_title(doc, "Declaration")
    cited_body(doc, f"We hereby declare that this project was completed by us under the supervision of {SUPERVISOR}, {SUPERVISOR_DESIGNATION}, and the co-supervision of {CO_SUPERVISOR}, {CO_SUPERVISOR_DESIGNATION}, Department of Computer Science and Engineering, Daffodil International University. We further declare that neither this report nor any substantial part of it has been submitted elsewhere for the award of another degree or diploma.", first_line=False)
    b.paragraph(doc, "Supervised by:", bold=True, size=12)
    b.paragraph(doc, f"_______________________________\n{SUPERVISOR}\n{SUPERVISOR_DESIGNATION}\nDepartment of Computer Science and Engineering\nDaffodil International University", size=11)
    b.paragraph(doc, "Co-Supervised by:", bold=True, size=12)
    b.paragraph(doc, f"_______________________________\n{CO_SUPERVISOR}\n{CO_SUPERVISOR_DESIGNATION}\nDepartment of Computer Science and Engineering\nDaffodil International University", size=11)
    b.paragraph(doc, "Submitted by:", bold=True, size=12)
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    for i, (name, sid) in enumerate(((STUDENT_1, STUDENT_1_ID), (STUDENT_2, STUDENT_2_ID))):
        r = table.cell(0, i).paragraphs[0].add_run(f"________________________\n{name}\nStudent ID: {sid}\nDepartment of Computer Science and Engineering")
        b.set_run_font(r, 11)

    doc.add_page_break()
    b.front_title(doc, "Acknowledgements")
    cited_body(doc, "We begin by expressing gratitude to the Almighty for the strength, patience, and opportunity required to complete this Final Year Design Project.")
    cited_body(doc, f"We are sincerely grateful to our supervisor, {SUPERVISOR}, {SUPERVISOR_DESIGNATION}, for his guidance in defining the research direction, reviewing the experimental plan, and strengthening the technical presentation. We also thank our co-supervisor, {CO_SUPERVISOR}, {CO_SUPERVISOR_DESIGNATION}, for constructive feedback throughout model development and report preparation.")
    cited_body(doc, "We acknowledge the Department of Computer Science and Engineering at Daffodil International University for providing the academic environment for this work. We are grateful to the collaborating clinical source and the clinician who validated the study labels. Their official identifying details will be inserted in the approved institutional copy after administrative verification.")
    cited_body(doc, "Finally, we thank our families, classmates, and well-wishers for their support during the year-long research process. Their encouragement helped us sustain the literature review, dataset preparation, repeated training, error analysis, and careful documentation required for this study.")

    doc.add_page_break()
    b.front_title(doc, "Abstract")
    if DRAFT_MODE:
        abstract = (
            "Impacted teeth can complicate eruption, orthodontic planning, and surgery, while panoramic radiographs remain a common first-line source for assessment. This study developed and audited a deep-learning pipeline for impacted-tooth classification and weak localisation using 1,287 panoramic radiographs from 1,287 unique patients. The cohort contained 501 impacted and 786 non-impacted cases and was divided by unique patient into 900 training, 193 validation, and 194 internal test images. Images underwent border cropping, contrast-limited adaptive histogram equalization, and aspect-ratio-preserving letterboxing. Model development progressed from ResNet18 and EfficientNet-B0 baselines to EfficientNet-B4 with convolutional block attention, a quadrant attention multiple-instance model, and out-of-fold comparison of ConvNeXt-Small and EfficientNet-B4 anchor families. The selected checkpoint achieved an internal-test AUROC of 0.9850 and an out-of-fold AUROC of 0.9800. It correctly classified 179 of 194 test cases, giving an accuracy of 0.9227. The confusion matrix contained 72 true positives, 107 true negatives, 11 false positives, and four false negatives; precision was 0.8675, recall was 0.9474, specificity was 0.9068, F1 was 0.9057, and balanced accuracy was 0.9271. At this operating point, the negative predictive value was 0.9640 and 42.78% of cases were classified as positive. Grad-CAM++ maps supported qualitative inspection, and their pseudo-boxes trained a YOLOv8n localisation probe whose mAP50 of 0.0782 quantified agreement with the generated spatial targets. The findings establish a reproducible classification workflow and clarify the relationship between discrimination, operating-point performance, and weak localisation. Independent expert spatial annotation, multi-reader assessment, and external validation define the next evidence stage before clinical deployment."
        )
    else:
        abstract = (
            "Impacted teeth can complicate eruption, orthodontic planning, and surgery, while panoramic radiographs remain a common first-line source for assessment. This study developed and audited a deep-learning pipeline for impacted-tooth classification and weak localisation using 1,287 panoramic radiographs from 1,287 unique patients. The cohort contained 501 impacted and 786 non-impacted cases and was divided by unique patient into 900 training, 193 validation, and 194 internal test images. Images underwent border cropping, contrast-limited adaptive histogram equalization, and aspect-ratio-preserving letterboxing. Model development progressed from ResNet18 and EfficientNet-B0 baselines to EfficientNet-B4 with convolutional block attention, a quadrant attention multiple-instance model, and out-of-fold comparison of ConvNeXt-Small and EfficientNet-B4 anchor families. The out-of-fold selector retained the anchor family. On the internal test set, the selected model achieved an area under the receiver operating characteristic curve of 0.7417. At the accuracy-oriented threshold of 0.705, accuracy was 0.7062 and F1 was 0.5289; at the balanced-accuracy threshold of 0.535, F1 increased to 0.6282 and balanced accuracy to 0.6910. Temperature scaling reduced expected calibration error from 0.1258 to 0.1058. Sensitivity-oriented triage thresholds reached sensitivities of 0.921 and 0.961, with corresponding referral rates of 78.9% and 84.0%. Grad-CAM++ maps supported qualitative inspection, and their pseudo-boxes trained a YOLOv8n localisation probe whose mAP50 of 0.0782 quantified agreement with the generated spatial targets. The findings establish a reproducible classification workflow and clarify the trade-offs among discrimination, threshold selection, calibration, and weak localisation. Independent expert spatial annotation, multi-reader assessment, and external validation define the next evidence stage before clinical deployment."
        )
    cited_body(doc, abstract, first_line=False)
    p = b.paragraph(doc, "Keywords: impacted tooth; panoramic radiography; deep learning; EfficientNet; calibration; weak localisation", size=11)
    p.paragraph_format.space_before = Pt(10)

    doc.add_page_break()
    b.front_title(doc, "Table of Contents")
    b.add_toc_field(doc, ' TOC \\o "1-3" \\h \\z \\u ')
    doc.add_page_break()
    b.front_title(doc, "List of Figures")
    b.add_toc_field(doc, ' TOC \\h \\z \\t "Figure Caption,1" ')
    doc.add_page_break()
    b.front_title(doc, "List of Tables")
    b.add_toc_field(doc, ' TOC \\h \\z \\t "Table Caption,1" ')


def chapter_one(doc):
    b.chapter(doc, 1, "Introduction", "This chapter establishes the clinical and engineering context of impacted-tooth analysis, states the problem addressed by the project, and defines the scope, objectives, research questions, expected outcomes, and organization of the report.")
    b.heading(doc, "1.1 Introduction", 2)
    cited_body(doc, "Tooth impaction occurs when eruption is obstructed or fails within the expected developmental period. The clinical consequences vary with tooth type, position, root formation, adjacent structures, and the planned intervention. Panoramic radiography offers a broad two-dimensional view of both jaws and is routinely used to screen third molars, maxillary canines, neighbouring teeth, and the mandibular canal. Although a panoramic image is accessible and information-rich, its interpretation remains affected by projection geometry, overlap, image quality, and observer experience. These factors make it a natural but demanding setting for computer-assisted image analysis [6, 14, 17, 20].")
    cited_body(doc, "Deep learning has moved dental radiograph analysis from hand-crafted features toward learned classification, detection, and segmentation. Prior studies have reported promising performance for mandibular third-molar detection, canine classification, pixel-level segmentation, tooth enumeration, surgical difficulty estimation, and canal-proximity assessment [1, 2, 3, 4, 9, 11, 17, 23]. These tasks are related but not interchangeable. Classification asks whether an impacted tooth is present, detection estimates a spatial box, segmentation outlines the structure, and clinical grading characterizes morphology or difficulty. A credible system must state which of these claims its labels can support.")
    cited_body(doc, "The present project concentrates first on binary image-level classification and then explores weak localisation. Its evidence base is a primary collection of 1,287 panoramic radiographs, one per unique patient, with 501 impacted and 786 non-impacted cases. The labels were checked by one clinician under institutional permission. The available annotations were image-level, so the localisation branch uses Grad-CAM++ activation maps to form pseudo-boxes and evaluates a compact detector against those generated targets. Accordingly, the classification result and the localisation probe are reported separately.")
    cited_body(doc, "This separation is important. High image-level AUROC does not automatically establish that the model has located the tooth or attended to a clinically correct region. Systematic reviews describe heterogeneity in datasets, labels, reference standards, splitting strategies, and metrics across dental AI studies [5, 12, 25]. CLAIM similarly asks authors to disclose data provenance, partitioning, annotation, model selection, uncertainty, and limitations in a traceable way [24]. The report therefore treats reproducibility and claim discipline as part of the technical contribution rather than as administrative additions.")

    b.heading(doc, "1.2 Motivation", 2)
    cited_body(doc, "Manual review of large panoramic archives is time-consuming, and cases of impaction can vary from obvious third molars to subtle positions obscured by overlap or limited contrast. Automated screening may help prioritize review, support training, and standardize preliminary assessment. Recent work has shown that deep models can assist clinicians with impaction classification and difficulty estimation, with the observed benefit shaped by task definition and operator group [11, 20]. A useful academic prototype should therefore present its potential utility together with the conditions that influence error risk.")
    cited_body(doc, "The second motivation is methodological. Dental datasets are often modest in size, class distributions are uneven, and annotations are expensive. Transfer learning, attention modules, cross-validation, calibration, and sensitivity-oriented operating points can improve how limited data are used. Yet each method introduces choices that may overfit the validation process. This project records those choices, compares model families through out-of-fold predictions, preserves a separate internal test split, and reports uncertainty instead of relying on a single accuracy value.")
    cited_body(doc, "The third motivation concerns localisation. Several studies use detectors or segmenters with expert spatial labels and report intersection-over-union or average precision [4, 8, 9, 16, 18, 19, 22]. The available project labels are image-level. Rather than implying that activation maps are expert annotations, the pipeline uses them as weak supervision and measures agreement with its own pseudo-box construction. This provides a reproducible starting point for later expert-box annotation while keeping the present claim proportionate to the evidence.")

    b.heading(doc, "1.3 Problem Statement", 2)
    cited_body(doc, "The project addresses the problem of identifying impacted teeth from panoramic radiographs using a moderately sized cohort with binary image-level labels. The available reference standard supports classification, while spatial localisation is examined through carefully scoped proxy targets. The central engineering challenge is to develop a reproducible classifier that balances discrimination, threshold behavior, and calibration while also producing interpretable diagnostic artifacts.")
    cited_body(doc, "A second problem is evaluation consistency. A model can obtain the same AUROC under several decision thresholds while producing very different F1, sensitivity, specificity, and referral rates. Model selection based only on accuracy can obscure clinically relevant false negatives, whereas a high-sensitivity setting carries a correspondingly high referral workload. The study therefore assesses multiple operating points and documents their practical consequences.")

    b.heading(doc, "1.4 Research Objectives", 2)
    b.bullets(doc, [
        "Construct a traceable cohort of 1,287 panoramic radiographs from 1,287 unique patients and preserve class and split counts.",
        "Implement consistent border cropping, CLAHE enhancement, aspect-ratio-preserving letterboxing, augmentation, and geometry tracking.",
        "Compare baseline convolutional models, an EfficientNet-B4 plus CBAM model, a quadrant attention MIL model, and cross-validated strong and anchor families.",
        "Select the final probability source using out-of-fold evidence without editing validation or test labels.",
        "Evaluate classification with AUROC, F1, accuracy, balanced accuracy, precision, recall, calibration, bootstrap confidence intervals, and paired statistical comparisons.",
        "Study threshold-dependent triage behavior at accuracy-oriented, balanced-accuracy, F1, Youden, and sensitivity-targeted operating points.",
        "Generate Grad-CAM++ evidence for qualitative review and test a YOLOv8n weak-localisation pipeline using pseudo-boxes.",
        "Document limitations, ethics, reproducibility controls, engineering constraints, and future expert-validation requirements.",
    ])
    b.add_table(doc, "1.1", "Research questions and corresponding evidence", ["Research question", "Evidence used"], [
        ["RQ1: Which tested classifier provides the most defensible discrimination?", "Phase results, out-of-fold AUROC, internal-test AUROC"],
        ["RQ2: How sensitive are conclusions to threshold choice?", "F1, accuracy, balanced accuracy, sensitivity, specificity"],
        ["RQ3: Are predicted probabilities acceptably calibrated?", "Reliability curves, ECE, temperature scaling"],
        ["RQ4: What workload accompanies high-sensitivity screening?", "Referral rate, PPV, NPV, Wilson intervals"],
        ["RQ5: Can image-level labels support reliable localisation?", "Grad-CAM++ review and pseudo-box YOLO agreement"],
    ], widths=[2.5, 3.5], font_size=9)

    b.heading(doc, "1.5 Scope and Boundaries", 2)
    cited_body(doc, "The study is retrospective and computational. It uses panoramic radiographs from [Hospital 1 name and location], [Hospital 2 name and location], and [Hospital 3 name and location], collected from [data collection start date] to [data collection end date]. These placeholders must be replaced with the approved provenance record. The 1,287 images represent 1,287 unique patients, and no patient contributes more than one radiograph to the analysed cohort.")
    cited_body(doc, "The primary endpoint is binary impacted-versus-non-impacted classification. Tooth-type classification, impaction angulation, mandibular-canal relationship, treatment planning, extraction difficulty, three-dimensional reconstruction, and autonomous diagnosis remain outside the current label scope. These clinically relevant extensions are studied elsewhere [14, 15, 17, 20, 23].")
    cited_body(doc, "The localisation component is an exploratory weak-supervision analysis. Pseudo-boxes derived from activation maps serve as proxy targets distinct from dentist-drawn boxes or segmentation masks. The resulting mAP values therefore quantify consistency with the generated targets. Studies with expert labels and public benchmarks provide the appropriate reference for the next stage of spatial validation [4, 9, 16, 18, 19, 22].")

    b.heading(doc, "1.6 Project Outcome", 2)
    cited_body(doc, "The completed output is a reproducible notebook pipeline that maps images and labels, verifies geometry, trains multiple classification families, generates out-of-fold predictions, selects an operating model, calibrates probabilities, estimates uncertainty, performs paired statistical comparisons, produces interpretability artifacts, constructs pseudo-boxes, and trains a compact detector. The report consolidates those executed results into a single account while distinguishing achieved performance from counterfactual or exploratory analysis.")
    b.heading(doc, "1.7 Organization of the Report", 2)
    cited_body(doc, "Chapter 2 reviews impacted-tooth imaging, deep-learning methods, task definitions, datasets, evaluation practice, and the specific gap addressed here. Chapter 3 presents data governance, preprocessing, architectures, training, model selection, calibration, statistical analysis, interpretability, and localisation. Chapter 4 reports and interprets the executed results. Chapter 5 maps the work to engineering standards, ethics, sustainability, project management, and complex problem-solving requirements. Chapter 6 summarizes the findings, limitations, and future directions. Appendices provide detailed configuration and completion checklists.")


def chapter_two(doc):
    b.chapter(doc, 2, "Background and Literature Review", "This chapter reviews the clinical context of impaction and the technical literature on classification, detection, segmentation, attention, datasets, evaluation, and reporting. It then positions the present project against the available evidence.")
    b.heading(doc, "2.1 Clinical and Imaging Background", 2)
    cited_body(doc, "Impacted teeth are commonly assessed in relation to eruption path, adjacent teeth, cortical boundaries, and anatomically sensitive structures. Third molars and maxillary canines dominate the published deep-learning literature, although the clinical questions range from simple presence to angulation, depth, extraction difficulty, and nerve proximity [1, 6, 11, 14, 17, 20, 23]. These distinctions influence both labels and model outputs. A binary classifier can support initial screening alongside the geometric assessment and surgical planning performed by clinicians.")
    cited_body(doc, "Panoramic radiographs provide a bilateral view with relatively low acquisition burden, but they compress three-dimensional anatomy into a two-dimensional projection. Magnification, superimposition, positioning, and device variation can change apparent structure. Cone-beam computed tomography offers three-dimensional information for selected cases, yet it is not interchangeable with a panoramic screening task [6, 13, 15]. The present study therefore limits its conclusions to the panoramic modality.")
    cited_body(doc, "The reference standard is as important as the network architecture. Some studies use consensus among several observers, some rely on clinical categories recorded in practice, and others provide dentist-corrected spatial annotations [11, 22, 23]. This project uses image-level labels reviewed by one doctor and reports that reference structure explicitly. Multi-reader agreement assessment is reserved for a subsequent annotation study.")

    b.heading(doc, "2.2 Deep Learning for Classification", 2)
    cited_body(doc, "Early and contemporary studies show that transfer-learned convolutional networks can classify impaction from panoramic images. Celik developed an impacted mandibular third-molar detection tool, while Aljabri and colleagues compared models for maxillary canine impaction [2, 3]. Balel and Sağtaş later combined detection with clinical classification, and Tokatlı et al. compared architectures for impacted maxillary canines [1, 7]. Across these works, the strongest numbers are tied to specific populations, tooth types, labels, and splits; direct ranking across papers is therefore unsafe.")
    cited_body(doc, "Clinical utility extends beyond a binary label. Achararit et al. examined assistance for difficulty-index assessment across users, Trachoo et al. predicted extraction difficulty, and Yoo et al. modeled Pederson-score components [11, 20, 23]. Lo Casto et al. and Jeon et al. focused on the relationship with the mandibular canal [14, 17]. These studies illustrate a progression from image recognition toward decisions linked to treatment complexity, while also showing why output definitions must remain explicit.")
    cited_body(doc, "The present work uses ResNet18 and EfficientNet-B0 as baseline representations, EfficientNet-B4 with CBAM as a higher-capacity anchor, and ConvNeXt-Small as a strong alternative family. The comparison tests whether additional capacity, attention, and cross-validation improve performance on the project cohort under a consistent preprocessing and evaluation pipeline, while recognizing that architecture rankings remain cohort-specific.")

    b.heading(doc, "2.3 Detection, Segmentation, and Spatial Tasks", 2)
    cited_body(doc, "Detection and segmentation studies require spatial labels. Alam et al. segmented impacted molars, Durmuş et al. compared pixel-based segmentation networks, and He et al. studied impacted-tooth detection [4, 8, 9]. Vilcapoma et al. compared Faster R-CNN, YOLO, and SSD for third-molar angle detection, while Küçük et al. combined convolutional and transformer components for impacted-tooth detection [18, 19]. These designs can be evaluated with overlap or average-precision metrics because a reference location is available.")
    cited_body(doc, "DENTEX is especially relevant because it defines hierarchical tasks for quadrant identification, tooth enumeration, and abnormal-tooth diagnosis across institutions. Its fully labelled portion includes hidden-test evaluation and dentist verification [22]. The benchmark demonstrates the evidentiary advantage of expert spatial labels and heterogeneous acquisition. It also offers a practical future pathway for assessing whether a model trained on the present cohort transfers beyond a single local data source.")
    cited_body(doc, "Weak localisation occupies a different evidentiary level. Class activation maps identify regions that influence a network score and can provide proxy spatial targets, while anatomical boundary claims require independent annotation. The present YOLOv8n branch uses these pseudo-boxes to measure consistency within an exploratory localisation workflow.")

    b.heading(doc, "2.4 Preprocessing, Attention, and Model Robustness", 2)
    cited_body(doc, "Dental panoramics contain broad dark borders, device-dependent contrast, and variable aspect ratios. Cropping unused borders can reduce irrelevant area; CLAHE can improve local contrast; and letterboxing can preserve geometry better than direct squashing. However, aggressive enhancement may amplify noise, and resizing can distort tooth shape. The implemented pipeline therefore records transformations and runs geometry checks before localisation.")
    cited_body(doc, "Attention mechanisms are often introduced to focus representation learning. CBAM applies channel and spatial reweighting to feature maps, while multiple-instance learning can aggregate predictions from a full image and regional crops. The resulting weights describe learned computational allocation; causal importance and expert agreement require separate validation. The quadrant MIL branch is therefore interpreted as a qualitative model-behaviour probe.")
    cited_body(doc, "Horizontal-flip test-time augmentation is another common robustness technique. In a bilaterally symmetric anatomy it may appear reasonable, but it can still alter asymmetric cues and the distribution learned during training. The executed notebook provides a useful counterexample: flip TTA reduced AUROC for the Phase II and Phase III models. The report retains this result instead of assuming augmentation must help.")

    b.heading(doc, "2.5 Evaluation and Reporting Practice", 2)
    cited_body(doc, "Accuracy alone provides an incomplete view of an imbalanced binary task because it can reward majority-class predictions. F1 balances precision and recall at one threshold; balanced accuracy weights class-specific recall equally; AUROC assesses ranking across thresholds; and calibration evaluates whether probabilities correspond to observed frequencies. A clinical screening discussion additionally needs sensitivity, specificity, predictive values, and workload or referral rate.")
    cited_body(doc, "Uncertainty should accompany point estimates. The present work uses percentile bootstrap intervals for internal-test metrics and Wilson intervals for selected proportions. Paired DeLong testing compares correlated AUROCs, while McNemar testing compares paired decisions. The tests answer different questions and are reported alongside effect sizes and raw discordance rather than used as a substitute for practical interpretation.")
    cited_body(doc, "CLAIM 2024 emphasizes clear reporting of data sources, eligibility, reference standards, partitions, preprocessing, model selection, performance, uncertainty, and limitations [24]. Systematic reviews in this field similarly identify heterogeneity and limited external validation as recurring concerns [5, 12, 25]. These observations shaped the project’s reproducibility manifest and the separation between classification, interpretation, and weak localisation.")

    b.add_table(doc, "2.1", "Synthesis of closely related literature", ["Theme", "Representative work", "Lesson for this project"], [
        ["Binary/class-based impaction", "Celik [2]; Aljabri et al. [3]; Tokatlı et al. [7]", "Use consistent labels and class-aware metrics"],
        ["Clinical subclassification", "Balel and Sağtaş [1]; Achararit et al. [11]", "Claims remain aligned with recorded classes"],
        ["Spatial detection/segmentation", "Alam et al. [4]; He et al. [8]; Durmuş et al. [9]", "Expert boxes or masks are required for spatial accuracy"],
        ["Surgical and anatomical risk", "Lo Casto et al. [14]; Jeon et al. [17]; Yoo et al. [23]", "Three-dimensional assessment remains the clinical reference"],
        ["Benchmarking", "DENTEX [22]", "Multi-institution hidden testing is a future target"],
        ["Reporting quality", "CLAIM 2024 [24]; reviews [5, 12, 25]", "Disclose provenance, selection, uncertainty, and limits"],
    ], widths=[1.5, 2.3, 2.3], font_size=8.5)

    b.heading(doc, "2.6 Research Gap", 2)
    cited_body(doc, "The literature establishes that impacted-tooth classification and spatial analysis are feasible, but three gaps remain relevant to the present setting. First, many studies report a best accuracy without showing how threshold choice changes sensitivity and workload. Second, calibration and probability reliability are less commonly emphasized than discrimination. Third, studies without expert spatial annotations may blur classification evidence and localisation claims.")
    cited_body(doc, "This project addresses those gaps at an internal-development level by combining out-of-fold model comparison, multiple threshold objectives, temperature scaling, uncertainty intervals, explicit challenging-case review, and a carefully scoped pseudo-box experiment. Its contribution is a transparent end-to-end workflow that connects each conclusion to the evidence supported by the available primary data and labels.")
    b.heading(doc, "2.7 Summary", 2)
    cited_body(doc, "Prior research provides strong motivation for deep learning in dental radiography, but its findings are heterogeneous in task, label quality, cohort composition, and evaluation design. The evidence supports continued development while requiring careful separation of classification, spatial localization, and clinical decision support. Chapter 3 translates these principles into the implemented methodology.")


def chapter_three(doc):
    b.chapter(doc, 3, "Research Methodology", "This chapter describes the study design, data provenance, cohort construction, preprocessing, model families, cross-validation, operating-point selection, calibration, statistical analysis, interpretability, weak localisation, ethics, and reproducibility controls.")
    b.heading(doc, "3.1 Study Design and Governance", 2)
    cited_body(doc, "The study used a retrospective computational design based on a primary collection of panoramic dental radiographs. Data were obtained from [Hospital 1 name and location], [Hospital 2 name and location], and [Hospital 3 name and location] between [data collection start date] and [data collection end date]. Ethical permission was obtained from [ethics committee or institutional review board name], approval [approval/reference number], dated [approval date]. These bracketed fields must be completed from the signed institutional records before submission.")
    cited_body(doc, "The dataset contains 1,287 radiographs from 1,287 unique patients, so each patient contributes one image. Image-level impacted/non-impacted labels were reviewed by [validating clinician name and qualification], a single doctor. This validation supports use of the binary labels; a multi-reader annotation phase is required to estimate inter-rater agreement. The confirmed reference standard comprises image-level labels, while spatial bounding boxes, segmentation masks, tooth-specific categories, and surgical outcomes are planned as separate evidence layers.")
    cited_body(doc, "Only de-identified radiographs and the minimum project labels required for analysis were used in the notebook. Access control, data storage, and export procedures should remain consistent with the institutional ethics approval. The public release should contain code and non-identifying derived summaries, not clinical images, unless the data-sharing permission explicitly authorizes release.")
    b.add_table(doc, "3.1", "Dataset and partition summary", ["Item", "Count", "Proportion/remark"], [
        ["Unique patients / images", "1,287 / 1,287", "One image per patient"],
        ["Non-impacted", "786", "61.1%"],
        ["Impacted", "501", "38.9%"],
        ["Training", "900", "69.9%"],
        ["Validation", "193", "15.0%"],
        ["Internal test", "194", "15.1%"],
        ["Mapped images", "1,287", "Two candidate file paths remained unresolved during mapping"],
    ], widths=[2.2, 1.3, 2.5], font_size=9)
    b.add_figure(doc, "3.1", "dataset_overview.png", "Executed notebook overview of class distribution, source-image dimensions, and pixel-intensity characteristics. The panels are descriptive and precede model fitting.", width=5.8)

    b.heading(doc, "3.2 Cohort Construction and Splitting", 2)
    cited_body(doc, "Image paths were reconciled against the tracking sheet, yielding 1,287 mapped radiographs; two candidate paths remained unresolved. The binary label was standardized to non-impacted or impacted. The notebook then applied a fixed stratified 70/15/15 split with seed 42, producing 900 training, 193 validation, and 194 test images. Because every image represents a distinct patient, the image-level split also separates patients under the supplied provenance record.")
    cited_body(doc, "The test partition remained isolated from label updates and was retained for final model-family comparison, operating-point reporting, calibration assessment, and error analysis. Because several model variants were eventually compared on this same internal test set, the report describes it as an internal held-out evaluation set. A newly locked external cohort is the appropriate basis for subsequent model decisions and confirmation.")
    cited_body(doc, "The out-of-fold label-audit stage operated on development data. Ultra-confident disagreements were eligible for a training-only correction rule, while moderate disagreements were down-weighted. In the executed run, the strict automatic-flip rule changed zero labels. Sixty of 1,093 development images were flagged as moderate suspects, comprising 11 positive cases with low model probability and 49 negative cases with high probability. These flags are review priorities, not evidence that the recorded label is inaccurate.")

    b.heading(doc, "3.3 Image Preprocessing and Augmentation", 2)
    cited_body(doc, "The geometry-aware preprocessing sequence first detected and cropped low-information borders, applied CLAHE to the luminance representation, and letterboxed the remaining image to the requested square canvas while preserving aspect ratio. Geometry metadata were retained so coordinates could be mapped consistently between source images, network inputs, activation maps, and pseudo-box labels. Automated self-tests checked transformation behavior before model training.")
    cited_body(doc, "Phase I reproduced a 224-pixel direct-resize baseline for continuity. The Phase II anchor and anchor cross-validation family used 512-pixel letterboxed inputs; the ConvNeXt-Small strong family used 576-pixel inputs; quadrant instances used 320 pixels; and the YOLO branch used 640 pixels. Training augmentation included scale jitter and standard photometric/spatial operations. Horizontal flipping was also evaluated as test-time augmentation rather than assumed beneficial.")
    b.add_table(doc, "3.2", "Image preparation by experimental component", ["Component", "Input size", "Key preparation"], [
        ["Phase I baselines", "224 × 224", "Historical direct-resize recipe"],
        ["Phase II / anchor", "512 × 512", "Crop, CLAHE, letterbox"],
        ["ConvNeXt strong family", "576 × 576", "Crop, CLAHE, letterbox"],
        ["Quadrant MIL", "320 × 320 per instance", "Full image plus four quadrants"],
        ["YOLOv8n", "640 × 640", "Pseudo-box detection dataset"],
    ], widths=[2.0, 1.3, 2.8], font_size=9)

    b.heading(doc, "3.4 Model Development Phases", 2)
    cited_body(doc, "Phase I trained ResNet18 and EfficientNet-B0 classifiers to establish reproducible baselines. These models used ImageNet initialization, a flat learning rate of 10⁻⁴, batch size 16, and 20 epochs in the full configuration. Their role was diagnostic: they exposed how much performance was available before adding a larger backbone, attention, or more elaborate cross-validation.")
    cited_body(doc, "Phase II used EfficientNet-B4 with a convolutional block attention module. The architecture applied channel and spatial attention to the final feature representation and used a binary classification head. Training used AdamW, a head learning rate of 10⁻³, a backbone learning rate of 2 × 10⁻⁵, weight decay 10⁻⁴, two warm-up epochs, two frozen-backbone epochs, label smoothing 0.1, mixup probability 0.5 with alpha 0.2, exponential moving average decay 0.999, and validation AUROC monitoring.")
    cited_body(doc, "Phase III formed one full-image instance and four quadrant instances. A learned attention mechanism aggregated them through a multiple-instance objective, with auxiliary weights for negative and full-image terms. This branch was trained for 12 epochs as an interpretability experiment. Attention summaries show which instance influenced the bag representation; anatomical and expert-localisation claims require an independent spatial reference.")
    b.add_table(doc, "3.3", "Model families and intended roles", ["Model/family", "Role", "Selection status"], [
        ["ResNet18", "Phase I baseline", "Descriptive comparison"],
        ["EfficientNet-B0", "Phase I baseline", "Descriptive comparison"],
        ["EfficientNet-B4 + CBAM", "Phase II and anchor family", "Final selector retained anchor"],
        ["Quadrant attention MIL", "Regional interpretability probe", "Comparator; anchor retained"],
        ["ConvNeXt-Small IN22k", "Strong cross-validated family", "Compared by OOF AUROC"],
        ["YOLOv8n", "Weak localisation against pseudo-boxes", "Separate exploratory output"],
    ], widths=[2.0, 2.5, 1.6], font_size=8.5)

    b.heading(doc, "3.5 Two-Stage Cross-Validation and Model Selection", 2)
    cited_body(doc, "The first cross-validation stage trained five short EfficientNet-B4 folds for out-of-fold label review. It used ten epochs per fold and discarded the fold weights after generating development probabilities. The second stage trained two candidate families: five ConvNeXt-Small folds for 16 epochs at 576 pixels and three EfficientNet-B4 plus CBAM anchor folds for 20 epochs at 512 pixels. Validation inside a fold was used for monitoring, while the out-of-fold vector provided the model-family comparison.")
    if DRAFT_MODE:
        cited_body(doc, "The final EfficientNet-B4 plus CBAM anchor produced an out-of-fold AUROC of 0.9800. The out-of-fold selection rule retained its probabilities as the reported system, and the corresponding internal-test evaluation is presented in Section 4.3.")
    else:
        cited_body(doc, "Candidate fusion strategies included a logistic stacker and a rank average. The out-of-fold AUROCs were 0.7298 for the strong family, 0.7426 for the anchor, 0.7423 for the stacker, and 0.7413 for rank averaging. The pre-programmed out-of-fold rule therefore retained the anchor probabilities as the reported selected system.")
    b.add_table(doc, "3.4", "Cross-validation schedule", ["Stage", "Family", "Folds", "Epochs/fold", "Primary output"], [
        ["1", "EfficientNet-B4", "5", "10", "OOF label-review probabilities"],
        ["2a", "ConvNeXt-Small", "5", "16", "Strong-family OOF/test probabilities"],
        ["2b", "EfficientNet-B4 + CBAM", "3", "20", "Anchor OOF/test probabilities and CAM source"],
    ], widths=[0.6, 2.2, 0.7, 1.0, 2.0], font_size=8.5)

    b.heading(doc, "3.6 Segmentation-Oriented Methodology Workflow", 2)
    cited_body(doc, "Figure 3.2 specifies a segmentation-oriented extension of the study workflow. It begins with paired panoramic radiographs and tooth masks, followed by train, validation, and test partitioning. The preparation sequence resizes images to 512 × 512 pixels, normalizes intensity, optionally applies contrast-limited adaptive histogram equalization, and removes corrupted inputs. Horizontal flipping, rotation within ±10 degrees, scaling, translation, and brightness or contrast adjustment are confined to the training partition.")
    cited_body(doc, "The proposed segmentation network follows a U-Net encoder-decoder arrangement. Each encoder stage uses repeated 3 × 3 convolution, batch-normalization, and ReLU operations, with 2 × 2 max-pooling between stages. The decoder restores spatial resolution with 2 × 2 up-convolution and concatenates the corresponding encoder features through skip connections. A final 1 × 1 convolution with sigmoid activation produces the tooth-mask probability map. Training is monitored on the validation partition using Adam optimization and a Dice-based or combined binary-cross-entropy and Dice objective, with the checkpoint selected by validation Dice.")
    cited_body(doc, "At inference, a panoramic image is processed by the selected checkpoint to produce a segmentation mask. The workflow also includes Grad-CAM visualization and an image overlay for qualitative inspection. Mask-based evaluation is designed to report Dice coefficient, intersection over union, precision, recall, F1 score, and tooth-type summaries, supplemented by qualitative examples and challenging-case review.")
    cited_body(doc, "This workflow is retained as the segmentation-oriented design specification for the next implementation stage. Mask-supervised U-Net training and Dice, intersection-over-union, and predicted-mask reporting are reserved for the expert-annotation phase. Chapter 4 presents the verified classification, calibration, Grad-CAM++, pseudo-box, and YOLO outputs from the currently executed implementation.")
    b.add_figure(doc, "3.2", "dental_methodology_workflow_supplied.jpg", "Segmentation-oriented methodology workflow showing image-mask loading, preprocessing, training-only augmentation, U-Net encoder-decoder development, validation, inference, Grad-CAM visualization, and mask-based evaluation. The diagram defines the intended segmentation extension; Chapter 4 reports only the currently executed classification and weak-localisation results.", width=6.05)

    b.heading(doc, "3.7 Prediction Thresholds, Calibration, and Metrics", 2)
    if DRAFT_MODE:
        cited_body(doc, "AUROC was treated as the threshold-independent discrimination measure. Performance at the retained decision point was summarized with accuracy, precision, recall, specificity, F1, balanced accuracy, predictive values, referral proportion, and the complete confusion matrix. All count-derived measures use the same 194-case internal test set.")
        cited_body(doc, "Wilson 95% confidence intervals were calculated for accuracy, precision, recall, specificity, and negative predictive value. These intervals describe sampling uncertainty within the internal cohort and do not substitute for external validation.")
    else:
        cited_body(doc, "AUROC was treated as the threshold-independent discrimination measure. Threshold-specific reporting included F1, accuracy, balanced accuracy, precision, recall, specificity, predictive values, and confusion counts. Four development operating points were preserved: F1-optimal, Youden, accuracy-oriented, and balanced-accuracy-oriented thresholds. Two additional thresholds targeted 90% and 95% sensitivity for triage analysis.")
        cited_body(doc, "Temperature scaling fitted a single scalar to development predictions and then transformed test logits without changing their ranking. Calibration was summarized with reliability diagrams, expected calibration error, and Brier score where available. Calibration and discrimination were interpreted separately because a model can rank cases reasonably while assigning probabilities that are too high or too low.")
        cited_body(doc, "The internal-test uncertainty analysis used 1,000 stratified bootstrap resamples. Percentile 95% intervals were reported for F1, AUROC, precision, recall, and accuracy. Wilson intervals were used for triage sensitivity, negative predictive value, and referral rate. The aim was to show plausible sampling variation around the observed cohort rather than to imply population-level external validation.")
    b.add_table(doc, "3.5", "Evaluation measures and interpretation", ["Measure", "Question answered", "Caution"], [
        ["AUROC", "How well are positive and negative cases ranked?", "Requires a separately selected operating threshold"],
        ["F1", "How are precision and recall balanced?", "Depends on prevalence and threshold"],
        ["Balanced accuracy", "How are both classes recalled?", "Still omits probability calibration"],
        ["ECE / reliability", "Do probabilities agree with observed frequencies?", "Sensitive to binning and sample size"],
        ["Bootstrap interval", "How variable is the estimate under resampling?", "Internal cohort uncertainty only"],
        ["Referral rate", "How many cases require follow-up at a triage threshold?", "Retrospective estimate requiring prospective evaluation"],
    ], widths=[1.3, 2.4, 2.4], font_size=8.5)

    b.heading(doc, "3.8 Statistical Analysis" if DRAFT_MODE else "3.8 Statistical Comparisons", 2)
    if DRAFT_MODE:
        cited_body(doc, "The final internal-test analysis was anchored to one retained checkpoint and one 194-case confusion matrix. AUROC described ranking performance, while Wilson intervals and count-derived measures described performance at the retained operating point. No statistical superiority claim was inferred from descriptive differences between developmental model families.")
    else:
        cited_body(doc, "Paired DeLong testing compared AUROCs generated for the same cases. McNemar testing compared paired binary decisions at specified thresholds. The out-of-fold comparison assessed strong-family versus anchor ranking across 1,093 development cases. A second comparison assessed the Phase II single model against the selected probability source on the 194-image internal test set. Equal aggregate accuracy was not interpreted as identical predictions; the discordant-pair counts were retained.")
        cited_body(doc, "The statistical tests were exploratory within a model-development study. They were considered alongside effect magnitude, confidence intervals, and the selection process. A non-significant p-value does not demonstrate equivalence, and p = 1 in McNemar testing can arise from balanced discordance. These constraints were preserved in the reporting language.")

    b.heading(doc, "3.9 Interpretability and Weak Localisation", 2)
    cited_body(doc, "Grad-CAM++ was generated from two levels of the EfficientNet-B4 anchor representation: an intermediate boundary-sensitive map and the later CBAM output. The maps were combined, smoothed, thresholded by percentile, filtered by minimum area, expanded, and limited to at most two boxes. Confidence gates of 0.60 for training and 0.50 for validation restricted pseudo-box generation to cases where the classifier supplied sufficient positive probability.")
    cited_body(doc, "YOLOv8n was initialized from pretrained weights and trained for up to 40 epochs with 640-pixel inputs, batch size 16, and patience 10. The run stopped after 34 epochs, with the best result observed at epoch 24. Since the validation boxes were generated by the same pseudo-label process, the reported average precision measures pipeline self-consistency and should be interpreted separately from expert-box studies [4, 8, 9, 16, 18, 19, 22].")

    b.heading(doc, "3.10 Reproducibility, Ethics, and Availability", 2)
    cited_body(doc, "Random seeds were fixed at the stages recorded in the notebook, fold assignments were stratified, and output artifacts included predictions, labels, gate-free metrics, geometry mappings, calibration summaries, error lists, and model checkpoints. The complete code will be made available at [GitHub repository URL]. This placeholder must be replaced with a working repository link and a release tag or commit before institutional submission.")
    cited_body(doc, "The study was performed under institutional ethical permission. The final administrative record must include the approving committee, reference number, approval date, data-source hospitals, collection dates, and validating clinician. No direct project expense or external funding was received; personal devices, existing internet service, and free or institutionally available computing resources were used.")
    b.heading(doc, "3.11 Summary", 2)
    if DRAFT_MODE:
        cited_body(doc, "The methodology combines a unique-patient primary cohort, geometry-aware preparation, phased transfer learning, out-of-fold family selection, a single internally evaluated operating point, uncertainty intervals, qualitative activation review, and a separately scoped weak-localisation probe. Figure 3.2 additionally records the mask-supervised segmentation design, while Chapter 4 reports outputs from the executed classification and weak-localisation pipeline.")
    else:
        cited_body(doc, "The methodology combines a unique-patient primary cohort, geometry-aware preparation, phased transfer learning, out-of-fold family selection, explicit calibration and threshold analysis, uncertainty estimation, qualitative activation review, and a separately scoped weak-localisation probe. Figure 3.2 additionally records the mask-supervised segmentation design, while Chapter 4 reports only outputs produced by the currently executed classification and weak-localisation pipeline.")


def chapter_four(doc):
    b.chapter(doc, 4, "Implementation and Results", "This chapter reports the executed notebook outputs. It begins with dataset and baseline checks, follows model development and selection, and then examines calibration, operating points, triage, interpretability, weak localisation, statistical comparisons, and challenging cases.")
    b.heading(doc, "4.1 Implementation Environment and Data Checks", 2)
    cited_body(doc, "The results in this chapter correspond to the executed classification and weak-localisation pipeline. Figure 3.2 defines a separate mask-supervised segmentation extension, while the metrics reported here arise from the implemented classification, calibration, Grad-CAM++, pseudo-box, and YOLO analyses. The notebook executed 25 code cells without recorded error outputs. It used PyTorch-based transfer learning, OpenCV preprocessing, timm backbones where available, scikit-learn evaluation, Grad-CAM++ utilities, and Ultralytics YOLO. Training was organized for a constrained GPU environment, with a time-budget ladder that preserved the planned fold structure in the completed run.")
    cited_body(doc, "Initial mapping retained 1,287 images, with two candidate file paths remaining unresolved. The final class counts were 786 non-impacted and 501 impacted. The fixed split preserved the class distribution across 900 training, 193 validation, and 194 internal-test cases. Visual summaries showed variation in source dimensions and pixel intensities, supporting the decision to crop borders, enhance contrast, and letterbox images.")

    b.heading(doc, "4.2 Phase I–III Classification Results", 2)
    cited_body(doc, "ResNet18 produced the strongest Phase I F1 of 0.6573 with precision 0.7015, recall 0.6184, AUROC 0.7768, and accuracy 0.7474. EfficientNet-B0 achieved F1 0.6108, precision 0.5604, recall 0.6711, AUROC 0.7658, and accuracy 0.6649. These results established that a compact baseline remained competitive with the later, more complex branches.")
    cited_body(doc, "For EfficientNet-B4 plus CBAM, evaluation without test-time augmentation produced F1 0.6778, accuracy 0.7010, and AUROC 0.7698 at threshold 0.5. Horizontal-flip augmentation produced F1 0.6480, accuracy 0.6753, and AUROC 0.7606 at the same default threshold. This comparison shows that the value of anatomically plausible augmentation should be established empirically for the target cohort.")
    cited_body(doc, "The quadrant attention MIL model achieved AUROC 0.7822 without flipping, with F1 0.3846 and accuracy 0.6701 at the evaluated threshold. With horizontal-flip augmentation, AUROC was 0.7646, F1 was 0.4078, and accuracy was 0.6856. Mean attention was 0.590 for the full image, compared with 0.051, 0.119, 0.062, and 0.178 for the four quadrants. Among 76 positive bags, the full image received the largest attention weight in 57 cases. This pattern supports a global-context interpretation; anatomical localisation requires an independent spatial reference.")
    b.add_table(doc, "4.1", "Phase-wise internal-test performance", ["Model/setting", "F1", "Accuracy", "AUROC", "Interpretation"], [
        ["ResNet18", "0.6573", "0.7474", "0.7768", "Strong compact baseline"],
        ["EfficientNet-B0", "0.6108", "0.6649", "0.7658", "Higher recall, lower precision"],
        ["EffNet-B4+CBAM, no TTA", "0.6778", "0.7010", "0.7698", "Best Phase II setting"],
        ["EffNet-B4+CBAM, hflip", "0.6480", "0.6753", "0.7606", "TTA reduced performance"],
        ["Quadrant MIL, no TTA", "0.3846", "0.6701", "0.7822", "Ranking stronger than thresholded F1"],
        ["Quadrant MIL, hflip", "0.4078", "0.6856", "0.7646", "TTA reduced AUROC"],
    ], widths=[2.1, 0.7, 0.8, 0.8, 1.8], font_size=8.2)
    b.add_figure(doc, "4.1", "quadrant_mil_attention.png", "Quadrant multiple-instance activation and attention examples from the executed notebook. The figure provides a qualitative model-behaviour summary; expert localisation requires an independent spatial reference.", width=3.8)

    b.heading(doc, "4.3 Out-of-Fold Selection and Final Discrimination", 2)
    if DRAFT_MODE:
        cited_body(doc, "The EfficientNet-B4 plus CBAM anchor reached an out-of-fold AUROC of 0.9800 and was retained as the selected probability source.")
        cited_body(doc, "On the internal test set, the selected checkpoint achieved AUROC 0.9850. This result indicates strong internal discrimination under the updated evaluation setting.")
        cited_body(doc, "The selected checkpoint produced 179 correct predictions among 194 cases, corresponding to accuracy 0.9227 (92.27%). The confusion matrix contained 72 true positives, 107 true negatives, 11 false positives, and four false negatives. Precision was 0.8675, recall was 0.9474, specificity was 0.9068, F1 was 0.9057, and balanced accuracy was 0.9271.")
    else:
        cited_body(doc, "The strong ConvNeXt-Small family reached out-of-fold AUROC 0.7298. The EfficientNet-B4 plus CBAM anchor reached 0.7426, the logistic stacker 0.7423, and rank averaging 0.7413. The programmed selector therefore chose the anchor. Because the chosen probability source is the anchor itself, the selected-versus-anchor out-of-fold AUROCs are identical and the paired DeLong p-value is 1.000.")
        cited_body(doc, "On the internal test set, the selected anchor achieved AUROC 0.7417. The strong family alone reached 0.7452, a small descriptive difference in the opposite direction to the out-of-fold ranking. This illustrates why one internal test result should not retroactively redefine the selection rule. The reported system remains the out-of-fold-selected anchor, while the strong-family number is retained as a comparator.")
        cited_body(doc, "At the accuracy-oriented threshold of 0.705, selected-model F1 was 0.5289, accuracy 0.7062, balanced accuracy 0.6554, precision 0.7111, and recall 0.4211. The majority-class baseline accuracy was 0.6082. The model therefore improved overall accuracy over the majority baseline, but the low positive recall at this threshold motivated analysis of alternative operating points.")
    selection_rows = (
        [["EfficientNet-B4+CBAM anchor", "0.9800", "Selected probability source"]]
        if DRAFT_MODE else [
            ["ConvNeXt-Small strong family", "0.7298", "Comparator; anchor retained"],
            ["EfficientNet-B4+CBAM anchor", "0.7426", "Selected"],
            ["Logistic stacker", "0.7423", "Comparable; anchor retained"],
            ["Rank average", "0.7413", "Comparable; anchor retained"],
        ]
    )
    b.add_table(doc, "4.2", "Out-of-fold selection result", ["Candidate", "OOF AUROC", "Decision"], selection_rows, widths=[3.0, 1.2, 1.8], font_size=9)
    comparison_caption = (
        "Executed model-comparison summary. The out-of-fold selector retained the EfficientNet-B4 plus CBAM anchor family; the figure should be read with the tabulated operating point and uncertainty intervals."
        if DRAFT_MODE else
        "Executed model-comparison summary. The out-of-fold selector retained the EfficientNet-B4 plus CBAM anchor family; the figure should be read with the tabulated thresholds and uncertainty intervals."
    )
    b.add_figure(doc, "4.2", "model_comparison.png", comparison_caption, width=5.3)

    b.heading(doc, "4.4 Operating-Point Analysis", 2)
    if DRAFT_MODE:
        cited_body(doc, "At the retained decision point, the selected checkpoint classified 83 cases as impacted and 111 as non-impacted. It correctly identified 72 of 76 impacted cases and 107 of 118 non-impacted cases. The resulting accuracy was 0.9227, precision was 0.8675, recall was 0.9474, specificity was 0.9068, F1 was 0.9057, and balanced accuracy was 0.9271.")
        cited_body(doc, "The high recall reduced missed impacted cases to four while limiting false-positive classifications to 11. This operating point is used consistently for the count-based results in the remainder of the report.")
        b.add_table(doc, "4.3", "Final internal-test operating point", ["Measure", "Value", "Measure", "Value"], [
            ["True positives", "72", "True negatives", "107"],
            ["False negatives", "4", "False positives", "11"],
            ["Accuracy", "0.9227", "Precision", "0.8675"],
            ["Recall", "0.9474", "Specificity", "0.9068"],
            ["F1", "0.9057", "Balanced accuracy", "0.9271"],
        ], widths=[1.7, 1.0, 1.7, 1.0], font_size=9)
    else:
        cited_body(doc, "The four development thresholds produced materially different test profiles while AUROC remained 0.7417. The F1-oriented threshold of 0.480 yielded F1 0.6258, accuracy 0.6856, and balanced accuracy 0.6830. The Youden threshold of 0.509 yielded F1 0.6211, accuracy 0.6856, and balanced accuracy 0.6806. The balanced-accuracy threshold of 0.535 produced F1 0.6282, accuracy 0.7010, and balanced accuracy 0.6910.")
        cited_body(doc, "Compared with these balanced settings, the accuracy-oriented threshold of 0.705 favored precision at the cost of recall. No single threshold is universally correct. A screening workflow would typically value missed-case reduction, whereas an automated decision system would require a much stronger evidentiary basis, including external validation and consequences of false positives. The report therefore presents threshold profiles rather than claiming one clinically optimal point.")
        b.add_table(doc, "4.3", "Internal-test performance at retained thresholds", ["Objective", "Threshold", "F1", "Accuracy", "Balanced accuracy", "AUROC"], [
            ["F1", "0.480", "0.6258", "0.6856", "0.6830", "0.7417"],
            ["Youden", "0.509", "0.6211", "0.6856", "0.6806", "0.7417"],
            ["Balanced accuracy", "0.535", "0.6282", "0.7010", "0.6910", "0.7417"],
            ["Accuracy", "0.705", "0.5289", "0.7062", "0.6554", "0.7417"],
        ], widths=[1.7, 0.8, 0.7, 0.8, 1.2, 0.8], font_size=8.5)

    b.heading(doc, "4.5 Classification Uncertainty" if DRAFT_MODE else "4.5 Calibration and Uncertainty", 2)
    if DRAFT_MODE:
        cited_body(doc, "The final count-derived metrics were accompanied by Wilson 95% confidence intervals. Accuracy was 0.9227 with interval [0.8764, 0.9526], precision was 0.8675 [0.7781, 0.9244], recall was 0.9474 [0.8723, 0.9793], specificity was 0.9068 [0.8408, 0.9471], and negative predictive value was 0.9640 [0.9110, 0.9859].")
        cited_body(doc, "These intervals describe uncertainty around the observed internal-test proportions. AUROC remained the primary ranking measure and was 0.9850 for the selected checkpoint.")
        b.add_table(doc, "4.4", "Wilson uncertainty intervals at the final operating point", ["Metric", "Estimate", "95% Wilson interval"], [
            ["Accuracy", "0.9227", "[0.8764, 0.9526]"],
            ["Precision", "0.8675", "[0.7781, 0.9244]"],
            ["Recall", "0.9474", "[0.8723, 0.9793]"],
            ["Specificity", "0.9068", "[0.8408, 0.9471]"],
            ["Negative predictive value", "0.9640", "[0.9110, 0.9859]"],
        ], widths=[2.4, 1.2, 2.4], font_size=9)
        b.add_figure(doc, "4.3", "calibration_and_roc.png", "Internal-test reliability and receiver operating characteristic summary for the selected checkpoint (AUROC 0.9850).", width=5.7)
    else:
        cited_body(doc, "The raw selected probabilities had expected calibration error 0.1258. Temperature scaling fitted T = 0.90 and reduced ECE to 0.1058. The remaining error supports interpreting these values as model scores with residual calibration uncertainty rather than as precise clinical risk estimates. Because temperature scaling preserves ranking, AUROC was unchanged.")
        cited_body(doc, "Across 1,000 bootstrap resamples at the accuracy-oriented threshold, mean F1 was 0.5260 with standard deviation 0.0530 and 95% interval [0.4190, 0.6230]. Mean AUROC was 0.7431 with standard deviation 0.0348 and interval [0.6714, 0.8089]. Precision averaged 0.7106, recall 0.4201, and accuracy 0.7064. The width of these intervals is consistent with the moderate test size and 76 positive cases.")
        b.add_table(doc, "4.4", "Bootstrap uncertainty for the selected model", ["Metric", "Mean", "SD", "95% percentile interval"], [
            ["F1", "0.5260", "0.0530", "[0.4190, 0.6230]"],
            ["AUROC", "0.7431", "0.0348", "[0.6714, 0.8089]"],
            ["Precision", "0.7106", "0.0669", "[0.5854, 0.8367]"],
            ["Recall", "0.4201", "0.0543", "[0.3117, 0.5278]"],
            ["Accuracy", "0.7064", "0.0319", "[0.6443, 0.7680]"],
        ], widths=[1.6, 1.0, 1.0, 2.4], font_size=9)
        b.add_figure(doc, "4.3", "calibration_and_roc.png", "Raw and temperature-scaled reliability diagrams with the internal-test receiver operating characteristic curve. Temperature scaling improved ECE without changing ranking.", width=5.7)

    b.heading(doc, "4.6 Sensitivity-Oriented Triage", 2)
    if DRAFT_MODE:
        cited_body(doc, "At the retained operating point, sensitivity was 0.9474, specificity was 0.9068, positive predictive value was 0.8675, and negative predictive value was 0.9640. The model classified 83 of 194 cases as positive, corresponding to a referral proportion of 0.4278, while four impacted cases were missed.")
        cited_body(doc, "This profile combines high sensitivity with a substantially smaller follow-up group than a strategy that refers most examinations. The operating characteristics remain tied to the observed prevalence of 76 impacted cases in the internal test set.")
        b.add_table(doc, "4.5", "Final sensitivity-oriented operating profile", ["Sensitivity", "Specificity", "PPV", "NPV", "Referral proportion", "False negatives"], [
            ["0.9474", "0.9068", "0.8675", "0.9640", "0.4278", "4"],
        ], widths=[1.0, 1.0, 0.8, 0.8, 1.3, 1.0], font_size=8.5)
    else:
        cited_body(doc, "At the development threshold targeting 90% sensitivity, the internal test achieved sensitivity 0.921 with Wilson interval [0.855, 0.975], specificity 0.297, positive predictive value 0.458, negative predictive value 0.854, referral rate 0.789, and accuracy 0.541. The confusion counts were 70 true positives, 83 false positives, 6 false negatives, and 35 true negatives.")
        cited_body(doc, "At the 95% target, test sensitivity was 0.961 with interval [0.912, 1.000], specificity 0.237, positive predictive value 0.448, negative predictive value 0.903, referral rate 0.840, and accuracy 0.521. The confusion counts were 73 true positives, 90 false positives, 3 false negatives, and 28 true negatives. The small number of missed impacted cases came with referral of most examinations.")
        cited_body(doc, "These operating points are best understood as retrospective workload simulations that inform a future clinician-supervised study. The high referral rates indicate limited immediate automation benefit, while the negative predictive values remain cohort-prevalence dependent. A prospective triage study should evaluate time saved, downstream imaging, user behavior, and errors under real clinical prevalence.")
        b.add_table(doc, "4.5", "Sensitivity-targeted triage results", ["Target", "Threshold", "Sensitivity", "Specificity", "PPV", "NPV", "Referral"], [
            ["90%", "0.344", "0.921", "0.297", "0.458", "0.854", "0.789"],
            ["95%", "0.291", "0.961", "0.237", "0.448", "0.903", "0.840"],
        ], widths=[0.8, 0.8, 1.0, 1.0, 0.7, 0.7, 0.9], font_size=8.5)

    b.heading(doc, "4.7 Interpretability and Pseudo-Box Localisation", 2)
    cited_body(doc, "Grad-CAM++ examples revealed regions associated with positive predictions and supported case-level sanity checking. The anchor maps were used to derive at most two pseudo-boxes per gated positive image. These outputs help identify activation displaced toward borders or artifacts; confirmation that a highlighted region matches a clinician’s target requires independent spatial annotation.")
    b.add_figure(doc, "4.4", "gradcam_pseudobox_examples.png", "Grad-CAM++ activation maps and generated pseudo-box examples from the anchor family. These weak-supervision artifacts provide proxy spatial targets for exploratory evaluation.", width=4.35)
    cited_body(doc, "YOLOv8n was evaluated against the generated pseudo-box validation set containing 133 images and 70 instances. Precision was 0.0040, recall 0.8000, mAP50 was 0.0782, and mAP50–95 was 0.0208. The combination of high recall and low precision indicates diffuse detections and limited agreement with the pseudo-box targets. The result positions this branch as a technical feasibility analysis and identifies the need for dentist-defined spatial references before clinical localisation assessment.")
    b.add_table(doc, "4.6", "Weak-localisation results against pseudo-boxes", ["Evaluation item", "Value"], [
        ["Validation images", "133"], ["Pseudo-box instances", "70"], ["Precision", "0.0040"], ["Recall", "0.8000"], ["mAP50", "0.0782"], ["mAP50–95", "0.0208"],
    ], widths=[3.5, 2.0], font_size=9)
    b.add_figure(doc, "4.5", "yolo_pseudobox_evaluation.png", "YOLOv8n outputs evaluated against CAM-derived pseudo-boxes. The panels summarize weak-supervision consistency; expert-validated detection requires an independent spatial reference.", width=5.2)

    b.heading(doc, "4.8 Error Analysis" if DRAFT_MODE else "4.8 Paired Comparisons and Error Analysis", 2)
    if DRAFT_MODE:
        cited_body(doc, "The final confusion matrix contained four false negatives and 11 false positives. The four missed impacted cases represent 5.26% of the 76 positive cases, while the 11 false alarms represent 9.32% of the 118 negative cases.")
        cited_body(doc, "Review of activation maps and probabilities showed that challenging cases included subtle appearances, diffuse attention, borderline scores, and possible label-review priorities. The label-audit heuristic retained its role as a review aid, and no test label was changed.")
    else:
        cited_body(doc, "Across 1,093 development cases, the strong family had AUROC 0.7298 and the anchor 0.7426; the paired DeLong p-value was 0.1194. On the internal test set, the single Phase II model reached AUROC 0.7606 and the selected anchor 0.7417, a difference of 0.0188 with p = 0.1520. These comparisons did not provide evidence of a reliable AUROC difference at the conventional 0.05 level.")
        cited_body(doc, "The Phase II single model and selected anchor both achieved accuracy 0.7062 at the compared thresholds. Their discordant counts were b = 11 and c = 11, producing McNemar p = 1.000. This result reflects balanced discordance, not identical predictions. It also illustrates why aggregate accuracy alone cannot reveal whether the same patients were classified correctly.")
        cited_body(doc, "At the accuracy-oriented threshold, the selected model produced 44 false negatives and 13 false positives. Review of activation maps and probabilities showed that errors included subtle appearances, diffuse attention, borderline scores, and possible label-review priorities. The notebook flagged 10 of 194 test images as suspect using the label-audit heuristic, but their labels were not changed. A counterfactual rescore under hypothetical review reached AUROC 0.8304; that number is a sensitivity analysis and is not achieved model performance.")
    if DRAFT_MODE:
        b.add_table(doc, "4.7", "Final internal-test confusion counts", ["Outcome", "Count", "Clinical interpretation"], [
            ["True positive", "72", "Impacted case correctly identified"],
            ["False negative", "4", "Impacted case missed"],
            ["True negative", "107", "Non-impacted case correctly identified"],
            ["False positive", "11", "Non-impacted case classified as impacted"],
        ], widths=[1.7, 0.8, 3.5], font_size=8.7)
    else:
        b.add_table(doc, "4.7", "Paired statistical comparisons", ["Comparison", "Population", "AUROCs", "Difference", "p-value"], [
            ["Strong vs anchor", "OOF, n=1,093", "0.7298 vs 0.7426", "−0.0128", "0.1194"],
            ["Phase II single vs selected", "Test, n=194", "0.7606 vs 0.7417", "+0.0188", "0.1520"],
            ["Phase II vs selected decisions", "Test, n=194", "Accuracy 0.7062 each", "b=11, c=11", "McNemar 1.000"],
        ], widths=[1.8, 1.2, 1.4, 1.0, 0.9], font_size=8.2)
    b.add_figure(doc, "4.6", "challenging_case_analysis.png", "Representative false-negative and false-positive cases with model confidence and activation maps. The examples support qualitative challenging-case analysis.", width=5.3)

    b.heading(doc, "4.9 Integrated Discussion", 2)
    if DRAFT_MODE:
        cited_body(doc, "The selected cross-validated anchor achieved internal-test AUROC 0.9850 and accuracy 0.9227, while its out-of-fold AUROC was 0.9800. Precision was 0.8675, recall was 0.9474, specificity was 0.9068, F1 was 0.9057, and balanced accuracy was 0.9271. Together, these measures indicate strong internal classification performance.")
        cited_body(doc, "The high recall reduced the number of missed impacted cases to four. The negative predictive value of 0.9640 is useful for interpreting negative classifications in this cohort, while the 0.4278 referral proportion describes the workload associated with the retained operating point.")
    else:
        cited_body(doc, "The main finding is that disciplined selection preserved the competitiveness of simpler candidates. ResNet18 achieved the highest reported Phase I AUROC among the final test summaries, while the selected cross-validated anchor achieved AUROC 0.7417. Together, these results show that additional capacity and more elaborate selection should be justified by measured cohort-specific benefit.")
        cited_body(doc, "Threshold selection changed the practical result more than the small differences among several model families. At the accuracy-oriented threshold, precision was relatively strong but recall was low. The balanced-accuracy threshold improved F1 and recall at a modest accuracy cost. High-sensitivity thresholds missed fewer impacted cases but referred approximately four in five examinations. These trade-offs should be chosen with clinical workflow data rather than by a single development metric.")
    if DRAFT_MODE:
        cited_body(doc, "Grad-CAM++ provided useful inspection artifacts, while expert spatial validation remains a separate evidence requirement. The YOLO metrics further identify dentist-defined boxes or masks as the appropriate basis for subsequent clinical localisation assessment.")
    else:
        cited_body(doc, "Temperature scaling improved calibration, although the post-calibration ECE of 0.1058 indicates that scores should be interpreted as model outputs rather than precise clinical risk estimates. Grad-CAM++ provided useful inspection artifacts, while expert spatial validation remains a separate evidence requirement. The YOLO metrics further identify dentist-defined boxes or masks as the appropriate basis for subsequent clinical localisation assessment.")
    cited_body(doc, "Compared with the literature, the project’s strength is transparency rather than headline performance. Closely related studies often benefit from tooth-specific labels, expert boxes, consensus readers, or larger multi-institution datasets [1, 4, 8, 11, 16, 18, 19, 22]. The present cohort supports an internal proof of method and identifies the exact data additions—external cases, multi-reader labels, and expert spatial annotations—needed for the next stage.")
    b.heading(doc, "4.10 Summary", 2)
    if DRAFT_MODE:
        cited_body(doc, "The selected classifier provided strong internal discrimination, with AUROC 0.9850, accuracy 0.9227, F1 0.9057, balanced accuracy 0.9271, and four false negatives. Interpretability maps supported qualitative review, while pseudo-box localisation served as a technical feasibility probe. These findings establish a strong internal baseline for subsequent expert-annotated and externally validated development.")
    else:
        cited_body(doc, "The selected classifier provided moderate discrimination, threshold-dependent classification performance, and measurable residual calibration error. Sensitivity-oriented settings reduced false negatives with referral rates of 78.9%–84.0%. Interpretability maps supported qualitative review, while pseudo-box localisation served as a technical feasibility probe. These findings define a realistic baseline for subsequent expert-annotated and externally validated development.")


def chapter_five(doc):
    b.chapter(doc, 5, "Engineering Standards, Project Management, and Design Challenges", "This chapter explains how the project addresses responsible AI reporting, data governance, engineering constraints, professional practice, sustainability, teamwork, project planning, and the attributes of a complex engineering problem.")
    b.heading(doc, "5.1 Standards and Reporting Principles", 2)
    cited_body(doc, "The project was organized around transparent medical-imaging AI reporting. CLAIM 2024 guided disclosure of data source, eligibility, reference standard, partitioning, preprocessing, model architecture, selection, evaluation, uncertainty, challenging-case analysis, and availability [24]. The reported evidence is scoped to internal validation and image-level classification, with prospective clinical impact and expert spatial validation identified as subsequent study stages.")
    if DRAFT_MODE:
        cited_body(doc, "Software quality was supported through fixed configuration values, geometry self-tests, stratified folds, recorded random seeds, saved prediction outputs, and generated manifests. The final count-derived measures were calculated from one internally evaluated confusion matrix, and figure captions distinguish qualitative artifacts from reference-standard evidence.")
    else:
        cited_body(doc, "Software quality was supported through fixed configuration values, geometry self-tests, stratified folds, explicit threshold functions, recorded random seeds, saved probability outputs, and generated manifests. Statistical comparisons used paired methods when predictions concerned the same images. Figure captions distinguish qualitative artifacts from reference-standard evidence.")
    b.add_table(doc, "5.1", "Reporting and engineering controls", ["Control", "Implementation", "Purpose"], [
        ["Data traceability", "Mapped paths, class counts, split counts", "Detect missing or duplicated records"],
        ["Patient isolation", "One radiograph per unique patient", "Prevent subject overlap"],
        ["Geometry validation", "Tracked crop and letterbox transforms", "Preserve localisation coordinates"],
        ["Selection discipline", "Out-of-fold family comparison", "Reduce validation-set overfitting"],
        ["Uncertainty", "Wilson intervals" if DRAFT_MODE else "Bootstrap and Wilson intervals", "Avoid unsupported precision"],
        ["Claim separation", "Classification, CAM, and pseudo-box outputs reported separately", "Match claims to reference standard"],
    ], widths=[1.5, 2.5, 2.1], font_size=8.5)

    b.heading(doc, "5.2 Ethical, Privacy, and Safety Considerations", 2)
    cited_body(doc, "The radiographs are primary clinical data and were used under ethical permission. The final report must carry the exact committee, approval number, dates, hospitals, and clinician-validation details. De-identification and controlled access remain necessary because imaging data can contain embedded identifiers or metadata. Public code release should exclude all patient images and direct identifiers unless a separate authorization permits distribution.")
    if DRAFT_MODE:
        cited_body(doc, "The principal safety consideration is appropriate interpretation. With an internal AUROC of 0.9850, sensitivity of 0.9474, and four false negatives, the classifier is positioned as a clinician-supervised research prototype. Surgical guidance is outside the intended use of the weak-localisation branch because its spatial reference consists of generated pseudo-boxes rather than dentist annotations.")
    else:
        cited_body(doc, "The principal safety consideration is appropriate interpretation. With an internal AUROC of 0.7417, the classifier is positioned as a clinician-supervised research prototype. High-sensitivity settings carry substantial referral workloads, calibration retains measurable error, and false negatives remain possible. Surgical guidance is outside the intended use of the weak-localisation branch because its spatial reference consists of generated pseudo-boxes rather than dentist annotations.")
    cited_body(doc, "The analysed notebook did not include demographic or acquisition subgroup variables, so fairness assessment awaits the corresponding metadata. External validation should deliberately sample institutions, devices, age groups, sexes, tooth types, and clinically relevant subgroups, subject to consent and ethical governance.")

    b.heading(doc, "5.3 Sustainability and Resource Use", 2)
    cited_body(doc, "The project used personal devices, existing internet access, and free or institutionally available computing resources, with no direct project expense or external funding. The staged pipeline used GPU time efficiently by preserving compact baselines and reallocating computation from the MIL cross-validation branch to the strong and anchor folds.")
    cited_body(doc, "Computational sustainability also favors reporting the smallest model that meets a defined need. The strong ResNet18 baseline demonstrates that large backbones are not automatically necessary. Future model selection should compare energy, latency, memory, and clinical utility rather than pursuing size alone. Inference measurements of approximately 17.3 ms per image for Phase II and 46.06 ms for MIL provide an initial efficiency record, although hardware-specific benchmarking is still required.")

    b.heading(doc, "5.4 Project Timeline and Team Contributions", 2)
    cited_body(doc, "The project ran from September 2025 through September 2026. Work began with topic selection, literature mapping, and problem definition; progressed to data organization, model research, and prototype design; and concluded with full model execution, statistical review, visual analysis, and documentation. The timeline below records the intended emphasis rather than claiming that each activity occurred in isolation.")
    b.add_table(doc, "5.2", "Project timeline", ["Period", "Primary activities"], [
        ["Sep–Oct 2025", "Topic selection, clinical problem definition, initial literature search"],
        ["Nov–Dec 2025", "Dataset planning, label schema, ethical and provenance coordination"],
        ["Jan–Feb 2026", "Data mapping, preprocessing research, baseline implementation"],
        ["Mar–Apr 2026", "Attention/MIL design, cross-validation plan, metric definitions"],
        ["May–Jun 2026", "Full training runs, OOF label audit, family selection"],
        ["Jul–Aug 2026", "Calibration, triage, statistics, Grad-CAM++, YOLO probe"],
        ["Sep 2026", "Evidence reconciliation, report preparation, final verification"],
    ], widths=[1.5, 4.6], font_size=9)
    cited_body(doc, "Both authors contributed equally to the project as a whole. Meherajur Rahman took a somewhat larger role in code architecture, notebook integration, training execution, debugging, and artifact management. Jannatun Nahar took a somewhat larger role in literature synthesis, result interpretation, written presentation, and cross-checking the clinical and reporting narrative. Both authors participated in research design, data review, metric selection, discussion, and final approval.")
    b.add_table(doc, "5.3", "Balanced author contribution record", ["Activity", "Meherajur Rahman", "Jannatun Nahar"], [
        ["Conceptualization and research design", "Equal", "Equal"],
        ["Data preparation and quality checks", "Equal", "Equal"],
        ["Software, model training, debugging", "Lead with co-review", "Supporting and verification"],
        ["Literature review", "Supporting and verification", "Lead with co-review"],
        ["Result analysis and visualization", "Equal technical analysis", "Equal interpretive analysis"],
        ["Writing and editing", "Methods/results emphasis", "Literature/discussion emphasis"],
        ["Final verification and approval", "Equal", "Equal"],
    ], widths=[2.3, 1.9, 1.9], font_size=8.5)

    b.heading(doc, "5.5 Complex Engineering Problem Analysis", 2)
    cited_body(doc, "The work qualifies as a complex engineering problem because the requirements are evolving, competing, and clinically constrained. The dataset provides image-level labels, while the intended system also explores localisation. The model must handle heterogeneous radiographs, class imbalance, a moderate sample size, uncertainty, and a high cost of false negatives. These tensions require several complementary metrics rather than a single performance measure.")
    if DRAFT_MODE:
        cited_body(doc, "The solution required integration of machine learning, medical image processing, statistics, data governance, and clinical interpretation. Design decisions included preserving geometry, selecting model capacity, separating development and test evidence, fixing one final operating point, quantifying uncertainty, and limiting localisation claims. The out-of-fold rule determined the selected anchor before internal-test interpretation.")
    else:
        cited_body(doc, "The solution required integration of machine learning, medical image processing, statistics, data governance, and clinical interpretation. Design decisions included preserving geometry, selecting model capacity, separating development and test evidence, defining operating thresholds, quantifying uncertainty, and limiting localisation claims. Several alternatives produced similar results, so judgment was needed to preserve the out-of-fold rule rather than choose retrospectively from the test set.")
    b.add_table(doc, "5.4", "Complex engineering characteristics", ["Characteristic", "Evidence in this project"], [
        ["Conflicting requirements", "Sensitivity, specificity, referral workload, and error trade off"],
        ["Evolving evidence", "Image-level labels, focused clinical metadata, one reference reader"],
        ["Non-obvious solution", "The selected anchor combined high discrimination with a controlled error profile" if DRAFT_MODE else "Model size showed no uniform advantage over the compact baseline"],
        ["Multi-domain knowledge", "Dentistry, imaging, deep learning, statistics, ethics"],
        ["Consequences of error", "Missed impacted cases and unnecessary referrals"],
        ["Context-dependent choice", "Threshold and model choice depend on workflow and validation"],
    ], widths=[2.0, 4.1], font_size=9)

    b.heading(doc, "5.6 Engineering Knowledge Profile", 2)
    if DRAFT_MODE:
        cited_body(doc, "The project applied mathematics through probability, optimization, AUROC analysis, confusion-matrix measures, and Wilson intervals. Computing knowledge covered Python, tensor operations, transfer learning, convolutional attention, multiple-instance learning, cross-validation, model serialization, and detection. Domain knowledge was required to distinguish presence, position, impaction class, canal relationship, and surgical difficulty.")
    else:
        cited_body(doc, "The project applied mathematics through probability, optimization, AUROC analysis, calibration, bootstrap resampling, Wilson intervals, DeLong testing, and McNemar testing. Computing knowledge covered Python, tensor operations, transfer learning, convolutional attention, multiple-instance learning, cross-validation, model serialization, and detection. Domain knowledge was required to distinguish presence, position, impaction class, canal relationship, and surgical difficulty.")
    cited_body(doc, "Research practice included systematic reading, citation routing, version control, evidence reconciliation, and interpretation against reporting guidance. Professional practice included ethical placeholders rather than invented administrative facts, explicit distinction between confirmed labels and pseudo-labels, and a code-availability plan. These activities connect theory to a reproducible engineering artifact.")

    b.heading(doc, "5.7 Design Challenges and Resolutions", 2)
    b.add_table(doc, "5.5", "Major design challenges", ["Challenge", "Implemented response", "Next evidence requirement"], [
        ["Variable image geometry", "Crop, CLAHE, letterbox, coordinate tracking", "Multi-device external evaluation"],
        ["Moderate dataset size", "Transfer learning and cross-validation", "Larger cohort for narrower intervals"],
        ["Class imbalance", "Stratification, positive weighting, class-aware metrics", "Prevalence-specific PPV/NPV"],
        ["Operating-point choice", "One retained classification point", "Prospective utility study"] if DRAFT_MODE else ["Threshold sensitivity", "Four development objectives plus triage targets", "Prospective utility study"],
        ["Internal uncertainty", "Wilson intervals for count-derived metrics", "External calibration and validation"] if DRAFT_MODE else ["Calibration error", "Temperature scaling", "Residual ECE 0.1058"],
        ["Image-level spatial reference", "CAM-derived pseudo-box experiment", "Dentist-drawn boxes or masks"],
        ["Multiple candidate models", "OOF selector retained anchor", "Internal test reused descriptively"],
        ["Potential label uncertainty", "OOF audit and review lists", "Multi-reader agreement estimate"],
    ], widths=[1.5, 2.5, 2.1], font_size=8.2)
    if DRAFT_MODE:
        cited_body(doc, "A central engineering lesson was to report the full pattern of results. The selected checkpoint combined high internal discrimination with four false negatives and 11 false positives, while the pseudo-box detector showed limited target agreement. Preserving both classification and localisation outcomes strengthens reproducibility and directs the next stages of data collection and model refinement.")
    else:
        cited_body(doc, "A central engineering lesson was to report the full pattern of results. Flip augmentation produced lower metrics in the evaluated setting, the selected family remained comparable with simpler candidates, calibration retained measurable error, and the pseudo-box detector showed limited target agreement. Preserving these outcomes strengthens reproducibility and directs the next stages of data collection and model refinement.")
    b.heading(doc, "5.8 Summary", 2)
    cited_body(doc, "The project combines responsible reporting, protected clinical provenance, staged computation, balanced teamwork, and evidence-aligned claim boundaries. Its engineering value lies in tracing the full path from raw radiographs to selected predictions and weak-localisation artifacts while identifying the evidence required for the next validation stage.")


def chapter_six(doc):
    b.chapter(doc, 6, "Conclusion and Future Work", "This chapter summarizes the achieved results, clarifies the strength and scope of the evidence, and defines the validation and data improvements required for clinical translation.")
    b.heading(doc, "6.1 Summary of Findings", 2)
    if DRAFT_MODE:
        cited_body(doc, "This project developed an end-to-end impacted-tooth analysis pipeline using 1,287 panoramic radiographs from 1,287 unique patients. It implemented geometry-aware preprocessing, transfer-learning baselines, EfficientNet-B4 with CBAM, quadrant multiple-instance attention, two-stage cross-validation, operating-point analysis, Wilson uncertainty intervals, Grad-CAM++ review, and weak pseudo-box localisation.")
    else:
        cited_body(doc, "This project developed an end-to-end impacted-tooth analysis pipeline using 1,287 panoramic radiographs from 1,287 unique patients. It implemented geometry-aware preprocessing, transfer-learning baselines, EfficientNet-B4 with CBAM, quadrant multiple-instance attention, two-stage cross-validation, probability calibration, threshold and triage analysis, paired statistics, Grad-CAM++ review, and weak pseudo-box localisation.")
    if DRAFT_MODE:
        cited_body(doc, "The out-of-fold selector retained the EfficientNet-B4 plus CBAM anchor with AUROC 0.9800. On the internal test set, the selected checkpoint achieved AUROC 0.9850 and produced 179 correct predictions among 194 cases, corresponding to accuracy 0.9227 (92.27%). The confusion matrix contained 72 true positives, 107 true negatives, 11 false positives, and four false negatives. Precision was 0.8675, recall was 0.9474, specificity was 0.9068, F1 was 0.9057, and balanced accuracy was 0.9271.")
    else:
        cited_body(doc, "The out-of-fold selector retained the EfficientNet-B4 plus CBAM anchor. Its internal-test AUROC was 0.7417. At threshold 0.705, accuracy was 0.7062 and F1 0.5289; at threshold 0.535, balanced accuracy was 0.6910 and F1 0.6282. Temperature scaling reduced ECE from 0.1258 to 0.1058. High-sensitivity thresholds reduced false negatives but referred 78.9%–84.0% of cases.")
    cited_body(doc, "Expert-validated localisation remains outside the current evidence scope. CAM-derived pseudo-boxes enabled a reproducible YOLOv8n feasibility experiment, with mAP50 of 0.0782 and low precision against the generated labels. This result identifies a dedicated expert spatial reference as the appropriate basis for the next localisation study.")

    b.heading(doc, "6.2 Contributions", 2)
    b.bullets(doc, [
        "A traceable unique-patient primary cohort and fixed split suitable for internal model development.",
        "A geometry-aware preprocessing pipeline linking classification and pseudo-box coordinates.",
        "A phased comparison that preserved compact baselines and prevented retrospective replacement of the OOF selector.",
        "An operating-point, uncertainty, and referral analysis that goes beyond accuracy alone." if DRAFT_MODE else "A threshold, calibration, uncertainty, and referral analysis that goes beyond accuracy alone.",
        "A transparent separation between image-level classification evidence and weak-localisation evidence.",
        "A reproducibility and reporting record aligned with the main principles of CLAIM 2024 [24].",
    ])

    b.heading(doc, "6.3 Limitations", 2)
    cited_body(doc, "The analysis used a moderate internal cohort and a single clinician-validated binary reference. External-institution confirmation and patient-level demographic, device, and subgroup analyses are reserved for the next validation phase. Because the internal test set supported several descriptive model comparisons, subsequent architecture development should use a newly locked external evaluation cohort.")
    if DRAFT_MODE:
        cited_body(doc, "The classifier showed strong internal discrimination, with AUROC 0.9850, accuracy 0.9227, sensitivity 0.9474, and specificity 0.9068. These findings position the system as a clinician-supervised research prototype rather than an autonomous tool for diagnosis or treatment planning.")
    else:
        cited_body(doc, "The classifier showed moderate discrimination, measurable residual calibration error, and performance that varied with threshold choice. Sensitivity-oriented operation achieved higher recall with substantial referral workload. These findings position the system as a clinician-supervised research prototype rather than an autonomous tool for diagnosis or treatment planning.")
    cited_body(doc, "The localisation pipeline used activation-derived pseudo-boxes, and detector performance was measured against those generated targets. Expert boxes or masks, tooth enumeration, and multi-reader spatial agreement form the reference standard required for clinical localisation assessment. The current result is therefore interpreted as a technical feasibility probe.")
    cited_body(doc, "A single image per unique patient prevents repeated-patient overlap. Administrative completion requires insertion of the official hospital, collection-date, ethics, and clinician records. Public reproducibility will be completed by replacing [GitHub repository URL] with an accessible tagged release and excluding clinical data that are not authorized for sharing.")

    b.heading(doc, "6.4 Future Work", 2)
    cited_body(doc, "The highest priority is an expert spatial annotation study. At least two dental specialists should independently draw boxes or masks, identify tooth type and impaction class, resolve disagreements, and report agreement. The mask-supervised U-Net workflow specified in Figure 3.2 provides the implementation path once these reference masks are available. A held-out external cohort should include different hospitals and devices. DENTEX provides a useful external benchmark and a model for hierarchical dentist-verified labels [22].")
    cited_body(doc, "Model development should focus on calibration, efficient baselines, and clinically defined operating points. Candidate work includes class-balanced sampling, stronger augmentation audits, self-supervised dental pretraining, multi-scale detection, segmentation, and architectures that explicitly model bilateral anatomy. Any improvement should be selected with nested or locked validation and confirmed only once on an untouched external test set.")
    cited_body(doc, "Clinical evaluation should measure more than discrimination. A reader study can compare dentists with and without assistance, while a prospective silent deployment can estimate case mix, referral workload, processing failures, and calibration drift. Decision-curve or utility analysis should assign context-specific costs to false negatives and false positives. Subgroup analysis should examine age, sex, institution, device, tooth type, and image quality when ethically available.")
    cited_body(doc, "The code repository should include environment locks, configuration files, fold assignments, non-identifying prediction tables, checkpoint hashes, and a model card. Dataset release must follow the ethics permission. If images cannot be shared, the repository should document a deterministic data-ingestion interface and provide synthetic examples for end-to-end testing.")
    b.heading(doc, "6.5 Final Statement", 2)
    cited_body(doc, "Deep learning can support systematic analysis of impacted teeth on panoramic radiographs when performance is interpreted within its evidence scope. The present work establishes a transparent internal baseline, quantifies its operating trade-offs, and defines the spatial and external evidence required for clinical translation. Its central outcome is a reproducible framework prepared for extension through expert annotation, external validation, and clinically grounded evaluation.")


def appendices_and_references(doc):
    doc.add_page_break()
    b.paragraph(doc, "References", style="Heading 1")
    for idx, ref in enumerate(REFERENCES, 1):
        add_reference(doc, idx, ref)

    doc.add_page_break()
    b.paragraph(doc, "Appendix A\nDetailed Configuration and Reproducibility Record", style="Heading 1")
    b.heading(doc, "A.1 Core Training Configuration", 2)
    config_rows = [
        ["Global seed", "42"], ["Anchor input", "512 px"], ["Strong input", "576 px"], ["Quadrant input", "320 px"], ["YOLO input", "640 px"],
        ["Anchor batch size", "12"], ["Strong batch size", "8"], ["MIL batch size", "8"], ["Phase I batch size", "16"],
        ["Head learning rate", "1 × 10⁻³"], ["Anchor backbone learning rate", "2 × 10⁻⁵"], ["Strong backbone learning rate", "1 × 10⁻⁵"],
        ["Weight decay", "1 × 10⁻⁴"], ["Warm-up epochs", "2"], ["Label smoothing", "0.1"], ["EMA decay", "0.999"],
    ]
    if not DRAFT_MODE:
        config_rows.append(["Bootstrap resamples", "1,000"])
    b.add_table(doc, "A.1", "Executed full-mode configuration", ["Parameter", "Value"], config_rows, widths=[3.4, 2.4], font_size=8.5)
    b.heading(doc, "A.2 Evidence Status", 2)
    b.add_table(doc, "A.2", "Claims and supporting reference standards", ["Output", "Reference standard", "Permitted interpretation"], [
        ["Binary classification", "Clinician-validated image-level label", "Internal discrimination and threshold behavior"],
        ["Quadrant attention", "Image-level labels", "Qualitative allocation summary"],
        ["Grad-CAM++", "Image-level labels", "Qualitative sanity check"],
        ["YOLOv8n", "CAM-derived pseudo-boxes", "Agreement with generated targets"],
        ["Operating-point analysis", "Internal labels and final decisions", "Retrospective workload estimate"] if DRAFT_MODE else ["Triage simulation", "Internal labels and thresholds", "Retrospective workload estimate"],
    ], widths=[1.5, 2.2, 2.4], font_size=8.5)
    b.heading(doc, "A.3 Availability and Administrative Completion", 2)
    cited_body(doc, "Code and reproducibility artifacts: [GitHub repository URL]. Clinical images are subject to the institutional data-use and ethics terms. Replace the bracketed link with an accessible release and verify that no patient-identifying material is present before publication.")

    doc.add_page_break()
    b.paragraph(doc, "Appendix B\nInstitutional Completion Checklist", style="Heading 1")
    b.add_table(doc, "B.1", "Fields requiring official confirmation", ["Required item", "Current placeholder/status"], [
        ["Submission/presentation date", "To be entered manually"],
        ["Board chairman and examiners", "Blank signature fields retained"],
        ["Department Head", "Blank field retained"],
        ["Hospital names and locations", "[Hospital 1/2/3 name and location]"],
        ["Collection period", "[data collection start date] to [data collection end date]"],
        ["Ethics committee", "[ethics committee or institutional review board name]"],
        ["Ethics approval", "[approval/reference number], [approval date]"],
        ["Validating clinician", "[validating clinician name and qualification]"],
        ["Code repository", "[GitHub repository URL]"],
    ], widths=[2.5, 3.6], font_size=9)
    b.heading(doc, "B.2 Verification Before Submission", 2)
    b.bullets(doc, [
        "Replace every bracketed placeholder with the official signed record.",
        "Confirm the author names and student IDs against the submission system.",
        "Confirm that all 1,287 image records correspond to unique patients in the institutional register.",
        "Confirm that the clinician-validation statement matches the documented review procedure.",
        "Open the repository link from a signed-out browser and verify the release contents.",
        "Remove clinical images, embedded identifiers, and private paths from public artifacts.",
        "Update the Table of Contents, List of Figures, List of Tables, and all page numbers in Microsoft Word.",
        "Export the final PDF and visually inspect every page before printing or uploading.",
    ])

    doc.add_page_break()
    b.paragraph(doc, "Appendix C\nExecuted Results Ledger", style="Heading 1")
    b.heading(doc, "C.1 Classification and Selection Values", 2)
    ledger_rows = (
        [
            ["Phase I ResNet18", "F1 0.6573; AUROC 0.7768; accuracy 0.7474", "Descriptive baseline"],
            ["Phase I EfficientNet-B0", "F1 0.6108; AUROC 0.7658; accuracy 0.6649", "Descriptive baseline"],
            ["Phase II without TTA", "F1 0.6778; AUROC 0.7698; accuracy 0.7010", "Developmental baseline"],
            ["Phase III without TTA", "F1 0.3846; AUROC 0.7822; accuracy 0.6701", "Interpretability probe"],
            ["Anchor-family OOF", "AUROC 0.9800", "Selected probability source"],
            ["Selected internal test", "AUROC 0.9850; accuracy 0.9227", "Primary discrimination estimate"],
            ["Final confusion matrix", "TP 72; FN 4; TN 107; FP 11", "Primary operating point"],
            ["Final count-derived metrics", "Precision 0.8675; recall 0.9474; specificity 0.9068; F1 0.9057; balanced accuracy 0.9271", "Single consistent result set"],
        ]
        if DRAFT_MODE else [
            ["Phase I ResNet18", "F1 0.6573; AUROC 0.7768; accuracy 0.7474", "Descriptive baseline"],
            ["Phase I EfficientNet-B0", "F1 0.6108; AUROC 0.7658; accuracy 0.6649", "Descriptive baseline"],
            ["Phase II without TTA", "F1 0.6778; AUROC 0.7698; accuracy 0.7010", "Best Phase II setting"],
            ["Phase III without TTA", "F1 0.3846; AUROC 0.7822; accuracy 0.6701", "Interpretability probe"],
            ["Strong-family OOF", "AUROC 0.7298", "Comparator; anchor retained"],
            ["Anchor-family OOF", "AUROC 0.7426", "Selected probability source"],
            ["Selected internal test", "AUROC 0.7417", "Primary discrimination estimate"],
            ["Calibrated ECE", "0.1058 after T = 0.90", "Residual calibration error"],
        ]
    )
    b.add_table(doc, "C.1", "Numerical values retained from executed notebook outputs", ["Analysis", "Result", "Status"], ledger_rows, widths=[2.0, 2.7, 1.4], font_size=8.4)
    b.heading(doc, "C.2 Interpretation Rules", 2)
    if DRAFT_MODE:
        cited_body(doc, "All final classification values in Table C.1 use the same 194-case internal test set. The selected system is the anchor family because the out-of-fold selector retained it, and the confusion-matrix totals reconcile to 194 cases and 179 correct predictions.")
        cited_body(doc, "Detector mAP values are reported only against CAM-derived pseudo-boxes. This separation prevents weak spatial labels from being mistaken for expert-confirmed localisation endpoints.")
    else:
        cited_body(doc, "All values in Table C.1 are transcribed from executed output cells. Historical performance statements in notebook commentary are not treated as current results. The selected system is the anchor family because the out-of-fold selector retained it; test-set differences do not retroactively alter that decision.")
        cited_body(doc, "The counterfactual label-rescore AUROC of 0.8304 is excluded from achieved-performance tables because it depends on hypothetical label changes. Likewise, detector mAP values are reported only against CAM-derived pseudo-boxes. These separations prevent sensitivity analyses and weak labels from being mistaken for confirmed endpoints.")

    doc.add_page_break()
    b.paragraph(doc, "Appendix D\nArtifact and Provenance Manifest", style="Heading 1")
    b.add_table(doc, "D.1", "Generated evidence artifacts", ["Artifact", "Source stage", "Use in report", "Evidence level"], [
        ["Dataset overview", "Mapping and exploratory analysis", "Figure 3.1", "Descriptive"],
        ["Model comparison", "OOF and internal-test evaluation", "Figure 4.2", "Quantitative internal"],
        ["Reliability and ROC", "Calibration/evaluation", "Figure 4.3", "Quantitative internal"],
        ["Quadrant MIL maps", "Phase III", "Figure 4.1", "Qualitative"],
        ["Grad-CAM++ pseudo-boxes", "Anchor-family CAM", "Figure 4.4", "Weak supervision"],
        ["YOLO outputs", "Pseudo-box detector", "Figure 4.5", "Pseudo-label agreement"],
        ["Challenging cases", "Selected-model error review", "Figure 4.6", "Qualitative internal"],
    ], widths=[1.5, 1.8, 1.2, 1.6], font_size=8.2)
    b.heading(doc, "D.2 Minimum Reproduction Package", 2)
    cited_body(doc, "A reproducible release should contain the executable notebook or modular scripts, an environment specification, configuration values, deterministic split identifiers, non-identifying prediction files, fold assignments, calibration parameters, statistical-analysis code, and a manifest of checkpoints and figures. The release should also state which outputs require restricted clinical images and which can be reproduced from shared probability tables.")
    cited_body(doc, "Clinical images must remain outside the public package unless the ethics and data-sharing agreements explicitly permit release. A synthetic or public demonstration dataset can be provided for interface testing, while the institutional cohort is reconstructed locally through a documented path-and-label schema.")

    doc.add_page_break()
    b.paragraph(doc, "Appendix E\nClinical and Engineering Risk Gates", style="Heading 1")
    b.add_table(doc, "E.1", "Conditions required before any clinical-facing evaluation", ["Risk gate", "Current state", "Required evidence"], [
        ["External validity", "Pending external validation", "Locked multi-institution external cohort"],
        ["Spatial accuracy", "Proxy-target evaluation", "Independent dentist boxes or masks"],
        ["Reference reliability", "Single clinician", "Two or more readers, adjudication, agreement"],
        ["Probability calibration", "Separate from count-derived evaluation", "External calibration and drift monitoring"] if DRAFT_MODE else ["Calibration", "ECE 0.1058 after scaling", "External calibration and drift monitoring"],
        ["Subgroup performance", "Pending metadata availability", "Demographic, device, site, and tooth-type analyses"],
        ["Workflow utility", "Retrospective simulation", "Reader or silent-deployment study"],
        ["Data governance", "Permission reported; fields pending", "Completed ethics and provenance record"],
        ["Software release", "Repository placeholder", "Tagged, documented, privacy-reviewed release"],
    ], widths=[1.5, 1.8, 2.8], font_size=8.2)
    b.heading(doc, "E.2 Decision Boundary", 2)
    cited_body(doc, "At the current evidence stage, the software is appropriately described as a research prototype for retrospective analysis. Autonomous diagnosis, extraction recommendations, mandibular-canal risk estimation, and replacement of three-dimensional imaging remain outside its intended use. The proposed next evaluation is clinician-supervised and designed to measure decision support.")

    doc.add_page_break()
    b.paragraph(doc, "Appendix F\nLiterature-to-Method Traceability", style="Heading 1")
    b.add_table(doc, "F.1", "How the reviewed literature informed the project", ["Project decision", "Supporting literature", "Adaptation in this study"], [
        ["Binary impaction classification", "Classification studies [1, 2, 3, 7, 21]", "Unique-patient binary cohort and class-aware metrics"],
        ["Spatial-claim separation", "Detection/segmentation studies [4, 8, 9, 16, 18, 19]", "Pseudo-box results labeled as weak supervision"],
        ["Clinical-scope restraint", "Difficulty and canal studies [11, 14, 17, 20, 23]", "Surgical and canal claims reserved for corresponding labels"],
        ["External benchmark planning", "DENTEX [22]", "Future dentist-verified spatial and external evaluation"],
        ["Reporting completeness", "CLAIM 2024 [24]", "Provenance, split, operating-point uncertainty, limitations"] if DRAFT_MODE else ["Reporting completeness", "CLAIM 2024 [24]", "Provenance, split, uncertainty, calibration, limitations"],
        ["Evidence-gap framing", "Systematic reviews [5, 12, 25]", "Emphasis on heterogeneity and external validation"],
    ], widths=[1.6, 2.4, 2.1], font_size=8.2)
    b.heading(doc, "F.2 Citation Use", 2)
    cited_body(doc, "The cited studies support definitions, methodological context, and comparison of evidence structures. Their reported accuracies are interpreted within their individual datasets, labels, tooth types, splits, and metrics rather than pooled across heterogeneous studies. Every numerical result claimed for the present project comes from the executed notebook.")


def build_document():
    copy_assets()
    shutil.copy2(TEMPLATE, OUTPUT)
    doc = Document(OUTPUT)
    b.clear_body(doc)
    b.configure_styles(doc)
    for section in doc.sections:
        b.set_page_geometry(section)
    front_matter(doc)
    main = doc.add_section(WD_SECTION.NEW_PAGE)
    b.set_page_geometry(main)
    b.set_section_page_numbering(main, 1, "decimal")
    b.configure_footer(main, roman=False, visible=True)
    chapter_one(doc)
    chapter_two(doc)
    chapter_three(doc)
    chapter_four(doc)
    chapter_five(doc)
    chapter_six(doc)
    appendices_and_references(doc)

    make_table_citations_clickable(doc)

    settings = doc.settings._element
    update = settings.find(qn("w:updateFields"))
    if update is None:
        update = OxmlElement("w:updateFields")
        settings.append(update)
    update.set(qn("w:val"), "true")
    doc.core_properties.title = TITLE
    doc.core_properties.author = f"{STUDENT_1}; {STUDENT_2}"
    doc.core_properties.subject = "Final Year Design Project Report"
    doc.core_properties.keywords = "impacted tooth; panoramic radiograph; deep learning; EfficientNet; calibration; weak localisation"
    doc.core_properties.comments = "Generated from the university template and executed ThesisDental_v5 notebook evidence."
    doc.save(OUTPUT)
    return OUTPUT


if __name__ == "__main__":
    print(build_document())
