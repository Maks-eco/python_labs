import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import pandas.DataFrame as df
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

data_train = pd.read_csv('text/tar_train.txt', sep=",", low_memory=False)
data_test = pd.read_csv('text/tar_test.txt', sep=",", low_memory=False)
nums = 8 #9. temp - temperature in Celsius degrees: 2.2 to 33.30
print(nums)
diabetes_X_train = data_train.iloc[:,nums] #10
diabetes_X_train = diabetes_X_train.values.reshape(-1,1)
diabetes_X_test = data_test.iloc[:,nums] #10
diabetes_X_test = diabetes_X_test.values.reshape(-1,1)
# print(diabetes_X)
diabetes_y_train = data_train.iloc[:,12]
diabetes_y_train = diabetes_y_train.values.reshape(-1,1)
diabetes_y_test = data_test.iloc[:,12]
diabetes_y_test = diabetes_y_test.values.reshape(-1,1)
# print(targ_X)

# # Split the data into training/testing sets
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]

# # print(diabetes.target)

# # Split the targets into training/testing sets
# diabetes_y_train = targ_X[:-20]
# diabetes_y_test = targ_X[-20:]
# print(diabetes_y_train)
# print(diabetes_y_test)
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()