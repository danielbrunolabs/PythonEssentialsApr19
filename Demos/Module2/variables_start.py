#
# Demo file for variables
#

# Declare a variable and initialize it
person_name = 'Ben Heard'
person_address = '8628 Windjammer'
print(f'{person_name} lives at {person_address}')

# Inspect the data type
print(type(person_name))

# re-declaring the variable works
person_name = 1
print(person_name)
print(type(person_name))
print(f'{person_name} lives at {person_address}')
print(str(person_name) + " lives at " + person_address)

# ERROR: variables of different types cannot be combined
#print("this is a string" + 123)

# But this works: variables of different types cannot be combined


# Global vs. local variables in functions

# delete definition of variable previously declared

# data type casting

# comparing float numbers
