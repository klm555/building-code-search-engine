import os
from unstructured.partition.auto import partition

pdf_name = '페이지 1.pdf'

elements = partition(os.path.join('./data', pdf_name), strategy='hi_res')

elements = group_broken_paragraphs(elements, paragraph_split='\n\n')
    
with open('output.txt', 'w', encoding='utf8') as f:
    for el in elements:
        f.write(str(el))

# print('\n\n'.join([str(el) for el in elements]))