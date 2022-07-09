# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

# X以上の素数で最小のものを求める
# LogNの式で素数判定すればいつかたどり着くのでは・・・・


def is_prime(n: int) -> bool:
    """
    素数判定(LogN)
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


X = int(input())
cur = X

while True:
    if is_prime(cur) is True:
        print(cur)
        exit()
    cur += 1
