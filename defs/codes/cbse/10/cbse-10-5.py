import numpy as np


#Given points
A = np.array(([6,-4]))
B = np.array(([-2,-7]))

#Standard Basis vectors
e_1 = np.array(([1,0]))
e_2 = np.array(([0,1]))

#Ratio 
k =  -((e_1@A)/(e_1@B))

#y-coordinate
y = (k*e_2@B+e_2@A)/(k+1)


print(k,y)
