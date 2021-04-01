def addition(A, B):
    rows = len(A)
    cols = len(A[0])
    Z = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            Z[i][j] = A[i][j] + B[i][j]
    return Z


def substruction(A, B):
    rows = len(A)
    cols = len(A[0])
    Z = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            Z[i][j] = A[i][j] - B[i][j]
    return Z


def product(A, B):
    arows = len(A)
    acols = len(A[0])
    bcols = len(B[0])

    Z = [[0] * bcols for _ in range(arows)]
    for i in range(arows):
        for j in range(acols):
            for k in range(bcols):
                Z[i][k] += A[i][j] * B[j][k]
    return Z


def fast_product(A, B):
    arows = len(A)
    acols = len(A[0])
    bcols = len(B[0])

    Z = [[0] * bcols for _ in range(arows)]
    for i in range(arows):
        Ai, Zi = A[i], Z[i]  # объявим константами, т.к они не меняются
        for k in range(bcols):
            acc = 0
            for j in range(acols):
                acc += Ai[j] * B[j][k]
            Zi[k] = acc
    return Z


def divide(A, B):
    rows = len(A)
    cols = len(A[0])
    Z = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            Z[i][j] = A[i][j] / B[i][j]
    return Z


def transpose(A):
    rows = len(A)
    cols = len(A[0])
    Z = [[0] * rows for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            Z[i][j] = A[j][i]
    return Z


def determinant_recursive(A, acc=0):
    assert len(A) == len(A[0]), 'Матрица должна быть квадратной'
    assert len(A) <= 12, 'Детерминант будет вычисляться долго...'

    idxs = list(range(len(A)))

    if len(A) == 2:
        d = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return d

    for i in idxs:

        minor = A.copy()[1:]

        height = len(minor)

        for j in range(height):
            # выкидываем i-й элемент
            minor[j] = minor[j][0:i] + minor[j][i + 1:]

        sign = (-1) ** (i % 2)

        sub_d = determinant_recursive(minor)

        acc += sign * A[0][i] * sub_d
    return acc

def determinant_fast(A):

    n = len(A)
    A_copy = A.copy()

    for d in range(n):
        if A_copy[d][d] == 0:
            A_copy[d][d] = 1.0e-12
        for i in range(d + 1, n):
            scaler = A_copy[i][d] / A_copy[d][d]
            for j in range(n):
                A_copy[i][j] = A_copy[i][j] - scaler * A_copy[d][j]

    product = 1.0
    for i in range(n):
        product *= A_copy[i][i]

    return product