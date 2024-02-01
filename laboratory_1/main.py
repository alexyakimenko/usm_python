print("Welcome, traveler")
name = input("Tell me your name: \n") # User Input
print("Nice to meet you, " + name)

age = 19
average_score = 5.5
short_string = "Lorem ipsum dolor sit amet"
long_string = """
Netus id sollicitudin. Pulvinar tincidunt curabitur pretium. Placerat eu fringilla nam sem, ultricies habitant ridiculus malesuada etiam nulla.

Non, vehicula taciti aliquet. Porta nec, luctus dictumst primis.

Sodales senectus ultrices eros egestas dictumst potenti leo natoque elementum Ac mus nunc.
"""

print(type(average_score))
print(type(long_string))

print(len(short_string))

upper_string = short_string.upper() # String to Upper Case
print(upper_string)

print(long_string[93:111]) # String slice 
