t=int(input())
for k in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(m,n):
        print(a[i],end=" ")
    for i in range(m):
        print(a[i],end=" ")
    print()