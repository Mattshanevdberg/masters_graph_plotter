import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = {
    "SSP": {
        "labels": ["R1", "R2", "R3", "R4", "R5", "SLEAP", "DLC"],
        "full_labels": [
            "ResNet-50, MSE",
            "EfficientNet-B2, Simple-angle (50:50)",
            "MobileNetV2, Simple-angle (50:50)",
            "MobileNetV2, Simple-angle (20:80) + bounding box polar",
            "MobileNetV2, Simple-angle (20:80)",
            "SLEAP",
            "DLC"
        ],
        "gflops": [4.086064384, 0.682148944, 0.31487032, 0.31487032, 0.31487032, 59.683428, 489.530834],
        "pck": [0.8798799992, 0.8741040826, 0.884296906, 0.8563422561, 0.8539961219, 0.7257240204, 0.7546848382],
        "color": "gold"
    },
    "AMP": {
        "labels": ["R1", "R2", "R3", "R4", "R5", "SLEAP"],
        "full_labels": [
            "ResNet-50, MSE",
            "EfficientNet-B2, Simple-angle (50:50)",
            "MobileNetV2, Simple-angle (50:50)",
            "MobileNetV2, Simple-angle (20:80) + bounding box polar",
            "MobileNetV2, Simple-angle (20:80)",
            "SLEAP"
        ],
        "gflops": [4.086064384, 0.682148944, 0.31487032, 0.31487032, 0.31487032, 5.831893628],
        "pck": [0.652569329, 0.6737609067, 0.6555232756, 0.6573637601, 0.6827429621, 0.7219010918],
        "color": "green"
    }
}

# Create the plot
plt.figure(figsize=(8, 6))

# Plot each dataset
for dataset_name, dataset in data.items():
    plt.scatter(dataset["gflops"], dataset["pck"], label=dataset_name, color=dataset["color"])
    for label, x, y in zip(dataset["labels"], dataset["gflops"], dataset["pck"]):
        plt.text(x, y, label, fontsize=9, ha='right', va='bottom')

# Set axis scales and labels
plt.xscale("log")
plt.xlabel("GFLOPs (log scale)")
plt.ylabel("PCK@0.1")
plt.title("Comparison of PCK@0.1 to GFLOPs")
plt.legend(title="Dataset")
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
