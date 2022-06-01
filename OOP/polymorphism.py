# polymorphism, means many forms
# methods belong to objects
# the idea of polymorphism refers to the way object classes can share same method name

class User():
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"attacking with power of {self.power}")
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 30)
print(wizard1.sign_in())
wizard1.attack() # attacking with power of 50
archer1.attack() # attacking with arrows: arrows left-100
# polymorphism
def player_attack(char):
    char.attack()
player_attack(wizard1)
player_attack(archer1)


