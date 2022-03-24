# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:39:52 2022

@author: matth
"""
from vpython import *

"""
mygraph = graph(xtitle="Time (s)", ytitle="Height (m)",fast=False)
myline = gcurve(color=color.red,width=2)
t = 0.001
while t <10:
    h = log(t)*sin(t**2)
    myline.plot(t,h)
    t = t+0.001
"""
#Task 6 Begins here
mygraph = graph(xtitle="x", ytitle="f(x)",fast=False)
myline = gcurve(color=color.blue, width = 3)
x = (-5)
while x < 5:
    h = x * cos(x)
    myline.plot(x, h)
    x = x + 0.001