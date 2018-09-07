import numpy as np

a = [[2, 2], [2, 2]]
b = [[4, 1], [2, 2]]
print(np.matmul(a, b))

def raiseMatrix(matrix, power):
    if power == 0:
        raise ValueError('Please enter a non-zero positive integer')
    else:
        return raiseMatrixHelper(matrix, matrix, power)

def raiseMatrixHelper(initmatrix, matrix, power):
    if power == 1:
        return matrix
    else:
        newMatrix = np.matmul(initmatrix, matrix)
        return raiseMatrixHelper(initmatrix, newMatrix, power - 1)

homeOwnerMatrix = [[.94, .05], [.12, .88]]

oneDecade = raiseMatrix(homeOwnerMatrix, 10)
twoDecades = raiseMatrix(homeOwnerMatrix, 20)

print('The percentage of homeowners after the first decade is : ', .36 * oneDecade.item((0,0)))
print('The percentage of homeowners after two decades is: ', .36 * twoDecades.item((0,0)))
