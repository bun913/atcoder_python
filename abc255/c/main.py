# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import ceil

setrecursionlimit(10**8)


def solve():
    X, A, D, N = arrange()
    act(X, A, D, N)


def arrange():
    return map(int, input().split())


def act(X, A, D, N):
    # Dが0のエッジケース
    if D == 0:
        ans = abs(X - A)
        print(ans)
        exit()

    start = A
    end = A + D * (N-1)

    i1 = max(0, (X - A) // D)
    # ここがキモ。先に範囲外の場合を考えておく
    ans = min(abs(start-X), abs(end-X))

    # 周辺を+10,-10くらいまで探してみる
    for cand in range(i1-10, i1 + 11):
        s = A + D * cand
        if start <= s <= end or end <= s <= start:
            ans = min(ans, abs(X - s))

    print(ans)


solve()
