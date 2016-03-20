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
    cnx = sqlite3.connect('data/50Feature.db')
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

    ax = df.groupby('class').size().plot(kind='bar',color = 'g',  figsize=(10,2))

    plt.show()

def tSNE(fileName):
    cnx = sqlite3.connect('data/50Feature.db')
    dforigtrain = pandas.read_csv(fileName)
    #print (mydata.shape)
    #print mydata.head()
    dforigtrain.rename(columns=lambda x: '_'.join([x.strip() for x in x.lower().split()]), inplace=True)
    df = dforigtrain[[c for c in dforigtrain.columns.values.tolist() if c != 'orig_set']]
    print(df.shape)

    # Write to DB to allow easier loading later
    df.to_sql('df_clean',cnx,if_exists='replace', index=None)

    df = pd.read_sql('select * from df_clean', cnx)

    scaler = StandardScaler().fit(df.iloc[:,2:])

    dfs = pd.DataFrame(scaler.transform(df.iloc[:,2:]), index=df.index, columns=df.columns[2:])
    
    # Commented part helps in creating SVD
    '''u, s, vt = svd(dfs)

    ax = pd.Series(s).plot(figsize=(10,3), logy=True)

    print('{} SVs are NaN'.format(np.isnan(s).sum()))
    print('{} SVs less than 1e-12'.format(len(s[s < 1e-12])))
    
    plt.show()

    # from here the Truncated SVD , this is mostly helpful in image data set where reducing dimensions is mostl;y possibel . In our case, every feature was contributing . Hence no Truncation is possible
   
    ncomps = 48

    svd = TruncatedSVD(algorithm='randomized', n_components = 48)
    
    svd_fit = svd.fit(dfs)
    
    Y = svd.fit_transform(dfs) 
    
    ax = pd.Series(svd_fit.explained_variance_ratio_.cumsum()).plot(kind='line', figsize=(10,3))
    
    print('Variance preserved by first '+ str(ncomps)+' components == {:.2%}'.format(
                svd_fit.explained_variance_ratio_.cumsum()[-1]))

    #plt.show()

    dfsvd = pd.DataFrame(Y, columns=['c{}'.format(c) for c in range(ncomps)], index=df.index)
    print(dfsvd.shape)
    #dfsvd.head()
    
    dfsvd.to_sql('df_svd',cnx,if_exists='replace', index=None)

    dfsvd = pd.read_sql('select * from df_svd', cnx)

    svdcols = [c for c in dfsvd.columns if c[0] == 'c']

    df = pd.read_sql('select * from df_clean', cnx)

    plotdims = 5
    ploteorows = 1
    dfsvdplot = dfsvd[svdcols].iloc[:,:plotdims]
    dfsvdplot['class'] = df['class']
    ax = sns.pairplot(dfsvdplot.iloc[::ploteorows,:], hue='class', size=1.8)

    plt.show()'''

if __name__ == '__main__':
    fileName = sys.argv[1]
    #dataPropPrint(fileName)
    tSNE(fileName)
    
