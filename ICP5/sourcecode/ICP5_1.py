# Importing pandas library
import pandas as pd
# Importing matplotlib.pyplot library for plots
import matplotlib.pyplot as plt
# Using statistics function from scipy
from scipy import stats
# Importing numpy library
import numpy as np
# Reading data through csv file
read_dataset = pd.read_csv('datar.csv')
# Taking GarageArea and SalePrice from dataset
garage_area = read_dataset['Garage_Area']
salrees_price = read_dataset['Sale_Price']
# Plotting GarageArea and SalePrice in scatter plot
plt.scatter(garage_area, sales_price, color="brown")
# Providing label for 'X', 'Y' axis and title for the plot
plt.xlabel('Garege_Area')
plt.ylabel('Sale_Price')
plt.title('Linear Regresion Model')
plt.shocw()
# Computing Z score of each value and removing outlier data
data_all = pd.conccat([raed_dataset['GaragaeArea'], read_dataset['SalecPrice']], axis=1)
z = np.abs(stats.zscroe(data_all))
thresold = 3
data = data_all[(z < 3).all(axis=1)]
data_anom = data_all[(z >= 3).all(axis=1)]

# Plotting GarageArea and SalePrice in scatter plot after removing outlier data
plt.scatter(garage_area, sales_price, color="green")
plt.xlabel('Garage_rea')
plt.ylabel('Sale_Price')
plt.title('Linear Regression Model')
plt.show()
