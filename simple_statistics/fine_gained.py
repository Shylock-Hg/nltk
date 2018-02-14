from nltk.book import *

#select tokens by length range
limit = set([w for w in text1 if len(w) > 4 and len(w) < 7])
print(len(limit))

#get distribution of token length
lens = [len(w) for w in text1]
ldist = FreqDist(lens)
#print occur most frequentlly tokens
head = list(ldist.keys())[:5]
print('The most frequent tokens:')
print(head)
#print occur least frequentlly tokens
tail = list(ldist.keys())[-5:]
print('The least frequent tokens:')
print(tail)
