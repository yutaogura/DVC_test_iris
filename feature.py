# coding: utf-8
from sklearn.datasets import load_iris
import pickle
import conf
import numpy as np 

iris = load_iris()

x = iris.data

y1 = x[:,0]**2
y2 = x[:,1]**2
y3 = x[:,2]**2
y4 = x[:,3]**2

y1 = y1.reshape(1,len(y1)).transpose()
y2 = y2.reshape(1,len(y2)).transpose()
y3 = y3.reshape(1,len(y3)).transpose()
y4 = y4.reshape(1,len(y4)).transpose()

iris.data = np.hstack((x,y1,y2,y3,y4))

with open(conf.feature_data,'wb') as f:
	pickle.dump(iris,f)

