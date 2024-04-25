import json
import re

employees = []
filename = "employees.json"

try:
    with open(filename, 'r') as file:
        employees = json.loads(file.read())
except FileNotFoundError:
    pass

def input_data():
    last_name = ""
    first_name = ""
    department = ""
    salary = 0

    while True:
        try:
            last_name = input("Фамилия сотрудника: ").strip()
            if not re.match('[а-яА-Яa-zA-Z-]+$', last_name):
                raise ValueError("Фамилия должна состоять только из букв")

            first_name = input("Имя сотрудника: ").strip()
            if not re.match('[а-яА-Яa-zA-Z-]+$', first_name):
                raise ValueError("Имя должна состоять только из букв")

            department = input("Департамент сотрудника: ").strip()
            if not re.match('^[а-яА-Яa-zA-Z]+(?: [а-яА-Яa-zA-Z]+)*$', department):
                raise ValueError("Департамет должен состоять из букв и одного пробела в качестве разделителя")

            salary = float(input("Зарплата сотрудника: "))
            if not 1000.0 <= salary <= 77000.0:
                raise ValueError("Зарплата это вещественное чило из интервала 1000.00 – 77000.00")
            break
        except Exception as e:
            print(e)
            pass
    
    employees.append({
        "last_name": last_name,
        "first_name": first_name,
        "department": department,
        "salary": salary
    })

    save_data()

def save_data():
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(employees, file, ensure_ascii=False)

def get_avg_salary():
    if not len(employees):
        print("Theres no employees")
        return
    salaries = list(map(lambda dict: dict['salary'], employees))
    avg_salary = sum(salaries) / len(salaries)
    print(avg_salary)

def get_avg_dep_salary():
    if not len(employees):
        print("Theres no employees")
        return
    dep_salary = {}
    for employee in employees:
        department = employee["department"]
        if department in dep_salary:
            dep_salary[department]['sum'] += employee['salary']
            dep_salary[department]['count'] += 1
        else:
            dep_salary[department] = {
                "sum": employee['salary'],
                "count": 1
            }
    for dep in dep_salary:
        avg_sal = dep_salary[dep]['sum'] / dep_salary[dep]['count']
        print(f'{dep}: {avg_sal}')

def get_highest_salary_employee():
    if not len(employees):
        print("Theres no employees")
        return
    highest = max(employees, key=lambda dict: dict['salary'])
    display_employee(highest)

def get_lowest_salary_employee():
    if not len(employees):
        print("Theres no employees")
        return
    lowest = min(employees, key=lambda dict: dict['salary'])
    display_employee(lowest)

def display_employee(employee):
    print(employee["last_name"],employee["first_name"])
    print(f"\tDepartment: {employee['department']}")
    print(f"\tSalary: {employee['salary']}")

def get_options():
    return {
        1: {
            "description": "Записать данные о зарплатах сотрудников",
            "handler": input_data
        },
        2: {
            "description": "Вывести среднюю зарплату сотрудников",
            "handler": get_avg_salary
        },
        3: {
            "description": "Вывести данные сотрудника с самой высокой зарплатой",
            "handler": get_highest_salary_employee
        },
        4: {
            "description": "Вывести данные сотрудника с наименьшей зарплатой",
            "handler": get_lowest_salary_employee
        },
        5: {
            "description": "Вывести ссреднюю зарплату по каждому департаменту ",
            "handler": get_avg_dep_salary
        },
    }