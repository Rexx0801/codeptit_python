t=int(input())
for i in range(t):
	s=input()
	a=s.find("\\")
	b=s.rfind("\\")
	res=s[:a+1]+".."+s[b:]
	print(res)