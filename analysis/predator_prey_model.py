import sys
sys.path.append('src')
from euler_estimator import *

meeting_rate = lambda c : c['D'] * c['W'] * 0.05

derivatives = {'D': (lambda t,x: x['D'] * 0.6 - meeting_rate(x)),'W': (lambda t,x: meeting_rate(x) * 0.4 - x['W'] * 0.9)}


predator_prey = EulerEstimator(derivatives = derivatives)

initial_values = {'D': 100, 'W': 10}
initial_point = (0, initial_values)

print(predator_prey.calc_derivative_at_point(initial_point))

predator_prey.plot(initial_point, 0.001, 100, plot_destination = 'analysis/predator_preyplot.png')