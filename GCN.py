import numpy as np

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]],
).astype(dtype=float)

print(A)

X = np.array([[i, -i] for i in range(A.shape[0])]).astype(dtype=float)
print(X)