# /usr/bin/python
# @author ranjanmanish
# this script  to get the followr names(screen_names)
import time
import tweepy
import os

auth = tweepy.OAuthHandler("EZwXKJPbhXFIUJhJ32xZVAYbI","b7syEKhbgr6sTe984AYJiQLsKQjm4c2TtuWwKc0o3V1fV2TqaC")
auth.set_access_token("96058036-nvf5aKMAKk8J2ITWsExEqmNgxYmp9QAQlMQUER5mj","96BvNtHt6kLaM6GQqJa29WwKWkBkJ09QvF2ILGlXLTs09")
api = tweepy.API(auth)

#ids = []
#for user in tweepy.Cursor(api.followers, screen_name="manishranjan84").items():
#    print user.screen_name
#    time.sleep(60)

def findFollowee(arg):
    print arg
    mapOfFollowee = {}
    followee = []
    counter = 0
    for user in tweepy.Cursor(api.followers, screen_name=arg).items():
        print user.screen_name
        followee.append(user.screen_name)
        counter = counter + 1
        if counter == 500:
            time.sleep( 30 )
            counter = 0 # reset the counter
    mapOfFollowee[arg] = followee
    print "Buckle up ladies!!"
    print mapOfFollowee

if __name__ == '__main__':
    C_DIR = os.getcwd()
    #C_DIR = C_DIR + "/RA/DrunkTweetAnalysis"
    fileName = C_DIR + '/data/finalResult.txt'
    with open(fileName) as fp:
        for line in fp:
		print line
        	findFollowee(line)
