# Task: Trigram
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
f = open('input.txt', 'r', encoding='utf-8')
input = f.read()
stokens = nltk.sent_tokenize(input)
print("\n")
print("Trigram")
for sent in stokens:
    wtokens = nltk.word_tokenize(sent)
    for j in range(len(wtokens) - 2):
        print(wtokens[j], wtokens[j + 1], wtokens[j + 2])