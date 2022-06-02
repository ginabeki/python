# reduce(), 
# from functools import reduce
# functools, is a tool box for tools that come with py installation
# 
from functools import reduce 
my_list = [1, 2, 3]
def multpily_by2(item):
    return item*2
# filter
def only_odd(item):
    return item % 2 != 0 # odd
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 0)) #01, 12, 33, 6
print(my_list) # [1,2,3]