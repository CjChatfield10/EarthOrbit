import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import math as m 

#variables

G = 6.674 * (m.pow(10, -11))
L = 2.661 * m.pow(10,40)
M = 1.989 * m.pow(10, 30)
n = 5.972 * m.pow(10,24)

#initial conditions

r0 = 1.471 * m.pow(10, 11)
v0 = 0

def model (initialradiusandradialspeed, t):
                
    r = initialradiusandradialspeed[0]

    drdt = initialradiusandradialspeed[1]

    d2rdt2 = ((L*L)/(n*n * r * r * r)) - (G * M)/ (r * r)

    return [drdt, d2rdt2]

initialradiusandradialspeed = [r0, v0]

t = np.linspace(0, 100000000, 1000) #time is about 3.17 years

#find solution to nonlinear problem
sol = odeint (model, initialradiusandradialspeed, t)

x = sol[:, 0]
y = sol[:, 1]


#plot results (nonlinear)

plt.plot (t, sol[:, 0])
plt.xlabel ('time')
plt.ylabel ('distance from sun')
plt.show()


#phase plane

plt.figure()
plt.plot (x, y)
plt.plot(x[0], y[0], 'ro')
plt.xlabel('r')
plt.ylabel('r dot')
plt.show()

