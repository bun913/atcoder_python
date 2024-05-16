# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, L, A = arrange()
    ans = act(L, A)
    print(ans)


def arrange():
    N, L = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return N, L, A


def act(L, A):
    ans = 0
    for a in A:
        if a >= L:
            ans += 1
    return ans


solve()
