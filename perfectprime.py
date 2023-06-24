import math
def snt(n):
    if n<2:return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0: return False
    return True
def check(n):
    res=0
    sum=0
    while n!=0:
        if n%10!=2 and n%10!=3 and n%10!=5 and n%10!=7: return False
        res=res*10+n%10
        sum+=n%10
        n//=10
    if snt(sum)==False or snt(res)==False:return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    if check(n)==True:print("Yes")
    else:print("No")
