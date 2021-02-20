# Importing pandas library
import pandas as pd
# Importing linear_model sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Importing numpy library
import numpy as np
# Importing matplotlib.pyplot library for plots
import matplotlib.pyplot as plt
# Reading data through csv file
restaurant_data = pd.read_csv("data.csv")
# Choosing train_data and test_data for further operation
train_data = restaurant_data.drop(['revenue', 'City Group', 'Type'], axis=1)
test_data = restaurant_data["revenue"].astype(str)
# Implementing linear model using library function
Regression = linear_model.LinearRegression()
Regression.fit(train_data, test_data)
revenue_prediction = Regression.predict(train_data)
# Printing R2 and RMSE score
print("R2: %.2f" % r2_score(test_data, revenue_prediction))
# Squaring errors for removing negative values
print("RMSE: %.2f" % mean_squared_error(test_data, revenue_prediction))

numeric_features = restaurant_data.select_dtypes(include=[np.number])
corr = numeric_features.corr()

quality_pivot = restaurant_data.pivot_table(index=['P2'], values=['revenue'], aggfunc=np.median)
quality_pivot.plot(kind='bar', color='green')
plt.show()

correlated_features = restaurant_data[['P2', 'P28', 'P6', 'P21', 'P11']]
correlated_target = restaurant_data['revenue']
Regression_1 = linear_model.LinearRegression()
Regression_1.fit(correlated_features, correlated_target)

prediction1 = Regression_1.predict(correlated_features)
