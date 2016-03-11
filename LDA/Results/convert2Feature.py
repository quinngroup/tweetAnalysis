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
            user, feature = line.split(" ", 1)
            feature = eval(feature)
            tempFeature = []
            for var in feature:

                
    else:
        print "The file was not found , Fatal Error, Exiting!!!"


# main feature
if __name__ == '__main__':
    fileName = sys.argv[1]
    path = os.getcwd()
    path = path + "/" + fileName 
    converDFileToFeature(path)
    
