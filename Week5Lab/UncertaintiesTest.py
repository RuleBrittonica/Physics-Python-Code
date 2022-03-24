# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:45:45 2022

@author: matth
"""

from uncertainties import ufloat 
from uncertainties.umath import *

x = ufloat(9.4,0.3)
y = ufloat(7.4,0.2)
z = ufloat(4.9,0.1)

print("r=",sqrt(x**2 + y**2 + z**2))
