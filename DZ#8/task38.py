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


def delete_data() -> None:
    '''Осуществляет удаление данных'''



while True:
    print('1. вывод, 2. добавление, 3. поиск')
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
