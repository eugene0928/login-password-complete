import os
import platform
import sys
import time

import mysql.connector


class User:
    def __init__(self):
        self.name = None
        self.login = None
        self.password = None
        self.age = None
        self.min_age = 10
        self.max_age = 150

        self.entering_system()

    @staticmethod
    def init_message():
        print("""             Welcome
        Register    [1]
        Log in      [2]""")

    def entering_system(self):
        self.clear()
        self.init_message()

        init_input = input("Enter your option: ").strip()
        option = ['1', '2']
        while init_input not in option or not init_input.isnumeric():
            self.clear()
            print("Invalid input. Please, try again and enter only options below: ")
            print(option)
            init_input = input("Enter your option: ").strip()

        self.register() if init_input == "1" else self.log_in()

    def register(self):
        self.clear()
        print("Welcome registering part")
        name = input("Enter your name: ").strip().capitalize()
        while not name.isalpha():
            self.clear()
            print("Invalid input. Try again")
            name = input("Enter your name: ").strip().capitalize()

        login = input("Enter your login: ").strip()
        while not login.isalnum() or self.is_login_exists(login):
            self.clear()
            print("Invalid input or exist login. Try again")
            login = input("Enter your login: ").strip()

        password = input("Enter your password(more than 5 characters): ")
        confirm_pass = input("Confirm your password: ")

        while len(password) == 0 or password != confirm_pass or len(password) < 5:
            self.clear()
            print("Invalid password or your password didn't match. Try again")
            password = input("Enter your password(more than 5 characters): ")
            confirm_pass = input("Confirm your password: ")

        age = input("Enter your age: ").strip()
        while not age.isnumeric():
            print("Please, enter only numbers")
            age = input("Enter your age: ").strip()

        age = int(age)
        while age < self.min_age or age > self.max_age:
            self.clear()
            print(f"Invalid age. To enter this website your age must be between {self.min_age}-{self.max_age} ages!")
            age = input("Enter your age: ").strip()
            age = int(age)

        self.name = name
        self.login = login
        self.password = password
        self.age = age
        my_data = self.database()
        my_cursor = my_data.cursor()
        my_cursor.execute(f"insert into login_info values('{self.name}', '{self.login}', '{self.password}', '{self.age}');")
        my_data.commit()
        print("You have entered the system!")

    def is_login_exists(self, login1):
        my_data = self.database()
        my_cursor = my_data.cursor()
        my_cursor.execute(f"select login from login_info where login='{login1}';")
        result = my_cursor.fetchall()

        if len(result) == 0:
            return False
        elif result[0][0] == login1:
            return True

    @staticmethod
    def database():
        my_data = mysql.connector.connect(
            host='localhost',
            user="eugene09",
            password="12345678",
            database="login"
        )
        return my_data

    def log_in(self):
        self.clear()
        input_login = input("Enter your login: ").strip()
        while not self.is_login_exists(input_login):
            self.clear()
            print("The login didn't match. Try again")
            input_login = input("Enter your login: ").strip()

        self.login = input_login

        input_password = input("Enter your password: ")
        while not self.is_password_correct(self.login, input_password):
            self.clear()
            print("Wrong password. Please, try again")
            input_password = input("Enter your password: ")

        self.clear()
        print("You've entered the system")

        print("""        Update account          [1]
        Delete account          [2]
        Exit                    [3]""")

        choice = input("Your choice: ").strip()
        options = ['1', '2', '3']
        while choice not in options:
            self.clear()
            print("Invalid input. Try again")
            choice = input("Your choice: ").strip()

        if choice == "1":
            self.update_account()
        elif choice == "2":
            self.delete_account()
        else:
            self.__init__()


    def update_account(self):
        self.clear()
        print("""What do you want to change?
        Login       [1]
        Password    [2]
        Username    [3]
        Age         [4]
        Exit        [0]""")

        option = input("Enter your option: ").strip()
        options = ['0','1', '2', '3', '4']
        while option not in options:
            self.clear()
            print("Invalid input. Try again")
            print(f"Options: {options}")
            option = input("Enter your option: ").strip()

        if option == '1':
            self.change_login()
        elif option == '2':
            self.change_password()
        elif option == '3':
            self.change_username()
        elif option == '4':
            self.change_age()
        else:
            sys.exit()

    def change_login(self):
        self.clear()
        login1 = input("Enter your login: ").strip()
        while login1 != self.login:
            self.clear()
            print("Your login didn't match. Try again")
            login1 = input("Enter your login: ").strip()

        new_login = input("Enter your new login: ").strip()
        while self.is_login_exists(new_login) or not new_login.isalnum():
            self.clear()
            print("This login exists or invalid login")
            new_login = input("Enter your new login: ").strip()

        check = input(f"Are you sure to change your login to {new_login}? [y/n]: ").strip().lower()
        options = ['y', 'yes', 'n', 'no']
        while check not in options:
            self.clear()
            print("Invalid input. Please, try again")
            check = input(f"Are you sure to change your login to '{new_login}'? [y/n]: ").strip().lower()

        if check in options[:2]:
            my_data = self.database()
            my_cursor = my_data.cursor()
            my_cursor.execute(f"update login_info set login='{new_login}' where login='{self.login}'")
            my_data.commit()
            print("Your login is changed")
        else:
            self.update_account()

    def change_password(self):
        self.clear()
        login1 = input("Enter your login: ").strip()
        while login1 != self.login:
            self.clear()
            print("Your login didn't match. Try again")
            login1 = input("Enter your login: ").strip()

        old_password = input("Enter your previous password: ")
        while not self.is_password_correct(login1, old_password):
            self.clear()
            print("Password didn't match. Try again")
            old_password = input("Enter your previous password: ")

        new_password = input("Enter your new password(more than 5 characters): ")
        while len(new_password) < 5:
            self.clear()
            print("Please, enter more than 5 characters")
            new_password = input("Enter your new password: ")

        check = self.check()
        options = ['y', 'yes', 'n', 'no']

        if check in options[:2]:
            my_data = self.database()
            my_cursor = my_data.cursor()
            my_cursor.execute(f"update login_info set password='{new_password}' where login='{login1}'")
            my_data.commit()
            print("Your password is changed")
        else:
            self.update_account()

    def change_username(self):
        self.clear()
        login1 = input("Enter your login: ").strip()
        while login1 != self.login:
            self.clear()
            print("Your login didn't match. Try again")
            login1 = input("Enter your login: ").strip()

        password = input("Enter your password: ")
        while not self.is_password_correct(login1, password):
            self.clear()
            print("Password didn't match. Try again")
            password = input("Enter your password: ")

        username = input("Enter your new username: ").strip().capitalize()
        while not username.isalpha():
            print("Invalid username. Try again")
            username = input("Enter your new username: ").strip().capitalize()

        check = self.check()
        options = ['y', 'yes', 'n', 'no']
        if check in options[:2]:
            my_data = self.database()
            my_cursor = my_data.cursor()
            my_cursor.execute(f"update login_info set name='{username}' where login='{login1}'")
            my_data.commit()
            print("Your password is changed")
        else:
            self.update_account()

    def change_age(self):
        self.clear()
        login1 = input("Enter your login: ").strip()
        while login1 != self.login:
            self.clear()
            print("Your login didn't match. Try again")
            login1 = input("Enter your login: ").strip()

        password = input("Enter your password: ")
        while not self.is_password_correct(login1, password):
            self.clear()
            print("Password didn't match. Try again")
            password = input("Enter your password: ")

        new_age = input("Enter your age: ").strip()
        while not new_age.isnumeric() or int(new_age) < self.min_age or int(new_age) > self.max_age:
            self.clear()
            print("Wrong age. Please, try again")
            new_age = input("Enter your age: ").strip()

        check = self.check()
        options = ['y', 'yes', 'n', 'no']
        if check in options[:2]:
            my_data = self.database()
            my_cursor = my_data.cursor()
            my_cursor.execute(f"update login_info set age='{int(new_age)}' where login='{login1}'")
            my_data.commit()
            print("Your age is changed")
        else:
            self.update_account()

    def delete_account(self):
        self.clear()
        login1 = input("Enter your login: ").strip()
        while login1 != self.login:
            self.clear()
            print("Your login didn't match. Try again")
            login1 = input("Enter your login: ").strip()

        password = input("Enter your password: ")
        while not self.is_password_correct(login1, password):
            self.clear()
            print("Password didn't match. Try again")
            password = input("Enter your password: ")

        options = ['y', 'yes', 'n', 'no']
        check = self.check()
        if check in options[:2]:
            my_data = self.database()
            my_cursor = my_data.cursor()
            my_cursor.execute(f"delete from login_info where login='{login1}'")
            my_data.commit()
            print("Your account has been deleted")

            time.sleep(2.5)
            self.__init__()
        else:
            self.update_account()

    def check(self):
        check = input(f"Are you sure to change your age? [y/n]: ").strip().lower()
        options = ['y', 'yes', 'n', 'no']
        while check not in options:
            self.clear()
            print("Invalid input. Please, try again")
            check = input(f"Are you sure to change your age? [y/n]: ").strip().lower()

        return check
