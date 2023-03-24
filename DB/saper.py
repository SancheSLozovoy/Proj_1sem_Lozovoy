import sqlite3 as sq
from data_users import info_users

#with sq.connect('saper.db') as con:
 # con.execute("""CREATE TABLE IF NOT EXISTS users (
  #      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
   #     name TEXT NOT NULL,
    #    sex INTEGER NOT NULL DEFAULT 1,
     #   old INTEGER,
      #  score INTEGER
    #)""")
#con.executemany("INSERT INTO users VALUES (?,?,?,?,?)", info_users)
#con.commit()

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE score > 1100 and old <=14")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE old IN(12, 32) AND score > 1000")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE old IN(12, 32) AND score > 1000 OR sex ==1")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE (old IN(12, 32) OR sex = 2) AND score > 200")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM users WHERE score < 1100 ORDER BY old")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET old = 18 WHERE old = 20")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET score = score+300 WHERE old <= 12 ")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE users SET score = score+100 WHERE old = 15 ")
#     res = cur.fetchall()
# print(res)
#
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM users WHERE score < 1000 ")
#     res = cur.fetchall()
# print(res)