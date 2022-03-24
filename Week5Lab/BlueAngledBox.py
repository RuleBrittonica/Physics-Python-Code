# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:56:32 2022

@author: matthew
"""

from vpython import *
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