# author ranjanmanish
import sys

fileName = sys.argv[1]
fp = open(fileName)
next (fp)
std_10 = 0.34
std_20 = 0.32
std_30 = 0.22
std_40 = 0.20
std_50 = 0.21
counter = 1
for line in fp:
    line = line.strip()
    lineList = line.split(",")[1:]
    #userName = line.split(",")[0]
    #val = lineList[7]
    #val = lineList[0]
    #val = lineList[19]
    val = lineList[3]
    #print userName, val
    val = float(val)
    #print val, type(val)
    myList = ','.join(map(str, lineList))
    if  val >= std_50:
        print "N,"+ str(counter) +"," +myList
        counter = counter + 1
    else:
        print "NN,"+  str(counter) + "," +myList
        counter = counter + 1
