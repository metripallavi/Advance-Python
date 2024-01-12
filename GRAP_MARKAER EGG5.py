#WAP TO PRINT MARKERS IN GRAPH AND LINE STYLE
import matplotlib.pyplot as plt
import numpy as np
u=np.array([3,8,1,10])
plt.plot(u,linestyle='dotted',marker='*',ms=15)
plt.show()