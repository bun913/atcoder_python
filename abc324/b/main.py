# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = int(input())
   # Nを2で破り続けられるか
    while N % 2 == 0:
        N //= 2
    # Nを3で破り続けられるか
    while N % 3 == 0:
        N //= 3
    if N == 1:
        print("Yes")
        exit()
    print("No")


solve()
