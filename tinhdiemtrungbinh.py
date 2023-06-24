n = int(input())
a = list(map(float,input().split()))
min = min(a)
max = max(a)
dem = 0
for i in range(n):
    if a[i] == min or a[i] == max:
        dem+=1
        a[i] = 0
res = sum(a)
res = res/(n-dem)
print("%.2f" %res)