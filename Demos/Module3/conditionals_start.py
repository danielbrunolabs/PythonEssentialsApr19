#
# Example file conditional statements
#

def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if( x < y):
        st = 'x is less than y'
    elif(x > y):
        st = 'x is greater than y'
    else:
        st = 'x is the same as y'
    
    print(st)

    # conditional statements let you use "a if C else b"
    st = 'x is less than y' if (x < y) else "x is greater or the same as y"

    print(st)

    # conditional logic with IN operator
    city = "Raleigh"
    if city in ('Raleigh', 'Charlotte', 'Asheville'):
        print('You live in North Carolina')
    else:
        print('You live somewhere else.')

    if 1.1 + 2.2 == 3.3:
        print('1.1 + 2.2 == 3.3')
    else:
        print('1.1 + 2.2 != 3.3')

    tolerance = 0.00001

    if abs((1.1 + 2.2) - 3.3) < tolerance:
        print('1.1 + 2.2 == 3.3')
    else:
        print('1.1 + 2.2 != 3.3')
    


if __name__ == "__main__":
    main()