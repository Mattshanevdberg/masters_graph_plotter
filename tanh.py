import numpy as np
import matplotlib.pyplot as plt

# Define the tanh function
def tanh(x):
    return np.tanh(x)

# Generate values for x from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate the corresponding y values using the tanh function
y = tanh(x)

# Create the plot
plt.figure(figsize=(4, 3))  # Adjusting figure size to match the uploaded image
plt.plot(x, y)

# Set labels and title
plt.xlabel('x')
plt.ylabel(r'$\tanh(x)$')  # Using LaTeX format for tanh symbol
plt.title('Tanh Activation Function')

# Display the plot
plt.show()
