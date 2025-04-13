import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.05):
    return np.where(x > 0, x, alpha * x)

def swish (x):
    return x * sigmoid(x)

# Generate x values
x = np.linspace(-4, 4, 200)

# Plot all activation functions
plt.figure(figsize=(6, 4))

plt.plot(x, sigmoid(x), label=r'$\mathrm{Sigmoid} (x)$')
plt.plot(x, tanh(x), label=r'$\tanh(x)$')
plt.plot(x, relu(x), label=r'$\mathrm{ReLU}(x)$')
plt.plot(x, leaky_relu(x), label=r'$\mathrm{LReLU}(x)$')
plt.plot(x, swish(x), label=r'$\mathrm{Swish}(x)$')

# Labels and legend
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Commonly used activation functions')
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
