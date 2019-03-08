from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
from keras.optimizers import Adam, SGD
from sklearn.datasets import load_boston

df = pd.read_csv('...Linear-Regression/test.csv')

model = Sequential(0)
model.add(Dense(1, input_shape=(len(X.columns),)))
print(model.summary())
model.compile(Adam(lr=0.8), 'mean_squared_error')
model.fit(X, y, epochs=50)

y_pred = model.predict(X)

df.plot(kind='scatter',
             x='Features',
        y='Price')
