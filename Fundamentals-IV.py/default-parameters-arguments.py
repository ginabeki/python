
# positional arguments, arguments that require to be in the right position

# default parameters allow us to give what we want for default
def say_hello(name='Darth Vader', emoji=':('):
    print(f'helloo {name} {emoji}')
say_hello(name = 'Bibi',
emoji=':('
) # this is a bad practice, or if you have to use ensure it is in order