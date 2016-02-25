#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os
def getReplyFreq(filename, fileAdd):
	user = fileName.split(".")[0]
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
				#get Rid of extra " at the begining : Based on observation
				word = word.replace("\"","")
				# now get the first char of this cleaned up word
				firstChar = word[0]
				# now lest extract the userName : it is in @twitter so extract twitter out of it
				word = word[1:]
				if firstChar == '@':
					# word == user : suggests how many reply user gets: and 
					# condition word !=user represents how many replies user sent
					if word == user:
						print user + "," + line.split(",")[1]

			except :
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
	    getReplyFreq(fileName,fileAdd)
