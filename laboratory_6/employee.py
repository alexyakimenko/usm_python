import re
import math
from datetime import date, timedelta

class Employee:
    def __init__(self, name = "", phone = "", birth_day = "", email = "", position = ""):
        self.__name = name 
        self.__phone = phone 
        self.__birth_day = birth_day
        self.__email = email 
        self.__position = position 

    @property
    def name(self):
        """The name property"""
        return self.__name 
    @name.setter
    def name(self, value):
        if not re.match("^[A-zА-я]+$", value):
            raise ValueError("Имя должно состоять только из букв") 
        self.__name = value

    @property
    def phone(self):
        """The phone property."""
        return self.__phone
    @phone.setter
    def phone(self, value):
        if not re.match("^\+373[0-9]{8}$", value):
            raise ValueError("Неправильнный формат номера: +373########") 
        self.__phone = value

    @property
    def birth_day(self):
        """The birth_day property."""
        return self.__birth_day
    @birth_day.setter
    def birth_day(self, value):
        date_list = list(map(lambda el: int(el), value.split('.')))
        date_list.reverse()

        self.__birth_day = date(*date_list)

    @property
    def email(self):
        """The email property."""
        return self.__email
    @email.setter
    def email(self, value):
        if not re.match("^[a-zA-Z0-9._-]{2,20}@[a-zA-Z0-9.-]{2,20}\.[a-zA-Z]{2,4}$", value):
            raise ValueError("Неправильный формат почты!")
        self.__email = value
    
    def get_position(self):
        """The get_position property."""
        return self.__position
    def set_position(self, value):
        if not re.match("^[A-zА-я]{4,20}$", value):
            raise ValueError("Можно использовать только буквы (4-20)") 
        self.__position = value

    position = property(get_position, set_position)

    def calculate_age(self):
        if not self.birth_day:
            print("Дата рождения не указана!")
            return
        timedelta = date.today() - self.birth_day
        return math.floor(timedelta.days / 365)

    def _calculate_salary(self):
        pass
    
    def input_data(self):
        while not self.name:
            try:
                self.name = input("Имя работника: ").strip()
            except Exception as e:
                print(e)    

        while not self.phone:
            try:
                self.phone = input("Телефон работника: ")
            except Exception as e:
                print(e)    

        while not self.birth_day:
            try:
                self.birth_day = input("Дата рождения работника (dd.mm.yyyy): ")
            except Exception as e:
                print(e)    

        while not self.email:
            try:
                self.email = input("Почта работника: ")
            except Exception as e:
                print(e)    

        while not self.position:
            try:
                self.position = input("Позиция работника: ")
            except Exception as e:
                print(e)    
