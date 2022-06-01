# MRO - Method Resolution Order, a rule that python follows when running a method, and which one to run
class A:
    num = 10

class B (A):
    pass

class C (A):
    num = 1

class D(B, C):
    pass

print(D.num) # 1
print(D.mro()) # gives us the order

# why inheritance can be confusing

class X:pass
class Y:pass
class Z:pass
class A(X, Y):pass
class B(Y,Z):pass
class M(B, A, Z): pass

print(M.__mro__)

