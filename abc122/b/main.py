# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S = arrange()
    act(S)


def arrange():
    return input()


def act(S):
    ans = 0
    n = len(S)
    for i in range(n):
        for j in range(n):
            l = S[i:j+1]
            ok = True
            for s in l:
                if s not in set('ACGT'):
                    ok = False
                    break
            if ok:
                ans = max(ans, len(l))
    print(ans)


solve()
