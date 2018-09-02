# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

N = int(input("Введите число элементов для исходного массива: "))
arr = [0] * N

print("\nВ одномерном массиве: ")
for i in range(N):
    arr[i] = int(random()*100)
print(arr)

min_id = 0
max_id = 0
for i in range(1, N):
    if arr[i] < arr[min_id]:
        min_id = i
    elif arr[i] > arr[max_id]:
        max_id = i
print(f"минимальный элемент = {arr[min_id]}, максимальный элемент = {arr[max_id]}")

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += arr[i]
print("\nCумма элементов, находящихся между минимальным и максимальным =", summa)