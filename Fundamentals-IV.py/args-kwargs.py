# *args **kwargs

def super_func(*args):
    print(*args) # 1 2 3 4 5
    print(args) #(1,2,3,4,5) tuples
    return sum(args)
super_func(1,2,3,4,5) #15

# kwargs
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1=5, num2=10)) # prints dicitionary

# rule of odering parameters
# params, *args, default parameters, **kwargs