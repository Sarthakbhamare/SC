#linear regression 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("/content/Salary_Data.csv")
print(data.head())

# split columns
X = data.iloc[:, 0].values.reshape(-1,1)
Y = data.iloc[:, 1].values.reshape(-1,1)

# model
reg = LinearRegression()
reg.fit(X, Y)

# prediction
pred = reg.predict(X)

# plot
plt.scatter(X, Y)
plt.plot(X, pred, color='red')
plt.show()
