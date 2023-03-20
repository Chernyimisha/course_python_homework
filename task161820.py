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

n = int(input('Введите количество элементов в массиве: '))
list_number = []
for i in range(n):
    list_number.append(int(input(f'Введите {i} элемент: ')))

print(list_number)

x = int(input('Введите число X: '))

list.sort(list_number)
min_deviation = abs(x - list_number[-1])
min_deviation_element = 0

for i in range(n):
    deviation = abs(x - list_number[i])

    if deviation < min_deviation:
        min_deviation = deviation
        min_deviation_element = list_number[i]
print(min_deviation_element)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

russian_dict = {}
russian_dict.update({1: 'А, В, Е, И, Н, О, Р, С, Т', 2: 'Д, К, Л, М, П, У', 3: 'Б, Г, Ё, Ь, Я',
                     4: 'Й, Ы', 5: 'Ж, З, Х, Ц, Ч', 8: 'Ш, Э, Ю', 10: 'Ф, Щ, Ъ'})
english_dict = {}
english_dict.update({1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P', 4: 'F, H, V, W, Y',
                     5: 'K', 8: 'J, X', 10: 'Q, Z'})

# print(russian_dict)
# print(english_dict)


input_word = input('Введите слово: ')
input_word = input_word.upper()
# print(input_word)
count = 0

for i in range(len(input_word)):
    for j in russian_dict.keys():
        if input_word[i] in russian_dict[j]:
            count += j
    for k in english_dict.keys():
        if input_word[i] in english_dict[k]:
            count += k

    # russian_dict[i] = input(f'Введите буквы для оценки в {i} оч.: ')
    # english_dict[i] = input(f'Введите буквы для оценки в {i} оч.: ')

print(count)
# print(english_dict)