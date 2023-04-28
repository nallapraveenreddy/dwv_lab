#program
import matplotlib.pyplot as plt
import numpy as np

# Data for the plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2

# Creating a figure
fig = plt.figure()

# Line plot
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y1, label='sin(x)')
ax1.plot(x, y2, label='cos(x)')
ax1.set_title('Line Plot')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.legend()

# Scatter plot
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(x, y1, label='sin(x)', color='r', marker='o')
ax2.scatter(x, y2, label='cos(x)', color='b', marker='x')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax2.legend()

# Bar plot
ax3 = fig.add_subplot(2, 2, 3)
bar_labels = ['A', 'B', 'C', 'D', 'E']
bar_values = [3, 5, 7, 9, 6]
ax3.bar(bar_labels, bar_values, color='g', alpha=0.5)
ax3.set_title('Bar Plot')
ax3.set_xlabel('Categories')
ax3.set_ylabel('Values')

# Histogram
ax4 = fig.add_subplot(2, 2, 4)
data = np.random.randn(1000)
ax4.hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')
ax4.set_title('Histogram')
ax4.set_xlabel('Bins')
ax4.set_ylabel('Frequency')

# Adjusting the layout and displaying the plots
plt.tight_layout()
plt.show()
