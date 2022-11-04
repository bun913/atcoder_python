# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
S = input()
x = 0
ans = -1000
for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(max(ans, 0))
