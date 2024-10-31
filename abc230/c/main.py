# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, B = arrange()
    act(N, A, B)


def arrange():
    return map(int, input().split())


def act(N, A, B):
    P, Q, R, S = map(int, input().split())

    # 二次元配列を作成
    grid = [["." for _ in range(S - R + 1)] for _ in range(Q - P + 1)]

    for i in range(Q - P + 1):
        for j in range(S - R + 1):
            curx = P + i
            cury = R + j
            # 要するに (curx, cury ) が (A+k, B+k) となっていれば良い
            # curx = A+k を式変形して k = curx - A
            # cury = B+k を式変形して k = cury - B
            if curx - A == cury - B:
                grid[i][j] = "#"
            # こちらも同様 (curx, cury) が (A+k, B-k)となっていればOK
            # curx = A+k を式変形して k = curx - A
            # cury = B-k を式変形して k = B - cury
            if curx - A == B - cury:
                grid[i][j] = "#"

    # 結果の出力
    for row in grid:
        print("".join(row))


solve()
