from django.shortcuts import render
from django.http import HttpResponse
from .forms import TxtForm
from konlpy.tag import Kkma
from nltk.tag import pos_tag
import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
'''from konlpy.utils import pprint 프린트 출력 관련'''
from googletrans import Translator
'''from nltk.stem.porter import PorterStemmer'''
from nltk.stem.wordnet import WordNetLemmatizer
from django.views.decorators.csrf import csrf_exempt

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

def index(request):
    return render(request, 'classifier/index.html')

@csrf_exempt
def form_test(request):
    kkma = Kkma()
    translator = Translator()
    if request.method == 'POST':
        form = TxtForm(request.POST)
        if form.is_valid():
            count = 0
            strings = request.POST['text']
            sen_spilt = strings.splitlines()
            while '' in sen_spilt:
                sen_spilt.remove('')
            sen = []
            for senten in sen_spilt:
                result = []
                sentence = kkma.sentences(senten)
                for string in sentence:
                    kor = kkma.pos(string)
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
                        temp1_result = translator.translate(key, src='ko', dest = 'en')     
                        temp1.append(temp1_result.text)

                    temp2 = []
                    for key in temp1:
                        temp2.append(Eng_classifier(key))

                    temp3 = []
                    for num in range (len(temp2)):                   
                        for num1 in range(len(temp2[num])):
                            if temp2[num][num1][1][0] == 'N' or temp2[num][num1][1][0] == 'V' or temp2[num][num1][1] == 'JJ' or temp2[num][num1][1] == 'IN' or temp2[num][num1][1] == 'RB' or temp2[num][num1][1] == 'RP':
                                if temp2[num][num1][1] == 'IN' or temp2[num][num1][1] == 'RP':
                                    if not temp3:
                                        temp3.append(temp2[num][num1][0])
                                    else:
                                        word = temp3.pop()
                                        isverb = Eng_classifier(word)
                                        if isverb[0][1][0] == 'V':
                                            temp3.append(word + ' ' + temp2[num][num1][0])
                                        else :
                                            temp3.append(word)
                                elif temp2[num][num1][1] == 'RB':
                                    if not temp3:
                                        temp3.append(temp2[num][num1][0])
                                    else:
                                        word = temp3.pop()
                                        isverb = Eng_classifier(word)
                                        if isverb[0][1] == 'JJ':
                                            temp3.append(temp2[num][num1][0] + ' ' + word )
                                        else :
                                            temp3.append(word)
                                else:
                                    temp3.append(temp2[num][num1][0])
                    temp4 = {}#최종적으로 사용될 딕셔너리 temp4(영어) temp5(한글)
                    temp5 = {}
                    for key in temp3:
                        temp5_result = translator.translate(key, src='en', dest = 'ko')
                        temp4[key] = count
                        temp5[temp5_result.text] = count

                    result.append(json.dumps(temp5, ensure_ascii=False))
                sen.append(result)
            return HttpResponse(sen)
        else:
            return('fail')

    elif request.method == 'GET':
        form = TxtForm()
        return render(request, 'classifier/form.html',{'form':form}) 
# Create your views here.
