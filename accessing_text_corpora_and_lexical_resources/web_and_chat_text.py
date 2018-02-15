from nltk.corpus import webtext
from nltk.corpus import nps_chat

#webtext overview
for idx in webtext.fileids():
    print('file={} , words={}'.format(idx,len(webtext.words(idx))))

