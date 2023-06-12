import matplotlib.pyplot as plt

# Data
hours = [
    "14:00", "15:00", "16:00", "17:00", "18:00",
    "19:00", "20:00", "21:00", "22:00", "23:00"
]
rx = [
    111.79, 109.28, 107.95, 111.92, 111.58,
    111.32, 111.10, 111.25, 111.23, 111.27
]
tx = [
    79.51, 78.23, 77.13, 79.86, 79.09,
    79.43, 79.63, 79.21, 79.45, 79.15
]

# Create the plot
plt.plot(hours, rx, label="Received", color="blue")
plt.plot(hours, tx, label="Transferred", color="red")

# Set labels and title
plt.xlabel("Hour")
plt.ylabel("Data (MiB)")
plt.title("Hourly Network Usage")

# Display the legend
plt.legend()

# Display the grid
plt.grid(True)

# Save the plot as a PNG file
plt.savefig("network_usage.png")

# Show the plot
plt.show()

