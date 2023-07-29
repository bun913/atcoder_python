# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
K = int(input())
ans = []
for i in range(K):
    # アルファベットのi文字目を取得
    c = chr(ord('a') + i % 26)
    a = c.upper()
    ans.append(a)
print(*ans, sep='')
