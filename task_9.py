# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

M = 5
N = 4
arr = []

print("В следующей матрице:")
for i in range(N):
    tmp = []
    for j in range(M):
        num = int(random() * 100)
        tmp.append(num)
        print(f"\t{num}", end='')
        arr.append(tmp)
    print()

mx = -1
for j in range(M):
    mn = 100
    for i in range(N):
        if arr[i][j] < mn:
            mn = arr[i][j]
    if mn > mx:
        mx = mn
print("максимальный элемент среди минимальных элементов столбцов матрицы:", mx)