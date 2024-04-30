# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

N, M = list(map(int, input().split()))
S = input()
T = input()


def solve():
    is_startwith = T.startswith(S)
    is_endwith = T.endswith(S)
    if is_startwith and is_endwith:
        print(0)
        exit()
    if is_startwith and is_endwith is False:
        print(1)
        exit()
    if is_startwith is False and is_endwith:
        print(2)
        exit()
    print(3)


solve()
