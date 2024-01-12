#stack() - used for prinitng array elements into stack format.we have 3 types of stack functions:
#simple stack()
#horizontal stack()
#vertical stack()

import numpy as np
x=([[1,2],[5,6]])
y=([[4,7],[9,15]])
z=np.stack((x,y))
print("simple stacked =",z)
