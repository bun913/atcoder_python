# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    # 最初に合成しても、最後に合成しても消費MPは同じ
    # そして合成さえ終われば、あとは+1するか、-1するかの選択で答えがでる
    # N本のたけそれぞれに対してAに向けて合成するか、Bに向けて合成するか、Cに向けて合成するか、合成しないかの4通りを全探索する
    # つまり再帰で解ける

    def rec(i, a, b, c):
        # N本目まで割り振っている
        if i == N:
            if min(a, b, c) > 0:
                return abs(a-A) + abs(b-B) + abs(c-C)
            # A, B, C に何も割り振ってない場合は問題を満たさないので大きい値を返す
            else:
                return float("inf")
        # i本目を使わない選択
        cost = rec(i+1, a, b, c)
        # A,B,Cに割り振る(1本目の時は合成MPを使わず、2本目以降のときから10MPを加算する)
        cost = min(cost, rec(i+1, a+L[i], b, c) + (10 if a > 0 else 0))
        cost = min(cost, rec(i+1, a, b+L[i], c) + (10 if b > 0 else 0))
        cost = min(cost, rec(i+1, a, b, c+L[i]) + (10 if c > 0 else 0))
        return cost

    print(rec(0, 0, 0, 0))


solve()
