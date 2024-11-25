import numpy as np
import matplotlib.pyplot as plt

# Define the ReLU function
def relu(x):
    return np.maximum(0, x)

# Generate values for x from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate the corresponding y values using the ReLU function
y = relu(x)

# Create the plot
plt.figure(figsize=(4, 3))  # Adjusting figure size to match the uploaded image
plt.plot(x, y)

# Set labels and title
plt.xlabel('x')
plt.ylabel(r'$\mathrm{ReLU}(x)$')  # Using LaTeX format for ReLU label
plt.title('ReLU Activation Function')

# Display the plot
plt.show()
