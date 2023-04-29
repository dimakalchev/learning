def gaussian_elimination(matrix, vector):
    """Решение системы линейных уравнений методом Гаусса"""
    n = len(matrix)
    for i in range(n):
        div = matrix[i][i]
        matrix[i] = [elem / div for elem in matrix[i]]
        vector[i] /= div
        for j in range(i+1, n):
            sub = matrix[j][i]
            matrix[j] = [elem - sub*matrix[i][k] for k, elem in enumerate(matrix[j])]
            vector[j] -= sub*vector[i]
    x = [0]*n
    for i in reversed(range(n)):
        x[i] = vector[i] - sum(matrix[i][j]*x[j] for j in range(i+1, n))
    return tuple(x)

matrix = [[1, 2, 1], [4, 5, 6], [7, 8, 10]]
vector = [8, 23, 34]
solution = gaussian_elimination(matrix, vector)
print(solution) # (1.0, 2.0, 3.0)
