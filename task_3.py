# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = int(input("Введите число элементов для исходного массива: "))
arr = [0] * N

for i in range(N):
    arr[i] = int(random() * 100)
print("\nИсходный массив:", arr)

mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print(f"Минимальный элемент = {arr[mn]}")
print(f"Максимальный элемент = {arr[mx]}")

arr[mn], arr[mx] = arr[mx], arr[mn]

print("\nПосле замены:\t", arr)
