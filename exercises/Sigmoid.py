import numpy as np
import matplotlib.pyplot as plt
# plot sigmoid curve
x = np.arange(-10.,10.,1.)
b = 0 # intercept
m = 1 # slope
sigmoid = lambda x,b,m: np.exp((b + m*x)) / (1 + np.exp((b + m*x)))
y = sigmoid(x,b,m)

## hint : scatter (x,y)
plt.scatter(x,y)
plt.title("Sigmoid (Logistic) Function")