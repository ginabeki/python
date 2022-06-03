# @classmethod
# @staticmethod
# decorators use @ sign
# decorators supercharge our function by adding extra features

# Higher Order Functions (HOC)
# can be a function that accepts inside its parameter other functions, example
def greet(func):
    func()

# 2
def greet2():
    def func():
        return 5
    return func

# decorator 2
# a function that modifies a function and enhances it

def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('hellooo')
hello()

# decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
hello('hiiii')

# why decorators are useful?

from cgitb import reset
from time import time
from unittest import result
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it toook {t2-t1} ms")
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5
long_time()