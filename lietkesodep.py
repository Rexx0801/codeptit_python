def check(n):
    i=0
    m=n
    res=0
    while m!=0:
        x=m%10
        res=res*10+x
        if x%2!=0:return False
        m//=10
        i+=1
    if i%2!=0:return False
    if res!=n:return False
    return True
t=int(input())
while t!=0:
    n=int(input())
    for i in range(22,n,2):
        if check(i)==True:print(i,end=" ")
    print(end="\n")
    t-=1