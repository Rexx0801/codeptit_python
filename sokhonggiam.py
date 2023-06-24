def check(n):
    while n!=0:
        x=n%10
        n//=10
        y=n%10
        if x<y:return False
    return True
t=int(input())
while t!=0:
    n=int(input())
    if check(n)==True:print("YES")
    else:print("NO")
    t-=1