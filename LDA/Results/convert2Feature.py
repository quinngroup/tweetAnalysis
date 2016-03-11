#@author ranjanmanish

import os
import sys
import json

def converDFileToFeature(path):
    """
    the job of this function is to, for a given input file convert them in to feature set 
    which could be consumed by any ML clustering algorithm
    """
    if os.path.exists(path):
        fileContent = open(path)
        
        # skip  first line as that has print of all the models
        next(fileContent)

        # now traversing file content one by one
        for line in fileContent:
            # get the user and feature, 1 helps in splitting on 1st whitespace
            user, feature = line.split(" ", 1)

            #feature is str type, converting that to list
            feature = eval(feature)
            
            # initialization
            presentList = []
            temp = []
            tempDict = {}
            tempStr = ""

            # now iterating on feature list 1) prepare the present list where data exists 
            # 2) create a dictionary of item so we can extract exactly what we need later

            for var in feature:
                presentList.append(var[0])
                tempDict[var[0]] = round(var[1],2)
            
            # now building the final feature vector of what is present in list or "0" otherwise
            temp = []
            # range will vary based on how many topics, basically Max(range) == #topics
            for index in range(0,9):
                if index in presentList:
                    temp.append(tempDict[index])
                else:
                    temp.append(0)
            
            tempStr = ','.join(map(str, temp))            
            print user + "," + tempStr


    else:
        print "The file was not found , Fatal Error, Exiting!!!"


# main feature
if __name__ == '__main__':
    fileName = sys.argv[1]
    path = os.getcwd()
    path = path + "/" + fileName 
    converDFileToFeature(path)
    
