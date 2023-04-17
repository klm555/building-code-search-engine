import os
import PyPDF2
# TESSDATA_PREFIX = C:\Program Files\Tesseract-OCR\tessdata

pdf_name = '페이지 1.pdf'

pdf = PyPDF2.PdfReader(os.path.join('./data', pdf_name))    

with open('output.txt', 'w', encoding='utf8') as f:
    for page in pdf.pages:
        text = page.extract_text()
        f.write(text)
