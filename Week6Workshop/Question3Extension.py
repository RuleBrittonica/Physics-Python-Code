from vpython import * 

t = 0
dt = 0.0002
G = 6.67401E-11
m1 = 8E30

blackholeEventHorizon = sphere(pos = vector(0, 0, 0),
                   radius = 11000,
                   color = color.cyan)

spacecraft = sphere(pos = vector(1000000, 0, 0),
                    radius = 10000,
                    color = color.yellow,
                    vel = vector(0, 15.87E6, 0))

blackholeDeathZome = sphere(pos = vector(0, 0, 0),
                              radius = 300000,
                              color = color.red,
                              opacity = 0.5)

while t < 10:
    t = t + dt
    spacecraft.pos = spacecraft.pos + spacecraft.vel * dt
    fG = -(norm(spacecraft.pos)) * (G * m1)/((mag(spacecraft.pos)) ** 2)
    spacecraft.vel = spacecraft.vel + fG * dt
    rate (100)