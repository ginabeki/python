# list comprehensions, set comprehensions, dict comprehensions
# Instead of this:
my_list = []

for char in 'hello':
    my_list.append(char)
print(my_list)

# do this:
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 ==0]
print(my_list) #['h','e','l','l','o']

# list comprehension is a shorthand way of doing things