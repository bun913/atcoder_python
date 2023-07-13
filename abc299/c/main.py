# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import groupby

N = int(input())
S = list(input())
grouped = [(key, len(list(group))) for key, group in groupby(S)]

ans = -1

# まずは前からみる
limit = len(grouped)
for i in range(1, limit):
    bef = grouped[i-1]
    if bef[0] != '-':
        continue
    cur = grouped[i]
    level = cur[1]
    ans = max(ans, level)

# 次に反転した配列を使って後ろからみる
reversed_grouped = grouped[::-1]
for i in range(1, limit):
    bef = reversed_grouped[i-1]
    if bef[0] != '-':
        continue
    cur = reversed_grouped[i]
    level = cur[1]
    ans = max(ans, level)

print(ans)
