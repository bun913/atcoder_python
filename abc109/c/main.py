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
from math import gcd

N, X = map(int, input().split())
orgs = list(map(int, input().split()))

# Xの初期位置を入れた配列をつくってソートする
numbers = orgs + [X]
numbers.sort()

# 自分と隣り合った数との差分を計算する
diff_list = []
for i in range(len(numbers)-1):
    diff_list.append(numbers[i+1] - numbers[i])

ans = reduce(gcd, diff_list)
print(ans)
