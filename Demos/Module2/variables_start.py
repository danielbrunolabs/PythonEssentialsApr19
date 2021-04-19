#
# Demo file for variables
#

# # Declare a variable and initialize it
# person_name = 'John Smith'
# person_address = '101 Main Street'
# print(f'{person_name} lives at {person_address}')

# # Inspect the data type
# print(type(person_name))

# # re-declaring the variable works
# person_name = 1
# print(person_name)
# print(type(person_name))
# print(f'{person_name} lives at {person_address}')
# print(str(person_name) + " lives at " + person_address)

# # String literals
# print('John says: "How are you?"')
# print('''John says: "That is Jenny's car".''')

# # delete definition of variable previously declared
# del(person_name)
# print(person_name)

# # data type casting
# item_price = '12.10'
# stock_price = 12.15

# result = 25 / 5 
# type(result)
# print(result)

# print(item_price * 2)

# type(item_price)
# type(stock_price)

# greeting = 'Hello world'
# print(greeting.upper())
# print(greeting.isnumeric())
# print(len(greeting))

full_name = input('Please enter Name:')

print(f'You entered: {full_name}')

age = input('Please enter age:')
print(type(int(age)))

print(f'{full_name} is {age} years old')
