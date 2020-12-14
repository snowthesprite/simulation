#import matplotlib.pyplot as plt

class EulerEstimator :
    def __init__(self, derivatives) :
        self.derivative = derivatives
        self.keys = [key for key in derivatives]
    
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

    def plot(self, point, step_size, num_steps) : 
        plt.style.use('bmh')
        all_points = self.calc_estimated_points(point, step_size, num_steps)
        x_points = [x[0] for x in all_points]
        y_points = [y[1] for y in all_points]
        plt.gca().set_aspect("equal")
        plt.plot(x_points,y_points)
        plt.savefig('tests/eulerplot.png')
        plt.clf()