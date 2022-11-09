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
# id = 9
# name = 'Степан'
# surname = 'Степанов'
# petronimic = 'Александрович'
# phone_number = +79456785432
# cursor.execute(
#     f"insert into phonebook (id, surname, name, petronimic, phone_number) "
#     f"values ('{id}', '{surname}', '{name}','{petronimic}', '{phone_number}')")
# conn.commit()

# удалить студента
# id = 9
# cursor.execute(
#     f"delete from phonebook where id={id}"
# )
# conn.commit()

# обновить данные о студенте
id = 9
cursor.execute(
    f"update phonebook set name='Юрий' where id={id}"
)
conn.commit()
conn.close()