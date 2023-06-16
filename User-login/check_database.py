import sqlite3 as sql

def is_same(key, table, where):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT * FROM " + table + " WHERE " + where + " = (?)", (key,))
    compare_str = cursor_db.fetchall()
    con.close()
    if compare_str == []:
        return 0
    return 1

def is_include_email(key):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT * FROM emails WHERE email LIKE (?)", ("%" + key + "%",))
    compare_str = cursor_db.fetchall()
    con.close()
    if compare_str == []:
        return 0
    return 1

def query(tablename):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute(f"SELECT * FROM {tablename}")
    result = cursor_db.fetchall()
    print("\n", result, "\n")
    con.close()

def password_query(username, password):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = (?)", (username,))
    id = cursor_db.fetchall()
    cursor_db.execute("SELECT password FROM passwords WHERE id = (?)", (id[0][0],))
    result = cursor_db.fetchall()
    con.close()
    if result[0][0] == password:
        return 1
    return 0

def user_info(username):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchone()
    cursor_db.execute("SELECT username, password, fullname, email, city "
                    "FROM Users "
                    "INNER JOIN passwords ON Users.id = passwords.id "
                    "INNER JOIN fullnames ON Users.id = fullnames.id "
                    "INNER JOIN emails ON Users.id = emails.id "
                    "INNER JOIN cities ON Users.id = cities.id "
                    "WHERE Users.id = (?)", (id[0],))
    result = cursor_db.fetchone()
    print("\nUsername : ", result[0])
    print("Password : ", result[1])
    print("Fullname : ", result[2])
    print("Email : ", result[3])
    print("City : ", result[4], "\n")
    con.close()

def user_info_specified(username, feature):
    con = sql.connect("database.db")
    cursor_db = con.cursor()
    cursor_db.execute("SELECT id FROM Users WHERE username = ?", (username,))
    id = cursor_db.fetchone()
    cursor_db.execute("SELECT username, password, fullname, email, city "
                    "FROM Users "
                    "INNER JOIN passwords ON Users.id = passwords.id "
                    "INNER JOIN fullnames ON Users.id = fullnames.id "
                    "INNER JOIN emails ON Users.id = emails.id "
                    "INNER JOIN cities ON Users.id = cities.id "
                    "WHERE Users.id = (?)", (id[0],))
    result = cursor_db.fetchone()
    con.close()
    if feature == "username":
        return result[0]
    elif feature == "password":
        return result[1]
    elif feature == "fullname":
        return result[2]
    elif feature == "email":
        return result[3]
    elif feature == "city":
        return result[4]
    else:
        return "Error"