import sys
sys.path.append('src')
from euler_estimator import *

''''
Once again, will fix this later so that it doesn't throw up errors
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

euler = EulerEstimator(derivative = lambda t: t+1)

#euler.plot(point=(-5,10), step_size=0.1, num_steps=100)

'''

derivatives = {'A': (lambda t,x: x['A'] + 1),'B': (lambda t,x: x['A'] + x['B']),'C': (lambda t,x: 2*x['B'])}

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)

print('Does everything work?')

assert euler.calc_derivative_at_point(initial_point) == {'A': 1, 'B': 0, 'C': 0}, 'Not calc_derivative_at_point for point_1'

point_2 = euler.step_forward(point = initial_point, step_size = 0.1)

rounded = point_2[1]
keys = [key for key in rounded]
for key in keys :
    rounded[key] = round(rounded[key], 1)

assert point_2 == (0.1, {'A': 0.1, 'B': 0, 'C': 0}), 'point_2 isnt quite right'

assert euler.calc_derivative_at_point(point_2) == {'A': 1.1, 'B': 0.1, 'C': 0}, 'Not calc_derivative_at_point for point_2'


point_3 = euler.step_forward(point = point_2, step_size = -0.5)

rounded = point_3[1]
keys = [key for key in rounded]
for key in keys :
    rounded[key] = round(rounded[key], 2)

assert point_3 == (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}), 'point_3 isnt quite right'

all_points = euler.calc_estimated_points(point=point_3, step_size=2, num_steps=3)

for point in all_points :
    rounded = point[1] 
    for key in keys :
        rounded[key] = round(rounded[key], 2)

assert all_points == [(-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}),  (1.6, {'A': 0.65, 'B': -1.05, 'C': -0.2}), (3.6, {'A': 3.95, 'B': -1.85, 'C': -4.4}), (5.6, {'A': 13.85, 'B': 2.35, 'C': -11.8})], 'one of the grouped points arent right'

print('Yes it does!')