# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
S = input()
T = input()
ans = "No"
if S.find(T) != -1:
    ans = "Yes"
print(ans)
