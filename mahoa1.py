t=int(input())
for k in range(t):
    b=[0]*300
    s=str(input())
    x=0
    res=0
    check=False
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            res=0
            check=True
            for j in range(x,i):
                res+=1
            print(res,s[i-1],sep='',end='')
            x=i
    if check==False:print(len(s),s[0],sep='',end='')
    else:
        ans=''
        for i in range(x,len(s)):
            ans+=s[i]
        print(len(ans),s[len(s)-1],sep='',end="")
    print()