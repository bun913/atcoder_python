# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S = arrange()
    sp = list(S)
    act(sp)


def arrange():
    return input()


def act(sp):
    print(*sp, sep=" ")


solve()
