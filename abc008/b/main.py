# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
c = Counter(S)
ans = c.most_common()[0][0]
print(ans)
