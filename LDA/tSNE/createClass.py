import sys

fileName = sys.argv[1]
fp = open(fileName)
median = 0.34

for line in fp:
    line = line.strip()
    userName = line.split(",")[0]
    val = line.split(",")[8]
    #print userName, val
    val = float(val)
    if  val >= median:
        print line+",N"
    else:
        print line+",NN"

