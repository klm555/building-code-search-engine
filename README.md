# building-code-search-engine
![Static Badge](https://img.shields.io/badge/Python-3.10.11-%233776AB?logo=Python)
![Static Badge](https://img.shields.io/badge/OpenAI-1.30.1-%23412991?logo=OpenAI)
![Static Badge](https://img.shields.io/badge/LangChain-0.2.0-%23000000)



**기준(또는 지침) 검색을 위한 프로그램 개발** 프로젝트입니다.

# 개발목표
5월 중 완료

# 진행상황
- searching algorithm (embedding) 구현중
- UI와 연결 완료

# 해결해야할 것
### 1. pdf $\rightarrow$ txt
   - 다른 방법이 있나? (unstructured in langchain community)
   - header, footer 제거
   - 수식 정리

### 2. Section별 분류 보완
   - KBC 또는 다른 기준들의 경우, pdf 형식이 다르기 때문에, 각각에 맞게 정규표현식을 수정해야 함
   - [정규표현식(regular expression)](https://wikidocs.net/1669) 스터디 필요
   - section별 분류가 잘 되지 않는 경우,
      - section을 더 잘 나눌 수 있는 알고리즘 필요
      - 해결방법을 찾지 못하는 경우, 수작업으로 분류

### 3. 출판년도별 기준 검색 기능 추가

### 4. 검색 성능 Benchmark Test

### 4. 개선 및 idea 도출을 위한 스터디
   - [자연어 처리](https://wikidocs.net/book/2155) 스터디
   - [google](https://developers.google.com/search/docs/fundamentals/how-search-works?hl=ko) 등에서 사용하는 검색 알고리즘
   - 검색 결과 ranking 매기기, ranking 또는 인기 순으로 결과 보여주기
   - 자동완성


### 기타 아이디어
- 검색어 ranking
- 인기검색어
- 자동완성

#  간략한 Flow Chart
![image](https://user-images.githubusercontent.com/95464748/235672748-5b68395f-34ac-4222-9945-2480451accd6.png)

