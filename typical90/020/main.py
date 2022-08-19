# -*- coding: utf-8 -*-
"""
log2の計算を素直にやろうとすると誤差がでる

対数の性質でググろう
https://manabitimes.jp/math/2046
"""
from math import log2

a, b, c = list(map(int, input().split()))
if a < c ** b:
    print('Yes')
    exit()
print('No')
