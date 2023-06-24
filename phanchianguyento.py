import math
def snt(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
n = int(input())
a = list(map(int,input().split()))
res = []
for i in range(n):
    if a[i] not in res:
        res.append(a[i])
check = 0
ans=[res[0]]
tmp=res[0]
for i in range(1,len(res)):
    tmp+=res[i]
    ans.append(tmp)
for i in range(len(ans)-1):
    if snt(ans[i])==True and snt(ans[len(ans)-1]-ans[i])==True:
        check=1
        print(i)
        break
if check == 0:
    print("NOT FOUND")