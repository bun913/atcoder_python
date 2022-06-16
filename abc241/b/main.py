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

N, M = list(map(int, input().split()))
# Aの内容を辞書に
A = list(map(int, input().split()))
dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
B = list(map(int, input().split()))

for b in B:
    if b in dic and dic[b] > 0:
        dic[b] -= 1
    else:
        print('No')
        exit()
print('Yes')
