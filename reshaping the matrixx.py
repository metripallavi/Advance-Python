##WAP TO PRINT RESHAPE  THE  MATRIX

import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print("the matrix is=", x)
print("the dimension is = ", x.ndim)
print("the shape of matrix is = ", x.shape)
y=x.reshape(3,3)
print( y)
