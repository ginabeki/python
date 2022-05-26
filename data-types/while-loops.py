# 
from multiprocessing import Condition

i = 0
while 0 < 50:
    print (i) # print infinity 0 as long as 0 is less than 50
# while loops helps to prevent infinity loop
# break helps to stop a loop from running
i = 0
while 0 < 50:
    print (i)
    i = i + 1 # i++, i+=1
    else:
        print('done with all the work')

# Part 2
# when should we use while loop and for loop
# for simple lopps use for loops, but when you are not sure how long it is going to take for looping, use while loop

my_list = [1,2,3]
for item in my_list:
    print(item) # 1 2 3

i = 0
while i < len (my_list):
    print(my_list[i]) # 1 2 3
    i += 1

while True:
    print (my_list[i])
    break
while True:
    input('say something: ')
    break