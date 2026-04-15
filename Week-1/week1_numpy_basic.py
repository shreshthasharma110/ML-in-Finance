import numpy as np

# Step 1: Create a vector
vector_length = 95
a = np.arange(vector_length)
print("Vector a:\n", a)

# Step 2: Convert to 2D array
a_2d = a.reshape(1, -1)
print("\n2D array:\n", a_2d)

# Step 3: Copy array
b = a_2d.copy()
print("\nCopied array:\n", b)

# Step 4: Print shape
print("\nShape of b:", b.shape)