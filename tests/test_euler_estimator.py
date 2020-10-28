import sys
sys.path.append('src')
from euler_estimator import *

euler = EulerEstimator(derivative = (lambda t: t+1))

print('Does the EulerEstimators calc_derivative_at_point correctly calculate the derivative?')
assert euler.calc_derivative_at_point((1,4)) == 2, 'No, it does not'
print('Yes, it does!')
print()

print('Does EulerEstimators step_forward correctly go foward the step size?')
assert euler.step_forward(point = (1,4), step_size = 0.5) == (1.5, 5), 'No, it does not'
print('Yes, it does!')
print()

print('Does EulerEstimators calc_estimated_points correctly calculate the estimated points?')
assert euler.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4) == [(1, 4), (1.5, 5), (2, 6.25), (2.5, 7.75), (3, 9.5)], 'No, it does not'
print('Yes, it does!')
print()