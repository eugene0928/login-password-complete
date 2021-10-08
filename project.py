 
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
