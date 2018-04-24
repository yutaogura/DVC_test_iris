# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import pickle
import conf

with open(conf.X_train,'rb') as f:
    X_train = pickle.load(f)
    
with open(conf.y_train,'rb') as f:
    y_train = pickle.load(f)


logreg = LogisticRegression()
logreg.fit(X_train, y_train)

output = conf.model

with open(output, 'wb') as fd:
    pickle.dump(logreg, fd)

