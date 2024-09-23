# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import sin, pi

setrecursionlimit(10**8)


def solve():
    act()


def act():
    A, B, C = map(int, input().split())
    ng = 0
    ok = 200
    while ok - ng > 10 ** -12:
        mid = (ok + ng) / 2
        x = A * mid + B * sin(C * mid * pi)
        if x >= 100:
            ok = mid
        else:
            ng = mid
    print(ok)


solve()
