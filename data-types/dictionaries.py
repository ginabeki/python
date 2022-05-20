# dict, it's a data type but also a data structure in python, help to organise our data
# dictionary, is an unordered key value pair
dictionary = {
    'a':1,
    'b':2,
    'x':3
}
print(dictionary['b'])
print(dictionary) # {'a':1,'b':2,'x':3}

dictionary = {
    'a':[1,2,3],
    'b':'Hello',
    'x':True
}
print(dictionary['a'][1])

my_list = [{

     'a':[1,2,3],
    'b':'Hello',
    'x':True

},
{
     'a':[1,2,3],
    'b':'Hello',
    'x':True
}]
print(my_list[0]['a'][2]) #3