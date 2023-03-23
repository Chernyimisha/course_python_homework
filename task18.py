# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input('Введите количество элементов в массиве: '))
# list_number = []
# for i in range(n):
#     list_number.append(int(input(f'Введите {i} элемент: ')))

import random
from random import randrange
from time import perf_counter

list_number = [random.randint(-400, 400) for _ in range(1000000)]

# print(list_number)

x = int(input('Введите число X: '))

start = perf_counter()
list.sort(list_number)
min_deviation = abs(x - list_number[-1])
min_deviation_element = 0

for i in range(len(list_number)):
    deviation = abs(x - list_number[i])

    if deviation < min_deviation:
        min_deviation = deviation
        min_deviation_element = list_number[i]
print(min_deviation_element)

end = perf_counter()
print(end - start)

