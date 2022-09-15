"""
"""
N, T = list(map(int, input().split()))
L = list(map(int, input().split()))

ans = 0

for i in range(N - 1):
    t1 = L[i]
    t2 = L[i + 1]
    dif = t2 - t1
    ans += min(dif, T)

print(ans + T)
