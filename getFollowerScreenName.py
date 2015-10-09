# /usr/bin/python
# 
# this script  to get the followr names(screen_names) 
import time
import tweepy

auth = tweepy.OAuthHandler("EZwXKJPbhXFIUJhJ32xZVAYbI","b7syEKhbgr6sTe984AYJiQLsKQjm4c2TtuWwKc0o3V1fV2TqaC")
auth.set_access_token("96058036-nvf5aKMAKk8J2ITWsExEqmNgxYmp9QAQlMQUER5mj","96BvNtHt6kLaM6GQqJa29WwKWkBkJ09QvF2ILGlXLTs09")

api = tweepy.API(auth)

ids = []
counter = 0
for user in tweepy.Cursor(api.followers, screen_name="manishranjan84").items():
    #print user.screen_name
    counter = counter + 1
    #time.sleep(60)
#print len(ids)
print counter
