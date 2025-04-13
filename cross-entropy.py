import numpy as np
import matplotlib.pyplot as plt

# Define the function
def cross_entropy_loss(x):
    return -np.log(x)

# Create X values between 0.01 and 1 (avoid log(0))
x = np.linspace(0.01, 1, 100)

# Compute Y values
y = cross_entropy_loss(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$-\log(X_i)$', color='blue')
plt.title('Graph of Cross-Entropy Loss for $y_i = 1$', fontsize=14)
plt.xlabel('$X_i$ (Predicted Probability)', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
