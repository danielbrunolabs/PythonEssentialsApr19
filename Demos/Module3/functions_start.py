#
#  Example file for working with functions
#

# name = "John Doe"

# # define a basic function
# def some_function():
#     global name
#     name = 'James Smith'
#     return f'Hello, {name}'

# greeting = some_function()

# print(name)
# print(greeting)


# Lambda functions
def addition(arg1, arg2):
    return arg1 + arg2

print(addition)
print((lambda arg1, arg2: arg1 + arg2))