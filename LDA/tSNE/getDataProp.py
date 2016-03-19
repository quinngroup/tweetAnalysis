#author ranjanmanish

import sys
import pandas as pd
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

#take fileName as input

# load data
def dataPropPrint(fileName):
    mydata = pd.read_csv(fileName)
    #check the size 
    #print len(mydata)

    print (mydata.describe())

if __name__ == '__main__':
    fileName = sys.argv[1]
    dataPropPrint(fileName)
