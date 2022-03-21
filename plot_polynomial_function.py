# this script should plot the curve function in 3rd polynomial
# y = a * x^3 + b * x^2 + c * x + d

import matplotlib.pyplot as plt
import numpy as np

a = 1.0
b = 0.9
c = 1.2
d =3.5

x = np.arange(0, 200, 0.1)
y = x * (x * (x * a + b) + c) + d

plt.plot(x,y)
plt.show()