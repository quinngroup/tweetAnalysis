#@author ranjanmanish
import sys
import json
from nltk.corpus import stopwords
import re
import os

cachedStopWords = stopwords.words("english")
commonWordList = ["i", "RT","\"RT", "|", "&", "love", "life", "i'm", "follow", "the", "-", "like", "don't", "my", "a", "if",  "you", "im", "music", "news", "one", "get", "new", "live", "never", "get", "make", "justin", "me","know", ":)", ":(", "world", "ig", "good", "/", "best", "fan", "//", ".", "tweets", "god", "living", "instagram", "snapchat", "believe", "let", ":", "account", "business", "snapchat:", "@justinbieber", "you.", "loves", "work", "ig:", "just", "always", "dont", "instagram:", "||", "people", "time", "want", "and", "go", "it's", "everything", "u", "we", "me.", "say", "back", "twitter", "to", "in", "life.", "!", "you're", "it", "no", "be", "~", "la", "2", "university", "3", "all", "food", "free", "keep", "n", "twitter", "come", "followed", "got", "hard", "day", "year", "life.", "better", "co", "thttps", "https", "http", "n", "t", "u", "for", "us", "is:", "it.", "on", "i'll", "also", "of", "years", "not", ] 
  
# =============================
# Do not modify above this line
def extractTweet(inputData):
    	fileContent = open(inputData)
	for line in fileContent:
        	try:
			line  = line.split(",")[2]
            		line = make_unicode(line)
			line = re.sub(r'#([^\s]+)', r'\1', line)
			line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',line)
			#Convert @username to blank
			line = re.sub('@[^\s]+','',line)
			line = line.replace("\"",'')
            		line = convertWordLowerCase(line)
			Test(line)
        	except KeyError:
            		pass
        	except ValueError:
            		pass
        	except:
            		pass


def convertWordLowerCase(line):
	line = re.sub(',','',line) # because presence of comma was giving the empty lines
	# get rid of common words defined at the top commonWordList
	text = ' '.join([word for word in line.split() if word not in commonWordList])
	return text


'''
This Test script takes the line as input and removes some of the top twitter keyword found based on 
research and practical results
'''
def Test(data):
        text = ' '.join([word for word in data.split() if word not in cachedStopWords])
	print text
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
	path = path +"/CSVs_NF/"
	#path = path +"/TEMP/"
	lst = os.listdir(path)
	for fileName in lst:
		fileName = path + fileName
		extractTweet(fileName)
