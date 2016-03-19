#author http://blog.applied.ai/visualising-high-dimensional-data/
# modified for my analysisranjanmanish

import sys
import pandas
from tsne import bh_sne
import numpy as np
from collections import OrderedDict
from time import time
import sqlite3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
#import seaborn as sns

from sklearn.preprocessing import StandardScaler
from scipy.linalg import svd
from sklearn.decomposition import TruncatedSVD

from sklearn.manifold import TSNE


#take fileName as input

# load data
def dataPropPrint(fileName):
    cnx = sqlite3.connect('data/10Feature.db')
    dforigtrain = pandas.read_csv(fileName)
    #print (mydata.shape)
    #print mydata.head()
    dforigtrain.rename(columns=lambda x: '_'.join([x.strip() for x in x.lower().split()]), inplace=True)
    print(dforigtrain.shape)
    print dforigtrain.head()
    df = dforigtrain[[c for c in dforigtrain.columns.values.tolist() if c != 'orig_set']]
    print(df.shape)
    
    # Write to DB to allow easier loading later
    df.to_sql('df_clean',cnx,if_exists='replace', index=None)
    
    df = pd.read_sql('select * from df_clean', cnx)

    ax = df.groupby('class').size().plot(kind='bar', figsize=(10,2))

    plt.show()


def plot_3d_scatter(A, elevation=30, azimuth=120):
    """ Create 3D scatterplot """
    
    maxpts=1000
    fig = plt.figure(1, figsize=(9, 9))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=elevation, azim=azimuth)
    ax.set_xlabel('component 0')
    ax.set_ylabel('component 1')
    ax.set_zlabel('component 2')

    # plot subset of points
    rndpts = np.sort(np.random.choice(A.shape[0], min(maxpts,A.shape[0]), replace=False))
    coloridx = np.unique(A.iloc[rndpts]['class'], return_inverse=True)
    colors = coloridx[1] / len(coloridx[0])   
    
    sp = ax.scatter(A.iloc[rndpts,0], A.iloc[rndpts,1], A.iloc[rndpts,2]
               ,c=colors, cmap="jet", marker='o', alpha=0.6
               ,s=50, linewidths=0.8, edgecolor='#BBBBBB')

    plt.show()



if __name__ == '__main__':
    fileName = sys.argv[1]
    dataPropPrint(fileName)
    
