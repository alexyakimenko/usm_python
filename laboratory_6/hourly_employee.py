from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name = "", phone = "", birth_day = "", email = "", position = "", number_of_hours = 0, hourly_pay = 0):
        super().__init__(name, phone, birth_day, email, position)
        self.__number_of_hours = number_of_hours
        self.__hourly_pay = hourly_pay

    @property
    def number_of_hours(self):
        """The number_of_hours property."""
        return self.__number_of_hours
    @number_of_hours.setter
    def number_of_hours(self, value):
        if(value < 0):
            raise ValueError("Количество часов не может быть меньше 0")
        self.__number_of_hours = value

    @property
    def hourly_pay(self):
        """The hourly_pay property."""
        return self.__hourly_pay
    @hourly_pay.setter
    def hourly_pay(self, value):
        self.__hourly_pay = value

    def _calculate_salary(self):
        return self.number_of_hours * self.hourly_pay

    def input_data(self):
        super().input_data()
        while not self.number_of_hours:
            try:
                self.number_of_hours = int(input("Количество часов работника: "))
            except Exception as e:
                print(e)    
        
        while not self.hourly_pay:
            try:
                self.hourly_pay = int(input("Почасовая зарплата работника: "))
            except Exception as e:
                print(e)    
