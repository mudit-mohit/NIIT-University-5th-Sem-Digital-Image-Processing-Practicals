import numpy as np
matrix = np.zeros((8,8), dtype = 'uint8')
print(matrix)
matrix[1:4, 1:4] = 1
print(matrix)
tx = 2
ty = -1
sm = np.roll(matrix, (ty,tx), axis = (0,1))
print(sm)
a = 45
rm = np.rot90(sm, k = -a//90)
print(rm)