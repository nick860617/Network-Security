# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:40:00 2019

@author: pc
"""
import scikitplot as skplt
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D


def confusion_matrix(clf, y_test, X_test):
    skplt.metrics.plot_confusion_matrix(y_test, clf.predict(X_test))
    plt.show()
    
def table(reg, X, y, intercept=1):
    if intercept:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))
    #RSS = sum(np.square(y-np.dot(X, reg.w)))
    RSS = sum(np.square(y-np.dot(reg.w, X.T)))
    RSE = RSS/(len(X)- 6 - 2)
    
    mat = (RSE*np.linalg.pinv(np.dot(X.T, X)))
    stdERROR = []
    for i in range(0, len(reg.w)):
        stdERROR.append(np.sqrt(mat[i][i]))
    
    stdERROR = np.array(stdERROR)
    ts_b = reg.w / stdERROR
    p_values =[2*(1-sp.stats.t.cdf(np.abs(i),(len(X)-1))) for i in ts_b]
    
    return (stdERROR, ts_b, p_values)

def plot_(X, reg):
    x, y = X[:, 0].reshape(len(X)), X[:, 1].reshape(len(X))
    intercept = np.ones((X.shape[0], 1))
    z = np.dot(np.hstack((intercept, X)), reg.w)
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(111, projection='3d')

    z_ = (z-min(z))/(max(z)-min(z))
    ax.scatter(x, y, z_)
    point  = np.array([1, X[0, 0], X[0, 1]])
    normal = reg.w
    d = -point.dot(normal)
    d_ = (d-min(z))/(max(z)-min(z))
    xx, yy = np.meshgrid([0.2, 0.7], [0.2, 0.7])
    z = (-normal[0] * xx - normal[1] * yy - d_) * 1. /normal[2]
    ax.plot_surface(xx, yy, z, alpha=0.2, color=[0,1,0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('normalized house age')
    ax.set_ylabel('normalized num of convenience store')
    ax.set_zlabel('normalized house price')
    plt.show()
    
        
    