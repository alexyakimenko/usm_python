import functions as f

mood = input("How is your day?\n").lower()
if(mood == "good"):
    print("WOW! its awesome")
elif(mood == "fine"):
    print("Not bad")
else:
    print("Why isn't it good?")


val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
val_map = {}

for item in val_list:
    count = val_map.get(item)
    val_map.update({item: count+1 if count else 1})

print(val_map)

doubled = map(lambda item: item*2, val_list)

print(list(doubled))

shopping_list = []

f.process_menu()
