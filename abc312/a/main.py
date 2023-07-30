# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = input()
cands = set([
    "ACE",
    "BDF",
    "CEG",
    "DFA",
    "EGB",
    "FAC",
    "GBD"
])
if S in cands:
    print("Yes")
    exit()
print("No")
