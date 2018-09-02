# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import random

N = int(input("Введите число элементов для исходного массива: "))
arr = []

print("\nВ одномерном массиве: ")
for i in range(N):
    arr.append(int(random() * 100))
print(arr)

if arr[0] > arr[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if arr[i] < arr[min1]:
        temp = min1
        min1 = i
        if arr[temp] < arr[min2]:
            min2 = temp
    elif arr[i] < arr[min2]:
        min2 = i

print(f"1-й наименьший элемент в позиции {min1 + 1}: {arr[min1]}")
print(f"2-й наименьший элемент в позиции {min2 + 1}: {arr[min2]}")
