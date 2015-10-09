#!/usr/bin/env python
# This python scripts takes raw json tweets and extract the usernames out of it.

""" To analyse the word freq of people who are using abusive language/are drunk in tweets."""
import sys
import json
import gzip
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# Do not modify above this line
def extractUserScreen_Name():
    tweet_data = []
    PATH="/home/manish/fall2015/RA/Data/Tweet-Archive-Alcohol/2014-03-27/"
    FILE = PATH+'2014-03-27-21-13.terms.json'
    #FILE = PATH+'2014-03-27-21-12.terms.json.gz'
    #OP_FILE = PATH+'result_rec.txt'
    flag = True
    with open(FILE) as data_file:
        data = json.loads(data_file.read())
    for k, v in data.iteritems():
        if flag:
            for tw in v:
                try:
                    tweet_data.append(tw)
                except ValueError:
                    print "something went wrong in decoding json?"
                except Exception as e:
                    print e
            flag = False
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweet_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweet_data)
    tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweet_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweet_data)
    tweets_by_lang = tweets['lang'].value_counts()
    tweets_by_country = tweets['country'].value_counts()
    tweets_by_username = tweets['screen_name']
    #print pd.get_option("display.max_rows")
    pd.set_option("display.max_rows",1000000000)
    #print pd.get_option("display.max_rows")
    print tweets_by_username

# Main function here
if __name__ == '__main__':
	extractUserScreen_Name()
