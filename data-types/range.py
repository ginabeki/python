# range (), returns a sequence of integers
print(range(100)) # range(0,100)

for number in range(0,100):
    print(number) # 0-100
for item in range (0, 10, 2): # 2 in this means stepover
    print(item) #0, 2, 4, 6, 8

for item in range(10, 0, -1):
    print(item) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

for item in range(2):
    print(list(range(10)))
# output
# [0,1,2,3,4,5,6,7,8,9]
# [0,1,2,3,4,5,6,7,8,9]

