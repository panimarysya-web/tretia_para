import sqlite3


def create_tbl1():
    conn = sqlite3.connect("OPLA.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()


def create_tbl2():
    conn = sqlite3.connect("OPLA.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, FOREIGN KEY(user_id) REFERENCES games(id))")
    conn.commit()
    conn.close()


def many_insert_into1(data):
    conn = sqlite3.connect("OPLA.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO games (name) VALUES(?)", data)
    conn.commit()
    conn.close()


def many_insert_into2(data):
    conn = sqlite3.connect("OPLA.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO users (user_id, amount) VALUES(?, ?)", data)
    conn.commit()
    conn.close()


# create_tbl1()
create_tbl2()

A = [('Ivan',), ('Peter',), ('Kolya',), ('Serj',)]
B = [(3, 100500), (1, 100), (4, 123), (2, 246), (1, 369), (999, 666)]

# many_insert_into1(A)
#many_insert_into2(B)