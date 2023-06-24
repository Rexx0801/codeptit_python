s=str(input())
s=s.lower()
check=True
res=s[len(s)-3]+s[len(s)-2]+s[len(s)-1]
if res!='.py':check=False
for i in range(len(s)-3):
    if s[i]<'a' and s[i]>'z' and s[i]!='_' and s[i]!='.':
        check=False
        break
if check:print("yes")
else:print("no")