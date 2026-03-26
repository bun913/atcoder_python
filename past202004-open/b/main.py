# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**7)


S = list(input())
memo = defaultdict(int)

# create memo
for s in S:
    memo[s] += 1

# create answer
l_t_memo = sorted(memo.items(), key=lambda item:item[1])
ans = l_t_memo[-1][0]
print(ans)

