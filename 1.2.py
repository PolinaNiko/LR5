import numpy as np

X = np.array([
    [1, 16, 60],
    [1, 17, 61],
    [1, 18, 62],
    [1, 19, 63],
    [1, 20, 64],
    [1, 21, 65],
    [1, 22, 66],
    [1, 23, 67],
    [1, 24, 68],
    [1, 25, 69],
    [1, 26, 70],
    [1, 27, 71]
])
Y = np.array([
    [13.5],
    [13.6],
    [13.7],
    [13.8],
    [13.9],
    [14.1],
    [14.2],
    [14.3],
    [14.4],
    [14.5],
    [14.6],
    [14.7]
])
A = np.linalg.pinv(X).dot(Y)
print("Вектор оценок А:\n ", A)
Y_predicted = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]
print("\nПроверка Y: ", Y_predicted)
