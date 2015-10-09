#! /usr/bin/python
'''
@author ranjanmanish
Utility Script to do some data cleaning stuff
this script should implement all the cleanup functions from string and
give a
used this shell command to get rid of all the empty lines
awk 'NF' <inputFile> | tee <outputFile>
to gert rid of all the wods which starts with @ => mostly it is just a mention
sed '/^@/ d' wcwithouthttpsandempy.txt | tee wordCountResult1.txt
awk '{$1="";$0=$0;$1=$1}1' < description1onlyFilteredhttps.txt | tee desclean1.txt  'To get rid of first column which was coming as no by default'
'''
import sys
import re

def cleanUphttp(fileName):
    with open (fileName) as fp:
        for line in fp:
            line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
            line = re.sub(r'^http?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
            print line

def getRidOfOnlyHttp(fileName):
    with open(fileName) as f:
        rep = re.compile(r"""
                        http[s]?://.*?\s
                        |www.*?\s
                        |(\n)
                        """, re.X)
        non_asc = re.compile(r"[^\x00-\x7F]")
        for line in f:
            non = non_asc.search(line)
            if non:
                continue
            m = rep.search(line)
            if m:
                line = line.replace(m.group(), "")
                if line.strip():
                    print(line.strip())


def getRidOfUrlShortner(fileName):
    httpVar = 'http://t.co'
    httpsVar = 'https://t.co'
    with open(fileName) as fp:
        for line in fp:
            if not httpVar in line:
                if not httpsVar in line:
                    print line

def getRidOfNoneString(fileName):
    filter1 = 'None'
    filter2 = 'NONE'
    with open(fileName) as fp:
        for line in fp:
            if not filter1  in line:
                if not filter2 in line:
                    print line

def GetCountGTTenThousand(fileName):
    rowList = []
    with open (fileName) as fp:
        for line in fp:
            rowList = line.split(":")
            temp = int(rowList[0])
            if (temp > 50000):
                print rowList[0] +":"+rowList[1]


def getRidOfRTtag(fileName):
    elemList = []
    myList = []
    with open(fileName) as fp:
        for line in fp:
            elemList = line.split(" ")
            if elemList[0] == "RT":
                myList = elemList[2:]
                print ', '.join(printList)



def createText(fileName):
    arrList = []
    printList = []
    with open(fileName) as fp:
        for line in fp:
            arrList = line.split(":")
            var = int(arrList[0])
            for x in range(0, var):
                print (arrList[1]),

def getRidOfFirstColumn(fileName):
    arrList = []
    with open(fileName) as fp:
        for line in fp:
            arrList = line.split(" ")
            var = arrList[1:]
            print var

if __name__ == '__main__':
    getRidOfNoneString(sys.argv[1])
    #getRidOfFirstColumn(sys.argv[1])
    #getRidOfOnlyHttp(sys.argv[1])
    #cleanUphttp(sys.argv[1])
    #getRidOfUrlShortner(sys.argv[1])
    #cleanUphttp(sys.argv[1])
    #getRidOfRTtag(sys.argv[1])
    #createText(sys.argv[1])
   # getRidOfUrlShortnerGetCountGTTenThousand(sys.argv[1])
