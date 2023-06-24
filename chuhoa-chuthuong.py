s=input()
h,t=0,0
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':t+=1
    else: h+=1
if h>t:print(s.upper())
else:print(s.lower())