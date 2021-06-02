import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 100, 100)
y=np.linspace(0,100,100)

# Plot the data
plt.plot(x, y, label='linear')


# Add a legend
plt.legend()

# Show the plot
plt.show()