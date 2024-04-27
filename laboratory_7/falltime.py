import math

G = 9.8

def get_fall_time(height):
    return math.sqrt(2 * height / G)

def run():
    try:
        height = float(input().strip())
        
        if math.isnan(height):
            raise ValueError
        
        print(f'Время падения: {get_fall_time(height):.3}')  
    except Exception as e:
        print("height mush be a number")