# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N = arrange()
    act(N)


def arrange():
    return int(input())


def act(N):
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        div = set()
        for a in range(1, int(i**0.5)+1):
            if i % a == 0:
                div.add(i // a)
                div.add(a)
        if len(div) == 8:
            ans += 1
    print(ans)


solve()
