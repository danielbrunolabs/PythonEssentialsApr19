#
# Error handling
#

 
x = 42
y = '2'

# Division
try:
    result = x / y
except ZeroDivisionError:
    result = 0
    print('y cannot be zero')
except TypeError as e:
    result = float(x) / float(y)
    print('Automatically casted string to float')
except:
    result = '0'
    print('Something went wrong!')
finally:
    print(f'Result: {result}')
