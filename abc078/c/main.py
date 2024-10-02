# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    n, m = arrange()
    act(n, m)


def arrange():
    return map(int, input().split())


def act(n, m):
    total = (1900*m) + (100*(n-m))
    print(total * (2**m))


solve()
