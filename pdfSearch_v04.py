import os
import PyPDF2
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import webbrowser

import openai
import langchain

from langchain import VectorDBQA, PromptTemplate
from langchain.llms import OpenAI

# 사용자 질문 입력 받기
query = simpledialog.askstring("검색", "질문을 입력하세요:")
root.geometry("500x300")

# query에서 가장 중요한 검색어 추출 (with GPT)
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0)
template = """ List the important words in '{query}' in order of importance with one sentence delimited by ','. """
prompt = PromptTemplate(input_variables=['query'], template=template)
final_prompt = prompt.format(query=query)
# 추출된 검색어를 list로 저장
search_words = []
for i in llm(final_prompt).split(','):
    i = re.sub('\n', '', i)
    i = re.sub(' ', '', i) 
    if i != '':
        search_words.append(i)

# PDF 파일 선택
link_window = tk.Tk()
link_window.withdraw()
file_path = filedialog.askopenfilename()

# PDF 파일 불러오기(KDS 41 12)
pdf_file = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 각 페이지에서 검색어 찾기
found_pages = []
for i, page in enumerate(pdf_reader.pages):
    text = page.extract_text() 
    if all(re.search(keyword, text) for keyword in search_words):
        found_pages.append(i + 1)

# 검색 결과 출력
if found_pages:
    result = "단어 '{}'가 모두 포함된 페이지: {}".format(', '.join(search_words), found_pages)
    messagebox.showinfo("검색 결과", result)
else:
    result = "단어 '{}'가 모두 포함된 페이지를 찾을 수 없습니다.".format(', '.join(search_words))
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

    # 링크 생성
    link = tk.Label(link_window, text=f"페이지 {page_num}", fg="black", cursor="hand2", anchor="center")
    link.grid(row=page_num, column=0, padx=10, pady=10, sticky='nsew')
    link.bind("<Button-1>", lambda e, file_path=file_path: webbrowser.open(file_path))

# PDF 파일 닫기
pdf_file.close()

# link_window 크기 조정 및 실행
link_window.geometry('180x180')
link_window.deiconify
