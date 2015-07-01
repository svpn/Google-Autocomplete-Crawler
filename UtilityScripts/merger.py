import glob
import os
import csv
import codecs

filelist = []
combinedList = []
combinedFile = 'combined.csv'
'''
os.chdir("generated-csv/")
for counter, files in enumerate(glob.glob("*.csv")):
    filelist.append(files)
    print(files)   
    reader = csv.reader(codecs.open(files, 'rU', 'utf-16'))
    for row in reader:
        if row:
            cleaned = row[0].replace("Keyword Ideas", " ")
            cleaned = cleaned.replace("SGD", ",")
            cleaned = cleaned.replace("N", "")
            combinedList.append(cleaned + "\n")
    print "do stuff with file:", files, counter

#print(combinedList)


with open(combinedFile,'w') as file:
    for item in combinedList:
        if("Ad group" in item):
            continue
        file.write(item)

'''


os.chdir("generated-csv/")
with open(combinedFile) as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            target = row[1]
            print(target)
            target = target.replace(" ","")
            index = target.find(".")
            #print(index)
            cleaned = target[:index-1]
            #print(cleaned)
            combinedList.append(row[0] + "," + cleaned + "\n")


            
print(combinedList)

with open('test.csv','w') as file:
    for item in combinedList:
        if("Ad group" in item):
            continue
        file.write(item)



'''
print filelist


for fileitem in filelist:
    print fileitem
'''
