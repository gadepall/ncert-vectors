
import numpy as np


#Given points
A = np.array(([0,-3]))
O = np.array(([0,0]))
B = np.array(([4,0]))

AB = np.linalg.norm(A-B)
print(AB)
