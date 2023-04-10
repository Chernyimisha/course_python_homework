# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book_name.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book_name.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book_name.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному кретерию'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def change_data() -> None:
    '''Осуществляет изменение данных'''

    data = input('Введите данные для поиска объекта изменений: ')
    with open('book_name.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    change_record = search(tel_book, data)
    tel_book = tel_book.split('\n')
    pos_change_record = tel_book.index(change_record)
    change_record = input_change(change_record)
    tel_book[pos_change_record] = change_record
    tel_book = "\n".join(tel_book)
    with open('book_name.txt', 'w', encoding='utf-8') as f:
        f.write(tel_book)


def input_change(record: str) -> str:
    record = record.split('|')
    number = input('Введите "0", если необходимо изменить ФИО и "1", если необходимо изменить телефон: ')
    if number == '0':
        record[int(number)] = input('Введите ФИО: ')
    elif number == '1':
        record[int(number)] = input('Введите номер телефона: ')
    else:
        print('Введены некорректные данные')
    return '| '.join(record)


def delete_data() -> None:
    '''Осуществляет удаление данных'''
    data = input('Введите данные для поиска объекта для удаления: ')
    with open('book_name.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    del_record = search(tel_book, data)
    tel_book = tel_book.split('\n')
    tel_book.remove(del_record)
    tel_book = "\n".join(tel_book)
    with open('book_name.txt', 'w', encoding='utf-8') as f:
        f.write(tel_book)


while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. изменение, 5. удаление')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        change_data()
    elif mode == 5:
        delete_data()
    else:
        break
