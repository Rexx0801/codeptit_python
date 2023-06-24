import math
def dao(n):
    res=0
    while n!=0:
        res=res*10+n%10
        n//=10
    return res
t=int(input())
for k in range(t):
    check=[0]*1000001
    check[0]=1
    check[1]=1
    for i in range(2,math.isqrt(1000001)+1):
        if check[i]==0:
            for j in range(i*i,1000001,i):
                check[j]=1
    n=int(input())
    for i in range(3,n,2):
        if check[i]==0:
            if i!=dao(i) and dao(i)<n and check[dao(i)]==0:
                print(i,dao(i),end=" ")
                check[i]=1
    print()
