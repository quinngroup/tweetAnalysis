#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os
from textblob import Word
from textblob import TextBlob
'''
This sscript will take the downlaoded tweets for individual user as input and create 
another file with only tweets in it, which will become input to next function which 
process it which in turn will become input to third function which will compute sentiment
'''
#get tweets only from a different format
# id, date time, tweet

def getTweetsOnly(inputData):
    fileOnly = inputData.split(".")[0]
    path = os.getcwd()
    fileForOP = path+"/OP5/"+fileOnly+".csv"
    sys.stdout = open(fileForOP,'w+')
    fileadd = path +"/renamed5/"+ inputData
    fileContent = open(fileadd)
    for tweetLine in fileContent:
        #print (tweetLine)
        try:
            #print (tweetLine)
            tweet = tweetLine.split(",")
            #print (tweet)
            processTweet(tweet[1],tweet[2])
        except:
            pass

#start process_tweet
def processTweet(time,tweet):
    # process the tweets
    try:
        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL -> later changed to blank
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
        # convert &amp; to empty string 
        tweet = re.sub('&amp;','',tweet)
        # getting rid of all "'" symbols as nltk package reacts to those
        tweet = re.sub("'",'',tweet)
        #Convert @username to AT_USER - later changed to blank
        tweet = re.sub('@[^\s]+','',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #trim
        tweet = tweet.strip('\'"')
        #spell CheckScore before correcting the tweet, to analyse and also get more accurate sentiment score
        cScore = getScore(tweet)        
        #correct the tweets
        cTweet = correctTheTweet(tweet)
        #print cTweet,
        #sentiment score , converting the TestBlob  object to string
        sScore = cTweet.sentiment.polarity
        print time + ","  + ("%.2f" % cScore) + ",", 
        print ("%.2f" % sScore),
        print cTweet
    except:
        pass

# to get the polarity score from textBlob 
def getScore(cTweet):
    try:
        #sen = TextBlob(str(cTweet))
        return cTweet.sentiment.polarity
    except:
        return '0.00'


# to correct the tweet text so sentiment analysis could be more accurate
def correctTheTweet(tweet):
    try:
        b = TextBlob(tweet)
        val  = (b.correct())
        return val
    except:
        return "NA"


# To compute score of correctness of a sentence and accumulating word correcteness to get score
def getScore(tweet):
    try:
        wordScore = 0
        # to get the score of sentence
        wordList = tweet.split()
        tweetLength = len(wordList)
        #iterating through the list
        for word in wordList:
            w = Word(word)
            var = w.spellcheck()
            wordScore = wordScore + var[0][1]
            #print wordScore
        val = wordScore/tweetLength
        return val
        #print tweet +","+ time +",",
        #print ("%.2f" % val)
    except:
        pass
'''
This method can take file as input and return 
username and avg SentiScore as output across 
months
Format : 2015-09-20 03:09:09,1.00, 0.00, story of my life
'''
def getAvg(fileName):
	avg = float(0)      # avg initialize
	cAvg = float(0)      # avg initialize
	sentTemp = 0
	ctemp = 0
	counter = 0  #initialize counter
	user = fileName.split(".")[0]
	path = os.getcwd()
	fileAdd = path + "/OUT_NLTK/" + fileName
	try:
		fp = open(fileAdd)
		for line in fp:
			counter = counter + 1
			sentTemp = float(line.split(",")[2])
			cTemp = float(line.split(",")[1])
			avg = avg + sentTemp
			cAvg = cAvg + cTemp
		val = float(avg/counter)
		cVal = float(cAvg/counter)
		print user + ",", # , at the end makes sure every thing comes in a single line
		print str(avg)  + "," + str(val) + "," +str(cAvg) + "," + str(cVal) # everuthing I need (for now) 
	except:
		pass

def getCorrectnessScore(fileName):
	path = os.getcwd()
	fileAdd = path + "/" + fileName
	fp = open(fileAdd)
	for line in fp:
		print line.split(",")[1]
#end
#main definition here

if __name__  == '__main__':
    path = os.getcwd()
    path = path +"/OUT_NLTK"
    lst=os.listdir(path)
    for fileName in lst:
        #getTweetsOnly(fileName)
	getAvg(fileName)
	#print fileName
