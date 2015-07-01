__author__ = 'tayyi'

import re


def cleanword(word):

    #word = re.sub(r'\)', "", word)

    word = word.replace(")", "")
    word = word.replace(".", "")
    word = word.replace("(", "")
    word = word.replace("/", "")
    word = word.replace(",", "")
    word = word.replace (" ", "+")
    return word

f = open("seeds2.txt","r")
f2 = open('cleaned.csv','w')
lines = f.readlines()
for line in lines:
    line = cleanword(str(line))
    print(line)
    f2.write(line)


