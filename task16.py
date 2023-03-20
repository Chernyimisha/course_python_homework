# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X. Попробуйте использовать метод count(), а также решите задачу с помощью своего
# алгоритма (без использования метода count). Замерьте время работы двух алгоритмов и сравните, подумайте почему оно
# отличается.
# 5
# 1 2 3 4 5
# 3
# -> 1
import time
import random
# РАБОТАЕМ СО СПИСКОМ
n = int(input('Введите количество элементов в массиве: '))
list_number = [random.randint(0, 50) for _ in range(n)]
#for i in range(n):
#     list_number.append(int(input(f'Введите {i} элемент: ')))
print(list_number)
x = int(input('Введите число X: '))
count = 0
start = time.perf_counter()
for i in range(len(list_number)):
    if list_number[i] == x:
        count += 1
end = time.perf_counter()
print(f'-> {count}')
first_time = end - start


# РАБОТАЕМ С КОРТЕЖОМ
n = int(input('Введите количество элементов в массиве: '))
list_number = [random.randint(0, 50) for _ in range(n)]
#for i in range(n):
#     list_number.append(int(input(f'Введите {i} элемент: ')))
print(list_number)
x = int(input('Введите число X: '))
count = 0
list_number_tuple = tuple(list_number)
start = time.perf_counter()
for i in range(len(list_number)):
    if list_number_tuple[i] == x:
        count += 1
end = time.perf_counter()
print(f'-> {count}')
second_time = end - start

print(f'{first_time/second_time}')








