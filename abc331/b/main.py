# -*- coding: utf-8 -*-
"""
解く前のメモ用
Sが卵6個入りの価格
Mが卵8個入りの価格
Lが卵10個入りの価格
N個以上の卵を買うための最小金額を求める
どのパックも何個でも買えるし、買わなくてもいい
Nがたかだか100なので、すべてのサイズのパターンを試せば良い
"""

from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, S, M, L = arrange()
    ans = act(N, S, M, L)
    print(ans)


def arrange():
    N, S, M, L = map(int, input().split())
    return N, S, M, L


def act(N, S, M, L):
    ans = float("inf")
    for s in range(0, 101):
        for m in range(0, 101):
            for l in range(0, 101):
                if s*6 + m*8 + l*12 >= N:
                    price = s * S + m * M + l * L
                    ans = min(ans, price)
    return ans


solve()
