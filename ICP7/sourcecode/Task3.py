# Task:Parts of Speech Tagging on the text output
import nltk
nltk.download('averaged_perceptron_tagger')
f = open('input.txt', 'r', encoding='utf-8')
input = f.read()
wtokens = nltk.word_tokenize(input)
print("\n")
print("Parts of Speech Tagging on the text output")
print(nltk.pos_tag(wtokens))