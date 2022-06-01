# public and private variables
# private variables, underscore implies that there is private variable
# double underscore is called dunder method, means they shouldn't be modified
class PlayerCharacter:
    def __init__(self, name, age): 
        self._name = name # underscore should'nt be modified.
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")
player1 = PlayerCharacter('andrei', 100)
print(player1.speak)
    