t=int(input())
while t!=0:
    s=input()
    for i in range(1,len(s),2):
        x=int(s[i])
        while x!=0:
            print(s[i-1],end="")
            x-=1
    print(end="\n")
    t-=1