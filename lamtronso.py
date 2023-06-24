t=int(input())
while t!=0:
    a=[]
    n=int(input())
    nho=0
    while n>9:
        res=n%10
        res+=nho
        nho=0
        if res>=5:nho=1
        a.append(0)
        n//=10
    a.append(n+nho)
    a.reverse()
    for i in a:print(i,end="")
    print(end="\n")
    t-=1
