import numpy as np
import matplotlib.pyplot as plt

# Define the Leaky ReLU function
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Generate values for x from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate the corresponding y values using the Leaky ReLU function
y = leaky_relu(x)

# Create the plot
plt.figure(figsize=(4, 3))  # Adjusting figure size to match the uploaded image
plt.plot(x, y)

# Set labels and title
plt.xlabel('x')
plt.ylabel(r'$\mathrm{LReLU}(x)$')  # Using LaTeX format for Leaky ReLU label
plt.title('Leaky ReLU Activation Function')

# Display the plot
plt.show()
