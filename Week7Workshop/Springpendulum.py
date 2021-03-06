from vpython import *
# import matplotlib.pyplot as plt
# import math

# setup the graph
tgraph = graph (title = "Weight Position against Period", xtitle = "T (s)", ytitle = "Maximum Displacement")
graph1     = gcurve ()

# setup the pivot
pivot = vector (0,10,0)

# setup loop constants
t  = 0
dt = 0.01

# gravity and spring force
g = vector (0,-9.8,0) # gravity
m = 5 # mass of weight
k = 10 # spring constant
L = 10 # length of spring

# setup drag
rho = 1.1 # air density
A   = pi * 0.2 ** 2 # surface area
C   = 0.7 # drag constant

# setup oscillation varaibles
T      = 1 # starter period of oscillation
amp    = 0.2 # amplitude
dT     = 0.02 # value to iterate T by every T loop
maxDis = 0 # initialise maxDis variable

# define new equilibrium
equilibrium = vector(0, -m * mag(g) / k, 0)

# setup weight and spring
weight = sphere (pos = equilibrium,
                  radius = 0.2,
                  color = color.red,
                  vel = vector (5, 0, 0),
                #   make_trail = True) removed for speed
                )

spring = helix (pos = pivot,
                axis = (weight.pos - pivot),
                color = color.yellow)

# while t <=30:
#     t = t + dt
#     rate (100)
#     x = mag(spring.axis) - L
#     F1 = (-k) * (x) * norm (spring.axis)
#     acc = (F1 / m) + g
#     Fd = 0.5 * rho * (mag (weight.vel)) ** 2 * norm (weight.vel) * C * A
#     weight.vel = weight.vel + acc * dt - Fd * dt
#     weight.pos = weight.pos + weight.vel * dt
#     spring.axis = weight.pos - pivot

# Quiz code starts here

while T <= 12:

    while t <= 100:
        # rate (100) # slows down the loop enough to make it observable to humans, rate (100) means iterate the loot a maximum of 100 times per second, removed to make graphing tolerable
        maxDis     = 0 # resets the comparison variable every loop
        t           = t + dt
        r           = weight.pos - pivot # r points from the pivot to the weight
        drag        = 0.5 * A * C * rho * mag(weight.vel) ** 2 * norm(weight.vel) / m
        a           = g - ((k * (mag(r) - L) * norm(r)) / m) - drag
        pivot       = amp * vector (sin(2 * pi * t / T), cos(2 * pi * t / T), 0) + vector(0, 10, 0)
        spring.pos  = pivot
        spring.axis = weight.pos - pivot
        weight.vel  = weight.vel + a * dt
        weight.pos  = weight.pos + weight.vel * dt
        dis         = mag (weight.pos - equilibrium)
        maxDis      = max (dis, maxDis) # graphs the displacement as long a its >= 0
        # print(weight.pos.x)
        # print(weight.pos.y)


    graph1.plot (T, maxDis)
    pivot = vector (0, 10, 0) # resets the pivot every time the t loop finishes
    spring.pos = pivot # resets the spring's position to the pivot every time the t loop finishes
    weight.vel = vector (5, 0, 0) # resets velocity every time the t loop finishes
    weight.pos = equilibrium # resets the weights position every time the t loop finishes
    spring.axis = (weight.pos - pivot)
    t = 0 # resets t to start the new t loop
    T = T + dT # iterates the T loop






