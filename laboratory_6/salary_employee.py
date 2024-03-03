from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, name = "", phone = "", birth_day = "", email = "", position = "", salary = 0):
        super().__init__(name, phone, birth_day, email, position)
        self.__salary = salary

    @property
    def salary(self):
        """The salary property."""
        return self.__salary
    @salary.setter
    def salary(self, value):
        self.__salary = value

    def input_data(self):
        super().input_data()
        while not self.salary:
            try:
                self.salary = int(input("Месячная зарплата работника: "))
            except Exception as e:
                print(e)    

    def _calculate_salary(self):
        return self.salary
