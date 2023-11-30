from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape((-1,1))
y = np.array([2,4,6,8,10,12,14,16,18,20])

model = LinearRegression()

model.fit(x,y)

# predit_x = np.array([20,30,40]).reshape((-1,1))
print(f"The predicted value:{model.predict(np.array([20,30,40]).reshape((-1,1)))}")