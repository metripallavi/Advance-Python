#WAP TO VIEW THE ARRAY USING VIEW()
import numpy as np
x=np.array([[2,4],[6,8]])
print("before viewing  array=",x)
y=x.view()
print("after viewing array=",y)