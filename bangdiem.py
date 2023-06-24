class Student:
    def __init__(self, STT, ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):
        self.STT = STT
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        self.d8 = d8
        self.d9 = d9
        self.d10 = d10
    def diem(self):
        return round((self.d1 * 2 + self.d2 * 2 + self.d3 + self.d4 + self.d5 + self.d6 + self.d7 + self.d8 + self.d9 + self.d10)/10/1.2, 1)
    def xepHang(self):
        if self.diem() >= 9: return 'XUAT SAC'
        elif self.diem() <= 8.9 and self.diem() >= 8: return 'GIOI'
        elif self.diem() <= 7.9 and self.diem() >= 7: return 'KHA'
        elif self.diem() <= 6.9 and self.diem() >= 5: return 'TB'
        else: return 'YEU'
    def chuanHoaSTT(self):
        if self.STT < 10: return f'HS0{self.STT}'
        else: return f'HS{self.STT}'
    def getDiem(self):
        return self.diem()
    def __str__(self):
        return f"{self.chuanHoaSTT()} {self.ten} {self.diem()} {self.xepHang()}"
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n + 1):
        ten = input()
        b=[float(x) for x in input().split()] 
        s = Student(i, ten, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9])
        a.append(s)
    a.sort(key = lambda x : - x.getDiem())
    for j in a:
        print(j)
    
 