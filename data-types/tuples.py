# Tuples are immutable lists.
# Tuples are important because they make things easier when you don't want to change a list. 
# They make code more predictable, and efficient. 
# You can't sort, run reverse which makes them less flexible than lists.
# They are faster than lists.
# geographic location and coordinates are a good example of a tuple.
my_tuple = (1,2,3,4,5)

user = {
    (1,2):[1,2,3],
    'basket':[1,2,3],
    'greet':'hello',
    'age':20    
}
print(user.items()) # returns key and values as tuples
print(user[(1,2)]) # [1,2,3]

# Tuples 2
my_tuple = (1,2,3,4,5)
# Tuple has only two methods, that are commonly used:  count() and index()
print(my_tuple.count(5)) # 1, gives number of occurence of  a specified number
print(my_tuple.index(5)) # 4
