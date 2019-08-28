from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer

stemmer = LancasterStemmer()
stemmer1 = PorterStemmer()

print(stemmer.stem('enters'))
print(stemmer.stem('enter'))
print(stemmer.stem('entering'))
print(stemmer.stem('cookery'))

print(stemmer1.stem('enter'))
print(stemmer1.stem('enters'))
print(stemmer1.stem('entering'))

print(stemmer1.stem('computing'))
