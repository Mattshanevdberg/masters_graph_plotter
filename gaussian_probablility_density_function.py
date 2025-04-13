import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Gaussian
mu = 0      # Mean
sigma = 1   # Standard deviation (this is the variance at 1, it essentially does not effect the loss ouput)
# the signma

# Generate x values
x = np.linspace(-5, 5, 500)

# Gaussian PDF
pdf = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f'Gaussian PDF (μ={mu}, σ={sigma})')
plt.title("Gaussian Probability Density Function")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.grid(True)
plt.show()
