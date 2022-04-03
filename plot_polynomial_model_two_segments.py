class PolymoialModel:
    def __init__(self,a,b,c,d,x) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x

class PolynomialModelTwoSegments:
    def __init__(self, seg_0,seg_1) -> None:
        self.seg_0= seg_0
        self.seg_1= seg_1
    


seg_0 = PolymoialModel(0.0,-0.000807,0.003739,0.0,0.0)
seg_1 = PolymoialModel(0.0,0.0,0.0,-0.411194,25.0)

curve_two_segments = PolynomialModelTwoSegments(seg_0,seg_1)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, seg_1.x, 0.1)
y_0 = x * (x * (x * seg_0.a + seg_0.b) + seg_0.c) + seg_0.d

x_1 = np.arange(seg_1.x, 70,0.1)
y_1 = x_1 * (x_1 * (x_1 * seg_1.a + seg_1.b) + seg_1.c) + seg_1.d

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x,y_0,color='tab:blue')
ax.plot(x_1,y_1,color='tab:red')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
