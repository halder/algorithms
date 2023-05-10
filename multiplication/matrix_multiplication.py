import numpy as np

def strassen(X, Y):
    """
    Strassen's matrix multiplication.
    X, Y square matrices of degree k, where k is a power of 2.

    Runs in less than O(n^3).

    Uses numpy arrays for easy index manipulations and slicing.
    """
    n, d = X.shape
    i, j = n // 2, d // 2
    result = np.zeros((n, d))

    A = X[:i, :j]
    B = X[:i, j:]
    C = X[i:, :j]
    D = X[i:, j:]

    E = Y[:i, :j]
    F = Y[:i, j:]
    G = Y[i:, :j]
    H = Y[i:, j:]
    
    # base case
    if (n, d) == (2, 2):
        p1 = A * (F - H)
        p2 = (A + B) * H
        p3 = (C + D) * E
        p4 = D * (G - E)
        p5 = (A + D) * (E + H)
        p6 = (B - D) * (G + H)
        p7 = (A - C) * (E + F)
    
    else:
        p1 = strassen(A, (F - H))
        p2 = strassen((A + B), H)
        p3 = strassen((C + D), E)
        p4 = strassen(D, (G - E))
        p5 = strassen((A + D), (E + H))
        p6 = strassen((B - D), (G + H))
        p7 = strassen((A - C), (E + F))

    Q1 = p5 + p4 - p2 + p6
    Q2 = p1 + p2
    Q3 = p3 + p4
    Q4 = p1 + p5 - p3 - p7

    result[:i, :j] = Q1
    result[:i, j:] = Q2
    result[i:, :j] = Q3
    result[i:, j:] = Q4

    return result

if __name__ == "__main__":
    # test
    for _ in range(10):
        X = np.random.randint(10, size=(8, 8))
        Y = np.random.randint(10, size=(8, 8))

        print(np.all((X @ Y) == strassen(X, Y).astype(int)))