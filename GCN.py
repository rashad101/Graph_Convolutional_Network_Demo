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

print(A.dot(X))

print(X.shape[0])
print(X.shape[1])

I = np.array(np.eye(A.shape[0]))
print(I)
A_hat = A+I
print(A_hat.dot(X))

D = np.array(np.sum(A, axis=0))
print(D)
D = np.array(np.diag(D))
print(D)
