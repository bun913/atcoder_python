# -*- coding: utf-8 -*-
"""
Nが3以上100以下
なので3重ループで全探索しても問題なさそう
"""
N, M = list(map(int, input().split()))

s = set()

for i in range(M):
    u, v = list(map(str, input().split()))
    s.add(u+v)

ans = 0
for a in range(1, N-1):
    for b in range(a+1, N):
        for c in range(b+1, N+1):
            ab = str(a) + str(b)
            bc = str(b) + str(c)
            ac = str(a) + str(c)
            if ab in s and bc in s and ac in s:
                ans += 1
print(ans)
