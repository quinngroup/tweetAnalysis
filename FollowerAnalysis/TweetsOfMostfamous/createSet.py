import sys
import os
# @author ranjanmanish

def getFinalSet(pathFile):
	userList = []
	fileOpen = open(pathFile)
	for line in fileOpen:
		if line not in userList:
			userList.append(line)
			print line

if __name__ == '__main__':
	fileName = sys.argv[1]
	path = os.getcwd() 
	pathFile = path + "/" + fileName
	getFinalSet(pathFile)
