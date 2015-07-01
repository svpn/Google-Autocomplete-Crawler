import csv
import os
from random import randint
import urllib
from string import ascii_lowercase
import urllib.request
import re
import time
import sys
import getopt

'''
Python Script to automatically crawl suggestions off Google's Suggest Algorithm
Version 0.0.1
Requires Python 3.4 

Takes a CSV file as an input. Passes each line to Google Suggest Algorithm
Appends to a result.txt file of the crawled suggestion data.

COMMAND LINE Usage
run 
python suggest.py -i "seed.csv" -o "output.txt" 

optional arguments -dp 
(don't persist)

'''

#PARAMETERS


END_POINT = "http://suggestqueries.google.com/complete/search?output=firefox&client=firefox&hl=en-US&q="
SLEEP_LOWER_LIMIT = 1       #lower window edge for randomized sleep time
SLEEP_UPPER_LIMIT = 3       #upper window edge for randomized sleep time


#Example csv contains nothing but examples, you may run the script without any arguments and it will parse example.csv. 
#You may also add your seed words to example.csv to test this script
SEED_FILE = "example.csv" 
PERSIST_SEEDS = "persist_seeds.txt" 
RESULT_FILE = "result.txt"
#If a command line arg for output is not specified. it will simply output to result.txt

#friendly reminder:please put + between spaces in the seed word list. for example Jurong+East instead of Jurong East

PERSIST = True; #Want to persist while crawling or not. Default is true 

# A seedword that is crawled before is persisted. 
# So as to not recrawl what has been crawled before.
# Useful when dealing with internet disconnections
# Automatically find where you have stopped last
 
#Appending a question prefix to generate more queries
#Google automatically knows if seed word is a noun or place or whatever. Try it.  
PREFIX = ['Why+','Who+','Where+','Can+','When+','What+','Are+','Is+',"Do+","Did+","How+"] #to generate question suggestions


def generateQueries(query):

    link = END_POINT +query
    with urllib.request.urlopen(link) as url:
        s = url.read()

    s = str(s)
    print(s)

    list = re.findall('"([^"]*)"', s)
    print("counting...")
    print(len(list))

    count = 0
    #finally write everything - append to result file
    with open(RESULT_FILE, "a") as myfile:
        for i,item in enumerate(list):
            if(i==0):
                #ignore the first item, which is usually the actual query-word itself
                print(item)
                continue
            myfile.write(item +'\n')
            count+=1
    print(count,"queries written to file")

    myfile.close()
    print("Resting :)")
    #Sleep is not technically needed. But good. Because you don't want to get banned
    #I have never gotten banned before, but I suppose crawling repeatedly without any sleep time is suspicious behaviour
    time.sleep(randint(SLEEP_LOWER_LIMIT,SLEEP_UPPER_LIMIT))


def hasCrawledBefore(seedword,persistSeeds):
    #Check if target seed word has been crawled before so as to not waste calls
    #this optionally could be disabled too?
    print("Checking seedword")
    seedword = seedword + "\n"
    print(seedword)
    if (seedword in persistSeeds):
        print("crawled before")
        return True
    else:
        return False


if __name__ == "__main__":

    #Simple Command Line Utilities
    #Could be extended. But for now, only cares about input text
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"i:o:d")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -i input " % sys.argv[0])
        sys.exit(2)

    for o, a in myopts:
        if o == '-i':
            ifile=a
            SEED_FILE = a 
        elif o == "-o":
            ofile=a
            RESULT_FILE = a
        elif o == "-d":
            print("Do not persist mode")
            PERSIST=False



    #Main Program

    #Existing seeds is basically what we have persisted in previous crawls
    persistSeeds = []
    with open(PERSIST_SEEDS,'r') as file:
        for i,item in enumerate(file):
            persistSeeds.append(item)

    #The real shit here
    with open(SEED_FILE) as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                #print("found seedword")
                seedword = row[0]+"+"
                if (hasCrawledBefore(seedword,persistSeeds)==False):
                    print("processing", seedword)
                    query = seedword
                    for c in ascii_lowercase:
                        query = seedword
                        query+=c
                        print(query)
                        generateQueries(query)
                    for prefix in PREFIX:
                        query = seedword
                        prefix+=query
                        query = prefix
                        print(query)
                        generateQueries(query)

                     #write to post_seeds file, to store all the seed words we have processed
                    if PERSIST==True:
                        with open(PERSIST_SEEDS,'a') as file:
                            print("Writing seed word to post file...")
                            file.write(seedword + '\n')

                    print("Done with seedword!")

    print("Done with all seeds. Process ending")





