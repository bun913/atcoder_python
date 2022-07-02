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

# 1以上K以下の整数a,b,cについて全てのgcdの和を求める
K = int(input())
s = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ab = math.gcd(a, b)
            abc = math.gcd(ab, c)
            s += abc
print(s)
