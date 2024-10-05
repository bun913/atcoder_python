# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # Nが小さいの素直に全探索する
    while True:
        is_all_even = True
        for i in range(N):
            a = A[i]
            if a % 2 == 1:
                is_all_even = False
                break
        if is_all_even is False:
            break
        for i in range(N):
            A[i] = A[i] // 2
        ans += 1
    print(ans)


solve()
