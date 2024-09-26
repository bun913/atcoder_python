# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""

from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    K, S = map(int, input().split())
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            z = S - x - y
            if 0 <= z <= K:
                ans += 1
    print(ans)


solve()
