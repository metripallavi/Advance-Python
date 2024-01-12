#WAP TO CHAGE FONT OF TITLE AND LABEL
#FONT DICT- ATTRIBUTE PRESENT IN TITTLE LAEL FOR CHANGING FONT STYLE
#WAP TO PLOT GRID LINES
#NOTE HERE X AXIS IS VERTICAL AND YAXIS IS HORIZONTAL
import numpy as np
import matplotlib.pyplot as plt
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
font1={'family':'serif','color':'blue','size':20}
font2 = {'family': 'serif', 'color': 'darkred','size':15}
plt.title("HEART BEAT",fontdict=font1)
plt.xlabel("AVERAGE PULSE",fontdict=font2)
plt.grid(color='green',linestyle='--',linewidth=0.5,axis='x')
plt.plot(x,y)
plt.show()