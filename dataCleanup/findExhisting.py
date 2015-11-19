#!/usr/bin/env python
#@author ranjanmanish
# need to recurse through a file which has set of unique user
# to find which user still exhists

import os
import urllib2
import json
import time
from urllib2 import HTTPError

def getData(req):
    req = urllib2.Request(request, headers=hdr)
    try:
        res = urllib2.urlopen(req)
        return res
    except HTTPError, e:
        if e.code == 429:
            print "Wait code 429.. and its gonna suck- will retry in 20 sec"
            time.sleep(20)
            return getData(req)
        raise

if __name__ == '__main__':
    C_DIR = os.getcwd()
    #C_DIR = C_DIR + "/RA/DrunkTweetAnalysis"
    fileName = C_DIR + '/uniqueSet.txt'
    URL = 'https://twitter.com/users/username_available?username='
    hdr = { 'User-Agent' : 'trying to check user ' }
    counter = 1
    with open(fileName) as fp:
        for line in fp:
            if (len(line) > 4):
                request = URL + line
                res = getData(request)
                data = json.loads(res.read())
    		counter = counter + 1
                res_data = data['valid']
         	if not res_data:
			print line
