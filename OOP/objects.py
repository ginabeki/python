# create objects
class PlayerCharacter:
    def __init__(self, name, age): #dunder method, magicmethod
        self.name = name # atrributes
        self.age = age
    
    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44) #call a class to create an object, which in this case is player1

player2 = PlayerCharacter('Tom', 22)

print(player1.name) # Cindy
print(player2.name) # Tom