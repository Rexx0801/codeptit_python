m,n,t=map(int,input().split())
a=[]
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
c=[]
for i in range(m):
    for j in range(n):
        if a[i][j]>t:
            a[i][j]=255
        else:
            a[i][j]=0
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()