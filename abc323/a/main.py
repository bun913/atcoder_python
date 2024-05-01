# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)
S = input()


def solve():
    for i in range(len(S)):
        s = S[i]
        n = i + 1
        if n % 2 == 0:
            if s == "1":
                print("No")
                exit()
    print("Yes")


solve()
