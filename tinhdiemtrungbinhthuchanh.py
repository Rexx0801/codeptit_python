import re
class Diem:
  def __init__(self,ten,diem1,diem2,diem3):
    self.ten = ten
    self.ma =""
    self.diem1 = diem1
    self.diem2 = diem2
    self.diem3 = diem3
    self.tong = round((diem1*3+diem2*3+diem3*2)/8+0.001,2)
    self.xeploai = 0
t = int(input())
a=[]
for i in range(t):
  x= str(input())
  x= x.strip().lower()
  res = re.findall("\w+", x) 
  ten=""
  for res2 in res:
    ten += res2[0:1].upper() + res2[1:]+" "
  ten = ten.strip()  
  diem1 = float(input())
  diem2 = float(input())
  diem3 = float(input())
  a.append(Diem(ten,diem1,diem2,diem3))
  if(i+1<10): a[i].ma = "SV0" + str(i+1)
  else: a[i].ma = "SV"+str(i+1)
a.sort(key= lambda x: x.ma)  
a.sort(key=lambda x: x.tong,reverse=True)
index =2
a[0].xeploai = 1
for i in range(1,t):
    if(a[i].tong == a[i-1].tong): a[i].xeploai = a[i-1].xeploai
    else: a[i].xeploai = index
    index+=1
for res in a:
  print("{} {} {:.2f} {}".format(res.ma,res.ten,res.tong,res.xeploai))