# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = 0
for k, v in C.items():
    ans += v // 2
print(ans)
