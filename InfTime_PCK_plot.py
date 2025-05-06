# Re-run after kernel reset

import matplotlib.pyplot as plt

# Define the new data for inference time
data_inference = {
    "SSP": {
        "labels": ["R1", "R2", "R3", "R4", "R5", "SLEAP", "DLC"],
        "gpu_times": [5.02, 9.13, 5.43, 3.15, 5.69, 37.52, 137.48],
        "cpu_times": [31.21, 18.89, 9.13, 10.16, 9.34, 290.02, 1093.49],
        "pck": [0.8799, 0.8741, 0.8843, 0.8563, 0.8540, 0.7257, 0.7547],
        "color": "gold"
    },
    "AMP": {
        "labels": ["R1", "R2", "R3", "R4", "R5", "SLEAP"],
        "gpu_times": [4.55, 6.77, 4.29, 3.28, 2.95, 9.76],
        "cpu_times": [31.90, 16.96, 9.40, 9.22, 8.97, 42.13],
        "pck": [0.6526, 0.6738, 0.6555, 0.6574, 0.6827, 0.7219],
        "color": "green"
    }
}

# Create the plot
plt.figure(figsize=(8, 6))

# Plot each dataset and type of inference
for dataset_name, dataset in data_inference.items():
    # GPU scatter
    plt.scatter(dataset["gpu_times"], dataset["pck"], label=f"{dataset_name} (GPU)", marker='o', color=dataset["color"])
    for label, x, y in zip(dataset["labels"], dataset["gpu_times"], dataset["pck"]):
        plt.text(x, y, label, fontsize=9, ha='right', va='bottom')

    # CPU scatter
    plt.scatter(dataset["cpu_times"], dataset["pck"], label=f"{dataset_name} (CPU)", marker='x', color=dataset["color"])
    for label, x, y in zip(dataset["labels"], dataset["cpu_times"], dataset["pck"]):
        plt.text(x, y, label, fontsize=9, ha='left', va='top')

# Set axis labels and title
plt.xscale("log")
plt.xlabel("Inference Time in ms (log scale)")
plt.ylabel("PCK@0.1")
plt.title("Comparison of PCK@0.1 to Inference Time (CPU and GPU)")
plt.legend(title="Dataset + Inference Type")
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
