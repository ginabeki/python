# lambda expressions, are one time anonymous functions that you dont need more that once
# 

from functools import reduce 
my_list = [1, 2, 3]
lambda param: action(param)
# filter
def only_odd(item):
    return item % 2 != 0 # odd
def accumulator(acc, item):
    return acc + item

print(list(map(lambda item: item*2, my_list))) # 2, 4, 6
print(my_list) # [1,2,3]

exercise
create a lambda expression that is going to square our list

from hashlib import new
from itertools import count
import math


my_list = [5,4,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list) # [25, 16, 9]

# list sorting

a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
# def sortList(x):
#     return x[1]

# a = [(0,2), (4,3), (9,9), (10, -1)]
# a.sort(key = sortList)
# print(a[1])
