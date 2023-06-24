import math

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def distance(self,Point):
        dist = math.sqrt((self.x - Point.x) * (self.x - Point.x) + (self.y - Point.y) * (self.y - Point.y))
        return "%.4f"%dist
    
def Decimal(n):
    return float(n)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
