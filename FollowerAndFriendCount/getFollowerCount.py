'''
This script just prints the follower count by taking file name as input
'''
import oauth, tweepy, sys, locale, threading, urllib3 
from time import localtime, strftime, sleep


#global api
consumer_key = "EZwXKJPbhXFIUJhJ32xZVAYbI"
consumer_secret = "b7syEKhbgr6sTe984AYJiQLsKQjm4c2TtuWwKc0o3V1fV2TqaC"
access_key="96058036-nvf5aKMAKk8J2ITWsExEqmNgxYmp9QAQlMQUER5mj"
access_secret="96BvNtHt6kLaM6GQqJa29WwKWkBkJ09QvF2ILGlXLTs09"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

def getFollower(userId):
        try:
            userId = userId.strip()
            user = api.get_user(userId)
            #to get rid of new line
	    print userId + "," + str(user.followers_count) + "," + str(user.friends_count)
        except :
            pass

if __name__ == '__main__':
	fileName = sys.argv[1]
	fileContent = open(fileName)
	for line in fileContent:
		getFollower("manishranjan84")
                time.sleep(30)
