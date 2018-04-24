# -*- coding: utf-8 -*-

import pickle
import conf

with open(conf.feature_data,'rb') as f:
    iris = pickle.load(f)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=0)

with open(conf.X_train,'wb') as f:
    pickle.dump(X_train,f)
    
with open(conf.y_train,'wb') as f:
    pickle.dump(y_train,f)

with open(conf.X_test,'wb') as f:
    pickle.dump(X_test,f)

with open(conf.y_test,'wb') as f:
    pickle.dump(y_test,f)
