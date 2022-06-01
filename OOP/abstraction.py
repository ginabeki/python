# we have 4 pillars of OOP
# Abstraction, hiding of information and giving access to what's necessary
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")
player1 = PlayerCharacter('andrei', 100)
print(player1.speak)
    