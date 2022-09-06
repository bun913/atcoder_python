"""
"""
N = int(input())
C = list(map(int, input().split()))
CD = sorted(C)
ans = 1
for i in range(N):
    ans = ans * max(0, CD[i] - i) % 1000000007
print(ans)
