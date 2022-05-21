# set, unordered collection of unique objects
my_set = {1,2,3,4,5,5}
print(my_set) # 1,2,3,4,5
# there are no duplicates in a set
my_set.add(100)
my_set.add(2)
print(my_set) # 1,2,3,4,5,100

# if you are given a list to return a collection that has only unique items, for example
my_list = [1,2,3,4,5,5]
print(set(my_list)) # 1,2,3,4,5
# set objects do not support indexing, you can only grab by the item, for example
my_set = {1,2,3,4,5,5}
print(1 in my_set) # true

# Sets 2
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # 1,2,3
print(my_set.discard(5)) # None
print(my_set) # 1,2,3,4
print(my_set.difference_update(your_set)) #None
print(my_set) # 1,2,3
print(my_set.intersection(your_set)) # 4,5
print(my_set.isdisjoint(your_set)) # True because of 4,5
print(my_set.union(your_set)) # 1,2,3,4,5,6,7,8,9,10. Unites sets together an removes any duplicate print(my_set | your_set)
print(my_set.issubset(your_set)) # true
print(your_set.issuperset(my_set)) # true

