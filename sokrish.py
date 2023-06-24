def factorial(n) :
    fact = 1
    while (n != 0) :
        fact = fact * n
        n = n - 1
    return fact
t=int(input())
for k in range(t):
    n=int(input())
    m=n
    ans=0
    while n!=0:
        ans+=factorial(n%10)
        if ans>m:break
        n//=10
    if ans==m:print("Yes")
    else:print("No")