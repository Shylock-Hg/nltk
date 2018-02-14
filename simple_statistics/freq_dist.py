from nltk.book import *

print(type(text1))

#frequence of token sort by freq from high to low
fdist = FreqDist(text1)
print(type(fdist))

#get most frequent token
head = list(fdist.keys())[:10]
print('The most frequent tokens:')
print(head)
print('\n')

#get least frequent tokens
tail = list(fdist.keys())[-10:]
print('The least frequent tokens:')
print(tail)
print('\n')
