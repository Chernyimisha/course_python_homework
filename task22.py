# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import time
import random

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
list_1 = [random.randint(10, 30) for i in range(n)]
list_2 = [random.randint(0, 25) for i in range(m)]
print(list_1)
print(list_2)
start1 = time.perf_counter()

# РЕШЕНИЕ ЧЕРЕЗ ОБЪЕДИНЕНИЕ МНОЖЕСТВ

set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set_1 & set_2
end1 = time.perf_counter()

print(end1-start1)

print(set_3)
start2 = time.perf_counter()

# РЕШЕНИЕ С ПОМОЩЬЮ ЦИКЛА

set_2 = set()
for i in list_1:
    for j in list_2:
        if i == j:
            set_2.add(i)
end2 = time.perf_counter()
print(set_2)
print(end2-start2)
print((end1-start1)/(end2-start2))

# ТАК И НЕ ПОНЯЛ КАКОЙ МЕТОД СПОСОБ БЫСТРЕЕ, РАЗНИЦА НЕ СУЩЕСТВЕННАЯ.