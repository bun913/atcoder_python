"""
長さNの整数列Cが与えられる
以下の要素を全て満たす長さNの整数列Aの個数を求める
1 <= Ai <= Ci
Ai != Aj(1 <=i < j <= N)
"""
N = int(input())
C = list(map(int, input().split()))
mod = 10**9 + 7

sort_c = sorted(C)
ans = 1

for i, c in enumerate(sort_c):
    cnt = c - i
    ans *= cnt
    if ans == 0:
        print(0)
        exit()
    ans %= mod
print(ans)
