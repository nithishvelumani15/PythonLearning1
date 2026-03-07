import matplotlib.pyplot as plt
import numpy as np

# Prepare data
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# Plot the data
plt.plot(xpoints, ypoints)

# Add labels and a title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot")

# Display the plot
plt.show()
