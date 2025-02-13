import math
from random import uniform,randint
from numpy import zeros
import matplotlib.pyplot as plt
# B = [[5, 2], [2, 1]]
B = [[5, 2], [2, 1]]
M = [[0, 0], [1, 1], [-1, 1]]

A = [[math.sqrt(B[0][0]), 0],
     [B[0][1] / math.sqrt(B[0][0]), math.sqrt(B[1][1] - B[0][1] ** 2 / B[0][0])]]
print("A =", A)
n = 2
N = int(input("N = "))
# y=[[0]*N]*n
y = zeros((len(M),n, N))
# x=[[0]*N]*(n*len(M))
x = zeros((len(M),n, N))
for z in range(len(M)):
    for l in range(n):
        for i in range(N):
            suma=0
            for j in range(11):
                suma += uniform(0.0, 1.0) - 0.5
            y[z][l][i] = suma
for z in range(len(M)):
    for k in range(n):
        for i in range(N):
            suma = 0
            for l in range(n):
                suma += A[k][l] * y[z][l][i]
            x[z][k][i] += suma + M[z][k]
print(x)


# for i in range(n):
#     for j in range(N):
#         suma=0
#         for l in range(11):
#             suma+=randint(0,1) - 0.5
#         y[i][j] = suma
#     print(y[i])
# for i in range(len(M)):
#     for k in range(n):
#         for j in range(N):
#             suma = 0
#             for l in range(n):
#                 suma += A[k][l] * y[l][j]
#             x[i][j] = suma + M[i][k]
#         print(x[i])

for i in range(len(x)):

    plt.scatter(x[i][0], y[i][0], color='b')
    plt.scatter(x[i][1], y[i][1], color='g')


plt.xlabel('Cлучайный вектор с требуемым нормальным законом распределением')
plt.ylabel('Независимые и нормально распределенные случайные величины.')
plt.grid(True)
plt.show()