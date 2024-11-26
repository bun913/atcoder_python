# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
import heapq
import math

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    return N, A


def act(N, A):
    s = sum(A)
    B = [s//N for _ in range(N)]
    # あまりがある場合の調整
    for i in range(s % N):
        B[N-i-1] += 1
    ans = 0
    for i in range(N):
        diff = abs(B[i] - A[i])
        ans += diff
    print(ans//2)


solve()
