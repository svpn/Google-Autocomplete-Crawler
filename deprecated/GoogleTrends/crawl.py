import csv

__author__ = 'tayyi'

from trendLib import pyGTrends
import time
from random import randint
import os

#constant variables
google_username = "megaprinceytay@gmail.com"
google_password = "171146sp"

#dynamic path
path = os.path.dirname(os.path.realpath(__file__)) + '/data/'

#seed file should be a csv file with only 1 column

#mass crawling for a long list of seed words
def massCrawl(seedFile, path):

    #connect to Google
    connector = pyGTrends(google_username, google_password)
    time.sleep(randint(200,600))
    print("connected to google!")
    print("opening seed file..")
    with open(seedFile) as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                crawl(connector,row[0], path)

#individual function for crawling ONE seed word
def crawl(connector,seedWord,path):

    #request report
    connector.request_report(seedWord)
    #wait a random amount of time between requests to avoid bot detection
    print("resting...")
    time.sleep(randint(20,30))
    print("saving to local data store.." + path)
    connector.save_csv(path, seedWord)
    time.sleep(randint(20,30))

#append ALL queries crawled so far into one big CSV

def makeBigCSV():

    #access file directory
    print("compiling directory into one big csv...")
    for file in os.listdir(path):
        if file.endswith(".csv"):
            print("parsing.." + file)
            parseCSV(path + file)

def parseCSV(csv_file):

    switch = False #control the switch for parsing only what we want
    writer = csv.writer(open('big.csv', 'a'))
    print("writing to big csv..")
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if "Top searches" in row[0]:
                    switch = True
                    continue
                if switch == True:
                    if "Rising searches" in row[0]:
                        continue
                    else:
                        print(row[0])
                        writer.writerow([row[0]])

def crawlOneTime(keyword):
    connector = pyGTrends(google_username, google_password)
    print("connected to google!")
    crawl(connector,keyword,path)


print("Local Path is:" + path)

#ACTUAL MAGIC

seedFile = "seed.csv"
massCrawl(seedFile, path)
#makeBigCSV()
#print("completed crawling procedure!")


#crawlOneTime("Orchard")

