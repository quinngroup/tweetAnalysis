#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os
def getRetweetsGraph(filename, fileAdd):
	user = fileName.split(".")[0]
	retweetList = ""
	#retweetList = []
	fileContent = open(fileAdd)
	try:
		for line in fileContent:
			try:
				#get The tweetText
				tweetText = line.split(",")[2]
				#clean up the text and later break the tweet text and look if the first word is RT
				tweetText = tweetText.strip()
				words = tweetText.split()
				#clean up the first word
				word = words[0].strip()
				#clean up for any thing other than word as "RT,'Rt,"RT" and many more weird forms of RT string was shoing up- not sure why
				word = re.sub(r'\W+', '', word)
				# to check if is a retweet or NOT a retweet
				if word == 'RT':
					print user + "," + line.split(",")[1]
			except :
				# this is the best action as of now as I have lot of tweets and if few gets excaped, its FINE
				pass
	except:
		pass
	#print user + retweetList

#main definition here
if __name__  == '__main__':
    path = os.getcwd()
    #path = path +"/TweetOfFiltered"
    path = path +"/CSVs_F"
    lst=os.listdir(path)
    for fileName in lst:
	    fileAdd = path + "/" +fileName
	    getRetweetsGraph(fileName,fileAdd)
