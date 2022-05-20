# list, is an ordered sequence of objects
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2, 'a', True]

# Data structure 
# A way for us to organise information and data into a folder so that it can be used for different purposes. A container around your data. 

amazon_cart = [
'notebooks', 
'sunglasses',
'toys',
'grapes']
print (amazon_cart[0]) # notebooks

# list slicing
print(amazon_cart[0:2]) #notebooks, sunglasses
print(amazon_cart[0::2]) # notebooks, toys

# lists are mutable
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:] # [:]used to copy the entire list
new_cart[0] = 'gum'
print(new_cart) # gum, sunglases, toys
print(amazon_cart) # laptop, sunglasses, toys, grapes
