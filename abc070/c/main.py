# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import lcm
from functools import reduce

setrecursionlimit(10**8)


def solve():
    N, T = arrange()
    act(N, T)


def arrange():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    return N, T


def act(N, T):
    lc = T[0]
    for i in range(1, N):
        lc = lcm(lc, T[i])
    print(lc)


solve()
