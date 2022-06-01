# pillars of oop
# encapsulation, the binding of data and functions that manipulate that data

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")
    player1 = PlayerCharacter('andrei', 100)