# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = input()
ans = len(S)
cnt = S.count("00")
print(ans-cnt)
