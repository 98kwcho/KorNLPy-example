from konlpy.tag import Kkma
#from konlpy.utils import pprint 프린트 출력 관련
from googletrans import Translator

translator = Translator();
kkma = Kkma()
dic = (kkma.pos(u'지금은 형태소 분석 실험 중입니다. '))
print(dic)

temp = [ ]

for key, value in dic:
        temp.append(key)

print(temp)
    
trans = translator.translate('지금은 형태소 분석 실험 중입니다.', src='ko', dest = 'en')

print(trans)
