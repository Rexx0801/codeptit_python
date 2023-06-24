t=int(input())
for i in range(t):
    n=int(input())
    f=[0]*2
    for i in range(2,n+1):
        x=i+f[len(f)-1]
        f.append(x)
    print(f[len(f)-1])