#@author ranjanmanish
import sys
import json
from nltk.corpus import stopwords
import re
import os
# =============================
# Do not modify above this line
def extractTweet(fileAdd, fileName):
    path = os.getcwd()
    fileContent = open(fileAdd)
    for line in fileContent:
            try:
                line = make_unicode(line)
                print line

            except KeyError:
                pass
            except ValueError:
                pass
            except:
                pass



'''
To take and convert it in to unicode  for less exceptions while processing the lines
'''
def make_unicode(input):
    if type(input) != unicode:
        input =  input.decode('utf-8')
        return input
    else:
        return input



# Do not modify below this line
# =============================
if __name__ == '__main__':
	path = os.getcwd()
	path = path +"/OUT_F/"
	#path = path +"/TEMP/"
	lst = os.listdir(path)
	for fileName in lst:
		fileadd = path + fileName
		extractTweet(fileadd, fileName)

