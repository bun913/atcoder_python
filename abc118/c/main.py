# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    m = min(A)
    S = sum(A)
    skip_ind = A.index(m)
    while True:
        if S == m:
            break
        next_min = m
        for i in range(N):
            # 一旦初期化
            S = 0
            a = A[i]
            # 自分は無視
            if i == skip_ind:
                continue
            A[i] %= m
            S += A[i]
            if a % m == 0:
                continue
            if a % m < next_min:
                next_min = a % m
        S += m
        m = next_min
        skip_ind = A.index(m)
    print(sum(A))


solve()
