import sys
sys.path.append('src')
from euler_estimator import *
import math as math

## constants
C = 1

V_Na = 115
V_K = -12
V_L = 10.6

_g_Na = 120
_g_K = 36
g_L = 0.3

## helper functions Voltage (?)
a_n = lambda x : (0.01 * (10 - x['V'])) / (math.exp(0.1 * (10 - x['V'])) - 1)
a_m = lambda x : (0.1 * (25 - x['V'])) / (math.exp(0.1 * (25 - x['V'])) - 1)
a_h = lambda x : 0.07 * (math.exp(-x['V'] / 20))

b_n = lambda x : 0.125 * (math.exp(-x['V'] / 80))
b_m = lambda x : 4 * (math.exp(-x['V'] / 18))
b_h = lambda x : 1 / (math.exp(0.1 * (30 - x['V'])) + 1)

## helper functions conductances (?)
g_Na = lambda x : _g_Na * (x['m'] ** 3) * x['h']
g_K = lambda x : _g_K * (x['n'] ** 4)

## helper functions Ion channels (?)
I_Na = lambda x : g_Na(x) * (x['V'] - V_Na)
I_K = lambda x : g_K(x) * (x['V'] - V_K)
I_L = lambda x : g_L * (x['V'] - V_L)

## the rest

def stim (t) :
    if t >= 10 and t <= 11 :
        return 150
    elif t >= 20 and t <= 21 :
        return 150
    elif t >= 30 and t <= 40 :
        return 150
    elif t >= 50 and t <= 51 :
        return 150
    elif t >= 53 and t <= 54 :
        return 150
    elif t >= 56 and t <= 57 :
        return 150
    elif t >= 59 and t <= 60 :
        return 150
    elif t >= 62 and t <= 63 :
        return 150
    elif t >= 65 and t <= 66 :
        return 150
    else :
        return 0

##Custom EulerEstimator
class EulerMk2 (EulerEstimator) :
    def __init__(self, derivatives) :
        self.derivative = derivatives
        self.keys = [key for key in derivatives]
    
    def plot(self, point, step_size, goal) : 
        plt.style.use('bmh')
        current_point = point[0]
        y_points = {'Voltage' : [], 'Stimulus' : [stim(current_point)]}
        num_steps = 0
        while current_point <= goal : 
            current_point += step_size
            num_steps += 1
            y_points['Stimulus'].append(stim(current_point)) 
        all_points = self.calc_estimated_points(point, step_size, num_steps)
        x_points = [x[0] for x in all_points]
        for point in all_points :
            y_points['Voltage'].append(point[1]['V'])
        plt.plot(x_points, y_points['Voltage'])
        plt.plot(x_points, y_points['Stimulus'], linewidth = 1.0)
        plt.legend(['Voltage', 'Stimulus'])
        plt.savefig('analysis/neuronplot.png')


derivatives = {'V' : (lambda t, x : (stim(t) - I_Na(x) - I_K(x) - I_L(x)) * (1/C)),'n' : (lambda t, x: a_n(x) * (1 - x['n']) - b_n(x) * x['n']), 'm' : (lambda t, x: a_m(x) * (1 - x['m']) - b_m(x) * x['m']), 'h' : (lambda t, x : a_h(x) * (1 - x['h']) - b_h(x) * x['h'])}

neuron = EulerMk2(derivatives = derivatives)

initial_values = {'V': 0, 'n': 0.3176769141, 'm' : 0.05293248526, 'h' : 0.5961207535}
initial_point = (0, initial_values)

neuron.plot(initial_point, 0.01, 80)