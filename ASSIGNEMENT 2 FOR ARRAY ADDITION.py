#WAP TO TAKE 2 ARRAY ROM USER ADD 2 ARAYS AND RESHAPE IT TO SINGLE DM ARRAY

import numpy as np
x=np.array([[1,2],[3,4]])
y= np.array([[5,6],[7,8]])
print("before reshaping x=",x)
print("before reshaping y=",y)
z=x+y
print("addition =",z)
a=z.reshape(-1)
print("reshaped = ",a)