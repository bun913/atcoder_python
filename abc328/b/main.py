# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, D = arrange()
    ans = act(N, D)
    print(ans)


def arrange():
    N = int(input())
    l = list(map(int, input().split()))
    return N, l


def act(N, D):
    # 1種類の文字だけで表せる日付が何個あるか愚直に数える
    ans = 0
    for y in range(1, N+1):
        d = D[y-1]
        for i in range(1, d+1):
            ys = list(str(y))
            ds = list(str(i))
            seted = set(ys + ds)
            if len(seted) == 1:
                ans += 1
    return ans


solve()
