# list comprehensions, set comprehensions, dict comprehensions
# Instead of this:
my_set = []

for char in 'hello':
    my_set.append(char)
print(my_set)
# sets
# do this:
my_set = {char for char in 'hello'} #['h','e','l','l','o']
my_list2 = {num for num in range(0,100)}
my_list3 = {num**2 for num in range(0,100)}
my_list4 = {num**2 for num in range(0,100) if num % 2 ==0}

# dict
simple_dict = {
    'a':1,
    'b':2
}
my_dict ={key:value**2 for key, value in simple_dict.items() }
print(my_dict)

# example 2
my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)