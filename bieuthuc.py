t = int(input())
for c in range(t):
    l = []
    s = input()
    mo,ngoac = 0,[]
    for c in s:
        if c == "(":
            mo +=1
            ngoac += [str(mo)]
            l +=[str(mo)]
        if c == ")":
            a = ngoac[-1]
            l += [a]
            ngoac.pop()
    print(" ".join(l))