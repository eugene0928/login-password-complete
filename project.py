 
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

