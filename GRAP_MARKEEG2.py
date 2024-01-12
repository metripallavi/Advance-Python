#WAP TO PRINT MARKERS IN GRAPH AND CHANGE COLOR OF MARKER
import matplotlib.pyplot as plt
import numpy as np
c=np.array([3,8,1,10])
plt.plot(c,marker='*',ms=20,mec='r')
plt.show()
