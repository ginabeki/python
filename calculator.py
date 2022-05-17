operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus
''')
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

# Addition
if operation =='+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

# Substraction
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

# Division
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

# Multiplication
elif operation == '*':
    print('{} * {} '.format(number_1, number_2))
    print(number_1 * number_2)

# Modulus
elif operation == '%':
    print('{} % {} '.format(number_1, number_2))
    print(number_1 % number_2)

else:
    print('Invalid operator!')





