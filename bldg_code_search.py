input_pdf = r'C:\Users\hwlee\Desktop\Python\building-code-search-engine\KDS 41 17 00 건축물 내진설계기준.pdf'

# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader

# # creating a pdf reader object
# reader = PdfReader(input_pdf)

# # printing number of pages in pdf file
# print(len(reader.pages))

# # getting a specific page from the pdf file
# page = reader.pages[29]

# # extracting text from page
# text = page.extract_text()
# print(text)


# import fitz

# doc = fitz.open(input_pdf)
# page = doc[29]
# text = page.get_text()
# print(text)

from pdfreader import SimplePDFViewer, PageDoesNotExist

with open(input_pdf, 'rb') as f:
    viewer = SimplePDFViewer(f)

    text = ''
    pdf_markdown = ''
    images=[]
    try:
        while True:
            viewer.render()
            text += ''.join(viewer.canvas.strings)
            pdf_markdown += viewer.canvas.text_content
            images.extend(viewer.canvas.inline_images)
            images.extend(viewer.canvas.images.values())
            viewer.next()
    except PageDoesNotExist:
        pass
    
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
with open('pdf_markdown.txt', 'w', encoding='utf-8') as f:
    f.write(pdf_markdown)