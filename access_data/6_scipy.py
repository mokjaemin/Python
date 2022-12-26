import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from scipy import interpolate

x = np.array([1,2,3,4,5])
y = np.array([1.,0.8,0.4,0.3,0.2])

# plt.plot(x,y, '*')
# plt.show()

# linear interpolate
# 선형 보간
f_lin = interpolate.interp1d(x,y)
x_new = np.arange(1,5,0.1)
y_lin = f_lin(x_new)


# splint interpolate
# 곡선 보간
tck = interpolate.splrep(x,y,s=0)
y_sp1 = interpolate.splev(x_new, tck, der=0)


fig, ax = plt.subplots()
ax.plot(x,y,'o', label='Data')
ax.plot(x_new, y_lin, label='linear')
ax.plot(x_new, y_sp1, label='linear')
ax.legend()
plt.show()