# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
populations = []
names = []
for _ in range(N):
    l = input().split()
    p = int(l[1])
    s = l[0]
    populations.append(p)
    names.append(s)
s = sum(populations)
ans = "atcoder"

for i in range(N):
    if s // 2 + 1 <= populations[i]:
        print(names[i])
        exit()
print(ans)
