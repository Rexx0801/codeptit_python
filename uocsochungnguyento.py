import math
def check(n):
    if n<2:return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:return False
    return True
t=int(input())
while t!=0:
    a,b=map(int,input().split())
    x=math.gcd(a,b)
    ans=0
    while x!=0:
        ans+=x%10
        x//=10
    if check(ans)==True:print("YES")
    else:print("NO")
    t-=1