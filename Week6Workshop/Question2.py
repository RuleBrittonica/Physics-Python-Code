from vpython import *

V = 40
theta = pi/4
dt = 0.01
t = 0
r = 0.5
C = 0.7
A = pi * r ** 2
p = 1.1
g = vector(0, (-9.8), 0)
vwind = vector(-2, 0, 0)


plane = box(pos = vector(0, 0, 0),
              length = 30, height = 0.25, width = 8,
              vel = vector(V*cos(theta), V*sin(theta), 0),
              color = color.green)

ball = sphere(pos = vector(-10, 0.625, 0),
                 radius = r,
                 vel = vector(V*cos(theta), V*sin(theta), 0),
                 color = color.orange)

while ball.pos.y > 0.625:
    t = t + dt 
    vrel = ball.vel - vwind
    dF1 = -0.5 * C * A * p * ((mag(ball.vel) ** 2) * norm(ball.vel))
    dF2 = -0.5 * C * A * p * ((mag(vrel) ** 2) * norm(vrel))
    ball.pos = ball.pos + ball.vel * dt
    ball.vel = ball.vel + g * dt + dF1 * dt + dF2 * dt
    rate (100)
    
    