import sqlite3 as sq
from data import anketa, bolnicnie_listi

with sq.connect('zarplata.db') as con:
    con.execute("PRAGMA foreing_keys = ON")
    con.execute("""CREATE TABLE IF NOT EXISTS anketa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL,
    birth_day DATE NOT NULL,
    sex VARCHAR NOT NULL,
    data_naima DATE NOT NULL,
    otdel VARCHAR NOT NULL,
    baza_stavka DECIMAL NOT NULL
    )""")
con.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?)", anketa)
con.commit()

with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bolnicnie_listi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sotr INTEGER NOT NULL,
    start_date DATE NOT NULL,
    stop_date DATE NOT NULL,
    prichina VARCHAR NOT NULL,
    diagnoz VARCHAR NOT NULL,
    oplachen BOOLEAN NOT NULL,
    FOREIGN KEY (id_sotr) REFERENCES anketa (id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")
con.executemany("INSERT INTO bolnicnie_listi VALUES (?, ?, ?, ?, ?, ?, ?)", bolnicnie_listi)
