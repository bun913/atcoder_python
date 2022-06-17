# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

A, B = list(map(int, input().split()))

# 相似と三平方の定理を使う
x = math.sqrt(A ** 2 / (A**2 + B**2))
y = math.sqrt(B ** 2 / (A ** 2 + B ** 2))


print("{} {}".format(x, y))
