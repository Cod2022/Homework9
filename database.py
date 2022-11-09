# https://habr.com/ru/post/321510/

import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# показать всех студентов
cursor.execute("select * from phonebook")
results = cursor.fetchall()
print(results)

# поиск записи
# surname = 'Мухина'
# cursor.execute(f"select * from phonebook where surname like '%{surname}%'")
# results = cursor.fetchall()
# print(results)

# добавить студента
# id = 10
# name = 'Степан'
# surname = 'Александров'
# petronimic = 'Александрович'
# phone_number = +79456785432
# cursor.execute(
#     f"insert into phonebook (id, surname, name, petronimic, phone_number) "
#     f"values ('{id}', '{surname}', '{name}','{petronimic}', '{phone_number}')")
# conn.commit()

# id = [11, 'Степан', 'Александров', 'Александрович', +79456785432]
# name = 'Степан'
# surname = 'Александров'
# petronimic = 'Александрович'
# phone_number = +79456785432
# cursor.execute(
#     f"insert into phonebook (id, surname, name, petronimic, phone_number) "
#     f"values ('{id[0]}', '{id[1]}', '{id[2]}','{id[3]}', '{id[4]}')")
# conn.commit()

# удалить студента
id = 11
cursor.execute(
    f"delete from phonebook where id={id}"
)
conn.commit()

# обновить данные о студенте
# id = 9
# cursor.execute(
#     f"update phonebook set name='Юрий' where id={id}"
# )
# conn.commit()
# conn.close()