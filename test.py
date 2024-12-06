import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color of the entire figure
fig.patch.set_facecolor((0, 0, 0, 0.3))  # Light gray

# Set the background color of the axis
ax.set_facecolor('#E0E0E0')  # Slightly darker gray

# Plot some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y, label='Data from how2matplotlib.com')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('How to Set Plot Background Color in Matplotlib')

# Add legend
ax.legend()

# Display the plot
plt.show()