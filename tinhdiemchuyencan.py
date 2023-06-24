
class SinhVien:
    def __init__(self,msv,name,lop):
        self.msv=msv
        self.name=name
        self.lop=lop
    def setCc(self,cc):
        self.cc=cc
    def out(self):
        print(self.msv,self.name,self.lop,self.cc,end=' ')
        if self.cc==0: print('KDDK',end='')
        print()
      

def cal_cc(k):
    s=10
    for i in k:
        if i=='m': s-=1
        if i=='v': s-=2
    if s<0: s=0
    return s
n=int(input())
a=[]
for i in range(n):
    a.append(SinhVien(input(),input(),input()))
for i in range(n):
    msv,k=map(str,input().split())
    for j in a:
        if j.msv==msv:
            j.setCc(cal_cc(k))
for i in a:
    i.out()
    
    