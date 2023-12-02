from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,4,5,6,7]).reshape(-1,1)
y = np.array([10,20,30,40,50,60,70])

model = LinearRegression()
model.fit(x,y)
predit_x = np.array([20,30,40]).reshape((-1,1))
print(f"The predicted value:{model.predict(predit_x)}")