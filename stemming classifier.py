from konlpy.tag import Kkma
from nltk.tag import pos_tag
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
#from konlpy.utils import pprint 프린트 출력 관련
from googletrans import Translator
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer

def Kor_classifier(text):
    kkma = Kkma()
    result = (kkma.pos(text))
    return result

def Eng_classifier(text):
    word = word_tokenize(text)
    tag = nltk.pos_tag(word)
    return tag

def Encryption(text):
    translator = Translator()
    result = translator.translate(text, src='ko', dest = 'en')
    return result.text

def Decryption(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest = 'ko')
    return result.text

def Stemmer(text):
    stemmer = PorterStemmer()
    result = stemmer.stem(text)
    return result

string = input("문장 입력 : ")

kor = Kor_classifier(string)
enc = Encryption(string)
eng = Eng_classifier(enc)
dec = Decryption(enc)

print(kor)

temp = [ ]
for key, value in kor:
        temp.append(key)
        
tmp = [ ]
for key, value in eng:
    if value[0] == 'N' or value[0] == 'V':
        if value[0] == 'V' :        
            tmp.append(Stemmer(key))
        else:
            tmp.append(key)
        
print(temp)
print(enc)
print(eng)
print(tmp)
print(dec)

