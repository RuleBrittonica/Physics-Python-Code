# %% [markdown]
# # Lab 9 report - Matthew Britton

# %% [markdown]
# ## Importing all libaries that are required
# Redefining ufloat to be u. Also please go easy on the formatting - this is my first time writing LaTeX in a JupterNotebook :)

# %%
from uncertainties import ufloat
from uncertainties.umath import *
def u (x,s):
  return ufloat (x,s)

# %% [markdown]
# ## Initialising variables:
# These are the things we measured initially, using a ruler for h_1 and h_2, calipers for r_roll and micrometer for r_marble.
# * r_marble is the radius of the marble .
# * r_roll is the distance between the inside edges of the run, where the marble actually rolls down.
# * g is grabity.
# * h_1 is the height difference from the start of the marble run to the end .
# * h_2 is the height difference between the end of the marble run and the ground.

# %%
r_marble = u (0.0161, 0.0001)
r_roll   = u (0.0088, 0.0001)
g        = 9.8
h_1      = u (0.49, 0.0005) - u (0.035, 0.0005)
h_2      = u (0.937, 0.0001)

# %% [markdown]
# ## Initialise data sets:
# Data is from the carbon paper and then was transfered to excel to calculate the standard deviation and standard error. Here is the data we gathered:
# | Set 1 (crosses) | Distance From edge of paper (+/- 0.5mm) | Distance from edge of run (+/-) 0.01m | Set 2 (dots) | Distance From edge of paper (+/- 0.5mm) | Distance from edge of run (+/-) 0.01m |
# |-----------------|-----------------------------------------|---------------------------------------|--------------|-----------------------------------------|---------------------------------------|
# | 1               | 0.187                                   | 0.877                                 | 1            | 0.243                                   | 0.933                                 |
# | 2               | 0.222                                   | 0.912                                 | 2            | 0.19                                    | 0.88                                  |
# | 3               | 0.221                                   | 0.911                                 | 3            | 0.204                                   | 0.894                                 |
# | 4               | 0.222                                   | 0.912                                 | 4            | 0.201                                   | 0.891                                 |
# | 5               | 0.204                                   | 0.894                                 | 5            | 0.199                                   | 0.889                                 |
# | 6               | 0.202                                   | 0.892                                 | 6            | 0.202                                   | 0.892                                 |
# | 7               | 0.21                                    | 0.9                                   | 7            | 0.197                                   | 0.887                                 |
# | 8               | 0.212                                   | 0.902                                 | 8            | 0.22                                    | 0.91                                  |
# | 9               | 0.218                                   | 0.908                                 | 9            | 0.21                                    | 0.9                                   |
# | 10              | 0.205                                   | 0.895                                 | 11           | 0.198                                   | 0.888                                 |
# | 11              | 0.213                                   | 0.903                                 | 12           | 0.219                                   | 0.909                                 |
# | 12              | 0.21                                    | 0.9                                   | 13           | 0.206                                   | 0.896                                 |
# | 13              | 0.219                                   | 0.909                                 | 14           | 0.214                                   | 0.904                                 |
# | 14              | 0.237                                   | 0.927                                 | 15           | 0.239                                   | 0.929                                 |
# | 15              | 0.213                                   | 0.903                                 | outlier - 10 | 0.109                                   | 0.799                                 |
# |                 |                 Average                 | 0.903                                 |              |                 Average                 | 0.900142857                           |
# |                 |            Standard Deviation           | 0.011027239                           |              |            Standard Deviation           | 0.015018356                           |
# |                 |             Standard Error              | 0.002947154                           |              |             Standard Error              | 0.004165343                           |

# %%
pre_set1 = [0.187, 0.222, 0.221, 0.222, 0.204, 0.202, 0.21, 0.212, 0.218, 0.205, 0.213, 0.21, 0.219, 0.237, 0.213]
pre_set2 = [0.243, 0.19, 0.204, 0.201, 0.199, 0.202, 0.197, 0.22, 0.21, 0.198, 0.219, 0.206, 0.214, 0.239] #outlier = 0.109
avg_1 = 0.903
avg_2 = 0.900142857
stdev_1 = 0.011027239
stdev_2 = 0.015018356
sterror_1 = 0.002947154
sterror_2 = 0.004165343

t0 = (2 * h_2 / g) ** 0.5 # ~= 0.4289
v0_m1 = 3.13
v0_m2 = 2.65
d0_m1 = 1.343
d0_m2 = 1.134

added_distance = u (0.69, 0.005)

