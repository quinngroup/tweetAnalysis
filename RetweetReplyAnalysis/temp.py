scoreFile = open("FretweetNumbers.csv")
retweetCount = {}
userF= {}
for line in scoreFile:
	try:
		name,score = line.split(",")
		retweetCount[name] = int(score)
	except ValueError:
		pass

fp = open("listF.txt")
for line in fp:
	try:
		print line.strip() + ",", 
		print str(retweetCount[line.strip()])
	except:
		print line.strip() + "," + "0"
		pass


