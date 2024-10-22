# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    A, B = arrange()
    act(A, B)


def arrange():
    A, B = input().split()
    return A, B


def act(A, B):
    a = int(A)
    tmp = B.replace(".", "")
    b = int(tmp)
    ans = a * b // 100
    print(ans)


solve()
