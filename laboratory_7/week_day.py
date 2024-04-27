from datetime import datetime
import calendar

week_day_names = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]

def get_week_day(date):
    return calendar.weekday(date.year, date.month, date.day)    

def run():
    while True:
        try:
            date_input = input("Введите дату (mm.dd.yyyy): ").strip()

            date = datetime.strptime(date_input, "%d.%m.%Y")
            
            day_name = week_day_names[get_week_day(date)]
            
            print(f'День недели: {day_name}')
            break
        except Exception as e:
            print("Invalid date!")