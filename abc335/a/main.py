# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S = arrange()
    act(S)


def arrange():
    return input()


def act(S):
    l = list(S)
    l[-1] = 4
    print(*l, sep="")


solve()
