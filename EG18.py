#WAP EG 3 RESHAPING
import numpy as np
x=np.array([[20,30],[40,50]])
print("before copying=",x)
y=x.copy()
print("after copying=",y)
x=x.reshape(-1)
print("after reshaping  the array=",x)
print("after reshaping x y is now=",y)