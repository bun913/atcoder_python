# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**7)
N, M = map(int, input().split())
# i皿目がi番目に食べた色
C = list(map(str, input().split()))
# Diの皿の料理は1皿Piとなる
D = list(map(str, input().split()))
P = list(map(int, input().split()))
# まずCに出てくる色とDに出てくる色を見て価格の対応表を作る
pc = defaultdict(int)
for i, d in enumerate(D):
    pc[d] = P[i+1]
ans = 0
for c in C:
    if c not in pc:
        ans += P[0]
        continue
    ans += pc[c]
print(ans)
