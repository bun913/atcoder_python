# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from bisect import bisect_left, bisect_right

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    ans = 0
    for i in range(N):
        middle = B[i]
        down_cnt = N - bisect_right(C, middle)
        up_cnt = bisect_left(A, middle)
        ans += down_cnt * up_cnt
    print(ans)


solve()
