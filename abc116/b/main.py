# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import lru_cache

s = int(input())


def f(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


@lru_cache(maxsize=None)
def recursion(i: int) -> int:
    if i == 0:
        return s
    return f(recursion(i-1))


_set = set()
for i in range(0, 1000001):
    ans = recursion(i)
    if ans in _set:
        print(i+1)
        exit()
    _set.add(ans)
