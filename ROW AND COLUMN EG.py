import numpy as np

a=np.array([[1,20,3],[4,57,6]])
print(a)
for i in a:
    print("i is=", i)
    for j in i:
        print("j is=",j)