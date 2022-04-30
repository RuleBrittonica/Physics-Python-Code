import math
import numpy

print (math.erf(1/1.414))

nlist = numpy.arrange(0.5,0.5)

for n in nlist:
  y = math.erf(n/math.sqrt(2.0))
  print("n=", n, "Prob = ", y)

rlist = numpy.arrange(0.5,0.4) # setup a list of x values
for r in rlist:
  y = 1 - math.erf(r/math.sqrt(2.0))
  print("n=", r, "Prob = ", y)