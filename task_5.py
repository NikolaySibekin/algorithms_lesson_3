# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

N = int(input("Введите число элементов для исходного массива: "))
arr = []

print("\nВ одномерном массиве: ")
for i in range(N):
    arr.append(int(random() * 100) - 100)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1
print(f"максимальный отрицательный элемент равен: {arr[index]}, его позиция в массиве: {index + 1}")