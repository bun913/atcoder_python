# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    M, D, y, m, d = arrange()
    act(M, D, y, m, d)


def arrange():
    M, D = list(map(int, input().split()))
    y, m, d = list(map(int, input().split()))
    return M, D, y, m, d


def act(M, D, y, m, d):
    if d == D and m == M:
        print(y+1, 1, 1)
    elif d == D:
        print(y, m+1, 1)
    else:
        print(y, m, d+1)


solve()
