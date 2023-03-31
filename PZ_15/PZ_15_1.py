import sqlite3 as sq
from data import anketa, bolnicnie_listi

with sq.connect('zarplata.db') as con:
    con.execute("PRAGMA foreing_keys = ON")
    con.execute("""CREATE TABLE IF NOT EXISTS anketa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    lastname TEXT,
    birth_day DATE,
    sex VARCHAR,
    data_naima DATE,
    dolznost VARCHAR,
    otdel VARCHAR,
    baza_stavka DECIMAL
    )""")
con.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", anketa)
con.commit()

with sq.connect('zarplata.db') as con:
    con.execute("""CREATE TABLE IF NOT EXISTS bolnicnie_listi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sotr INTEGER,
    start_date DATE,
    stop_date DATE,
    prichina VARCHAR,
    diagnoz VARCHAR,
    oplachen BOOLEAN,
    FOREIGN KEY (id_sotr) REFERENCES anketa (id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")
con.executemany("INSERT INTO bolnicnie_listi VALUES (?, ?, ?, ?, ?, ?, ?)", bolnicnie_listi)
con.commit()
