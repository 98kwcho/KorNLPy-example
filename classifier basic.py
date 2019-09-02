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
count = 0
kkma = Kkma()
sentence = kkma.sentences(strings)
for string in sentence:
    kor = Kor_classifier(string)
    count += 1
    temp = {}
    for key, value in kor:
        if value[0] == 'N' or value[0] == 'V':
            if value[0] == 'V':
                key += '다'
                temp[key]  = value
            else:
                temp[key]  = value

        temp1 = []
        for key in list(temp.keys()):        
            temp1.append(Encryption(key))

        temp2 = []
        for key in temp1:
            temp2.append(Eng_classifier(key))

        temp3 = []
        for num in range (len(temp2)):
                if temp2[num][0][1][0] == 'N' or temp2[num][0][1] == 'VB' or temp2[num][0][1] == 'JJ' or temp2[num][0][1] == 'IN' or temp2[num][0][1] == 'RB' :
                    if temp2[num][0][1] == 'IN':
                        if not temp3:
                            temp3.append(temp2[num][0][0])
                        else:
                            word = temp3.pop()
                            isverb = Eng_classifier(word)
                            if isverb[0][1] == 'VB':
                                temp3.append(word + ' ' + temp2[num][0][0])
                            else :
                                temp3.append(word)
                    elif temp2[num][0][1] == 'RB':
                        if not temp3:
                            temp3.append(temp2[num][0][0])
                        else:
                            word = temp3.pop()
                            isverb = Eng_classifier(word)
                            if isverb[0][1] == 'JJ':
                                temp3.append(temp2[num][0][0] + ' ' + word )
                            else :
                                temp3.append(word)
                    else:
                        temp3.append(temp2[num][0][0])
        temp4 = {}
        temp5 = {}
        for key in temp3:
            temp4[key] = count
            temp5[Decryption(key)] = count
        
print(temp)
print(temp1)
print(temp2)
print(temp2[0][0])
print(temp3)
print(temp4)
print(temp5)
