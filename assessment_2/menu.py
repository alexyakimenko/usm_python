import os

should_close = False # lifecycle variable

# cross-platform clear console function
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def close_menu():
    global should_close

    should_close = True
    print("Пока!!!")

# close option dictionary
_close_option = {
    "description": "Выйти из программы",
    "handler": close_menu
}

def draw_menu(options = {}):
    # append close option to menu
    options.update({
        len(options) + 1: _close_option
    })

    # display all the options
    for n, option in options.items():
        print(f"{n}: {option.get('description')}")

    try: # validate user input
        choice = int(input("Твой выбор?\n")) 
        # get requested option and run handler function
        clear()
        options.get(choice, {}).get("handler", lambda: print("Нет такого варианта!!!"))()
    except ValueError as ve: # not integer as input
        print("Можно писать только цифры!!!")
        return 
    except KeyboardInterrupt as ki: # Ctrl + C
        close_menu()
        return 
    except Exception as e: # anything else
        print(e)
        return
    finally:
        # pause before next action
        if not should_close: 
            input("Нажмите Enter...")
            clear()

