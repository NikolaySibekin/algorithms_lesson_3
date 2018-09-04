# Определить, какое число в массиве встречается чаще всего.

from random import random

N = int(input("Введите число элементов для исходного массива: "))
arr = [0] * N

print("\nВ одномерном массиве: ")
for i in range(N):
    arr[i] = int(random() * 100)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(f"число {num} встречается {max_frq} раз(а).")
else:
    print('все элементы уникальны, повторяющихся нет!')