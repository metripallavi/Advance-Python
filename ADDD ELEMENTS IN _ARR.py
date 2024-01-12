#WAP TO ADD ELEMENTS OF ARRAY
import numpy as np
x=np.array([1,2,3,4,5,6])
for i in x:
    print(x[i])
    count=0
    for i in x:
        count=count+x[i]
        print(count)