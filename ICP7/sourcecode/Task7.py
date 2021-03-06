# Task: Named Entity Recognition
import nltk
print("\n")
print("Task: Named Entity Recognition")
f = open('input.txt', 'r', encoding='utf-8')
input = f.read()
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
stokens = nltk.sent_tokenize(input)
for i in stokens:
    print(ne_chunk(pos_tag(wordpunct_tokenize(i))))