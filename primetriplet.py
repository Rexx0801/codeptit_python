import math
check=[0]*1000001
check[0]=1
check[1]=1
for i in range(2,math.isqrt(1000001)+1):
    if check[i]==0:
        for j in range(i*i,1000001,i):
            check[j]=1
t=int(input())
for k in range(t):
    n=int(input())
    ans=0
    for i in range(2,n-6):
        if check[i]==0 and check[i+6]==0:
            if check[i+2]==0 or check[i+4]==0:ans+=1
    print(ans)
