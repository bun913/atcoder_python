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

# N種類から人気の商品をM選ぶ
# 得票数が 1/4M未満の商品を選べない
# これでM個選べるかどうかだけ

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
AD = sorted(A, reverse=True)
s = sum(A)

ans = 'Yes'
for i in range(M):
    a = AD[i]
    t = (1 / (4*M))
    if a < t*s:
        ans = 'No'
        break
print(ans)
