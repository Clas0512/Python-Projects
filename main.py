import check_database, init_table, update_tables
import subprocess as shell
import random
import array
import sqlite3 as sql

def p_admin_menu():
    print("-------*- Admin Menu  -*-------")
    print("0. Change Admin Password")
    print("1. Username Query")
    print("2. Password Query")
    print("3. Full-Name Query")
    print("4. Email Query")
    print("5. City Query")
    print("6. Exit")

def utils_menu():
    print("-------*-  Change Menu  -*-------")
    print("0. Change Password")
    print("1. Change Full-Name")
    print("2. Change Email")
    print("3. Change City")
    print("4. Back to Main Menu")

def utils2_menu():
    print("0. Get your account info:")
    print("1. Change your account info:")
    print("2. Exit")


def user_menu(username):
    shell.call("clear", shell=True)
    while True:
        print(f"  ~~~~ {username}'s account ~~~~  \n")
        utils2_menu()
        choice = input("Choose (0-2): ")
        if choice == "0":
            check_database.user_info(username)
        elif choice == "1":
            utils_menu()
            choice = input("Choose (0-4): ")
            if choice == "0":
                password = input("Enter new password: ")
                if check_database.user_info_specified(username, "password") == password:
                    print("This password is already your password!")
                    continue
                while len(password) < 4:
                    print("Password must be at least 4 characters long!")
                    password = input("Enter new password: ")
                while password == check_database.is_same(password, "passwords", "password"):
                    print("Password must be different from the previous one!")
                    password = input("Enter new password: ")
                update_tables.change_password(username, password)
            elif choice == "1":
                fullname = input("Enter new full-name: ")
                if check_database.user_info_specified(username, "fullname") == fullname:
                    print("This full-name is already your full-name!")
                    continue
                while check_database.is_same(fullname, "fullnames", "fullname") == 1:
                    print("This Full-name is already taken.")
                    fullname = input("Full-name: ")
                update_tables.change_fullname(username, fullname)
            elif choice == "2":
                email = input("Enter new email: ")
                if check_database.user_info_specified(username, "email") == email:
                    print("This email is already your email!")
                    continue
                while "@" not in email or check_database.is_same(email, "emails", "email") == 1:
                    print("Invalid email!")
                    email = input("Enter new email: ")
                update_tables.change_email(username, email)
            elif choice == "3":
                city = input("Enter new city: ")
                if (check_database.user_info_specified(username, "city")) == city:
                    print("This city is already your city!")
                    continue
                update_tables.change_city(username, city)
            elif choice == "4":
                continue
        elif choice == "2":
            print("Exiting...")
            exit()
        else:
            print("Please try again!")

def admin_menu():
    shell.call("clear", shell=True)
    while True:
        p_admin_menu()
        choice = input("Choose (0-6): ")

        if choice == "0":
            password = input("Enter new password: ")
            while len(password) < 4:
                print("Password must be at least 4 characters long!")
                password = input("Enter new password: ")
            update_tables.change_password("admin", password)
            print("Password changed successfully!")
        if choice == "1":
            check_database.query("Users")
        elif choice == "2":
            check_database.query("passwords")
        elif choice == "3":
            check_database.query("fullnames")
        elif choice == "4":
            check_database.query("emails")
        elif choice == "5":
            check_database.query("cities")
        elif choice == "6":
            print("Exiting...")
            exit()
        else:
            print("Please try again!")

def random_password(len):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(len - 4):
        temp_pass += random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password += x

    print("Your own safe password is " + password)
    return password

def error_integer(b):
    try:
        type(b) is int
    except: 
        print("Your answer must be ")

def cleandb(username):
    if username == "cleandb":
        shell.call("rm -rf database.db", shell=True)
        shell.call("make", shell=True)
        return 1
    return 0


def generate_password(answer):
    try:
        assert answer in ["yes", "no"]

        if answer.lower() == "no":
            password = input("We are sorry for you not choosing us.\nPlease enter your unique password: ")
            while len(password) <= 4:
                password = input("Password must be more than 4 characters.\nPlease enter your unique password: ")
        elif answer.lower() == "yes":
            MAX_LEN = input("Please enter the password's length: ")

            try:
                MAX_LEN = int(MAX_LEN)
                while MAX_LEN <= 4:
                    MAX_LEN = int(input("Password must be more than 4 characters.\nPlease enter the password's length: "))
            except:
                MAX_LEN = int(input("The length must be an integer.\nPlease enter the password's length: "))
            password = random_password(MAX_LEN)
    except:
        print("You must type either 'yes' or 'no'. Please try again.")
    return password


def login():
    while True:
        selection = input("Hello, do you have an account? (y/n): ")
        if selection == "n":
            username = input("What's your username? ")
            i = 0
            while check_database.is_same(username, "Users", "username") == 1:
                if i == 2:
                    print("You have reached the maximum number of tries. Exiting...")
                    exit()
                print("This username is already taken.")
                username = input("What's your username? ")
                i += 1
            if cleandb(username) == 1:
                exit()
            while len(username) < 4:
                print("Your username must be at least 4 characters long.")
                username = input("What's your username? ")
                if cleandb(username) == 1:
                    exit()
            password = generate_password(input("Do you want us to generate a password for you? (yes/no): "))
        elif selection == "y":
            username = input("What's your username? ")
            if cleandb(username) == 1:
                exit()
            if check_database.is_same(username, "Users", "username") == 0:
                print("You don't have an account. Please try again.")
                continue
            else :
                password = input("What's your password? ")
                if check_database.password_query(username, password) == 1:
                    print("Welcome back, " + username)
                    if (username == "admin"):
                        admin_menu()
                    else :
                        user_menu(username)
                else :
                    i = 0
                    while i < 3:
                        if i == 2:
                            print("You have entered wrong password 3 times. Please try again later.")
                            exit()
                        password = input("Wrong password. Please try again: ")
                        if check_database.password_query(username, password) == 1:
                            print("Welcome back, " + username)
                            if (username == "admin"):
                                admin_menu()
                            else :
                                user_menu(username)
        else :
            print("Please try again.")
            continue

        init_table.add_list(username, password)
        print("Now, you must set your Full-name, email and city:")
        fullname = input("Full-name: ")
        while check_database.is_same(fullname, "fullnames", "fullname") == 1:
            print("This Full-name is already taken.")
            fullname = input("Full-name: ")
        email = input("Email: ")
        while "@" not in email or check_database.is_same(email, "emails", "email") == 1:
                    print("Invalid email!")
                    email = input("Enter new email: ")
        city = input("City: ")
        init_table.set_tables(fullname, email, city)
        print("Your username is: " + username)
        print("Your password is: " + password)
        print("Your Full-name is: " + fullname)
        print("Your email is: " + email)
        print("Your city is: " + city)
        print("Your information has been saved.")
        print("DON'T FORGET YOUR PASSWORD!")

init_table.create_first_table()
init_table.create_table_password()
init_table.create_table_full_name()
init_table.create_table_email()
init_table.create_table_cities()
init_table.add_admin("1234")
login()