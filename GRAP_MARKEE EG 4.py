#WAP TO PRINT MARKERS IN GRAPH AND CHANGE COLOR OF MARKER AND FACE COLOUR
import matplotlib.pyplot as plt
import numpy as np
k=np.array([3,8,1,10])
plt.plot(k,marker='o',ms=20,mec='r',mfc='hotpink')
plt.show()