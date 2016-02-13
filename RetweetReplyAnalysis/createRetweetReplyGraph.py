#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os
'''
'''
fileOfUser = open("userList.txt")
usersF = []
for user in fileOfUser:
	usersF.append(user)

print len(usersF)
def getRetweetsGraph(filename, fileAdd):
	user = fileName.split(".")[0]
	retweetList = ""
	#retweetList = []
	fileContent = open(fileAdd)
	try:
		for line in fileContent:
			try:
				tweetText = line.split(",")[2]
				tweetText = tweetText.strip()
				#print tweetText
				words = tweetText.split()
				word = words[0].strip()
				word = re.sub(r'\W+', '', word)
				if word == 'RT':
					retweet = re.sub(r'\W+','',words[1])
					retweetList = retweetList + ";" + retweet 			 				
			except :
				pass
	except:
		pass
	print user + retweetList

#main definition here
if __name__  == '__main__':
    path = os.getcwd()
    #path = path +"/TweetOfFiltered"
    path = path +"/OUT"
    lst=os.listdir(path)
    for fileName in lst:
	    fileAdd = path + "/" +fileName
	    getRetweetsGraph(fileName,fileAdd)
