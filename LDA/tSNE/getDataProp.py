#author ranjanmanish

import sys
import pandas

#take fileName as input

# load data
def dataPropPrint(fileName):
    mydata = pandas.read_csv(fileName)

    #check the size 
    print len(mydata)

    print (mydata.describe())

if __name__ == '__main__':
    fileName = sys.argv[1]
    dataPropPrint(fileName)
