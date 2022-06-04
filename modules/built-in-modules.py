import random

# print(random)
# print(dir(random)) # dir shows all the methods available in a package

print(random.random()) # gives us number between 0 and 1
print(random.randint(1, 10)) # random int within this range
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

# Part 2
import sys
# sys 
print(sys)
sys.argv