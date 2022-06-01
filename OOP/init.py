# __init__, 
# cls means class
# classmethod aren't used as often, but cls can be used to instantiate an object
@classmethod
def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)

# staticmethod cannot access class 
@staticmethod
def adding_things(num1, num2):
    return num1 + num2