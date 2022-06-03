# error handling in python
# syntax error
from unicodedata import name


def hooooo()
    pass

# Name error
def hooooo():
    1 + name
hooooo()
#key error

# how to avoid errors? use try, except block
# error handling

while True:
    try:
        age = int(input('what is your age'))
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break

# error handling 2
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers')
print(sum(1, 2))

# error handling 3
