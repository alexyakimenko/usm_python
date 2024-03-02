import re

should_close = False

def stop_program():
    global should_close
    should_close = True

    print("\nBye!")

def input_data():
    while True:
        try:
            last_name = input("Фамилия работяги: ").strip()
            if not re.match("^[A-zА-я-]{2,20}$", last_name):
                raise ValueError("ValueError: Фамилия должна быть в пределах 2-20 знаков и не содержать символов кроме -")

            first_name = input("Имя работяги: ").strip()  
            if not re.match("^[A-zА-я-]{2,20}$", first_name):
                raise ValueError("ValueError: Имя должно быть в пределах 2-20 знаков и не содержать символов кроме -")

            department = input("Где работает работяга?: ").strip()
            if not re.match("([A-zА-я0-9]+\s?)*$", department):
                raise ValueError("ValueError: Можно использовать только буквы, цифры и один пробел")

            children_count = int(input("Сколько у работяги детей?: "))
            if children_count < 0 or children_count > 19:
                raise ValueError("ValueError: Количество детей должно быть в пределах от 0-19")

            break
        except ValueError as e:
            print(e)
            continue
        except KeyboardInterrupt:
            stop_program()
            return

    with open("data.txt", mode = "a", encoding = "utf-8") as data_f:
        data_f.write(f"{last_name}|{first_name}|{department}|{children_count}\n")

def get_employee_data():
    with open("data.txt", mode = "r", encoding = "utf-8") as data_f:
        data_lines = map(
            lambda data_string: data_string[:-1].split('|'),
            data_f.readlines()
        )
    return list(data_lines)

def get_children_data():
    try:
        data_lines = get_employee_data()

        for data in data_lines:
            print(f"{data[0]} {data[1]} with {data[3]} children")
            
        childer_amount = sum(map(lambda data: int(data[3]), data_lines))
        print(f"Total amount of children: {childer_amount}")

    except FileNotFoundError:
        print("Пока что нет файла с данными!")
        return

def get_childless_employee():
    try:
        data_lines = get_employee_data()

        childless = filter(lambda data: int(data[3]) == 0, data_lines)

        for employee in childless:
            print(f"{employee[0]} {employee[1]}") 

    except FileNotFoundError:
        print("Пока что нет файла с данными!")
        return

def serve_menu():
    menu_options = [
        "Ввод данных в файл",
        "Просмотр данных о детях сотрудников",
        "Поиск и вывод списка бездетных сотрудников",
        "Выход из программы"
    ]

    for index, item in enumerate(menu_options):
        print(f"{index+1}: {item}")

    try:
        choice = int(input())
    except ValueError as e:
        print("Неправильный ввод!")
        return
    except KeyboardInterrupt:
        stop_program() 
        return 

    { # process choice
        1: input_data,
        2: get_children_data,
        3: get_childless_employee,
        4: stop_program
    }.get(
        choice,
        # default behavior
        lambda: print("Нет такого варианта!")
    )()

while not should_close:
    serve_menu()
