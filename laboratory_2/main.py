
# List

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(arr[0]) # 1th element

print(arr[2]) # 3rd element

arr[3] = 5

print(arr[2:8]) # from 3rd element to 8th included

arr.sort()

print(arr)

# arr.append(0)
arr.extend([0])
print(arr)
print(len(arr)) # list length
print(max(arr)) # max element
print(min(arr)) # min element
print(sorted(arr)) # sort list

arr.clear()

print(arr)


# Tupple

turtle = (0, 1, 3, 5)

print(turtle)
print(type(turtle))
print(turtle[0], turtle[3])
print(turtle[0:3])

print(max(turtle))
print(min(turtle))
print(sum(turtle))

# Set

numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
letters = set("lorem ipsum dolor sit amet")
print(letters)

letters.remove(' ')
print(letters)

print(letters.union(numbers))

print(len(letters))

# Dict

str_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}

num_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

print(str_dict.get('one'))
print(str_dict['five'])

print(num_dict.get(1))
# Peak usage
print(num_dict.get(str_dict.get(num_dict.get(str_dict.get('one')))))

str_dict.update({'six': 6})
print(str_dict)

num_dict.update({6: 'six'})
print(num_dict)

print(str_dict.keys())
print(num_dict.values())

print(len(str_dict))

str_dict.clear()
num_dict.clear()

user = dict(username = 'Sergey', password = 'arrrrrrrrmeow')
print(user)

# f 
set_from_tupple = set(turtle)
print(set_from_tupple)

# Task 2

prices = [1, 2, 3]
products = ['milk', 'silk', 'ink']

for i in range(len(products)):
    print("{}: {}".format(products[i], prices[i]))


age = int(input("Lemme know your age: \n"))
print("Через 5 лет тебе будет " + str(age + 5))

if('milk' in products):
    print('There is a milk')
    if('bread' not in products):
        print('But there is no bread')


























