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

# 普通にやる場合,ひたすら試していけば良い
# でもNが10**18 で Kも最小1からなので、この場合ループだとTLEになってしまう
# そこでn%Kを値を出して、そのあまりとKとの絶対値との差を出す。あまりとのminを出して終わり

N, K = list(map(int, input().split()))
mod = N % K
ans = min(mod, abs(mod-K))
print(ans)
