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

A, B, C, K = list(map(int, input().split()))
s = 0

# Kの値が10**9まであり得るので1ループでもできない
# O(N)で求められるようにする必要がありそう
a = K if A >= K else A
b = K-a if B >= K-a else B
c = K - (a+b)
print(a+(b*0)+(c*-1))
