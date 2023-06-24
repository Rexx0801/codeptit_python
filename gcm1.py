from re import A
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        res=max(res,gcd(a[i],a[j]))
print(res)