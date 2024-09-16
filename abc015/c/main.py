# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from itertools import product

setrecursionlimit(10**8)


def solve():
    N, K, T = arrange()
    act(N, K, T)


def arrange():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    return N, K, T


def act(N, K, T):
    cands = product(*T)
    for cand in cands:
        # 長さが1の場合はその要素が0じゃなければOK
        if len(cand) == 1:
            if cand[0] == 0:
                print("Found")
                exit()
        # 長さが2以上の場合はxorを取って0じゃなければOK
        else:
            xor = 0
            for c in cand:
                xor ^= c
            if xor == 0:
                print("Found")
                exit()
    print("Nothing")


solve()
