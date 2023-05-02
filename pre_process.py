import os
import re
import PyPDF2
import ast


def pdf2section(pdf_file, start_page=1, end_page=0):
    r'''
    기준(또는 지침) pdf 파일을 section 단위로 분할하여 txt로 출력하는 함수.
    
    * KDS(2022) 형식에 맞춰 작성되었으며, 추후 다른 기준에 맞춰 수정 필요.
    * PyPDF2 패키지를 사용하여, 이미지 형식의 pdf 파일은 읽을 수 없음.
    
    Parameters
    ----------
    pdf_file : str
    기준(또는 지침) pdf 파일. (ex. 'C:\Users\KDS 41 17 00 건축물 내진설계기준.pdf')
                 
    start_page : int, optional, default=1
    pdf에서 변환을 시작할 페이지. 표지 또는 목차 등을 제외할 때 사용 가능함.
    end_page : int, optional, default=0
    pdf에서 변환을 종료할 페이지. 입력하지 않을 경우(end_page=0), pdf의 마지막 페이지로 설정.
                
    Returns
    -------
    txt 파일 : list of tuples - (Code Name, Page Number, Section Title, Section Content)
    
    * With line 110,111 : txt파일을 불러와 list of tuples로 변환하여 사용 가능.
    
    Other Parameters
    ----------------
    None
    
    Raises
    -------
    None
    '''

    # 파일명 읽을 때 생기는 unicode error 방지
    pdf_file = pdf_file.replace('\\', '/') # pdf_file의 경로를 '/'로 통일

    # PdfReader 객체 생성, pdf 파일 읽기
    pdf = PyPDF2.PdfReader(pdf_file)

    # 변수 정리
    code_name = os.path.basename(pdf_file).split('.')[0] # 기준(또는 지침) 이름
    if end_page == 0: # end_page가 0이면, pdf의 마지막 페이지로 설정
        end_page = len(pdf.pages)

    # pdf 내용 추출 후, 추후 section으로 나누기 용이한 형식의 text로 변환
    structured_text = ''
    for i in range(start_page-1, end_page):
        page = pdf.pages[i]
        text = page.extract_text()
        structured_text += '###{}###'.format(str(i+1)) + text + '\n'

    # structured_text를 먼저 line 단위로 분할
    lines = structured_text.split('\n')
    lines = [s + '\n' for s in lines] # 각 line의 마지막에 '\n' 추가 (optional. 필요에 따라 제거 가능)

    # section 단위로 분할
    section_list = []
    title = ''
    content = ''
    for line in lines:
        # 기준(또는 지침) 이름
        code = code_name

        # Page Number를 포함하는 line
        if line.startswith('###'):
            page = line.split('###')[1] # ###가 또 나오기 전까지는 변하지 않음

        # Chapter Number로 시작하는 line
        elif re.match('[0-9]+[.]', line): # 해당 패턴으로 시작되는 라인 찾기. *** regex 패턴 수정 필요!!! ***
            title = line
            content = '' # content 초기화

        # Page Number, Champter Number 모두 없는 line
        else:
            content += line

        # section tuple 생성
        section = (code, page, title, content)
        section_list.append(section)

    # section_list에서 필요한 elements만 slice
    remove_list = []

    for i in range(len(section_list)-1):
        if len(section_list[i][3]) < len(section_list[i+1][3]):
            remove_list.append(i)

    for i in remove_list[::-1]:
        section_list.pop(i) # section_list : tuple(Code Name, Page Number, Section Title, Section Content)

    # 변환된 txt를 별도로 저장할 폴더 생성
    if not os.path.exists('converted_txt'):
        os.mkdir('converted_txt')
    
    # section_list를 txt 파일로 저장
    with open('converted_txt/{}.txt'.format(code_name), 'w', encoding='utf8') as f:
        f.write(str(section_list))

# test
pdf2section(r'C:\Users\hwlee\Desktop\Python\building-code-search-engine\data\KDS 41 17 00 건축물 내진설계기준.pdf'
            , start_page=9, end_page=130)
# test - txt 파일을 읽어서 list로 변환
with open('converted_txt/KDS 41 17 00 건축물 내진설계기준.txt', 'r', encoding='utf8') as f:
    section_list = ast.literal_eval(f.read())