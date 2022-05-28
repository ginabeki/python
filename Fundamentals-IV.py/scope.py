# scope - what variables do I have access to?
# functional scope means that when we create a function 

from re import A


if True:
    x = 10

def some_func():
    total = 100
print(x) # 10


# scope rules

a = 1
def confusion():
    a = 5
    return a
print(a) # 1
print(confusion()) # 5
# 1 - start with local

# 2 - look for a parent local scope?
a = 1
def parent():
    a = 10
    def confusion():
        return a
    return confusion()
print(parent()) #10
print(a) # 1
# 3 - Global
# 4 - built in python functions.
a = 1
def parent():
    def confusion():
        return confusion()
print(parent())
print(a)

# global keyword

total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total)))) #3

# nonlocal scope, used to refer to parent local
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x) # inner: nonlocal
    inner()
    print('outer:', x) # outer: nonlocal
outer()

# why do we need scope
# machines dont have infinity memory, power. They have limited resources
# scope is a great demonstration of this. When a function is run a memory is created in our system
# 
