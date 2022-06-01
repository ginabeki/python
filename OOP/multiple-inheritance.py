# multiple inheritance

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


class HybridBorg(Wizard, Archer):
    def __init__(self, anme, power, arrows):
        Archer.__init__(self, name, arrows)
hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows())