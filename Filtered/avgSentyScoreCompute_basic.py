#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os
from textblob import Word
from textblob import TextBlob
'''
This method can take file as input and return 
username and avg SentiScore as output across 
months
Format : 2015-09-20 03:09:09,1.00, 0.00, story of my life
'''
def getAvg(fileName):
	avg = float(0)      # avg initialize
	negAvg = float(0)      # avg initialize
	posAvg = float(0)      # avg initialize
	sentTemp = 0
	pos = 0
	neg = 0
	ctemp = 0
	counter = 0  #initialize counter
	user = fileName.split(".")[0]
	path = os.getcwd()
	fileAdd = path + "/OUT_DICT_BASIC/" + fileName
	try:
		fp = open(fileAdd)
		for line in fp:
			counter = counter + 1
			sentTemp = float(line.split(",")[2])
			neg = float(line.split(",")[1])
			pos = float(line.split(",")[0])
			avg = avg + sentTemp
			negAvg = negAvg + neg
			posAvg = posAvg + pos
		val = float(avg/counter) 
		nval = float(negAvg/counter) 
		pval = float(posAvg/counter) 
		print user + ",",
		print str(val) + "," +str(nval) + "," + str(pval) 
	except:
		pass

#end
#main definition here

if __name__  == '__main__':
    path = os.getcwd()
    path = path +"/OUT_DICT_BASIC"
    lst=os.listdir(path)
    for fileName in lst:
	getAvg(fileName)
