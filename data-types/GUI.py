# Our first GUI
# Exercise
# loop through the list
# display empty space anytime you encounter zero when looping
# display pixel or * when you encounter one
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# iterate over picture
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print ('*', end='')
        else: 
            print(' ', end='')
    print('')
    
    # if 0 print " "
    # if 1 print *
