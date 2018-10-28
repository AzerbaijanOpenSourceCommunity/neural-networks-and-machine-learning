
import numpy as np
import pandas as pd
import matplotlib.pyplot as mt
import stats as st
import scipy as sc
import sklearn


from sklearn.datasets import load_boston

boston = load_boston()

bos = pd.DataFrame(boston.data)
bos.head()
bos['PRICE'] = boston.target
from sklearn.linear_model import LinearRegression

X = bos.drop("PRICE",axis=1)
lm = LinearRegression()
lm.fit(X,bos.PRICE) #F(x,y) = 0



import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout #Dense - neuron layers
from keras.optimizers import RMSprop

batch_size = 128
num_classes = 1
epochs = 20 # epochs - iteration

#train and test sets
(x_train,y_train),(x_test,y_test)  = mnist.load_data()

x_train  = x_train.reshape(60000,784)
x_test = x_test.reshape(10000,784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model = Sequential()
model.add(Dense(512,activation='relu',input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes,activation='softmax'))


model.compile(loss="categorical_crossentropy",
              optimizer=RMSprop(),
              metrics=['accuracy'])

model.summary()

