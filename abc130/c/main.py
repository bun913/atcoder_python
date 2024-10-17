# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    W, H, x, y = arrange()
    act(W, H, x, y)


def arrange():
    return map(int, input().split())


def act(W, H, x, y):
    # 中心を求める
    center_x = W / 2
    center_y = H / 2
    if center_x == x and center_y == y:
        print(W * H / 2, 1)
        exit()
    print(W * H / 2, 0)


solve()
