# /usr/bin/python
# I got this error while running the python script 
#sudo pip install requests[security] 
#/usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning

import time
import tweepy

auth = tweepy.OAuthHandler("EZwXKJPbhXFIUJhJ32xZVAYbI","b7syEKhbgr6sTe984AYJiQLsKQjm4c2TtuWwKc0o3V1fV2TqaC")
auth.set_access_token("96058036-nvf5aKMAKk8J2ITWsExEqmNgxYmp9QAQlMQUER5mj","96BvNtHt6kLaM6GQqJa29WwKWkBkJ09QvF2ILGlXLTs09")

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="McDonalds").pages():
    ids.extend(page)
    time.sleep(60)
print ids
