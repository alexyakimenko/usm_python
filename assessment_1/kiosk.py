products_sold = {}

# initialize
def create_list():
    global products_sold
    products_sold = {}
    print("Добро пожаловать в программу для учета проданных товаров!!!")


# print one object
def print_product(name, info):
    print(f"{name}:")
    print(f"\tPrice: {info.get('price')}")
    print(f"\tSold: {info.get('sold_count')}")

# print all objects
def print_products():
    if not len(products_sold):
        print("Ничего не продано :(")
        return

    print("Products:\n")
    for name, info in products_sold.items():
        print_product(name, info)

def add_product():
    name = input("Название товара? ").lower()

    while True: # until there won't be any problems
        price = input("Цена: ")
        sold_count = input("Всего продано: ")

        # if both are numbers
        if price.isdigit() and sold_count.isdigit():
            price = int(price)
            sold_count = int(sold_count)
            break # end this cycle of hatred
        else:
            print("Цена и Количество должна быть числом!!!")
            continue # continue this endless cycle

    # add new product
    products_sold.update({name: {
        "price": price,
        "sold_count": sold_count
    }})

    # log it
    print("Продукт был добавлен!")
    print_product(name, products_sold.get(name))

def update_product():
    name = input("Название товара? ").lower()

    product = products_sold.get(name) 

    if not product:
        return print("Не существует такого товара!!!")

    print("Нажмите Enter, чтобы не менять свойство")
    price = input(f"Цена ({product.get('price')}): ")
    if not (price.isdigit() and price): # if there is nothing or not number
        price = product.get('price') # change nothing
        print(f"Для цена остается значение по умолчанию: {price}")

    sold_count = input(f"Всего продано ({product.get('sold_count')}): ")
    if not (sold_count.isdigit() and sold_count):
        sold_count = product.get('sold_count') # keep old value
        print(f"Для количества остается значение по умолчанию: {sold_count}")

    # not it is actually update
    products_sold.update({name: {
        "price": int(price),
        "sold_count": int(sold_count)
    }})

    # loooog
    print("Продукт был обновлен!")
    print_product(name, products_sold.get(name))

def remove_product():
    name = input("Название товара? ").lower()

    product = products_sold.get(name) 

    if not product:
        return print("Не существует такого товара!!!")
    
    removed_info = products_sold.pop(name) # returns removed object

    # lg
    print("Продукт был удален из списка!")
    print_product(name, removed_info)

def get_profit():
    # take dictionary items
    # then get total profit from one object
    # create list from this values
    profit_list = list(
        map(
            lambda product: product[1].get('price') * product[1].get('sold_count'),
            products_sold.items()
        )
    )
    # total profit
    result = sum(profit_list)

    # CONSOLE.LOG
    print(result)

def get_options():
    return {
        # Options with actions for Menu
        1: {
            "description": "Создать список проданных товаров за день (сотрет старый)",
            "handler": create_list
        },
        2: {
            "description": "Отображение введенных продуктов, со всеми деталями",
            "handler": print_products 
        },
        3: {
            "description": "Добавить новый продукт в список",
            "handler": add_product 
        },
        4: {
            "description": "Изменить какие-то детали выбранного продукта",
            "handler": update_product 
        },
        5: {
            "description": "Далить какой-то товар по его названию",
            "handler": remove_product 
        },
        6: {
            "description": "Вывод общей стоимости проданных товаров за день",
            "handler": get_profit 
        }
    }