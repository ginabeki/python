# enumerate, not as common but still useful
for i, char in enumerate('Helllooo'):
    print(i, char) # means index of each item
# output
# 0 H
# 1 e
# 2 l
# 3 l
# 4 l
# 5 0
# 6 o
# 7 o

# create a script that creates an index of 50 in the counter of number in the range (100)
for i, char in enumerate (list(range(100))):
    if char == 50:
        print (f'index of 50 is: {i}')
    