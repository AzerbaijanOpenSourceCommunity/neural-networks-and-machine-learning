from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
from keras.optimizers import Adam, SGD
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt


df = pd.read_csv("datasets/weight-height.csv")
X = df[['Height']].values
y = df[['Weight']].values

model = Sequential()
model.add(Dense(1, input_shape=(1,)))
print(model.summary())
model.compile(Adam(lr=0.8), 'mean_squared_error')
model.fit(X, y, epochs=40)

y_pred = model.predict(X)

df.plot(kind='scatter',
        x='Height',
        y='Weight')

plt.plot(X, y_pred, color='red')
