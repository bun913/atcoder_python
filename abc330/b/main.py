# -*- coding: utf-8 -*-
"""
解く前のメモ用
L <=X <= Rである整数Xiを求める
ただし 1 <= L <= R <= 10^9
であるためLからRのすべての整数を調べると計算量が大きすぎる
もとめる整数は常に一意に定まる
L以上R以下であるどの整数Yについても
Xi - Ai <= Y - A を満たす
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, L, R, A = arrange()
    ans = act(N, L, R, A)
    print(*ans, sep=" ")


def arrange():
    N, L, R = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return N, L, R, A


def act(N, L, R, A):
    ans = []
    for i in range(N):
        a = A[i]
        x = min(max(a, L), R)
        ans.append(x)
    return ans


solve()
