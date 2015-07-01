__author__ = 'tayyi'

'''
Python Script for cutting crawled queries
Use-case : Slice text data files into chunks of 3000 to be fed into google adwords (to get search query volume)

This script takes in a txt file and cuts them into chunks of N (default = 3000)

Is this the best way to go about it? I don't know. But hey it works. 

This will dump the files into a directory called cut-files.

make sure this script is in the same dir as the data file you want to slice


HOW TO USE:
1. Move crawled data to root of project
2. Run python cutter.py -i example.txt -n 3000
3. n is segment size, i is file to Reading
4. segmented files is then output to cut-files dir

'''

import sys
import os
import getopt

DATA = "result.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'cut-files')
SEGMENT_NUM = 3000
WriteList=[]

if __name__ == "__main__":

	#Simple Command Line Utilities
	try:
		myopts, args = getopt.getopt(sys.argv[1:],"i:o:n:")
	except getopt.GetoptError as e:
		print (str(e))
		print("Usage: %s -i input -n segment number " % sys.argv[0])
		sys.exit(2)

	for o, a in myopts:
		if o == '-i':
			ifile=a
			DATA = a 
		elif o == "-n":
			print("Number cutter")
			SEGMENT_NUM = int(a)
			

	assert(isinstance(SEGMENT_NUM,int))

	
	SIZE_DATA = sum(1 for line in open(DATA))

	#There is no point if data is already smaller than segment size
	if(SIZE_DATA < SEGMENT_NUM):
		print("Data File too Small. Exiting")
		sys.exit(2)

	print("Reading file of length:" + str(SIZE_DATA))

	numFiles = int(SIZE_DATA / SEGMENT_NUM)

	print(numFiles)

	for i in range(0,numFiles+1,1):
		filename = str(i) + ".txt"
		filepath = os.path.join(dest_dir, filename)
		print(filepath)
		WriteList.append(filepath)

	print(WriteList)

	startWindow = 0
	stopWindow = SEGMENT_NUM


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
		startWindow = startWindow + SEGMENT_NUM
		stopWindow = stopWindow + SEGMENT_NUM
		
	print("CUTTER FINISHED")
