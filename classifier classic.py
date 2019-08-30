from konlpy.tag import Kkma
from nltk.tag import pos_tag
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
'''from konlpy.utils import pprint 프린트 출력 관련'''
from googletrans import Translator
'''from nltk.stem.porter import PorterStemmer'''
from nltk.stem.wordnet import WordNetLemmatizer

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

'''def Stemmer(text):
    stemmer = PorterStemmer()
    result = stemmer.stem(text)
    return result'''

def Lemmatizer(text, pos1):
    lemmatizer = WordNetLemmatizer()
    result = lemmatizer.lemmatize(text,pos = pos1)
    return result

strings = input("문장 입력 : ")

kkma = Kkma()
sentence = kkma.sentences(strings)
for string in sentence:
    kor = Kor_classifier(string)
    enc = Encryption(string)
    eng = Eng_classifier(enc)
    
    print(kor)

    temp = [ ]
    for key, value in kor:
        if value[0] == 'N' or value[0] == 'V':
            if value == 'VV':
                key += '다'
                temp.append(key)
            else:
                temp.append(key)
    
    tmp1 = [ ]
    for key, value in eng:
        if value[0] == 'N' or value[0] == 'V' or value[0] == 'J' or value == 'IN':
            if value[0] == 'V' :        
               tmp1.append(Lemmatizer(key, 'v'))
            elif value[0] == 'J':
               tmp1.append(Lemmatizer(key, 'a'))
            elif value == 'IN':
                word = tmp1.pop()
                isverb = Eng_classifier(word)
                if isverb[0][1] == 'VB':
                    tmp1.append(word + ' ' + key)
                else :
                    tmp1.append(word)
            else:
                tmp1.append(key)

    tmp2 = []          
    for char in tmp1:
        tmp2.append(Decryption(char))

    res = ''
    for char1 in temp:
        for char2 in tmp2:
            if char1 == char2:
                res += (' ' + char2)
        
    print(temp)
    print(enc)
    print(eng)
    print(tmp1)
    print(tmp2)
    print(res)

