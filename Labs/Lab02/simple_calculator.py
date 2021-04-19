# Instructions
print('''This short program computes the circumference of a circle
from a provided raduis.  Provide the radius as a floating
point value.\n''')

# Prompt user for circumference
radius = input('Enter a radius: ')

# Assume correct type
circ = 2 * 3.14159 * float(radius);

# Provide output
print(f'The circumference of a circle with radius {radius} is {circ}')
