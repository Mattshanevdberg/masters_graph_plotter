import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to plot 2D graph with data points and a line equation
def plot_2d_graph(data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    plt.scatter(x, y, label='Training examples')

    # Performing polynomial regression to fit the data points with a polynomial of degree 3
    coefficients = np.polyfit(x, y, 9)
    polynomial = np.poly1d(coefficients)

    # Plotting y = 5x + 10 line
    x_line = np.linspace(min(x), max(x), 100)
    #y_line = 0.9*x_line 
    y_line = polynomial(x_line)
    plt.plot(x_line, y_line, color='red', label='Model prediction')

    plt.xlabel('Input data')
    plt.ylabel('Prediction')
    #plt.title('Theoretical Representation of a Goldilocks Model')
    #plt.title('Underfitting model')
    plt.title('Overfitting model')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot a 3D graph
'''
def plot_3d_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.random.standard_normal(100)
    y = np.random.standard_normal(100)
    z = np.random.standard_normal(100)

    ax.scatter(x, y, z, c='r', marker='o')

    plt.plot(0.2*y^2 + 0.1*sin(y+x^3) - Exp[(-(x+0.3)^2-y+0.1^2)]+ 10, x=-2..2, y=-2..2)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Scatter Plot')
    plt.show()
'''

def plot_3d_graph(scatter_points, equation_range=(-20, 2)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    x_scatter = [point[0] for point in scatter_points]
    y_scatter = [point[1] for point in scatter_points]
    z_scatter = [point[2] for point in scatter_points]
    ax.scatter(x_scatter, y_scatter, z_scatter, c='r', marker='o', label='Scatter Points')

    # Equation plot
    x_range = np.linspace(equation_range[0], equation_range[1], 100)
    y_range = np.linspace(equation_range[0], equation_range[1], 100)
    x, y = np.meshgrid(x_range, y_range)
    
    # Define the equation
    z = 0.2 * y**2 + 0.1 * np.sin(y + x**3) - np.exp(-(x + 0.3)**2 - y + 0.1**2) + 10

    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8, label='Equation Surface')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Scatter Plot with Equation Surface')
    ax.legend()

    plt.show()



def plot_3d_function2():
    # Rosenbrock function
    def rosenbrock(x, y):
        return (1 - x)**2 + 100 * (y - x**2)**2

    # Generate x, y values
    x_values = np.linspace(-2, 2, 100)
    y_values = np.linspace(-2, 2, 100)
    x, y = np.meshgrid(x_values, y_values)

    # Calculate z values using the Rosenbrock function
    z = rosenbrock(x, y)

    # Find the global minimum
    global_min_x = 1
    global_min_y = 1
    global_min_z = rosenbrock(global_min_x, global_min_y)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

 # Plot the global minimum
    ax.scatter(global_min_x, global_min_y, global_min_z, color='red', s=50, label='Minima', zorder=1)
    ax.scatter(1.85, -1.85, rosenbrock(1.85, -1.85), color='blue', s=50, label='Starting Point', zorder=2)

    # Plot the Rosenbrock function
    ax.plot_surface(x, y, z, cmap='viridis', alpha=1, label='Loss Function', zorder=0)

   
    ax.set_xlabel(r'First Trainable Parameter: $w_0$')
    ax.set_ylabel(r'Second Trainable Parameter: $w_1$')
    ax.set_zlabel(r'Loss: $L(w_0,w_1)$', labelpad=10)
    ax.set_title('Visual Representation of the Optimisation Function Minimising the Loss')
    ax.legend()

    plt.show()

# plot_3d_function2()

# Example scatter points for 3D graph
#scatter_points = [(-0.3, -2.5, 3)]

# Plotting 3D graph with scatter points and equation surface plot
#plot_3d_graph(scatter_points)

# Example data points for 2D graph
data_points = [(0.1, 0.1), (0.75, 1), (1.75, 2.2), (2.8, 2.8), (3.9, 2.75), (3.9, 2.2), (3.3, 2.2), (2.6, 2.25), (1.5, 3), (1, 2), (0.5, 0.3)]

# Plotting 2D graph with data points and line
plot_2d_graph(data_points)

# Plotting a 3D graph
#plot_3d_graph()
