from nltk.book import *

#the bigrams
pairs = bigrams(['w0','w1','w2','w3','w4'])
for item in pairs:
    print(item)

#the collocations
cols = text1.collocations()
print(cols)
