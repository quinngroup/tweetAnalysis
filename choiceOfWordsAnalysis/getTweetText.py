#from __future__ import print_function
import sys
import json
from nltk.corpus import stopwords
import re
import os

cachedStopWords = stopwords.words("english")
commonWordList = ["i", "|", "&", "love", "life", "i'm", "follow", "the", "-", "like", "don't", "my", "a", "if",  "you", "im", "music", "news", "one", "get", "new", "live", "never", "get", "make", "justin", "me","know", ":)", ":(", "world", "ig", "good", "/", "best", "fan", "//", ".", "tweets", "god", "living", "instagram", "snapchat", "believe", "let", ":", "account", "business", "snapchat:", "@justinbieber", "you.", "loves", "work", "ig:", "just", "always", "dont", "instagram:", "||", "people", "time", "want", "and", "go", "it's", "everything", "u", "we", "me.", "say", "back", "twitter", "to", "in", "life.", "!", "you're", "it", "no", "be", "~", "la", "2", "university", "3", "all", "food", "free", "keep", "n", "twitter", "come", "followed", "got", "hard", "day", "year", "life.", "better", "co", "thttps", "https", "http", "n", "t", "u", "for", "us", "is:", "it.", "on", "i'll", "also", "of", "years", "not", ] 
  
# =============================
# Do not modify above this line
def extractTweet(inputdata):
    	count = 0 
    	for line in inputdata:
        	try:
			line  = line.split(",")[2]
            		line = make_unicode(line)
			line = re.sub(r'#([^\s]+)', r'\1', line)
			line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',line)
			line = line.strip('\'"')
            		line = convertWordLowerCase(line)
                        removesStopWords(line)
        	except KeyError:
            		pass
        	except ValueError:
            		pass
        	except:
            		pass
def Test(inputData):
	print inputData

def make_unicode(input):
    if type(input) != unicode:
        input =  input.decode('utf-8')
        return input
    else:
        return input

def removeStopWords(line):
        text = ' '.join([word for word in line.split() if word not in cachedStopWords])
        print text

'''
Take file as input and convert the words to smaller 
'''
def convertWordLowerCase(inputData):
        line = re.sub(',','',line) # because presence of comma was giving the empty lines
        # get rid of common words defined at the top commonWordList
        text = ' '.join([word for word in line.split() if word not in commonWordList])
        return text

'''
this method will filter most common words so we can look at the tail of the 
word distribution.  
'''
def getTailOfDistribution(inputdata):
    for line in inputdata:
        line = make_unicode(line)
        text = ' '.join([word for word in line.split() if word not in commonWordList])
        print (text)

# Do not modify below this line
# =============================
if __name__ == '__main__':
	path = os.getcwd()
	path = path +"/CSVs_F/"
	lst = os.listdir(path)
	for fileName in lst:
		fileName = path +fileName
		extractTweet(fileName)
  	#removeStopWords(inputdata)
  	#convertWordLowerCase(inputdata)
  	#getTailOfDistribution(inputdata)
