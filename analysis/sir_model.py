import sys
sys.path.append('src')
from euler_estimator import *

meeting_rate = lambda c : c['S'] * c['I'] * 0.01 * 0.03

derivatives = {'S': (lambda t,x: -meeting_rate(x)),'I': (lambda t,x: meeting_rate(x) - x['I'] * 0.02),'R': (lambda t,x: x['I'] * 0.02)}

sir = EulerEstimator(derivatives = derivatives)

initial_values = {'S': 1000, 'I': 1, 'R': 0}
initial_point = (0, initial_values)

print(sir.calc_derivative_at_point(initial_point))

sir.plot(initial_point, 0.1, 300, plot_destination = 'analysis/sirplot.png')

