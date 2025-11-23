#RBF 
import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
T = np.array([0,1,1,0])

# RBF centers
C = np.array([[0,0], [1,1]])

# RBF Layer (Gaussian)
H = np.exp(-((X[:,None] - C) ** 2).sum(axis=2))

# weights by least squares
W = np.linalg.pinv(H).dot(T)

# prediction
Y = H.dot(W)

# MSE
print("MSE =", np.mean((T - Y) ** 2))
