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
    n = to_custom_base26(N)
    print(n)


def to_custom_base26(n):
    if n == 0:
        return "a"

    result = []
    while n > 0:
        n -= 1
        result.append(chr(ord('a') + (n % 26)))
        n //= 26

    result.reverse()
    return ''.join(result)


solve()
