# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
H, W = list(map(int, input().split()))
C = [list(input()) for _ in range(H)]
cd = [list(x) for x in zip(*C)]
ans = []
for c in cd:
    t = c.count("#")
    ans.append(t)
print(*ans, sep=" ")
