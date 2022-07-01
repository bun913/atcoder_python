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

# 普通に変換しても良いけどどNが10**9まであるので、2真数とかすごい桁になる
# K真数で桁が上がるタイミングは、Kの冪乗が1上がったタイミング
# 例えば2真数なら、Kが2,4,8のタイミングで桁が増えるのでlog計算で一発では？
N, K = list(map(int, input().split()))
log = math.log(N, K)
print(int(log) + 1)
