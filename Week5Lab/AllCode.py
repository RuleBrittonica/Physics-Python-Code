# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:56:31 2022

@author: matth
"""

from vpython import *
from uncertainties import ufloat 
from uncertainties.umath import *

#Task 1

x0 = 0
y0 = 0
z0 = 0
a = 1 
b = 2
c = 1
L = 2
H = 0.2
W = 0.2
mybox = box(pos=vector(x0,y0,z0),
            axis=vector(a,b,c), length=L,
            height=H, width=W,
            color=color.blue)

#Task 2

R = 1
mysphere = sphere(radius=R, color = color.cyan)
volume = (4/3) *pi*R**3
print("The volume of the sphere is:", volume)

#Task 3

x0 = 0
y0 = 0
z0 = 0
x1 = 4
y1 = 0
z1 = 0
a = 1 
b = 2
c = 1
L = 2
H = 0.2
W = 0.2
mybox = box(pos=vector(x0,y0,z0),
            axis=vector(a,b,c), length=L,
            height=H, width=W,
            color=color.blue)
pointer = arrow(pos=vector(0,4,1),
            axis=vector(5,0,0), shaftwidth=0.5,
            color=color.orange)
myspring = helix(pos=vector(0,8,1),
            axis=vector(0,5,0), radius=0.5,
            color=color.green)
myRing = ring(pos=vector(1,1,1),
            axis=vector(0,1,0),
            radius=0.5, thickness=0.1,
            color=color.magenta)
myell = ellipsoid(pos=vector(x1,y1,z1),
            axis=vector(a,b,c),
            length=1, height=2, width=1.5,
            color=color.cyan)

#Task 4

c = 3E8
massProton = 1.67E-27

print("Energy of a proton is: ", massProton*c**2, "Joules")

#Task 5

t = -20
while t < 100:
    print("t= ", t)
    t = t + 5
    
#Task 6

mygraph = graph(xtitle="x", ytitle="f(x)",fast=False)
myline = gcurve(color=color.blue, width = 3)
x = (-5)
while x < 5:
    h = x * cos(x)
    myline.plot(x, h)
    x = x + 0.001
    
#Task 7

x = ufloat(9.4,0.3)
y = ufloat(7.4,0.2)
z = ufloat(4.9,0.1)

print("r=",sqrt(x**2 + y**2 + z**2))

