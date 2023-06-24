t=int(input())
for i in range(t):
    s=str(input())
    res=""
    a=[]
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            res+=s[i]
        else:
            if res!="":
                a.append(int(res))
                res=""
    if res!="":a.append(int(res))
    print(max(a))