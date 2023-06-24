from datetime import date

class HoaDon:
    def __init__(self):
        self.banggia=[25,34,50,80]
        self.stt=0
        self.name=""
        self.sophong=""
        self.ngaynhan=""
        self.ngaytra=""
        self.dichvu=0
        self.ngayo=0
        self.tongtien=0
    def calc(self):
        self.ngayo=(date(self.ngaytra[2],self.ngaytra[1],self.ngaytra[0])-date(self.ngaynhan[2],self.ngaynhan[1],self.ngaynhan[0])).days+1
        self.tongtien=self.banggia[int(self.sophong[0])-1]*self.ngayo+self.dichvu
    def info(self):
        print("KH{:0>2} {} {} {} {}".format(self.stt,self.name,self.sophong,self.ngayo,self.tongtien))
    def setSTT(self,n):
        self.stt=n
    def read(self):
        self.name=input()
        self.sophong=input()
        self.ngaynhan=[int(x) for x in input().split("/")]
        self.ngaytra=[int(x) for x in input().split("/")]
        self.dichvu=int(input())

if __name__ == "__main__":
    n=int(input())
    data=[]
    for i in range(n):
        x=HoaDon()
        x.setSTT(i+1)
        x.read()
        x.calc()
        data.append(x)
    data.sort(reverse=True,key=lambda x:x.tongtien)
    for i in data:
        i.info()