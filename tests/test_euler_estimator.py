import sys
sys.path.append('src')
from euler_estimator import *

euler = EulerEstimator(derivative = (lambda t: t+1))

assert euler.calc_derivative_at_point((1,4)) == 2


assert euler.step_forward(point = (1,4), step_size = 0.5) == (1.5, 5)

print(euler.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4))

assert euler.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4) == [(1, 4), (1.5, 5), (2, 6.25), (2.5, 7.75), (3, 9.5)]