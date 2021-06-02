import matplotlib.pyplot as plt
import math
import numpy as np

# Prepare the data
y=list(range(1,101))                     
x=list(range(1,101)) 
for i in range(99):
 y[i] = x[i]**2 + math.log(x[i]/2)
  


# Plot the data
plt.plot(x, y, label='graph')

# Add a legend
plt.legend()

# Show the plot
plt.show()