# %% [markdown]
# ## Setup Equations
# ### For non rolling model:
#
# $$m * g * h_1 = \frac{1}{2} * m * v ^ 2$$
# $$v = (2 * g * h _ 1) ^ \frac{1}{2}$$
# $$u_v = 0, s = (-h_2), a = -9.8$$
# $$-h_2 = \frac{1}{2} * a * t ^ 2$$
# $$t = (2 * \frac{h_2}{a}) ^ 2$$
# $$u_h = (2 * g * h_1) ^ 2$$
# Hence: $$s_1 = u_h * t = 2 * (h_1 * h_2) ^ \frac{1}{2}$$ This is printed below as model 1
#
# ### For the rolling model:
#
# $$I = \frac{2}{5} * m * r ^ 2$$
# $$\omega = (\frac{v}{r}) ^ 2 $$
#
# $$m * g * h = \frac{1}{2} * m * v ^ 2 + 1 / 2 * I * w ^ 2 $$
# $$          = \frac{1}{2} * m * v ^ 2 + \frac{1}{2} * \frac{2}{5} * m * r ^ 2 * (\frac{v}{r}) ^ 2$$
# $$          = m * v ^ 2 * \frac{7}{10} $$
# $$    g * h = \frac{7}{10} * v ^ 2 $$
#
# Hence:
# $$ s_2 = u * t = (\frac{20}{7} * h_1 * h_2) ^ 2$$
# This is printed below as model 2
#
# However, the radius the marble rolls down is actually smaller than the radius of the marble - this means we need to account for a larger amount of energy lost to the rolling motion, which will decrease the theoretical distance the marble rolls. This is calculated below.
#
# $$g * h = v ^ 2 * (\frac{1}{2} + \frac{1}{5}) * (\frac{r_{marble}}{r_{roll}}) ^ 2$$
# $$      = v ^ 2 * (\frac{1}{2} + \frac{1}{5}) * (\frac{~8.05}{~6.74} ) ^ 2$$
# $$      = v ^ 2 * ~0.785$$
# $$    v = (\frac{g * h}{~0.785})^\frac{1}{2}$$
# Hence:
# $$s_3 = v * t = \frac{g * h_1}{0.785}) ^ \frac{1}{2} * (\frac{2 * h_2}{g}) ^ 2$$
# This is printed below as model 3
#
# Doing some theoretical calculations (these are also defined in the above module):
# $$t = 2 * (\frac{h_2}{g}) ^ \frac{1}{2} = ~0.4289$$
# $$v_{m1} ~= 3.13 ms^{-1}$$
# $$v_{m2} ~= 2.65 ms^{-1}$$
# $$d_{m1} ~= 1.343 ms^{-1}$$
# $$d_{m2} ~= 1.134 ms^{-1}$$

# %%
# r_roll = math.sqrt (r_marble ** 2 - w_rail ** 2)
# v0 = math.sqrt (g * h_1 * (0.5 + 0.2 * (r_marble / r_roll)))

set1 = [u (x, 0.0005) + added_distance for x in pre_set1]
set2 = [u (x, 0.0005) + added_distance for x in pre_set2]

new_r = r_marble / r_roll
t = (2 * h_2 / g) ** 0.5

v1 = (g * h_1 / 0.5) ** 0.5 # calculation for distance using model 1, with error calculations.
v2 = ((g * h_1) / (0.5 + 0.2)) ** 0.5 # calculation for distance using model 3, with error calculations.
v3 = (g * h_1 / (0.5 + 0.2 * new_r) ** 2) ** 0.5 # calculation for distance using model 3, with error calculations.

d1 = v1 * t
d2 = v2 * t
d3 = v3 * t

# %% [markdown]
# Print the calculated distances with their errors to the standard output.

# %%
print ("Prediction for model 1 is:", d0_m1)
print ("Distance calculated with model 1 is: ", d1)
print ("Difference between prediction and actual for model 1 is: ", d0_m1 - d1)
print ("Prediction for models 2 and 3 are: ", d0_m2)
print ("Distance calculated with model 2 is: ", d2)
print ("Difference between prediction and actual for model 2 is: ", d0_m2 - d2)
print ("Distance calculated with model 3 is: ", d3)
print ("Difference between prediction and actual for model 3 is: ", d0_m2 - d3)
print ("Hence it is clear that model three is a much better model than either model one or two, as the difference")
print ("between the theoretical and expected values is smaller than even that of model two by a factor of 5.")

# %% [markdown]
# ## Final Results
# Prediction for model 1 is: 1.343
# Distance calculated with model 1 is:  1.3059+/-0.0010
# Difference between prediction and actual for model 1 is:  0.0371+/-0.0010
# Prediction for models 2 and 3 are:  1.134
# Distance calculated with model 2 is:  1.1037+/-0.0009
# Difference between prediction and actual for model 2 is:  0.0303+/-0.0009
# Distance calculated with model 3 is:  1.066+/-0.006
# Difference between prediction and actual for model 3 is:  0.068+/-0.006
# Hence it is clear that model three is a much better model than either model one or two, as the difference
# between the theoretical and expected values is smaller than even that of model two by a factor of 5.
# Overall the difference between the model and the observations was relatively fairly large in terms of standard deviations for both models 1 and 2.
# However, the difference between the model and the observations for model 3 was significantly smaller. There is still some error,
# with the measured being ~6.8cm shorter than the model, indicating that this rolling energy accounts for a significant amount of the difference, but that
# other issues such as air resistance (drag), need to be accounted for as well before we can get a model that approaches
# the observations.
#

# %% [markdown]
# ## Visual error calculations:
#
# I completely forgot to take a photograph of the carbon paper, so here are the results, sans a photograph.
# Standard deviation for model 1 = ~ 0.01 - 0.015m (every point in that 2/3rds circle was at most 0.015m from the average point)
# Standard deviation for model 2 = ~ 0.015 - 0.02m (every point in that 2/3rds circle was at most 0.020m from the average point)
# Standard error =  0.02 - 0.0015 = ~0.005m
#


