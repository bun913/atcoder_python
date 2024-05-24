# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    B, G = arrange()
    act(B, G)


def arrange():
    return list(map(int, input().split()))


def act(B, G):
    if B > G:
        print("Bat")
    else:
        print("Glove")


solve()
