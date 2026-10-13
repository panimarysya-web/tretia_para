# import json
# data = здесь инфа о студентах из файла
# with open("many_users.json", "w", encoding="utf-8") as f:
#     for i in range(100000):
#         for user in data:
#             json.dump(user, f, ensure_ascii=False)
#             f.write("\n")
#
#

# работа с SQL таблицами
# CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     mark REAL,
#     age INTEGER)
# INSERT INTO students(name, mark, age) VALUES("Иванов", 4.1, 19)      синтаксис SQL таблиц
# SELECT * FROM students WHERE age > 18
# UPDATE students SET age = 20 WHERE name = "Иванов"
# DELETE FROM students WHERE id = 1


import sqlite3

def create_tbl():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)")
    conn.commit()
    conn.close()
def insert_into(a, b, c):
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, mark, age) VALUES(?, ?, ?)" , (a, b, c))
    conn.commit()
    conn.close()
def many_insert_into(data):
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (name, mark, age) VALUES(?, ?, ?)" , data)
    conn.commit()
    conn.close()
def update_into():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute( "UPDATE students SET age=25 WHERE id =1")
    conn.commit()
    conn.close()
def delete_into(a):
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute( "DELETE FROM students WHERE id = ?" , (a))
    conn.commit()
    conn.close()

create_tbl()
# for i in range():
#     delete_into(i)
# insert_into('Vasisualiy', 4.8, 45)
# update_into()
# A =[("Mariah", 5, 19), ("Zlata", 5, 19), ("Lohankin", 4, 20)]
# many_insert_into(A)



# ПРИНЦИПЫ ACID:
#     -Атомарность
#     -Согласованность
#     -Изолированность
#     -Долговечность

#ORM - Object-Relational Mapping  это технология которая помогает переводить питоновский код в SQL

def show_data():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students WHERE age > 19")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        users.append(row[1])
    print(users)

show_data()

users = session.query(student).filter(student.age > 19).all()