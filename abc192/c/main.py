# -*- coding: utf-8 -*-
"""
解く前のメモ用
言われた通りにやるだけの問題に見える
Nもたかだか9桁だし、Kも10**5で特に問題なく全探索できそう
"""
from sys import setrecursionlimit
setrecursionlimit(10**7)


def g1(x: str) -> int:
    tmp = sorted(x, reverse=True)
    s_tmp = "".join(tmp)
    return int(s_tmp)


def g2(x: str) -> int:
    tmp = sorted(x)
    s_tmp = "".join(tmp)
    return int(s_tmp)


def f(x: str) -> str:
    g1ans = g1(x)
    g2ans = g2(x)
    int_ans = g1ans - g2ans
    return str(int_ans)


def solve(N: str, K: int):
    k = K
    n = N
    while k > 0:
        n = f(n)
        k -= 1
    return n


N, K = map(int, input().split())
ans = solve(str(N), K)
print(ans)
