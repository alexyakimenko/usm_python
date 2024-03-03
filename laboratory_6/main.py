from employee import Employee
from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee


empl = Employee()
sal = SalaryEmployee()
hour = HourlyEmployee()

empl.input_data()
sal.input_data()
hour.input_data()

print(empl.calculate_age())
print(sal._calculate_salary())
print(hour._calculate_salary())
