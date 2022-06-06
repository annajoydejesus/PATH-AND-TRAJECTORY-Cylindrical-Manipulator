#Created on Fri Jun  01 23:11:32 2022
# @author: Annajoydejesus

import numpy as np
import matplotlib.pyplot as plt

#degrees to radian converter
def mm_to_m(d):
    m = 1000
    return d/m

di = float(input('di = ')) #initial position
di = mm_to_m(di)

vi = float(input('vi = ')) #initial velocity
vi = mm_to_m(vi)

df = float(input('df = ')) #final position
df = mm_to_m(df)

vf = float(input('vf = ')) #final velocity
vf = mm_to_m(vf)

ti = float(input('ti = ')) #initial time
tf = float(input('tf = ')) #final time

#cubic
# a = di  b = df  c= tf
#Solve the solution for d(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return  a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x, di, df, tf)

plt.figure()
plt.plot(x, y, 'r', linestyle='-')
plt.text(1,1.5,'a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()









