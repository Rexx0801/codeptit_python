t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    k=int(s,2)
    if n==2: print(s)
    elif n==8:print(oct(k)[2::])
    elif n==16:print(hex(k)[2::].upper())
    else:
        a=[]
        while k>0:
            a.append(k%4)
            k//=4
        a.reverse()
        for j in a:print(j,end="")
        print()