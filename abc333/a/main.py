# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = arrange()
    ans = act(N)
    print(ans)


def arrange():
    return int(input())


def act(N):
    return str(N) * N


solve()
