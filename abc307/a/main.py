# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))
new_list = [A[i:i+7] for i in range(0, len(A), 7)]
ans = []
for l in new_list:
    ans.append(sum(l))
print(*ans, sep=" ")
