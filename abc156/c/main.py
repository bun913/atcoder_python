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

# xiが1以上、100以下でNもたかだか100なので全探索で間に合いそう
N = int(input())
X = list(map(int, input().split()))

ans = float('inf')

for i in range(1, 101):
    sum_hp = 0
    for x in X:
        hp = (x-i) ** 2
        sum_hp += hp
    ans = min(ans, sum_hp)
print(ans)
