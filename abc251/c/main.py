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
from collections import OrderedDict

# 同じ文字列でも特典が違う可能性がある
# N回の提出のうち、ようするにその文字列の中で一番早く出したものがオリジナル
# そのオリジナルの中から、最も特典が高いものを最優秀とする
# さらに得点が被るなら提出が早いものを最油臭とする
point_dic = OrderedDict()
index_dic = {}

N = int(input())

_max = -1
# dictにメモをする
for i in range(N):
    tmp = list(input().split())
    s = tmp[0]
    t = int(tmp[1])
    if s not in point_dic:
        point_dic[s] = t
        index_dic[s] = i + 1
        _max = max(t, _max)

for k, v in point_dic.items():
    if v == _max:
        print(index_dic[k])
        exit()
