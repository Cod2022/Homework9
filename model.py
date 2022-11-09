import sqlite3


def show_all():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("select * from phonebook")
    results = cursor.fetchall()
    results2 = []
    for i in results:
        i = str(i)
        results2.append(i)
        print(i)
    results3 = '\n'.join(results2)
    print(type(results3))
    return results3

def find_by_surname(surname):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from phonebook where surname like '%{surname}%'")
    results = cursor.fetchall()
    print(results)
    return results

def add_recording(id, surname, name, petronimic, phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    id = input('Введите номер записи: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    petronimic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    cursor.execute(
        f"insert into phonebook (id, surname, name, petronimic, phone_number) "
        f"values ('{id}', '{surname}', '{name}','{petronimic}', '{phone_number}')")
    conn.commit()


