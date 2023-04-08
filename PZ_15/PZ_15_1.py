# Вариант 3.
# Разработать БД «ЗАРПЛАТА», содержащую две таблицы Анкета и
# Больничные листы. Установить связь между таблицами. Заполнить
# таблицы произвольными данными (не менее 10 записей). Реализовать
# SQL-запросы на выборку, обновление, удаление данных из БД.
# Таблица "Анкета"
# id (INT, PK) - уникальный идентификатор сотрудника
# имя (VARCHAR)
# фамилия (VARCHAR)
# дата_рождения (DATE)
# пол (VARCHAR)
# дата_найма (DATE)
# должность (VARCHAR)
# отдел (VARCHAR)
# базовая_ставка (DECIMAL)
# Таблица "Больничные листы"
# id (INT, PK) - уникальный идентификатор больничного листа
# id_сотрудника (INT, FK) - идентификатор сотрудника, на которого выписан больничный
# лист
# дата_начала (DATE)
# дата_окончания (DATE)
# причина (VARCHAR)
# диагноз (VARCHAR)
# оплачен (BOOLEAN)
# В данной структуре таблица "Больничные листы" связана с таблицей "Анкета" через
# внешний ключ id_сотрудника. Это означает, что каждый больничный лист относится к
# определенному сотруднику из таблицы "Анкета".

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

# SQL-запросы на выборку данных:
# 1. Вывести список всех сотрудников и их должностей
# 2. Вывести список всех сотрудников и их базовых ставок
# 3. Вывести список всех сотрудников, работающих в отделе "IT"
# 4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
# 5. Вывести список всех больничных листов, выписанных сотруднику с id = 42
# 6. Вывести список всех больничных листов, оплаченных компанией
# 7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
# 8. Вывести среднюю базовую ставку всех сотрудников
# 9. Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
# 10. Вывести список всех сотрудников и общее количество дней, проведенных ими на
# больничном
# 11. Вывести информацию о сотрудниках и их больничных листах за последний месяц
# 12. Вывести среднюю продолжительность больничных листов сотрудников в каждом
# отделе
# 13. Вывести список сотрудников и информацию о последнем больничном листе,
# который они оформляли
# 14. Вывести список сотрудников и информацию о первом больничном листе, который
# они оформляли
# 15. Вывести список сотрудников и суммарную продолжительность их больничных
# листов в текущем году

with sq.connect("zarplata.db") as con:
    cur = con.cursor()
    res1 = cur.execute("SELECT name, lastname, dolznost FROM anketa ").fetchall()
    res2 = cur.execute("SELECT name, lastname, baza_stavka FROM anketa ").fetchall()
    res3 = cur.execute("SELECT name, lastname FROM anketa WHERE otdel='IT' ").fetchall()
    res4 = cur.execute("SELECT name, lastname FROM anketa WHERE data_naima>'2022-01-01'").fetchall()
    res5 = cur.execute("SELECT * FROM bolnicnie_listi WHERE id_a=42 ").fetchall()
    res6 = cur.execute("SELECT * FROM bolnicnie_listi WHERE oplachen=1").fetchall()
    res7 = cur.execute("SELECT anketa.name, anketa.lastname FROM anketa INNER JOIN bolnicnie_listi b ON "
                       "anketa.id_a = b.id_a WHERE strftime('%m', b.start_date) = strftime('%m', 'now')").fetchall()
    res8 = cur.execute("SELECT AVG(baza_stavka) FROM anketa").fetchall()
    res9 = cur.execute("SELECT name, lastname FROM anketa WHERE baza_stavka > 100000").fetchall()
    res10 = cur.execute("SELECT anketa.name, anketa.lastname, "
                        "SUM(julianday(bolnicnie_listi.stop_date) - julianday(bolnicnie_listi.start_date)) "
                        "FROM anketa INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a "
                        "GROUP BY anketa.name, anketa.lastname").fetchall()
    res11 = cur.execute("SELECT anketa.name, anketa.lastname, bolnicnie_listi.start_date, bolnicnie_listi.stop_date, "
                        "bolnicnie_listi.prichina, bolnicnie_listi.diagnoz, bolnicnie_listi.oplachen FROM anketa "
                        "INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a WHERE "
                        "bolnicnie_listi.start_date >= DATE('now', '-1 month')").fetchall()
    res12 = cur.execute("SELECT otdel, AVG(julianday(stop_date) - julianday(start_date) + 1) FROM anketa "
                        "INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a GROUP BY otdel").fetchall()
    res13 = cur.execute("SELECT anketa.name, anketa.lastname, bolnicnie_listi.start_date, bolnicnie_listi.stop_date, "
                        "bolnicnie_listi.prichina, bolnicnie_listi.diagnoz, bolnicnie_listi.oplachen FROM anketa "
                        "INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a "
                        "WHERE bolnicnie_listi.start_date = (SELECT MAX(start_date) "
                        "FROM bolnicnie_listi WHERE bolnicnie_listi.id_a = anketa.id_a)").fetchall()
    res14 = cur.execute("SELECT anketa.name, anketa.lastname, bolnicnie_listi.start_date, bolnicnie_listi.stop_date, "
                        "bolnicnie_listi.prichina, bolnicnie_listi.diagnoz, bolnicnie_listi.oplachen FROM anketa "
                        "INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a "
                        "WHERE bolnicnie_listi.start_date = (SELECT MIN(start_date) "
                        "FROM bolnicnie_listi WHERE bolnicnie_listi.id_a = anketa.id_a)").fetchall()
    res15 = cur.execute("SELECT name, lastname, SUM(julianday(stop_date) - julianday(start_date)) AS summ  FROM anketa "
                        "INNER JOIN bolnicnie_listi ON anketa.id_a = bolnicnie_listi.id_a "
                        "WHERE strftime('%Y', start_date) = strftime('%Y', 'now') "
                        "GROUP BY name, lastname ORDER BY summ").fetchall()
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)
print(res10)
print(res11)
print(res12)
print(res13)
print(res14)
print(res15)

