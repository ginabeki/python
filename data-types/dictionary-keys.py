dictionary = {
    123: [1,2,3],
    True: 'hello',
    [100]: True
}
print(dictionary[100]) # this will print an error because lists cannot be used as keys
# keys should be descriptive like a string

# Dictionary Methods 1

user = {
    'basket': [1,2,3],
    'greet': 'hello'
}
print(user.get('age')) # error

print(user.get('age', 55)) # if age does not exist print 55, but if it exists print default value

# Methods 2
user  = {
    'basket':[1,2,3],
    'greet': 'hello',
    'age': 20

}
print('basket' in user) # does basket exist in user, prints True. Anything that does not exists will print false
print('age' in user.keys()) # check keys. Print true cos it exists
print('hello' in user.values()) # true

print(user.clear()) #None, get an empty dictionary
print(user.copy()) # allows us to copy a user
user2 = user.copy() # prints a copy of users

print(user.pop('age')) # returns the value removed
print(user.popitem()) # removes the last item in a dictionary, or randomly key-value pair
print(user.update({'age':55})) # age: 55


