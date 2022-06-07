with open('test.txt') as my_file:
    print(my_file.readlines())

#read
with open('test.txt', mode = 'r+_') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text)
    print(my_file.readlines())
# write, allows us to write to a file. write also creates a file
# append
with open('sad.txt', mode='_w_') as my_file:
    text = my_file.write(':(')
    print(text)