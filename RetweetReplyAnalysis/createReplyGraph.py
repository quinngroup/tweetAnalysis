#@author ranjanmanish
#from __future__ import print_function
import re
import sys
import os

fileOfUser = open("userNF.txt")
usersNF = []
for user in fileOfUser:
	# strip() is required to get rid of new line at the end
	user = user.strip()
	usersNF.append(user)

def getRetweetsGraph(filename, fileAdd):
	user = fileName.split(".")[0]
	replyList = ""
	fileContent = open(fileAdd)
	try:
		for line in fileContent:
			try:
				tweetText = line.split(",")[2]
				tweetText = tweetText.strip()
                                #split based on whitespace
				words = tweetText.split()
                                # get rid of whitespaces
				word1 = words[0].strip()
                                # get rid of extra " at the begining
                                word1 = word1.replace("\"", "")
                                #get the first char based on decision if this is a reply can be taken
                                firstChar = word1[0]
				# the the exact userName i.e from @manishranjan it will give manishranjan
				word1 = word1[1:]
				#print word1
                                if firstChar == '@':
					# if the userName is in the list of users => to find how the user interacts within his/her network
					#if word1 in usersNF and word1 != user:
					if word1 != user:
						replyList = replyList + ";" + word1
			except :
				pass
	except:
		pass
	if len(replyList) > 1:
		print user + replyList

#main definition here
if __name__  == '__main__':
    path = os.getcwd()
    #path = path +"/TweetOfFiltered"
    #path = path +"/OUT"
    path = path +"/CSVs_F"
    lst=os.listdir(path)
    for fileName in lst:
	    fileAdd = path + "/" +fileName
	    getRetweetsGraph(fileName,fileAdd)
