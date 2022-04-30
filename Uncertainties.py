from re import M
from uncertainties import ufloat
from uncertainties.umath import *
import math

# Vcell = ufloat (1.1, 0.01)
# Icell = ufloat (16.5, 0.2)
# Vlight = ufloat (12.1, 0.3)
# Ilight = ufloat (1.72, 0.3)
# AcellL = ufloat (2.5, 0.1)
# Acellh = ufloat (6.2, 0.1)
# Alightr = ufloat (10, 0.1)
# x = 3.5 / 100
# Plight = Vlight * Ilight
# Acell = AcellL * Acellh
# Alight = Alightr * Alightr * 3.14159

# Top = Vcell * Icell
# Bottom = (Acell / Alight) * x * Plight

# print (Top / Bottom)

x = 0.05

a = ufloat (13.96, x)
b = ufloat (14.04, x)
c = ufloat (13.83, x)
d = ufloat (13.99, x)
e = ufloat (14.23, x)
f = ufloat (13.90, x)
g = ufloat (14.39, x)
h = ufloat (14.09, x)
i = ufloat (13.95, x)

total = a + b + c + 2 * d + e + f + g + h + i
avg1 = total / 10

j = ufloat (14.22, x)
k = ufloat (14.11, x)
l = ufloat (14.16, x)
m = ufloat (14.03, x)
n = ufloat (14.03, x)
o = ufloat (14.46, x)
p = ufloat (14.48, x)
q = ufloat (14.10, x)
r = ufloat (14.04, x)
s = ufloat (14.40, x)

newtotal = j + k + l + m + n + o + p + q + r + s
avg2 = newtotal / 10

avgDif = avg2 - avg1
uncertainty = 0.07184 #from error propagation
Zscore = avgDif / uncertainty

print ("Average 1930s = ", avg1)
print ("Average 2000s = ",avg2)
print ("Difference of averages = ", avgDif)
print ("Scatter in individuals of 1930s = ", (g - c) / (math.sqrt (10)))
print ("Scatter in individuals of 2000s = ", (p - m) / (math.sqrt (10)))
print ("Scatter in mean of 1930s = ", (g - c) / 10)
print ("Scatter in mean of 2000s = ", (p - m) / 10)
print ("Z-score = ", Zscore)

