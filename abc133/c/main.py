# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    L, R = arrange()
    act(L, R)


def arrange():
    return map(int, input().split())


def act(L, R):
    mod = 2019
    # 2019で割った章が繰り上がるなら絶対どこかで0が出るので0を出力
    ls = L // mod
    rs = R // mod
    if rs - ls >= 1:
        print(0)
        return
    # 商が同じってことは素直に計算すればいい
    ans = 2019
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j) % mod)
    print(ans)


solve()
