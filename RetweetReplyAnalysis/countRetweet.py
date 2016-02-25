import os
import sys

def countTheRetweet(fileName):
	path = os.getcwd()
	fileName = path + "/" + fileName
	fileContent = open(fileName)
	for line in fileContent:
		users = line.split(";")
		print users[0] + "," + str(len(users[1:]))


if __name__ == '__main__':
	fileName = sys.argv[1]
	countTheRetweet(fileName)

