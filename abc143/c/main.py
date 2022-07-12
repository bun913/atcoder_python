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
from itertools import groupby
import math

# 同じ色をもつ隣接スライムは融合する
# 要するに隣接した文字をグループにまとめて終えば良い
# ラングレス圧縮の考え方でまとめて仕舞えば良い
N = int(input())
S = input()
grouped = groupby(list(S))
print(len(list(grouped)))
