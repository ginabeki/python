from email.mime import image


# File I/O
# mostly used when reading files

my_file = open('test.txt')
print(my_file.read()) # hi my name is Andrei Mac
my_file.seek(0) # cursor

print(my_file.readline()) # read line
print(my_file.readlines()) # reads all lines

# close
my_file.close()