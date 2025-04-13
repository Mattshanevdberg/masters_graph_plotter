import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Laplace distribution
mu = 0      # Mean (location parameter)
b = 1       # Scale parameter

# Generate x values
x = np.linspace(-10, 10, 500)

# Laplace PDF
pdf = (1 / (2 * b)) * np.exp(-np.abs(x - mu) / b)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f'Laplace PDF (μ={mu}, b={b})')
plt.title("Laplace Probability Density Function")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.grid(True)
plt.show()
