n=int(input())
m=int(n/2)
a=[]
b=[]
d=1
for i in range(m):
    a.append(d)
    d+=1
for i in range(m,n): 
    a.append(0)
b=a[::-1]
for i in range(m):
    for j in a:
        print (j,end=" ")
    print()
for i in range(m,n):
    for j in b:
        print(j,end=" ")
    print()