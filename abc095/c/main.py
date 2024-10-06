# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    A, B, C, X, Y = map(int, input().split())
    ans = float("inf")
    for ab in range(max(X, Y) * 2 + 1):
        # abピザを買う枚数をabとして全探索する
        a = max(X - (ab // 2), 0)
        b = max(0, Y - (ab // 2))
        price = a * A + b * B + ab * C
        ans = min(ans, price)
    print(ans)


solve()
