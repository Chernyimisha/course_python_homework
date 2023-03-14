# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Введите трехзначное число: ")

print(f"{number} -> {int(number[0]) + int(number[1]) + int(number[2])} ({number[0]} + {number[1]} + {number[2]})")
