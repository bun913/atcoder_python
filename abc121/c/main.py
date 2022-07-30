# -*- coding: utf-8 -*-
"""
Nが最大で10**5なので線形探索はできる

単純に安い順に並べかえてMになるまで買えば良いだけでは
"""
N, M = list(map(int, input().split()))
memo = []

for i in range(N):
    a, b = list(map(int, input().split()))
    memo.append((a, b))


_sorted = sorted(memo)
cnt = 0
ans = 0

for a, b in _sorted:
    if cnt >= M:
        break
    num = min(b, M-cnt)
    cnt += num
    ans += (a * num)
print(ans)
