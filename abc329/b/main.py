# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(A):
    se = set(A)
    l = list(se)
    so = sorted(l, reverse=True)
    print(so[1])


solve()
