# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""

from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S, K = arrange()
    ans = act(N, S, K)
    print(ans)


def arrange():
    return list(map(int, input().split()))


def act(N, S, K):
    ans = 0
    for i in range(N):
        p, q = list(map(int, input().split()))
        ans += p * q
    if ans < S:
        ans += K
    return ans


solve()
