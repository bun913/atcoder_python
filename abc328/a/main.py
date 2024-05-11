# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, X, S = arrange()
    ans = act(X, S)
    print(ans)


def arrange():
    N, X = map(str, input().split())
    S = list(map(int, input().split()))
    return [N, X, S]


def act(X, S):
    x = int(X)
    ans = list(filter(lambda s: s <= x, S))
    return sum(ans)


solve()
