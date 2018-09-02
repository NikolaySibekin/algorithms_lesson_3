# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

M = 5
N = 4
arr = []

for i in range(N):
    tmp = []
    summa = 0
    print(f"Введите элементы {i + 1}-й строки матрицы:")
    for j in range(M - 1):
        num = int(input())
        summa += num
        tmp.append(num)
    tmp.append(summa)
    arr.append(tmp)

print("\nПолученная матрица:")
for i in arr:
    print(i)
