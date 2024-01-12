#WAP TO PRINT VIEW(VIEW FUNCTION )
import numpy as np
x=np.array([[1,4],[6,8]])
print("before view = ",x)
y=x.view()
print("after view = ",y)
