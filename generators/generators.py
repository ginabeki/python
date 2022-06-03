# generators allow us to generate a sequence of values over time.
# allows us to use special type of keyword
from unittest import result

# interable
# range(100)
# iterable is an object we can loop through
# generators are iterable



def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g)) # 4

# generators performance
def gen_func(num):
    for i in range(num):
        yield i
for item in gen_func(100)

# generators under the hood

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break
special_for([1,2,3])

# range function
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration
gen = MyGen(0,100)
for i in gen:
    print(i) # 0 -99


# exercise: Fibonacci numbers
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
for x in fib(20)
print(x)
