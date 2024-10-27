# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    a, b, c, d = arrange()
    act(a, b, c, d)


def arrange():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    return a, b, c, d


def act(a, b, c, d):
    # 0手で行ける場合
    if a == c and b == d:
        print(0)
        exit()
    # 一手で行ける場合
    if abs(a-c) + abs(b-d) <= 3 or a - b == c-d or a + b == c + d:
        print(1)
        exit()
    # パリティが一緒
    # 移動A + 移動B
    if (a+b+c+d) % 2 == 0:
        print(2)
        exit()
    # 移動Cが2回
    if abs(a-c) + abs(b-d) <= 6:
        print(2)
        exit()
    # 移動Aと移動Cが1回ずつ
    if abs((a+b) - (c+d)) <= 3:
        print(2)
        exit()
    # 移動Bと移動Cが1回ずつ
    if abs((a-b) - (c-d)) <= 3:
        print(2)
        exit()
    print(3)


solve()
