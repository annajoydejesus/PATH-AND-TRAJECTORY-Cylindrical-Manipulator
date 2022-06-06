#Created on Fri Jun  01 23:11:32 2022
# @author: Annajoydejesus

from ctypes import RTLD_GLOBAL
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lenths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# link limits converted to meters
lm2 = float(input("lm2 = "))
lm2 = mm_to_meter(lm2)
lm3 = float(input("lm3 = "))
lm3 = mm_to_meter(lm3)

# Create Links
#revolute=d,r/a, theta, alpha,offset   prisma=theta,r/a, alpha,d, offset
Cyli_RPP = DHRobot([
    RevoluteDH(a1, 0, (0/180)*np.pi , 0, qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH((270/180)*np.pi, 0, (270/180)*np.pi, a2, qlim=[0,lm2]),
    PrismaticDH(0, 0, 0, a3, qlim=[0,lm3]),
], name='CYLINDRICAL_RPP')
print(Cyli_RPP)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q_o = np.array([0,0,0])
q_pick = np.array([deg_to_rad(float(input("T1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = ")))])
q2 = np.array([deg_to_rad(float(input("T1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = ")))])
q3 = np.array([deg_to_rad(float(input("T1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = ")))])

#Trajectory Commands
traj1 = rtb.jtraj(q_o,q_pick,10)
print(traj1)
print(traj1.q)
traj2 = rtb.jtraj(q_pick,q2,10)
print(traj2)
print(traj2.q)
traj3 = rtb.jtraj(q2,q3,10)
print(traj3)
print(traj3.q)

#PLOT SCALE
x1 = -0.05
x2 = 0.05
y1 = -0.05
y2 = 0.05
z1 = -0.05
z2 = 0.05

#for Joint Variable vs Time(s) table
rtb.qplot(traj1.q)
rtb.qplot(traj2.q)
rtb.qplot(traj3.q)

# plot of trajectory
Cyli_RPP.plot(traj1.q, limits = [x1, x2, y1, y2, z1, z2],movie='CYLI_1.gif')
Cyli_RPP.plot(traj2.q, limits = [x1, x2, y1, y2, z1, z2], movie='CYLI_2.gif')
Cyli_RPP.plot(traj3.q, limits = [x1, x2, y1, y2, z1, z2],movie='CYLI_3.gif', block=True)
#Cyli_RPP.teach(jointlabels=1)

