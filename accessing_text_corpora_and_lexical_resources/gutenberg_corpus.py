import nltk

#show the corpus name
print(nltk.corpus.gutenberg.fileids())

#load text emma
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print(type(emma))

#simple statistics of gutenberg corpus
for fid in nltk.corpus.gutenberg.fileids():
    num_char = len(nltk.corpus.gutenberg.raw(fid))
    num_word = len(nltk.corpus.gutenberg.words(fid))
    num_sent = len(nltk.corpus.gutenberg.sents(fid))
    num_volc = len(set([w for w in nltk.corpus.gutenberg.words(fid)]))
    print('{} , {} , {} , {}'.format(int(num_char/num_word),int(num_word/num_sent),int(num_word/num_volc),fid))
