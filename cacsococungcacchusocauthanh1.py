t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    check=True
    if a[0]=='0' or b[0]=='0':check=False
    if len(a)!=len(b):check=False
    else:
        x=[]
        y=[]
        for i in range(len(a)):
            x.append(int(a[i]))
            y.append(int(b[i]))
        x.sort()
        y.sort()
        for i in range(len(a)):
            if x[i]!=y[i]:
                check=False
                break
    if check==True:print("True")
    else: print("False")