# Task:Stemming
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
ps = PorterStemmer()
sb = SnowballStemmer('english')
lc = LancasterStemmer()
f = open('input.txt', 'r', encoding='utf-8')
input = f.read()
wtokens = nltk.word_tokenize(input)
print("\n")
print("Stemming")
for x in wtokens:
    print(ps.stem(x))
    print(sb.stem(x))
    print(lc.stem(x))