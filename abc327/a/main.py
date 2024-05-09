# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S = arrange()
    ans = act(S)
    if ans is True:
        print("Yes")
        exit()
    print("No")


def arrange():
    N = int(input())
    S = input()
    return N, S


def act(S) -> bool:
    if S.count("ab") > 0 or S.count("ba") > 0:
        return True
    return False


solve()
