# https://habr.com/ru/post/321510/

import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# показать всех студентов
cursor.execute("select * from phonebook")
results = cursor.fetchall()
print(results)

# поиск записи
# surname = 'Иванов'
# cursor.execute(f"select * from students where surname like '%{surname}%'")
# results = cursor.fetchall()
# print(results)

# добавить студента
# name = 'Степан'
# surname = 'Степанов'
# phone = 45648
# description = 'Инженер'
# cursor.execute(
#     f"insert into students (name, surname, phone, description) "
#     f"values ('{name}', '{surname}', {phone}, '{description}')")
# conn.commit()

# удалить студента
# id = 5
# cursor.execute(
#     f"delete from students where id={id}"
# )
# conn.commit()

# обновить данные о студенте
# id = 3
# cursor.execute(
#     f"update students set name='Юрий' where id={id}"
# )
conn.commit()
conn.close()