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

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))
S = [(x1, y1), (x2, y2), (x3, y3)]
x4, y4 = 101, 101

# 排他的論理和を使えば、一発で仲間外れを見つけることができる
x4 = x1 ^ x2 ^ x3
y4 = y1 ^ y2 ^ y3

print("{} {}".format(x4, y4))
