t=int(input())
a=[]
for i in range(t):
    b=[]
    s=input()
    b.append(s)
    x,y=map(int,input().split())
    b.append(x)
    b.append(y)
    a.append(b)
a.sort(key= lambda x:(-x[1],x[2],x[0]))
for ten,ac,sub in a:
    print(ten,ac,sub)