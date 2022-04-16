from Vpython import *

# Set up ground

ground = box(pos=vector(0,0,0),
             width=8, height=0.1, length=8, 
             color=color.green)

# Set up ball

V = 20.0
theta = 60.0*pi/180.0 # Convert to radians
rad = 0.5
ball = sphere(pos=vector(0,rad,0), 
              vel = vector(V*cos(theta), V*sin(theta), 0),
              radius = rad, 
              color=color.red)

# Set up gravity
m = 0.3
g = vector(0,-9.8,0)

# Set up other variables 
C = 0.7
A = pi * ball.radius ** 2
a = 0
rho = 1.1
vwind = vector(-9, 0, 0)

# Loop
t = 0
dt = 0.002

while ball.pos.y >= rad:
    rate(100)
    t = t + dt
    vrel = ball.vel - vwind
    ball.pos = ball.pos + ball.vel*dt
    # a = g - 0.5 * A * C * rho * mag(vrel)**2*norm(vrel)
    a = g - 0.5*A*C*rho*mag(vrel)**2*norm(vrel)/m
    # a = g + 0.5*A*C*rho*mag(vrel)**2*norm(vrel)/m
    ball.vel = ball.vel + a*dt
    
print(ball.pos)