# importing python library for plotting graphs
import matplotlib.pyplot as plt

# Creating y-axis and x-axis sample values
a1 = [x for x in range(-11,12,1)]
a2 = [x**2 for x in range(-11,12,1)]
b = a1

# Plotting the two graphs
plt.plot(b,a1,b,a2)
# Adding graph title
plt.title("Graphs for two data sets")
# Adding legends for the two line
plt.legend(["y=x","y=x^2"])
# Adding labels for graph axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# Adding grid lines to graph
plt.grid()
# Showing the graph
plt.show()

