# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:23:20 2022

@author: matth
"""

from vpython import *

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
