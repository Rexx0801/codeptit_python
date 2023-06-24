m,n,t=map(int,input().split())
a=[[0 for _ in range(n)] for _ in range(m)]
b=[[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    a[i]=list(map(int,input().split()))
for i in range(m):
    for j in range(n):
        if a[i][j]>t: b[i][j]=1
for i in range(m):
    for j in range(n):
        print(b[i][j],end=" ")
    print()