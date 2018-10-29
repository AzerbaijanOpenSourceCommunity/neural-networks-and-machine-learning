import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston

# Importing dataset
boston = load_boston()
# Converting dataset type into DataFrame
bos = pd.DataFrame(boston.data)

# Exploring dataset
descrpition = boston['DESCR']
first_5_rows = bos.head()
statistical_description = bos.describe()
info = bos.info()

# Convert index into the column names
bos.columns = boston.feature_names

# Adding new PRICE column to the dataframe , which is the  target value
bos['PRICE'] = boston['target']
X = bos[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
         'PTRATIO', 'B', 'LSTAT']]

y = bos['PRICE']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# coeff shows that how change of 1 unit  can affect Price

cdf = pd.DataFrame(model.coef_, X.columns, columns=['Coeff'])

# result is the predicted values of houses which are located in different regions

predictions = model.predict(X_test)
predictions
from sklearn import metrics

# These 3 mehtods used for minimize error  - to get best fit  regression line

MAE = metrics.mean_absolute_error(y_test, predictions)
MSE = metrics.mean_squared_error(y_test, predictions)
RMSE = np.sqrt(metrics.mean_squared_error(y_test, predictions))

print('MAE : {} \n\nMSE :  {} \n\nRMSE :{}   \n\n'.format(MAE, MSE, RMSE))  # 3.80 ; 28.88 ;  5.37

plt.scatter(model.predict(X_train), model.predict(X_train) - y_train, c='b', s=40, alpha=0.4, label='Training Data')
plt.scatter(model.predict(X_test), model.predict(X_test) - y_test, c='g', s=40, label="Test Data")
plt.hlines(y=0, xmax=50, xmin=0, label="Regression Line", linestyles='solid')
plt.title("Residual Plot using training(blue) & test(green) data")
plt.ylabel('Residuals')
plt.legend()

plt.show()
