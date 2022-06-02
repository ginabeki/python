# zip(), 
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5,4,3]
def multpily_by2(item):
    return item*2
# filter
def only_odd(item):
    return item % 2 != 0 # odd
# zip

print(list(zip(my_list, your_list, their_list))) # [(1,10,5) (2,20,4). (3,30,3)]
print(my_list) # [1,2,3]