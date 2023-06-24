t=int(input())
while t!=0:
    n=int(input())
    a=[]
    while n!=0:
        a.append(n%10)
        n//=10
    if a[0]==a[len(a)-2] and a[1]==a[len(a)-1]:print("YES")
    else:print("NO")
    t-=1
    