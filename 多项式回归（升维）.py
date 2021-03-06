import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as ply
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(42)
m = 100
X = 6*np.random.rand(m, 1) - 3
y = 0.5*X**2 + X + 2 + np.random.randn(m, 1)
plt.plot(X, y, 'b.')
plt.show()


X_train = X[:80]
y_train = y[:80]
X_test = X[80:]
y_test = X[80:]

d = {1: 'g-', 2:'r+', 10:'y*'}
for i in d:
    # degree升到几维，include_bias是否要截距项
    poly_features = PolynomialFeatures(degree=i, include_bias=True)
    X_poly_train = poly_features.fit_transform(X_train)
    X_poly_test = poly_features.fit_transform(X_test)
    print(X_train[0])
    print(X_poly_train[0])
    print(X_train.shape)
    print(X_poly_train.shape)

