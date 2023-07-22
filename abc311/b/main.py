# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, D = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

free_humans = [0 for _ in range(D)]

for s in S:
    for i, status in enumerate(s):
        if status == "o":
            free_humans[i] += 1

cur = 0
ans = 0

for cnt in free_humans:
    if cnt == N:
        cur += 1
        ans = max(ans, cur)
        continue
    cur = 0
print(ans)
