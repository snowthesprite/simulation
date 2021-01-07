import matplotlib.pyplot as plt
import random

class EulerEstimator :
    def __init__(self, derivatives) :
        self.derivative = derivatives
        self.keys = [key for key in derivatives]
        self.color = {key:(random.random(), random.random(), random.random()) for key in self.keys}
    
    def calc_derivative_at_point(self, point) :
        derivative = {}
        for key in self.keys :
            derive = self.derivative[key]
            derivative[key] = derive(point[0], point[1])
        return derivative

    def step_forward(self, point, step_size) :
        list_point = [point[0], point[1].copy()]
        list_point[0] += step_size
        for key in self.keys :
            list_point[1][key] = point[1][key] + self.calc_derivative_at_point(point)[key] * step_size
        return tuple(list_point) 
    
    def calc_estimated_points(self, point, step_size, num_steps) :
        all_points = []
        steps_taken = 0
        current_point = point
        while steps_taken <= num_steps :
            all_points.append(current_point)
            current_point = self.step_forward(current_point, step_size)
            steps_taken += 1
        return all_points

    def plot(self, point, step_size, goal) : 
        plt.style.use('bmh')
        current_point = point[0]
        num_steps = 0
        while current_point <= goal :  
            current_point += step_size
            num_steps += 1
        all_points = self.calc_estimated_points(point, step_size, num_steps)
        x_points = [x[0] for x in all_points]
        y_points = {key : [] for key in self.keys}
        for point in all_points :
            for key in self.keys :
                y_points[key].append(point[1][key])
        #plt.gca().set_aspect("equal")
        for key in self.keys :
            plt.plot(x_points, y_points[key], color = self.color[key])
        plt.legend(self.keys)
        plt.savefig('tests/eulerplot.png')