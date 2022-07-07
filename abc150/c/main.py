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
from itertools import combinations, permutations
import math

# Nの順列を考えて、与えられる順列P,Qがその順列たちの中で何番目か考える
# その差の絶対値を出せばOK
# 幸いにもNが8の階乗なので全列挙でも余裕
# pythonはpermutationsがあるから余裕

N = int(input())
P = list(input().split())
Q = list(input().split())

perm = list(permutations([i for i in range(1, N+1)]))
ps = ''.join(P)
qs = ''.join(Q)

_sorted = sorted([''.join(map(str, p)) for p in perm])
a = _sorted.index(ps) + 1
b = _sorted.index(qs) + 1

print(abs(a-b))
