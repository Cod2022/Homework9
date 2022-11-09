def show_menu():
    print('1 - показать все записи')
    print('2 - найти по фамилии')
    print('3 - удалить запись')
    print('4 - изменить телефон')
    return int(input('Выберите цифру из меню (1, 2, 3 или 4): '))

def find_by_surname():
    surname = input('Введите фамилию для поиска: ')
    return surname