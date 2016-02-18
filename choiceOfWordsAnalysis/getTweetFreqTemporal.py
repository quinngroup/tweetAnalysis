#@author ranjanmanish
import sys
import json
from nltk.corpus import stopwords
import re
import os

# =============================
# Do not modify above this line
def extractTemporalDetail(inputData,path):
	fileAdd = path + inputData
	user = inputData.split(".")[0]
    	fileContent = open(fileAdd)
	for line in fileContent:
        	try:
			line  = line.split(",")[1]
			date = line.split(" ")[0]
			time = line.split(" ")[1]
			print user + "," + date + "," + time + "," + line
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
	path = path +"/CSVs_F/"
	#path = path +"/TEMP/"
	lst = os.listdir(path)
	for fileName in lst:
		extractTemporalDetail(fileName,path)
