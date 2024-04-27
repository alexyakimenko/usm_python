from datetime import datetime

def get_life_days(date):
    return (datetime.now() - date).days

def run():
    while True:
        try:
            date_input = input("Введите дату рождения (mm.dd.yyyy): ").strip()

            date = datetime.strptime(date_input, "%d.%m.%Y")

            print(f'Прошло дней: {get_life_days(date)}')
            break
        except Exception as e:
            print("Invalid date!")
