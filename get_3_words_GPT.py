import os
import platform
import re
import PyPDF2
import fitz

import openai
import langchain

from langchain import VectorDBQA, PromptTemplate
from langchain.llms import OpenAI

query = '등가정적해석법에서 밑면전단력 어떻게 구함?'

#%% query에서 가장 중요한 검색어 추출 (with GPT)

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

print(search_words)

#%% PDF 불러오기
pdf_name = 'KDS 41 17 00 건축물 내진설계기준.pdf'

pdf = PyPDF2.PdfReader(os.path.join('./data', pdf_name))    

# 검색 후 페이지 저장
# with open('output.txt', 'w', encoding='utf8') as f:
result_page = []
page_count = 0
for page in pdf.pages:
    # Ignore Header and Footer
    parts = []
    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > 50 and y < 700:
            parts.append(text)

    text = page.extract_text(visitor_text=visitor_body)
    # f.write(text)   
    
    if all(x in text for x in search_words):
        result_page.append(page_count)    
    page_count += 1

page_count = 0
for page in pdf.pages:
    # Ignore Header and Footer
    parts = []
    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > 50 and y < 700:
            parts.append(text)

    text = page.extract_text(visitor_text=visitor_body)
    
    if all(x in text for x in search_words[:-1]):
        result_page.append(page_count)    
    page_count += 1

# for page in pdf.pages:
#     text = page.extract_text()    
#     if all(x in text for x in search_words[:-2]):
#         result_page.append(page_count)    
#     page_count += 1


for i in result_page:
    page = pdf.pages[int(i)] 
    print(page.extract_text())



#%% txt 파일에서 검색어가 포함된 문단 추출
'''
# text 파일 Parsing
with open('output.txt', 'r', encoding='utf8') as f:
    text = f.read()

pattern = r"^\d+(?:\.\d+)+\b(.*)((?:\n(?!\d+\.\d).*)*)"

# text 파일에서 문단별로 나누기
sections = re.split(pattern, text)

result = []
for section in sections:
    if all(x in section[1] for x in search_words):
        result.append(section)
    
    elif all(x in section[0] for x in search_words[:-1]):
        result.append(section)

    elif all(x in section[0] for x in search_words[:-2]):
        result.append(section)
'''
        


