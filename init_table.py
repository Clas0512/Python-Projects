import sqlite3 as sql
import check_database

def create_first_table():
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute('''CREATE TABLE IF NOT EXISTS Users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT)''')
    con.commit()
    con.close()

def create_table_password():
    con = sql.connect("database.db")
    cursor_db = con.cursor()

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS passwords
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password TEXT,
                        FOREIGN KEY (id) REFERENCES Users (id))''')
    con.commit()
    con.close()

def create_table_full_name():
    con = sql.connect("database.db")
    cursor_db = con.cursor()

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS fullnames
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fullname TEXT,
                        FOREIGN KEY (id) REFERENCES Users (id))''')
    con.commit()
    con.close()

def create_table_email():
    con = sql.connect("database.db")
    cursor_db = con.cursor()

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS emails
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT,
                        FOREIGN KEY (id) REFERENCES Users (id))''')
    con.commit()
    con.close()

def create_table_cities():
    con = sql.connect("database.db")
    cursor_db = con.cursor()

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS cities
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city TEXT,
                        FOREIGN KEY (id) REFERENCES Users (id))''')
    con.commit()
    con.close()

def set_tables(fullname, email, city):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("INSERT INTO fullnames (fullname) VALUES (?)", (fullname,))
    cursor_db.execute("INSERT INTO emails (email) VALUES (?)", (email,))
    cursor_db.execute("INSERT INTO cities (city) VALUES (?)", (city,))
    con.commit()
    con.close()

def add_list(username, password):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("INSERT INTO Users (username) VALUES (?)", (username,))
    cursor_db.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    con.commit()
    con.close()

def add_admin(password):
    admin = "admin"
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    if check_database.is_same("admin", "Users", "username") == 0:
        cursor_db.execute("INSERT INTO Users (username) VALUES (?)", (admin,))
        cursor_db.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
        cursor_db.execute("INSERT INTO fullnames (fullname) VALUES (?)", (admin,))
        cursor_db.execute("INSERT INTO emails (email) VALUES (?)", (admin,))
        cursor_db.execute("INSERT INTO cities (city) VALUES (?)", (admin,))
    con.commit()
    con.close()