# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""

from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N, D, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(D)]
    ST = [list(map(int, input().split())) for _ in range(K)]
    for i in range(K):
        s, t = ST[i]
        x, y = s, s
        for j in range(D):
            l, r = LR[j]
            # 範囲が重なる場合
            if max(x, l) <= min(y, r):
                x = min(x, l)
                y = max(y, r)
            if x <= t <= y:
                print(j+1)
                break


solve()
