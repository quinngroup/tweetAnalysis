#@author ranjanmanish
import sys
import json
from nltk.corpus import stopwords
import re
import os

# =============================
# Do not modify above this line
def extractTemporalDetail(inputData,path):
	user = inputData.split(".")[0]
	fileAdd = path + inputData
    	fileContent = open(fileAdd)
	for line in fileContent:
        	try:
			line  = line.split(",")
			print str(user) + "," + str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "," + str( line[3])
        	except KeyError:
            		pass
        	except ValueError:
            		pass
        	except:
            		pass

# Do not modify below this line
# =============================
if __name__ == '__main__':
	path = os.getcwd()
	#path = path +"/CSVs_F/"
	path = path +"/OUT_NF/"
	#path = path +"/TEMP/"
	lst = os.listdir(path)
	for fileName in lst:
		extractTemporalDetail(fileName,path)
