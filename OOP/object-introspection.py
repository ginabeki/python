# object introspection

class User(object):
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self, name, power,email):
        super().__init__(email)
        self.name = name
        self.power = power

#introspection, means the ability to identify an object type at runtime
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
print(dir(wizard1))

