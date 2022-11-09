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
        #print(i)
    results3 = '\n'.join(results2)
    #print(type(results3))
    return results3

def find_by_surname(surname):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from phonebook where surname like '%{surname}%'")
    results = cursor.fetchall()
    #print(results)
    return results

# def add_recording_list(values):
#     conn = sqlite3.connect('phonebook.db')
#     cursor = conn.cursor()
#     cursor.execute(
#         f"insert into phonebook (id, surname, name, petronimic, phone_number) "
#         f"values ('{values[0]}', '{values[1]}', '{values[2]}','{values[3]}', '{values[4]}')")
#     conn.commit()

def add_record(string):
    values = string.split()
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(
        f"insert into phonebook (id, surname, name, petronimic, phone_number) "
        f"values ('{values[0]}', '{values[1]}', '{values[2]}','{values[3]}', '{values[4]}')")
    conn.commit()

def delete_record(id):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(
    f"delete from phonebook where id={id}"
    )
    conn.commit()





