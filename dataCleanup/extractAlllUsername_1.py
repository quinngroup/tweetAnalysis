#!/usr/bin/env python
# This python scripts takes raw json tweets and extract the usernames out of it.

""" To analyse the word freq of people who are using abusive language/are drunk in tweets."""
import sys
import os
import json
import gzip
import time
import pandas as pd

# =============================
# Do not modify above this line
def extractUserScreen_Name(FILE):
    tweet_data = []
    #FILE = PATH+'2014-03-27-21-12.terms.json.gz'
    #OP_FILE = PATH+'result_rec.txt'
    flag = True
    with gzip.open(FILE) as data_file:
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
    #tweets['text'] = map(lambda tweet: tweet['text'], tweet_data)
    #tweets['lang'] = map(lambda tweet: tweet['lang'], tweet_data)
    tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweet_data)
    #tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweet_data)
    #tweets_by_lang = tweets['lang'].value_counts()
    #tweets_by_country = tweets['country'].value_counts()
    tweets_by_username = tweets['screen_name']#.to_string(index=False,justify='left')
    #tweets_text = tweets['text']#.to_string(index=False,justify='left')


    #print pd.get_option("display.max_rows")
    #print pd.get_option("display.max_columns")
    pd.set_option("display.max_rows",100000000000)
    pd.set_option('max_colwidth',10000000) # twitter deals in 140s
    #pd.set_option('colheader_justify', 'right')
    #print pd.get_option("display.max_rows")
    '''tweetToPrint= tweets_by_username+":#:"+ tweets_text
    print tweetToPrint
    '''
    # now to get the profile description
    #tweets['desc'] = map(lambda tweet: tweet['user']['description'], tweet_data)
    #tweetsprofDesc = tweets['desc']
    #print tweetsprofDesc
    tweets['friends_count'] = map(lambda tweet: tweet['user']['friends_count'], tweet_data)
    friendsCount =  tweets['friends_count']

# Main function here
if __name__ == '__main__':
    PATH = "/home/manish/fall2015/RA/Data/Tweet-Archive-Alcohol-2/"
    folders = os.listdir(PATH)
    counter = 0
    for folderName in folders:
        folderPath = PATH + folderName
        files = os.listdir(folderPath)
        for fileName in files:
            FILE = folderPath+"/"+fileName
            extractUserScreen_Name(FILE)
