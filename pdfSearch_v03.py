import os
import PyPDF2
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import webbrowser

# def open_pdf(file_path, page_num):
#     pdf_writer = PyPDF2.PdfWriter()
#     pdf_writer.add_page(PyPDF2.PdfReader(open(file_path, 'rb')).pages[page_num-1])
#     with open('temp/temp.pdf', 'wb') as f:
#         pdf_writer.write(f)
#     os.startfile('temp/temp.pdf')

def open_pdf(file_path):
    os.startfile(file_path)

link_window = tk.Tk()
link_window.withdraw() # 창 비활성화

file_path = filedialog.askopenfilename()

# PDF 파일 불러오기(KDS 41 12)
pdf_file = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 사용자로부터 단어 입력 받기
keyword_str = simpledialog.askstring("검색", "단어를 입력하세요(여러 개의 단어는 쉼표로 구분):") # 일단 simpledialog 사용
keywords = [k.strip() for k in keyword_str.split(",")] # 쉼표 기준 분리

# 각 페이지에서 단어를 찾기
found_pages = []
for i, page in enumerate(pdf_reader.pages):
    text = page.extract_text() 
    if all(re.search(keyword, text) for keyword in keywords):
        found_pages.append(i + 1)

# 검색 결과 출력
if found_pages:
    result = "단어 '{}'가 모두 포함된 페이지: {}".format(keyword_str, found_pages)
    messagebox.showinfo("검색 결과", result)
else:
    result = "단어 '{}'가 모두 포함된 페이지를 찾을 수 없습니다.".format(keyword_str)
    messagebox.showinfo("검색 결과", result)

# 검색된 페이지의 내용을 각각의 pdf 형식으로 출력
folder_path = 'temp'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for page_num in found_pages:
    pdf_writer = PyPDF2.PdfWriter()
    page = pdf_reader.pages[page_num-1]
    pdf_writer.add_page(page)
    file_name = f"검색결과_{page_num}.pdf" # 생성될 pdf 파일명
    file_path = os.path.join(folder_path, file_name)
    pdf_output = open(file_path, "wb")
    pdf_writer.write(pdf_output)
    pdf_output.close()
    # messagebox.showinfo("PDF 파일 생성 완료", f"PDF 파일 '{file_name}'에 임시 저장됨") 

    # 링크 생성
    link = tk.Label(link_window, text=f"페이지 {page_num}", fg="black", cursor="hand2", anchor="center") # hand2 : 커서가 링크 위에 있을 때 손가락 모양
    link.grid(row=page_num, column=0, padx=10, pady=10, sticky='nsew') # link 위치 설정
    link.bind("<Button-1>", lambda e, file_path=file_path: open_pdf(file_path))

# PDF 파일 닫기
pdf_file.close()

# link_window 크기 조정 및 실행
link_window.geometry('180x180')
link_window.deiconify()  # 창 활성화
link_window.mainloop()
