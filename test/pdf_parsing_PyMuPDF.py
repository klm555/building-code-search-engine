import os
import fitz
# TESSDATA_PREFIX = C:\Program Files\Tesseract-OCR\tessdata

pdf_name = '페이지 1.pdf'

# with fitz.open(os.path.join('./data', pdf_name)) as doc, open('output.txt', 'w', encoding='utf8') as f:
#     for page in doc:
#         partial_tp = page.get_textpage_ocr(flags=0, full=False)
#         text = page.get_text(textpage=partial_tp)
#         f.write(text)

with fitz.open(os.path.join('./data', pdf_name)) as doc, open('output.txt', 'w', encoding='utf8') as f:
    for page in doc:
        text = page.get_text()
        f.write(text)