# determines whether a matrix is orthogonal. A square matrix is orthogonal,
# if its columns and rows are orthogonal unit vectors,
# which is equivalent to: MT M = I

import numpy as np


def check_orthogonal(M):
    # make sure the input is a matrix
    if len(np.shape(M)) !=2:
        print("error: input is not a matrix")
        return
    # make sure the input is not a square matrix
    dim = np.shape(M)[0]
    if dim != np.shape(M)[1]:
        print("error: input is not a square matrix")
        return
    A = np.dot(M, M.T)
    #  if np.array_equal(A, np.identity(dim)):
    [rows, cols] = A.shape
    I = np.identity(dim)
    for i in range(rows):
        for j in range(cols):
            if not (A[i, j] - I[i, j] <= 10e-3):
                print("matrix is not orthogonal")
                return
    print("matrix is orthogonal")


if __name__ == '__main__':
    # Verify check_orthogonal function
    D = 1. / 3. * np.array(
        [[2, 2, -1],
         [2, -1, 2],
         [-1, 2, 2]])
    check_orthogonal(D)

    #  Test 2
    R = np.array([[np.cos(np.pi / 4), -np.sin(np.pi / 4)],
    [np.sin(np.pi / 4), np.cos(np.pi / 4)]])
    check_orthogonal(R)
