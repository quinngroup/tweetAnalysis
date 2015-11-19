#! /usr/bin/python
# to get the follower count , thin code

import tweepy

for user in tweepy.Cursor(api.followers, screen_name="manishranjan84").items():
    print user.screen_name
