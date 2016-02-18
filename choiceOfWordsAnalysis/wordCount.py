# author http://stackoverflow.com/users/3113477/a-j
# modified ranjanmanish

def num_there(s):
	return any(i.isdigit() for i in s)

file=open("TweetTextOfFiltered.txt","r+")
#file=open("out.txt","r+")
wordcount={}
tweet = file.read()
for word in tweet.split():
	if len(word) > 2 and not num_there(word):
    		word = word.lower()
    		word = word.replace(".",'')
		word = word.replace("!",'')
    		word = word.replace("#",'')
    		word = word.replace("$",'')
    		word = word.replace("-",'')
    		if word not in wordcount:
			wordcount[word] = 1
    		else:
            		wordcount[word] += 1
copy = []
for k,v in wordcount.items():
    copy.append((v, k))


copy = sorted(copy, reverse=True)

for k in copy:
        print '%s, %d' %(k[1], k[0])
        #print '%s' %(k[1])

