# -*- coding: utf-8 -*-
"""
解く前のメモ用
容量Gのグラスと容量Mのマグカップがある
G < M
操作をK回行う
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    K, G, M = arrange()
    g, m = act(K, G, M)
    print(g, m)


def arrange():
    K, G, M = list(map(int, input().split()))
    return K, G, M


def act(K, G, M):
    g = 0
    m = 0
    for i in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            capa = G - g
            if capa >= m:
                g += m
                m = 0
            else:
                m -= capa
                g = G
    return g, m


solve()
