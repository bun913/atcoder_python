# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from bisect import bisect_left

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    acc = [0] * (N)
    acc[0] = A[0]
    for i in range(1, N):
        acc[i] = acc[i - 1] + A[i]
    acc = [0] + acc
    ans = float('inf')
    for i in range(1, N):
        left = acc[i]
        right = acc[-1] - left
        ans = min(ans, abs(left - right))
    print(ans)


solve()
