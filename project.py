 
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

            
