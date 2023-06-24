n=int(input())
a=[[0 for _ in range(n)] for _ in range(n)]
b=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
res=a[n//2][n//2]
for i in range(n): 
    for j in range(n):
        if a[i][j]>res: b[i][j]=1
b[n//2][n//2]=res
for i in range(n):
    for j in range(n):
        if b[i][j]!=res: print(b[i][j],end=" ")
        else: print("x",end=" ")
    print()
s=[]
h1,h2,c1,c2=0,n-1,0,n-1
cnt=1
while cnt<n*n:
    for i in range(c1,c2+1):
        s.append(b[h1][i])
        cnt+=1
    h1+=1
    for i in range(h1,h2+1):
        s.append(b[i][c2])
        cnt+=1
    c2-=1
    for i in range(c2,c1-1,-1):
        s.append(b[h2][i])
        cnt+=1
    h2-=1
    for i in range(h2,h1-1,-1):
        s.append(b[i][c1])
        cnt+=1
    c1+=1
for i in s:print(i,sep="",end="")
print()
ans=len(s)-1
sum=0
for i in range(0,len(s)):
    sum+=s[i]*(2**ans)
    ans-=1
print(sum)