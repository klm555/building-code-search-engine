import os
import platform
import re
import ast
import PyPDF2
import fitz

import openai
import langchain

from langchain import VectorDBQA, PromptTemplate
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

import pre_process # pre_process.py

#%% Example 1 - KDS 22
##### 사용자 입력
query = '등가정적해석법에서 밑면전단력 어떻게 구함?'

# pdf 파일 경로
pdf_name = r'C:\Users\hwlee\Desktop\Python\building-code-search-engine\data\KDS 41 17 00 건축물 내진설계기준.pdf'
start_page = 9 # 표지, 목차 등 제외
end_page = 130

# openai api key
os.environ["OPENAI_API_KEY"] = "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"


##### pre_process.py의 pdf2section 함수 사용하여 
# pdf->section 단위로 분할하여 txt로 저장
pre_process.pdf2section(pdf_name, start_page=start_page, end_page=end_page)

# 저장된 txt 파일을 읽어서 list로 변환
with open('converted_txt/KDS 41 17 00 건축물 내진설계기준.txt', 'r', encoding='utf8') as f:
    section_list = ast.literal_eval(f.read())


##### query에서 가장 중요한 검색어 추출 (with GPT)
llm = OpenAI(temperature=0)

# 프롬프트 템플릿
template_extract = """ List the important words in '{query}' in order of importance with one sentence delimited by ','. """

# 프롬프트 생성
prompt_extract = PromptTemplate(input_variables=['query'], template=template_extract)
final_prompt_extract = prompt_extract.format(query=query)

# 추출된 검색어를 list로 저장
search_words = []
for i in llm(final_prompt_extract).split(','):
    i = re.sub('\n', '', i)
    i = re.sub(' ', '', i) 
    if i != '':
        search_words.append(i)


##### 검색 후 페이지 번호 저장
result_page = []

# 검색어가 포함된 페이지 번호 저장
for section in section_list:
    if all(x in section[3] for x in search_words):
        result_page.append(section[1])

# 검색어가 포함된 페이지 번호 저장 (우선순위 가장 낮은 검색어 1개 제외)
for section in section_list:
    if all(x in section[3] for x in search_words[:-1]):
        result_page.append(section[1])

# 검색어가 포함된 페이지 번호 저장 (우선순위 가장 낮은 검색어 2개 제외)
for section in section_list:
    if all(x in section[3] for x in search_words[:-2]):
        result_page.append(section[1])

#%% Example 2 - ASCE 17
##### 사용자 입력
query = 'How to calculate the base shear force with the equivalent static method?'
# query = 'shear stress concrete frames'

# pdf 파일 경로
pdf_name = r'C:\Users\hwlee\Desktop\Python\building-code-search-engine\data\[US] ASCE SEI 41-17 Seismic Evaluation and Retrofit of Existing Buildings.pdf'
start_page = 66 # 표지, 목차 등 제외
end_page = 601

# openai api key
os.environ["OPENAI_API_KEY"] = "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"

##### pre_process.py의 pdf2section 함수 사용하여 
# pdf->section 단위로 분할하여 txt로 저장
pre_process.pdf2section(pdf_name, start_page=start_page, end_page=end_page)

# 저장된 txt 파일을 읽어서 list로 변환
with open('converted_txt/[US] ASCE SEI 41-17 Seismic Evaluation and Retrofit of Existing Buildings.txt', 'r', encoding='utf8') as f:
    section_list = ast.literal_eval(f.read())


##### query에서 가장 중요한 검색어 추출 (with GPT)
llm = OpenAI(temperature=0)

# 프롬프트 템플릿
template_extract = """ List the important words in '{query}' in order of importance with one sentence. """

# 프롬프트 생성
prompt_extract = PromptTemplate(input_variables=['query'], template=template_extract)
final_prompt_extract = prompt_extract.format(query=query)
test = llm(final_prompt_extract)

# 추출된 검색어를 list로 저장
search_words = []
for i in llm(final_prompt_extract).split('.'):
    if ':' in i: 
        i = i.split(':')[0]
        search_words.append(i.strip(' '))

##### 검색 후 페이지 번호 저장
result_page = []

# 검색어가 포함된 페이지 번호 저장
for section in section_list:
    if all(x.casefold() in section[3].casefold() for x in search_words): # casefold() : 대소문자 구분 없이 비교
        result_page.append(section[1])

# 검색어가 포함된 페이지 번호 저장 (우선순위 가장 낮은 검색어 1개 제외)
for section in section_list:
    if all(x.casefold() in section[3].casefold() for x in search_words[:-1]):
        result_page.append(section[1])

# 검색어가 포함된 페이지 번호 저장 (우선순위 가장 낮은 검색어 2개 제외)
for section in section_list:
    if all(x.casefold() in section[3].casefold() for x in search_words[:-2]):
        result_page.append(section[1])