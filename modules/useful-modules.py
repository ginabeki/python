# useful modules
from collections import counter, defaultdict, OrderedDict
from typing import Counter
# counter, can be used to count duplicate users or emails
li = [1,2,3,4,5,6,7]
print(Counter(li)) # creates a dict
sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

dictionary = {'a':1, 'b':2}
print(dictionary('c')) #1

dictionary = defaultdict(lambda:'does not exist', {'a':1, 'b':2})
print(dictionary ['c']) # does not exist

#Ordered dict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['a'] = 1
d['b'] = 2

print(d == d2) # true

# Useful modules 2
# time
import datetime
print(datetime.time(5,45,2)) # 05:45:02
print(datetime.date.today()) # prints current date

# array
from array import array
# list in py are dynamic
# arrays take up less memory and perform fatser in python
arr = array('i', [1,2,3])
print(arr) # i, [1,2,3]

