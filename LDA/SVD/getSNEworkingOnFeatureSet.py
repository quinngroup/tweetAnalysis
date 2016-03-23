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
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from scipy.linalg import svd
from sklearn.decomposition import TruncatedSVD

from sklearn.manifold import TSNE
#from IPython.html.widgets import interactive, fixed


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
    cnx = sqlite3.connect('data/40Feature.db')
    dforigtrain = pandas.read_csv(fileName)
    print (dforigtrain.shape)
    print dforigtrain.head()
    dforigtrain.rename(columns=lambda x: '_'.join([x.strip() for x in x.lower().split()]), inplace=True)
    df = dforigtrain[[c for c in dforigtrain.columns.values.tolist() if c != 'orig_set']]
    print(df.shape)

    # Write to DB to allow easier loading later
    df.to_sql('df_clean',cnx,if_exists='replace', index=None)

    df = pd.read_sql('select * from df_clean', cnx)

    print (df.shape)
    scaler = StandardScaler().fit(df.iloc[:,2:])

    dfs = pd.DataFrame(scaler.transform(df.iloc[:,2:]), index=df.index, columns=df.columns[2:])
    
    # Commented part helps in creating SVD
    '''u, s, vt = svd(dfs)

    ax = pd.Series(s).plot(figsize=(10,3), logy=True)

    print('{} SVs are NaN'.format(np.isnan(s).sum()))
    print('{} SVs less than 1e-12'.format(len(s[s < 1e-12])))
    
    plt.show()
    '''
    # from here the Truncated SVD , this is mostly helpful in image data set where reducing dimensions is mostl;y possibel . In our case, every feature was contributing . Hence no Truncation is possible
   
    ncomps = 49

    svd = TruncatedSVD(algorithm='randomized', n_components = ncomps)
    
    svd_fit = svd.fit(dfs)
    
    Y = svd.fit_transform(dfs) 
    
    ax = pd.Series(svd_fit.explained_variance_ratio_.cumsum()).plot(kind='line', figsize=(10,3))
    
    print('Variance preserved by first '+ str(ncomps)+' components == {:.2%}'.format(
                svd_fit.explained_variance_ratio_.cumsum()[-1]))

    #plt.show()

    dfsvd = pd.DataFrame(Y, columns=['c{}'.format(c) for c in range(ncomps)], index=df.index)
    
    dfsvd.to_sql('df_svd',cnx,if_exists='replace', index=None)

    dfsvd = pd.read_sql('select * from df_svd', cnx)

    
    print(dfsvd.shape)
    
    svdcols = [c for c in dfsvd.columns if c[0] == 'c']

    df = pd.read_sql('select * from df_clean', cnx)
    
    print(dfsvd.shape)
#
    print (dfsvd.head())
    
    #rowsubset = [10,20,40,80,160,320,640, 1280, 1900]
    tsne = TSNE(n_components=2, random_state=0)
    '''runs = np.empty((len(rowsubset),1))

    for i, rows in enumerate(rowsubset):
        t0 = time()
        Z = tsne.fit_transform(dfsvd.iloc[:rows,:][svdcols])
        runs[i] = time() - t0

    ax = pd.DataFrame(runs, index=rowsubset).plot(kind='bar', logy=False, figsize=(10,4))
    plt.show()'''
    
    
    Z = tsne.fit_transform(dfsvd[svdcols])
    dftsne = pd.DataFrame(Z, columns=['x','y'], index=dfsvd.index)
    ax = sns.lmplot('x', 'y', dftsne, fit_reg=False, size=8
                            ,scatter_kws={'alpha':0.7,'s':60})
    ax.axes.flat[0].set_title('Scatterplot of a 50D dataset reduced to 2D- Unsupervised')
    
    #plt.show()

    
    dftsne['class'] = df['class']
    
    
    g = sns.lmplot('x', 'y', dftsne, hue='class', fit_reg=False, size=8, scatter_kws={'alpha':0.7,'s':60})

    g.axes.flat[0].set_title('Scatterplot of a 50D dataset reduced to 2D -Supervised')
    

   	
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
    #dataPropPrint(fileName)
    tSNE(fileName)
    
