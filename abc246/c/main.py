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

N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))

use_comp = 0
rests = {}
r_price = sum(A)

for a in A:
    use = a // X
    rest = a % X
    use_comp += use
    # 完全にXのクーポンを使い切れる場合はこの時点で終了
    if use_comp >= K:
        ans = r_price - (K * X)
        print(ans)
        exit()
    if rest not in rests:
        rests[rest] = 1
    else:
        rests[rest] += 1

# ここまで来る時点でK枚のクーポンを最大限の効果(X円)で使い切ることができなかった場合
keys = sorted(rests.keys(), reverse=True)
rest_coupon = K - use_comp
tmp_price = r_price - (use_comp * X)

for key in keys:
    v = rests[key]
    # クーポンを使い切った場合
    if rest_coupon - v <= 0:
        rest_use = rest_coupon
        ans = tmp_price - (rest_use * key)
        print(ans)
        exit()
    tmp_price -= (key * v)
    rest_coupon -= v

print(tmp_price)
