n, m, x = input().split()
chuaxet = [0 for i in range(int(n)+1)]
chuoi = [[] for i in range(int(n))]
def dfs(u):
    chuaxet[u] = 1
    for i in range(len(chuoi[u-1])):
        v = chuoi[u-1][i]
        if chuaxet[v] == 0: dfs(v)

for i in range(int(m)):
    a, b = input().split()
    chuoi[int(a)-1].append(int(b))
    chuoi[int(b)-1].append(int(a))
dfs(int(x))
for i in range(1, int(n)+1):
    if chuaxet[i]==0:
        print(i)