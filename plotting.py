import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to plot 2D graph with data points and a line equation
def plot_2d_graph(data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    plt.scatter(x, y, label='Training Examples')

    # Performing polynomial regression to fit the data points with a polynomial of degree 3
    coefficients = np.polyfit(x, y, 3)
    polynomial = np.poly1d(coefficients)

    # Plotting y = 5x + 10 line
    x_line = np.linspace(min(x), max(x), 100)
    #y_line = 0.9*x_line 
    y_line = polynomial(x_line)
    plt.plot(x_line, y_line, color='red', label='Model Prediction')

    plt.xlabel('Input data')
    plt.ylabel('Prediction')
    plt.title('Theoretical Representation of a Model Underfitting')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot a 3D graph
def plot_3d_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.random.standard_normal(100)
    y = np.random.standard_normal(100)
    z = np.random.standard_normal(100)

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Scatter Plot')
    plt.show()

# Example data points for 2D graph
data_points = [(0.1, 0.1), (0.75, 1), (1.75, 2.2), (2.8, 2.8), (3.9, 2.75), (3.9, 2.2), (3.3, 2.2), (2.6, 2.25), (1.5, 3), (1, 2), (0.5, 0.3)]

# Plotting 2D graph with data points and line
plot_2d_graph(data_points)

# Plotting a 3D graph
plot_3d_graph()
