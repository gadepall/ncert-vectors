import numpy as np


#Given points
A = np.array(([-4,0]))
B = np.array(([10,0]))
e_1 = np.array(([1,0]))

#Diection vector
n = A-B
c = (np.linalg.norm(A)**2- np.linalg.norm(B)**2)/2

x = c/(n@e_1)

print(x)
