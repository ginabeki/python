# map(), filter(), zip(), reduce()
# map(), allows us to simplify code
my_list = [1, 2, 3]
def multpily_by2(item):
    return item*2

print(list(map(multpily_by2, my_list))) #[2,4,6]
print(my_list) # [1,2,3]