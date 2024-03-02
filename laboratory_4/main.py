def lorentz_form(age, height, sex):
    first_factor = 4 if sex == "m" else 2.5
    second_factor = 4 if sex == "m" else 6
    
    return height - 100 - (
        (height - 150) / first_factor + (age - 20) / second_factor
    )


while True:
    global sex
    global age
    global height
    global weight

    try:
        sex = input("What is your sex? (M, W)\n").lower()
        if(sex not in ['m', 'w']):
            raise ValueError("ValueError: Invalid sex")

        age = int(input("Tell me your age (years): "))
        if(age < 0 or age > 150):
            raise ValueError("ValueError: Invalid age")

        height = int(input("Tell me your height (cm): "))
        if(height < 0 or height > 500):
            raise ValueError("ValueError: Invalid height")

        weight = int(input("Tell me your weight (kg): "))
        if(weight < 0 or weight > 700):
            raise ValueError("ValueError: Invalid weight")

        break
    except Exception as e:
        print(e)
        continue

ideal_weight = lorentz_form(age, height, sex)
print(f"Your ideal weight is: {ideal_weight}kg")

if(ideal_weight == weight):
    print("Your weight is perfect")
else:
    print("You should " + ("gain", "lose")[ideal_weight < weight] + "some weight")
