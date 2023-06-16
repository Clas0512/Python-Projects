import sqlite3 as sql

def change_password(username, password):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchall()
    cursor_db.execute("UPDATE passwords SET password = (?) WHERE id = (?)", (password, id[0][0]))
    con.commit()
    con.close()

def change_fullname(username, fullname):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchall()
    cursor_db.execute("UPDATE fullnames SET fullname = (?) WHERE id = (?)", (fullname, id[0][0]))
    con.commit()
    con.close()

def change_email(username, email):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchall()
    cursor_db.execute("UPDATE emails SET email = (?) WHERE id = (?)", (email, id[0][0]))
    con.commit()
    con.close()

def change_city(username, city):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchall()
    cursor_db.execute("UPDATE cities SET city = (?) WHERE id = (?)", (city, id[0][0]))
    con.commit()
    con.close()
