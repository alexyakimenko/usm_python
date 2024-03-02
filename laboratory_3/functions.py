def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    try:
        shopping_list.remove(item)
    except Exception as e:
        print(e)

def show_list():
    for item in shopping_list:
        print(item.capitalize())

def show_menu():
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в списке")
    print("3. Удалить товар из списка (по названию)")
    print("4. Выход")

def process_menu():
    choice = 0
    while(choice != 4):
        show_menu()

        try:
            choice = int(input("Ваш выбор: "))
        except Exception as e:
            print("Ошибка вводa!")
            continue

        if(choice == 1):
            print("{")
            show_list()
            print("}")
        elif(choice == 2):
            item = input("Название товара: ").lower()
            add_item(item)
        elif(choice == 3):
            item = input("Название товара (для удаления):\n").lower()
            remove_item(item)

