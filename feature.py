# coding: utf-8
from sklearn.datasets import load_iris
import pickle
import conf
import numpy as np 

iris = load_iris()

with open(conf.feature_data,'wb') as f:
    pickle.dump(iris,f)

