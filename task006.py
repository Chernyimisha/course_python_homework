# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

str_az = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'


def rle(str_1):
    new_str = ''
    temp_letter = str_1[0]
    count = 0
    for i in range(len(str_1)):
        if str_1[i] == temp_letter:
            count += 1
        else:
            if count > 1:
                new_str += temp_letter + str(count)
            else:
                new_str += temp_letter
            count = 1
            temp_letter = str_1[i]
    new_str += temp_letter + str(count)
    return new_str


if str_az.isalpha():
    str_az_count = rle(str_az)
    print(str_az_count)
else:
    print('Invalid')
