import math
import sys
import time
from twython import Twython
from authinfo1 import *

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret)

def get_All_Follwoers(user):
    #user = "manishranjan84"
    suser = twitter.show_user(screen_name=user)
    fnum = 200
    pnum = int(math.ceil(float(suser["followers_count"]) / fnum))

    pages = []
    for i in range(pnum):
        pages.append("p"+str(i+1))

    oldpages = []
    for i in range(pnum):
        oldpages.append("p"+str(i))

    p0 = { "next_cursor": -1 } # So the following exec() call doesn't fail.

    for i in range(pnum):
        exec(pages[i]+" = twitter.get_followers_list(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")

    followers = []

    for p in range(pnum):
        try:
            exec("for i in range(fnum): followers.append("+pages[p]+"['users'][i])")
        except(IndexError):
            pass

    followersList = []

    for x in followers:
        followersList.append(x["screen_name"])

    print user + ":" + ','.join(followersList) +":" + str(len(followers))

if __name__ == '__main__':
    fileName = sys.argv[1]
    for line in open(fileName):
        try:
            get_All_Follwoers(line)
            time.sleep(120)
        except:
            time.sleep(120)
            pass

#print("""Name:  %s
#Username:  %s
#""" % (x["name"], x["screen_name"]))
