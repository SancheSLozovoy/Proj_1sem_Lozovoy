import sqlite3 as sq
from data_users import info_users, info_games

# with sq.connect('saper.db') as con:
#  con.execute("""CREATE TABLE IF NOT EXISTS users (
#        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        name TEXT NOT NULL,
#        sex INTEGER NOT NULL DEFAULT 1,
#        old INTEGER,
#        score INTEGER
#     )""")
# con.executemany("INSERT INTO users VALUES (?,?,?,?,?)", info_users)
# con.commit()

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE score > 1100 and old <=14")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE old IN(12, 32) AND score > 1000")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE old IN(12, 32) AND score > 1000 OR sex ==1")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE (old IN(12, 32) OR sex = 2) AND score > 200")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE score < 1100 ORDER BY old")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET old = 18 WHERE old = 20")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET score = score+300 WHERE old <= 12 ")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET score = score+100 WHERE old = 15 ")
#     res = cur.fetchall()
# print(res)

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM users WHERE score < 1000 ")
#     res = cur.fetchall()
# print(res)

# with sq.connect('saper.db') as con:
#  con.execute("""CREATE TABLE IF NOT EXISTS games (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        user_id INTEGER,
#        score INTEGER,
#        time INTEGER
#     )""")
# con.executemany("INSERT INTO games VALUES (?,?,?,?)", info_games)
# con.commit()

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE score < 1100")
    res = cur.fetchall()
print(res)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE user_id = 1")
    res = cur.fetchall()
print(res)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE score > 1000 ORDER BY user_id")
    res = cur.fetchall()
print(res)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE time >= 15500000")
    res = cur.fetchall()
print(res)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE user_id IN(2, 5)")
    res = cur.fetchall()
print(res)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE games SET score = score+1000 WHERE user_id = 3")
    res = cur.fetchall()

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE games SET time = time-20000 WHERE score >= 2000")
    res = cur.fetchall()

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM games WHERE score < 500")
    res = cur.fetchall()

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM games WHERE score <= 2900 and SCORE >=2000")
    res = cur.fetchall()