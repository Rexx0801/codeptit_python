from math import gcd
class Phanso:
    def __init__(self, a = None, b = None):
        self.a = a 
        self.b = b
    def Rutgon(self):
        x = gcd(self.a, self.b)
        self.a //= x
        self.b //= x 
    def __add__(self, other):
        tmp = Phanso()
        tmp.a = self.a*other.b + other.a*self.b
        tmp.b = self.b * other.b
        tmp.Rutgon()
        return tmp
    def __str__(self):
        return f'{self.a}/{self.b}'
arr = [int (i) for i in input().split()]
P1 = Phanso(arr[0], arr[1])
P2 = Phanso(arr[2], arr[3])
tmp = P1 + P2
print(tmp)
