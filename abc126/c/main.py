# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import log2, ceil
from decimal import *

setrecursionlimit(10**8)


def solve():
    N, K = arrange()
    act(N, K)


def arrange():
    return map(int, input().split())


def act(N, K):
    # まずは普通に計算してみる
    ans = Decimal(0)
    for i in range(N):
        a = i + 1
        if a >= K:
            prob = Decimal(1) / Decimal(N)
            ans += prob
            continue
        si = ceil(log2(K/a))
        prob = Decimal(1) / Decimal(N) * Decimal(0.5) ** si
        ans += prob
    print("{:.12f}".format(ans))


solve()