# SQL-запросы на обновление данных из БД:
# 1. Обновить базовую ставку сотрудника на определенной должности.
# 2. Обновить отдел для всех сотрудников в определенном диапазоне возраста.
# 3. Обновить дату найма для сотрудника, получившего повышение.
# 4. Обновить причину больничного листа для сотрудника.
# 5. Обновить базовую ставку сотрудника в таблице "Анкета" на определенный
# процент, используя INNER JOIN с таблицей "Больничные листы". При этом
# необходимо исключить из обновления сотрудников, у которых были неоплаченные
# больничные листы.
# 6. Обновить дату начала больничного листа в таблице "Больничные листы" на
# определенную дату, используя INNER JOIN с таблицей "Анкета". При этом
# необходимо исключить из обновления больничные листы с уже пройденной датой
# начала
# 7. Обновить причину больничного листа в таблице "Больничные листы" на
# определенное значение для всех сотрудников, работающих в отделе "Бухгалтерия".

with sq.connect("zarplata.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE anketa SET baza_stavka = 30000 WHERE dolznost = 'Бухгалтер'")
    cur.execute("UPDATE anketa SET otdel = 'Маркетинг' WHERE birth_day BETWEEN '1950-01-01' AND '1970-01-01'")
    cur.execute("UPDATE anketa SET data_naima = '2019-12-24' WHERE id_a = 5")
    cur.execute("UPDATE bolnicnie_listi SET prichina = 'Простуда' WHERE id_a = 9")
    cur.execute("UPDATE anketa SET baza_stavka = baza_stavka * 1.2 "
                "WHERE id_a IN(SELECT id_a FROM bolnicnie_listi WHERE oplachen = 1)")
    cur.execute("UPDATE bolnicnie_listi SET bolnicnie_listi.start_date = '2020-01-01' "
                "WHERE bolnicnie_listi.start_date < '2020-01-01'")
    cur.execute("UPDATE bolnicnie_listi SET prichina = 'Ушиб' WHERE id_a "
                "IN (SELECT id_a FROM anketa WHERE otdel = 'Бухгалтерия')")
    s = cur.execute("SELECT * FROM bolnicnie_listi").fetchall()
print(s)

# SQL-запросы на удаление данных из БД:
# 1. Удалить все записи о больничных листах для сотрудника с именем "Иван"
# 2. Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
# 3. Удалить все записи о больничных листах для сотрудника с должностью
# "Менеджер"
# 4. Удалить все записи о больничных листах для сотрудника с отделом "Отдел
# продаж"
# 5. Удалить все записи о больничных листах для сотрудника женского пола
# 6. Удалить все записи о больничных листах для сотрудников старше 50 лет
# 7. Удалить все записи о неоплаченных больничных листах
# 8. Удалить все записи о больничных листах, дата окончания которых прошла
# 9. Удалить все записи о больничных листах, начиная с определенной даты
# 10. Удалить все записи о больничных листах, закончившихся до определенной даты
# 11. Удалить все больничные листы сотрудника с именем "Иван" из таблицы
# "Больничные листы"
# 12. Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву
# "С" из таблицы "Больничные листы"
# 13. Удалить все больничные листы, которые еще не были оплачены, у сотрудников с
# должностью "Менеджер" из таблицы "Больничные листы"
# 14. Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1
# января
# 15. Удалить все больничные листы, связанные со сотрудниками старше 50 лет из
# таблицы "Больничные листы"

with sq.connect("zarplata.db") as con:
    cur = con.cursor()
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches "
                "FROM bolnicnie_listi WHERE id_a IN(SELECT id_a FROM anketa WHERE name = 'Иван'").fetchall()
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches "
                "FROM bolnicnie_listi WHERE id_a IN(SELECT id_a FROM anketa WHERE lastname = 'Петов'").fetchall()
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches FROM bolnicnie_listi "
                "WHERE id_a(SELECT id_a FROM anketa WHERE dolznost = 'Менеджер'")
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches FROM bolnicnie_listi "
                "WHERE id_a(SELECT id_a FROM anketa WHERE otdel = 'Продажа'")
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches FROM bolnicnie_listi "
                "WHERE id_a(SELECT id_a FROM anketa WHERE sex = 'ж'")
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches FROM bolnicnie_listi "
                "WHERE id_a(SELECT id_a FROM anketa WHERE birth_day < 1973-01-01")
    cur.execute("DELETE start_date, stop_date, prichina, diagnoz, oplaches FROM bolnicnie_listi "
                "WHERE oplachen = 0")

