import sqlite3 as sq
from data import anketa, bolnicnie_listi

# with sq.connect('zarplata.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
#     id_a INTEGER PRIMARY KEY,
#     name TEXT,
#     lastname TEXT,
#     birth_day DATE,
#     sex VARCHAR,
#     data_naima DATE,
#     dolznost VARCHAR,
#     otdel VARCHAR,
#     baza_stavka DECIMAL
#     )""")
# cur.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", anketa)
# con.commit()
#
# with sq.connect('zarplata.db') as con:
#     cur = con.cursor()
#     cur.execute("PRAGMA foreing_keys = ON")
#     cur.execute("""CREATE TABLE IF NOT EXISTS bolnicnie_listi (
#     id INTEGER PRIMARY KEY,
#     id_a INTEGER,
#     start_date DATE,
#     stop_date DATE,
#     prichina VARCHAR,
#     diagnoz VARCHAR,
#     oplachen BOOLEAN,
#     FOREIGN KEY (id_a) REFERENCES anketa(id_a) ON DELETE CASCADE ON UPDATE CASCADE
#     )""")
# cur.executemany("INSERT INTO bolnicnie_listi VALUES (?, ?, ?, ?, ?, ?, ?)", bolnicnie_listi)
# con.commit()

with sq.connect("zarplata.db") as con:
    cur = con.cursor()
    res1 = cur.execute("SELECT name, lastname, dolznost FROM anketa ").fetchall()
    res2 = cur.execute("SELECT name, lastname, baza_stavka FROM anketa ").fetchall()
    res3 = cur.execute("SELECT name, lastname FROM anketa WHERE otdel='IT' ").fetchall()
    res4 = cur.execute("SELECT name, lastname FROM anketa WHERE data_naima>'2022-01-01'").fetchall()
    res5 = cur.execute("SELECT * FROM bolnicnie_listi WHERE id_a=42 ").fetchall()
    res6 = cur.execute("SELECT * FROM bolnicnie_listi WHERE oplachen=1").fetchall()
    res7 = cur.execute("SELECT * FROM bolnicnie_listi WHERE start_date='2023-04-01'").fetchall()
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)