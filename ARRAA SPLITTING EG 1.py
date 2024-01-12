#WAP TO USING ARRAY_SPLIT()
#ARRAY_SPLIT() - USED for dividing the array into parts
import numpy as np
arr=np.array([2,7,8,9,4,7,8,9,11])
x=np.array_split(arr,2)
print("after splitting of array= ",x)