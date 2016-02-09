import urllib
import json
import sys
import re
import os

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
# now adding the foul word which are filtered from google adding that in the list
foulwordfile = open("foulWordList.txt")
for line in foulwordfile:
    term,score = line.split(":")
    scores[term] = int(score)

#http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
# soem more generic negative words to boost results
nwordsFile = open("negative-words.txt")
for word in nwordsFile:
	if word in scores:
		pass
	else:
		scores[word] = -3

def getSentiment(fileName, d):
    fileOnly = fileName.split(".")[0]
    path = os.getcwd()
    fileForOP = path+"/OUT_NF_ADDEDNEG/"+fileOnly+".csv"
    sys.stdout = open(fileForOP,'w+')
    fileadd = path +"/IN/"+d+"/"+ fileName
    fileContent = open(fileadd)
    for line in fileContent:
        posS = 0
        negS = 0
        try:
            line = line.split(",")[2]
            line = re.sub(r'#([^\s]+)', r'\1', line)
            line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',line)
            line = line.strip('\'"')
            sentiment = 0
            wordArray=line.split(" ")
            for word in wordArray:
                word = word.lower()
	        if word in scores:
                    sentiment = sentiment + scores[word]
            if sentiment != 0:
                if sentiment > 0:
                    posS = posS + sentiment
                else:
                    negS = negS + sentiment
        except ValueError:
            pass
        except KeyError:
            pass
        except:
            pass
        print str(posS) + "," + str(negS) + "," + str(posS + negS)


if __name__  == '__main__':
    path = os.getcwd()
    d = sys.argv[1]
    path = path +"/IN/"+d
    #print path
    lst=os.listdir(path)
    for fileName in lst:
	    getSentiment(fileName,d)

