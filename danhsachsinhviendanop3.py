class SinhVien:
  def __init__(self,name,file,tinhtrang):
    self.ma = name.split("-")[0]
    self.ten = name.split("-")[1]
    self.file = file
    self.tinhtrang = tinhtrang
n = int(input())
a=[]
for i in range(n):
  name = str(input())
  file = str(input())
  tinhtrang = str(input())
  sv = SinhVien(name,file,tinhtrang)
  if(sv.file != "No attachments" and sv.tinhtrang =="Turned in late"):
    a.append(sv.ma.upper())
print(len(a)) 
a.sort()
for i in a:
  print(i)