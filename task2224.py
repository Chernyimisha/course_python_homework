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

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
import random
n = int(input('Задайте число кустов: '))
list_1 = [random.randint(3, 15) for i in range(n)]
list_2 = list()
sum_number = 0

for i in range(len(list_1)-1):
    sum_number = list_1[i-1] + list_1[i] + list_1[i + 1]
    list_2.append(sum_number)
    sum_number = 0
list_2.append(list_1[-1] + list_1[-2] + list_1[0])

print(f'{n} -> {list_1}')
print(max(list_2))