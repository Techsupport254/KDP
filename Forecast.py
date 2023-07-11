# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df1 = pd.read_csv('Clean_CSV.csv')

df1.drop(df1.columns[0], axis=1, inplace=True)
# use polynomial regression to forecast

# 1. TotalRevenue
# create a linear regression object
linear_reg = LinearRegression()
# create a polynomial regression object
poly_reg = PolynomialFeatures(degree=4)
# split the data into training upto 2018 and testing sets from 2019
x_train = df1['Year'].values.reshape(-1,1)
y_train = df1['TotalRevenue'].values.reshape(-1,1)
x_test = df1['Year'].values.reshape(-1,1)
y_test = df1['TotalRevenue'].values.reshape(-1,1)

# fit the polynomial regression to the data
x_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_poly,y_train)
linear_reg.fit(x_poly,y_train)

# test the model on the test set
y_pred1 = linear_reg.predict(poly_reg.fit_transform(x_test))
# convert to data frame
y_pred1 = pd.DataFrame({'Year':x_test.reshape(1,-1)[0], 'TotalRevenue':y_pred1.reshape(1,-1)[0]})
# display
print(y_pred1)

# predict for 2023 to 2033
y_pred1 = linear_reg.predict(poly_reg.fit_transform(np.array([2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]).reshape(-1,1)))
# convert to data frame
y_pred1 = pd.DataFrame({'Year':[2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], 'TotalRevenue':y_pred1.reshape(1,-1)[0]})
# display
print(y_pred1)



# 2. CostOfRevenue
# create a linear regression object
linear_reg = LinearRegression()
# create a polynomial regression object
poly_reg = PolynomialFeatures(degree=4)
# split the data into training upto 2018 and testing sets from 2019
x_train = df1['Year'].values.reshape(-1,1)
y_train = df1['CostOfRevenue'].values.reshape(-1,1)
x_test = df1['Year'].values.reshape(-1,1)
y_test = df1['CostOfRevenue'].values.reshape(-1,1)

# fit the polynomial regression to the data
x_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_poly,y_train)
linear_reg.fit(x_poly,y_train)

# test the model on the test set
y_pred2 = linear_reg.predict(poly_reg.fit_transform(x_test))
# predict for 2023 to 2033
y_pred2 = linear_reg.predict(poly_reg.fit_transform(np.array([2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]).reshape(-1,1)))
# convert to data frame
y_pred2 = pd.DataFrame({'Year':[2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], 'CostOfRevenue':y_pred2.reshape(1,-1)[0]})
# display
print(y_pred2)

# 3. OperatingIncome
# create a linear regression object
linear_reg = LinearRegression()
# create a polynomial regression object
poly_reg = PolynomialFeatures(degree=4)
# split the data into training upto 2018 and testing sets from 2019
x_train = df1['Year'].values.reshape(-1,1)
y_train = df1['OperatingIncome'].values.reshape(-1,1)
x_test = df1['Year'].values.reshape(-1,1)
y_test = df1['OperatingIncome'].values.reshape(-1,1)

# fit the polynomial regression to the data
x_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_poly,y_train)
linear_reg.fit(x_poly,y_train)

# test the model on the test set
y_pred3 = linear_reg.predict(poly_reg.fit_transform(x_test))
# predict for 2023 to 2033
y_pred3 = linear_reg.predict(poly_reg.fit_transform(np.array([2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]).reshape(-1,1)))
# convert to data frame
y_pred3 = pd.DataFrame({'Year':[2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], 'OperatingIncome':y_pred3.reshape(1,-1)[0]})
# display
print(y_pred3)

# FreeCashFlow
# create a linear regression object
linear_reg = LinearRegression()
# create a polynomial regression object
poly_reg = PolynomialFeatures(degree=4)
# split the data into training upto 2018 and testing sets from 2019
x_train = df1['Year'].values.reshape(-1,1)
y_train = df1['FreeCashFlow'].values.reshape(-1,1)
x_test = df1['Year'].values.reshape(-1,1)
y_test = df1['FreeCashFlow'].values.reshape(-1,1)

# fit the polynomial regression to the data
x_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_poly,y_train)
linear_reg.fit(x_poly,y_train)

# test the model on the test set
y_pred4 = linear_reg.predict(poly_reg.fit_transform(x_test))
# predict for 2023 to 2033
y_pred4= linear_reg.predict(poly_reg.fit_transform(np.array([2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]).reshape(-1,1)))
# convert to data frame
y_pred4 = pd.DataFrame({'Year':[2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], 'FreeCashFlow':y_pred4.reshape(1,-1)[0]})
# display
print(y_pred4)

# combine the data frames
df2 = pd.concat([y_pred1,y_pred2,y_pred3,y_pred4], axis=1)

# drop the year column
df2.drop('Year', axis=1, inplace=True)

# make year the index
df2.set_index(np.array([2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]), inplace=True)

# convert the values to decimal notation
df2 = df2.applymap(lambda x: '%.2f' % x)
# remove the decimal part
df2 = df2.applymap(lambda x: x.split('.')[0])
# display
print(df2)

# calculate the gross profit using the predicted values
df2['GrossProfit'] = df2['TotalRevenue'].astype('float') - df2['CostOfRevenue'].astype('float')
# convert the gross profit to decimal notation
df2['GrossProfit'] = df2['GrossProfit'].apply(lambda x: '%.2f' % x)
# remove the decimal part
df2['GrossProfit'] = df2['GrossProfit'].apply(lambda x: x.split('.')[0])
# display
print(df2)

# download the data frame as a csv file
df2.to_csv('PredictedValues.csv')
