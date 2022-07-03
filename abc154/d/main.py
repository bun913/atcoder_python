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

# N個のサイコロが左から一列に並んでいる
# i番目のサイコロは1からpiまでの種類の目が、等確率で出る
# 隣接するKこのサイコロを選んで、それぞれ独立に降った時に、出る目の合計の期待値の最大値を求める

# K,Nはそれぞれ200,000まで, pは1000まで
# ループする場合1ネストしかできな
# Kの場合基本的に、出る目の数が多い順番に取れば期待値はデカくなる

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

ans = 0

_max = -1

for i in range(N-K+1):
    l = P[i:i+K]
    expect_sum = 0.0
    for a in l:
        s = (a * (1 + a)) / 2
        e = s / a
        expect_sum += e
    _max = max(_max, expect_sum)

print(_max)
