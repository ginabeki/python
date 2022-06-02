# filter(), filters things for us
my_list = [1, 2, 3]
def multpily_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0 # odd

print(list(filter(only_odd, my_list))) #[1, 3]
print(my_list) # [1,2,3]