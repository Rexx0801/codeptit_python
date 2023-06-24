def tong(N):
    S = 0
    if N % 2 == 0: 
        for i in range(2, N+1, 2):
            S += (-1) ** (i // 2 + 1) / i
    else: 
        for i in range(1, N+1, 2):
            S += -(-1) ** ((i+1) // 2) / i
    return S
t = int(input())
for k in range(t):
    N = int(input())
    kq = tong(N)
    print(f"{kq:.5f}")