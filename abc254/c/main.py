# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, A = arrange()
    act(N, K, A)


def arrange():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A


def act(N, K, A):
    # エッジケース K = 1ならどんな並びでもOK
    if K == 1:
        print("Yes")
        exit()
    B = sorted(A)
    SA = [[] for _ in range(K)]
    SB = [[] for _ in range(K)]
    for i in range(N):
        SA[i % K].append(A[i])
        SB[i % K].append(B[i])
    for i in range(K):
        if sorted(SA[i]) != SB[i]:
            print("No")
            exit()
    print("Yes")


solve()
