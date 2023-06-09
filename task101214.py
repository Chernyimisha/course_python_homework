# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монеток: '))
pos_0 = 0
pos_1 = 0

for i in range(n):
    pos = input()
    if pos == '0':
        pos_0 += 1
    elif pos == '1':
        pos_1 += 1
    else:
        print('Введено неверное значение')
        break

if pos_0 > pos_1:
    print(pos_1)
else:
    print(pos_0)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('Введите сумму двух чисел: '))
p = int(input('Введите произведение двух чисел: '))
x = 0
y = 0

for i in range(1, 1001):
    if x != 0 and y != 0:
        break         # добавил break, чтобы не продолжать цикл когда первая пара чисел уже найдена.
    for j in range(1, 1001):
        if i + j == s and i * j == p:
            x = i
            y = j
            break

if x == 0 and y == 0:
    print('Даны некорректные числа суммы и произведения')
else:
    print(f'{s} {p} -> {x} {y}')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
count = 0
k = 0
while count < n - 2:
    count = 2 ** k
    k += 1
    print(count, end=' ')