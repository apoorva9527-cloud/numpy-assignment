import numpy as np

# Create NumPy array
data = np.array([10, 20, 30, 40])

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# Normalize the data
normalized = (data - mean) / std

# Reshape into 2D array
reshaped = normalized.reshape(2, 2)

# Print results
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", round(std, 2))
print("Normalized data:", np.round(normalized, 2))
print("Reshaped data:")
print(np.round(reshaped, 2))
print("Reshaped data shape:", reshaped.shape)