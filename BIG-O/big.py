# BIG O NOTATION and Time Complexity
from re import I


given_array = [1, 4, 3, 2, ..., 10]

# How much time does it take to run this function?


def find_sum(given_array):
    total = 0
    for each i in given_array:
        total +=i
    return total

# How much time does it take to run this function?
# Types of time complexity
# linear time complexity - time increases with the size of input
# constant time - time does not increase with increase in size
# quadratic time complexity-

# expressing time complexity in a more mathematical way
# Linear Time O(n) - big O of n 
# Constant time O(1) -big O of 1
# Quadratic time O(n2) - big O of n2

# Linear time - T = an + b - n is the size of the input or number of elements in an array, and a and b are constants.
# steps 1. find the fastest growing term, in this case is a and n 2. take out the coefficient

# Quadratic time - T = cn2 + dn + e

# example 2
given_array = [1, 4, 3, 2, ..., 10]
def stupid_function(given_array):
    total = 0
    return total

# constant time 
# T = c = 0.115ms, express this with big O. 1. find the fastest growing term 2. Take out the coefficient
# T = 0.115 x 1 = O(1)
# BIG O Notation helps to allow you to quicky compare multiple functions in terms of their performance. 
# Constant time is better than linear time because it takes less time


# another way of finding time complexity without running an experiment

# example 3
given_array = [1, 4, 3, 2, ..., 10]
def stupid_function(given_array):
    total = 0
    return total
# step1 consider each line of the function above. the first line initialises total and assigns it a value 0, which takes O(1). Takes constant time
# the second line also takes constant time O(1)

# T = O(1) + O(1) = C1 + C2 = C3 = C3 x 1 = O(1), when you add O(1) + O(1) you get result to be O(1)

# another example

def find_sum(given_array):
    total = 0
    for each i in given_array:
        total +=i
    return total

# in the above function finding time complexity and Big oh. The total = 0 will take a constant time which is O(1), the same to return total
# the total +=i takes constant amount of time O(1)
# the for loop also takes O(1)
# T2 = O(1) + n x O(1) + O(1) = c4+nxC5 = O(n)


array_2d = [[1, 4, 3],[3,1,9],[0, 5, 2]]
# double for loops T4 = O(2n2) O(n2) - quadratic time
# fastest growing terms
