def show_menu():
    print('1 - показать все записи')
    print('2 - найти по фамилии')
    print('3 - добавить запись')
    print('4 - изменить телефон')
    return int(input('Выберите цифру из меню (1, 2, 3 или 4): '))

def find_by_surname():
    surname = input('Введите фамилию для поиска: ')
    return surname

# def add_recording_list():
#     values = []
#     id = input('Введите номер записи: ')
#     values.append(id)
#     surname = input('Введите фамилию: ')
#     values.append(surname)
#     name = input('Введите имя: ')
#     values.append(name)
#     petronimic = input('Введите отчество: ')
#     values.append(petronimic)
#     phone_number = input('Введите номер телефона: ')
#     values.append(phone_number)
#     print(values)
#     return values

def add_record():
    values = input('Введите номер записи(id), фамилию, имя, отчество, номер телефона: ')
    return(values)



