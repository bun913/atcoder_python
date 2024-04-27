# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)
S = input()
if len(S) == 1:
    print("Yes")
    exit()

for i in range(1, len(S)):
    if S[i-1] <= S[i]:
        print("No")
        exit()
print("Yes")
