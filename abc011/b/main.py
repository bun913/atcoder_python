# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
S = input()
L = list(S)
L[0] = L[0].upper()
ans = [L[0]] + [s.lower() for s in L[1:]]
print(*ans, sep="")
