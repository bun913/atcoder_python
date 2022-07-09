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

K = int(input())

if K <= 59:
    print("21:{}".format(str(K).zfill(2)))
    exit()
rest = K % 60
ans = '22:' + str(rest).zfill(2)
print(ans)
