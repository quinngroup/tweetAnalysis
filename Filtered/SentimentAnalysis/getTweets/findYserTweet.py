#!/usr/bin/python3
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
import time
import urllib3

#author ranjanmanish
#Twitter API credentials

consumer_key="EZwXKJPbhXFIUJhJ32xZVAYbI"
consumer_secret="b7syEKhbgr6sTe984AYJiQLsKQjm4c2TtuWwKc0o3V1fV2TqaC"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_key="96058036-nvf5aKMAKk8J2ITWsExEqmNgxYmp9QAQlMQUER5mj"
access_secret="96BvNtHt6kLaM6GQqJa29WwKWkBkJ09QvF2ILGlXLTs09"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	with open(screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	fileName = sys.argv[1]
	for line in open(fileName):
		try:
			print line
			get_all_tweets(line)
                        time.sleep(30)
		except tweepy.TweepError, e:
			if e == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
				time.sleep(60*15) #Sleep for 5 minutes
                        elif e == "Not authorized.":
                            time.sleep(30)
                        else:
                            time.sleep(60*15)
		except:
                    pass
		    time.sleep(300)
                    #get_all_tweets(line)  #so that it does not escape this user - retrying
	#pass in the username of the account you want to download
