# -*- coding: utf-8 -*-
"""
高橋が同じ座標にいたことがあるか判定する
"""
N = int(input())
S = list(input())
cur = (0, 0)
visited = set()
visited.add(cur)

for s in S:
    if s == 'R':
        cur = (cur[0]+1, cur[1])
    elif s == 'L':
        cur = (cur[0]-1, cur[1])
    elif s == 'U':
        cur = (cur[0], cur[1]+1)
    elif s == 'D':
        cur = (cur[0], cur[1]-1)
    if cur in visited:
        print("Yes")
        exit()
    visited.add(cur)
print("No")
