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

A, B, C, D, E, F, X = list(map(int, input().split()))

t = 0
a = 0

# 何セット歩けるか
t_set = X // (A+C)
a_set = X // (D+F)
# あまりが何秒あるか
t_mod = X % (A+C)
a_mod = X % (D+F)

# まずはセット数で進んだメートルを計算
t = (B * A) * t_set
a = (E * D) * a_set

# あまりで進める文をたす
t += (min(t_mod, A) * B)
a += (min(a_mod, D) * E)


if t > a:
    print('Takahashi')
elif a > t:
    print('Aoki')
elif t == a:
    print('Draw')
