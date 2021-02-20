# Importing pandas library
import pandas as pd
# Importing linear_model sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Reading data through csv file
restaurant_data = pd.read_csv("data.csv")
# Choosing train_data and test_data for further operation
train_data = restaurant_data.drop(['revenue','City Group','Type'], axis=1)
test_data = restaurant_data["revenue"].astype(str)
# Implementing linear model using library function
Regresion = linear_model.LinearRegression()
Regresion.fit(train_data, test_data)
revecnue_prediction=Regresion.predict(train_data)
# Printing R2 score
print("R2: %.2f" % r2_score(test_data, reveue_prediction))
# Printing RMSE score
print("RMSE: %.2f" % mean_squaed_error(test_data, revenue_prediction))