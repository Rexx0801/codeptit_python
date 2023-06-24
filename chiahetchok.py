a,k,n=map(int,input().split())
check=0
for i in range(1,n//k+1):
    if (k*i-a)>0:
        check=1
        print (k*i-a,end=" ")
if check==0:print("-1")
