# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    S = sorted(list(set(A)))
    ranking = {x: i for i, x in enumerate(S)}
    for a in A:
        print(ranking[a])


solve()
