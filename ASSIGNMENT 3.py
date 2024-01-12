#WAP TO TAKE 1DM ARRAY,MULTIPLY EVERY ELEMENT BY 3 AND COPY IT INOT ANOTEHR ELEMENT
import numpy as np
x=np.array([2,3,4])
print("array element are = ",x)
y=3*x
print("elements after muliplying with 3 is = ", y)
z=y.copy()
print("matrix after copying the elements = ", z)