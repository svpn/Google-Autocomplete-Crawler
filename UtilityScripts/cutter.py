__author__ = 'tayyi'

DATA = 'test.txt'


WriteList = []

SIZE_DATA = sum(1 for line in open(DATA))
print("Reading file of length:" + str(SIZE_DATA))

numFiles = SIZE_DATA / 3000

print(numFiles)

for i in range(0,numFiles+1,1):
	filename = str(i) + ".txt"
	WriteList.append(filename)

print(WriteList)

startWindow = 0
stopWindow = 3000


for writeFile in WriteList:

	count = 0
	TempList = []


	with open(DATA,'r') as file:
	    for i,item in enumerate(file):
	    	if (i>startWindow and i<stopWindow):
	    		TempList.append(item)
	    	else:
	    		continue
	        
	with open(writeFile,'w') as file:
	    for item in TempList:
	        if "\\" in item or '(' in item or ')' in item:
	            #ignore
	            continue
	        file.write(item)

	print("Writer done for wave:") 
	print("Start Window:" + str(startWindow))
	print("Stop Window:" +  str(stopWindow)) 
	startWindow = startWindow + 3000
	stopWindow = stopWindow + 3000
	
print("CUTTER FINISHED")
