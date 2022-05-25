# iterable is a collection that can be iterated over
# can be a list, dictionary, tuple, set, string
# iterated one by one to check each item in  the collection.
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

for item in user.items():
    print(item) # this will print key value pair

for item in user.values():
    print(item) # this print the values of user

for item in user.keys():
    print(item) #name age can_swim
