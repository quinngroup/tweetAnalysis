#@author ranjanmanish

import os
import sys
def converDFileToFeature(path):
    """
    the job of this function is to, for a given input file convert them in to feature set 
    which could be consumed by any ML clustering algorithm
    """

# main feature
if __name__ == '__main__':
    fileName = sys.argsv[1]
    path = os.getcwd()
    path = path + "/" + fileName 
    converDFileToFeature(path)
    
