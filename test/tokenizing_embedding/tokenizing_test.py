#%% Word Tokenization (NLTK)
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer

text = 'I am actively looking for Ph.D. students.'
print(word_tokenize(text))
print(WordPunctTokenizer().tokenize(text))
treebank = TreebankWordTokenizer()
print(treebank.tokenize(text))

#%% Sentence Tokenization (NLTK)
from nltk.tokenize import sent_tokenize

text = 'I am actively looking for Ph.D. students. And you are a Ph.D. student.'
print(sent_tokenize(text))

#%% Part-of-speech Tagging (NLTK)
from nltk.tag import pos_tag

tokenized_sentence = word_tokenize(text)
print(pos_tag(text))
print(pos_tag(tokenized_sentence))

#%% Morpheme Tokenization (KoNLPy)
from konlpy.tag import Okt
from konlpy.tag import Kkma

text = '열심히 코딩한 당신, 연휴에는 여행을 가봐요'

okt = Okt()
kkma = Kkma()

print(okt.morphs(text))
print(kkma.morphs(text))

#%% Part-of-speech Tagging (KoNLPy)
from konlpy.tag import Okt
from konlpy.tag import Kkma

text = '열심히 코딩한 당신, 연휴에는 여행을 가봐요'

okt = Okt()
kkma = Kkma()

print(okt.pos(text))
print(kkma.pos(text))

#%% Extracting Nouns (KoNLPy)
from konlpy.tag import Okt
from konlpy.tag import Kkma

text = '열심히 코딩한 당신, 연휴에는 여행을 가봐요'

okt = Okt()
kkma = Kkma()

print(okt.nouns(text))
print(kkma.nouns(text))

#%% Sentence Tokenization (KSS)
import kss

text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다.'
print(kss.split_sentences(text))
