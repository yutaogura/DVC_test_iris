# -*- coding: utf-8 -*-
import pickle
import conf

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

with open(conf.X_test,'rb') as f:
    X_test = pickle.load(f)

with open(conf.y_test,'rb') as f:
    y_test = pickle.load(f)
    
y_pred = model.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))