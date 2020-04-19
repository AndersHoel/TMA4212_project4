import numpy as np

import numpy.linalg as npl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from scipy.sparse import identity, dok_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import factorized


xgrid = np.linspace(0,1,100)

Apoints_x = [0.2*x for x in range(6)]+[0 for x in range(1,6)]
Apoints_y = [0 for x in range(6)]+[0.2*x for x in range(1,6)]

Bpoints_x = [.2,.4,.6,.2,.4,.2,.4]
Bpoints_y = [.2,.2,.2,.4,.4,.6,.6]

Cpoints_x = [.2,.4,.6,.6,.8]
Cpoints_y = [.8,.8,.4,.6,.2]

Dpoints_x = [0.2*x for x in range(1,5)]+[np.sqrt(1-(0.2*x)) for x in range(1,5)]
Dpoints_y = [1-(0.2*x)**2 for x in range(1,5)]+ [(0.2*x) for x in range(1,5)]

plt.plot(xgrid,1-xgrid**2, color='grey', linestyle='dashed')
plt.grid()
plt.plot([0 for x in range(100)],xgrid, color='black')
plt.plot(xgrid,[0 for x in range(100)], color='black')
plt.scatter(Apoints_x,Apoints_y, color='green', label="A")
plt.scatter(Bpoints_x,Bpoints_y, color='blue', label="B")
plt.scatter(Cpoints_x,Cpoints_y, color='orange', label="C")
plt.scatter(Dpoints_x,Dpoints_y, color='red', label="D")
#plt.legend()

plt.show()
