import matplotlib.pyplot as plt

class EulerEstimator :
    def __init__(self, derivative) :
        self.derivative = derivative
    
    def calc_derivative_at_point(self, point) :
        return self.derivative(point[0])

    def step_forward(self, point, step_size) :
        list_point = list(point)
        list_point[0] += step_size
        list_point[1] += self.calc_derivative_at_point(point) * step_size
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