# -*- coding: utf-8 -*-
import os

data_dir = 'data'

feature_data = os.path.join(data_dir, 'iris_data.pickle')

X_test = os.path.join(data_dir, 'X_test.pickle')
X_train = os.path.join(data_dir, 'X_train.pickle')
y_test = os.path.join(data_dir, 'y_test.pickle')
y_train = os.path.join(data_dir, 'y_train.pickle')

model = os.path.join(data_dir, 'model.p')

