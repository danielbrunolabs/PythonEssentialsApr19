def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = 0
        print("Cannot divide by zero.")
    finally:
        return result


operation = input("Please enter operation:")
first_number = input("Please enter first number:")
second_number = input("Please enter second number:")

first_number = float(first_number)
second_number = float(second_number)

if operation.upper() == 'ADD':
    result = add(first_number, second_number)
elif operation.upper() == 'SUB':
    result = sub(first_number, second_number)
elif operation.upper() == 'MUL':
    result = mul(first_number, second_number)
elif operation.upper() == 'DIV':
    result = div(first_number, second_number)
else:
    result = 0
    print(f'Unknown Operation: {operation}')

print(f"Result: {result}")