from konlpy.tag import Kkma
from nltk.tag import pos_tag
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
from googletrans import Translator

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
    tmp.append(key)

print(temp)
print(enc)
print(eng)
print(tmp)
print(dec)

