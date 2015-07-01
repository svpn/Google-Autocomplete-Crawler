__author__ = 'tayyi'

#THIS FILE extracts 'important' words from files for future processing
#Uses POS tagger extract nouns and JJ + nouns

import nltk


import os
import codecs
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict

filename = "sample2.txt"
path = os.path.dirname(os.path.realpath(__file__))

os.chdir(path)
print(path)


file = codecs.open(filename,'r','utf-8')
text = file.read()

thelist = []
tokenizer = RegexpTokenizer(r'\w+')
tokenized = nltk.word_tokenize(text)
#tokenized = tokenizer.tokenize(text)
#print(tokenized)
tagged = nltk.pos_tag(tokenized)
print(tagged)
#extract = [word for word,pos in tagged if pos == 'JJ']
#print(extract)

for i, (word,pos) in enumerate(tagged):
    if i+1 < len(tagged):
        get_next = tagged[i+1]
    if i+2 < len(tagged):
        get_next2 = tagged[i+2]

    if pos == 'JJ':
        if get_next[1]=="NN" or get_next[1]=="NNS":
            thelist.append(word + " " + get_next[0])
            '''
        if get_next2[1]=="NN" or get_next2[1]=="NNS":
            thelist.append(word + " " + get_next[0] + " " + get_next2[0])
            '''


    if pos == 'NN' or pos == 'NNS':
        thelist.append(word)
        if get_next[1] == "NN" or get_next[1] == "NNS":
            thelist.append(word + " " + get_next[0])
            '''
        if get_next2[1] == "NN" or get_next2[1] == "NNS":
            thelist.append(word + " " + get_next[0] + " " + get_next2[0])
'''



namedEnt = nltk.ne_chunk(tagged, binary = True)
#print(namedEnt)
result = np = [' '.join([y[0] for y in x.leaves()]) for x in namedEnt.subtrees() if x.label() == "NE"]
#print(result)
for item in result:
    thelist.append(item)
print(len(thelist))
thelist = set(thelist)
print(len(thelist))
print(thelist)

with open("seeds2.txt", "a") as myfile:
    for item in thelist:
        print(item)
        item = item.encode('utf-8')
        item = item.decode('utf-8')
        #string = item.decode()
        try:
            myfile.write(str(item) +'\n')
        except:
            print("error decoding:")
            print(item)
            pass





