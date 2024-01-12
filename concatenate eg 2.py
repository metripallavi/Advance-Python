#WAP TO CONCATENATE USING AXIS
import numpy as np
x=np.array([[4,6],[2,5]])
y=np.array([[8,9],[1,2]])
z=np.concatenate((x,y),axis=1)
print("concatenated elements are as follows =", z)