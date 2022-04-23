from vpython import *

# setup the pivot
pivot = vector (0,10,0)

# setup loop constants
t = 0
dt = 0.01

# shape initialisation

r = 0.2
m1 = 5

# gravity and spring force
k = 10
m1 = 5
g = vector(0,-9.8,0)
L=10

# setup drag

density = 1.1
A = pi * r ** 2
C = 0.7

# backdrop = box (Length = 50, Height = 50, Width = 50,
#                 pos = vector (0, 0, -100),
#                 color = color.white)

weight = sphere (pos = vector (0, 0, 0),
                  radius = r,
                  color = color.red,
                  vel = vector (5, 0, 0),
                  make_trail = True)

spring = helix (pos = pivot,
                axis = (weight.pos-pivot),
                color = color.blue)


while t <=30:
    t = t + dt
    rate (100)
    x = mag(spring.axis) - L
    F1 = (-k) * (x) * norm (spring.axis)
    acc = (F1 / m1) + g
    Fd = 0.5 * density * (mag (weight.vel)) ** 2 * norm (weight.vel) * C * A 
    weight.vel = weight.vel + acc * dt - Fd * dt
    weight.pos = weight.pos + weight.vel * dt
    spring.axis = weight.pos - pivot





