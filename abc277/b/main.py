# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
S = [input() for _ in range(N)]
for s in S:
    l = s[0]
    r = s[1]
    if l not in set(["H", "D", "C", "S"]):
        print("No")
        exit()
    if r not in set(["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]):
        print("No")
        exit()
if len(set(S)) != N:
    print("No")
    exit()
print("Yes")
