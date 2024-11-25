import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate values for x from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate the corresponding y values using the sigmoid function
y = sigmoid(x)

# Create the plot
plt.figure(figsize=(4, 3))  # Adjusting figure size to match the uploaded image
plt.plot(x, y)

# Set labels and title
plt.xlabel('x')
plt.ylabel(r'$\sigma (x)$')
plt.title('Sigmoid Activation Function')

# Display the plot
plt.show()
