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

# 最大値を求めるforをネストさせない
# 合計が最大となる区間を探して、その区間の期待値を求める方向にする
_max_sum = -1
max_dist = []
for i in range(N-K+1):
    l = P[i:i+K]
    s = sum(l)
    if s > _max_sum:
        _max_sum = s
        max_dist = l

ans = 0
for a in max_dist:
    s = (a * (1 + a)) / 2
    e = s / a
    ans += e
print(ans)

# for i in range(N-K+1):
#     l = P[i:i+K]
#     expect_sum = 0.0
#     for a in l:
#         if a not in memo:
#             s = (a * (1 + a)) / 2
#             e = s / a
#             expect_sum += e
#             memo[a] = e
#         else:
#             expect_sum += memo[a]
#     _max = max(_max, expect_sum)

# print(_max)
