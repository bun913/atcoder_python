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

# Nは最大で@*10**5なのでループはネストできない
# 辞書にメモで1回、辞書からの取り出しで1回、並び替えでnlogn

N = int(input())
dic = {}
_max = -1
# 辞書にメモ
for i in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
    _max = max(_max,  dic[s])
# 辞書から_maxの要素を取得して並び替え
keys = [k for k, v in dic.items() if v == _max]
_sorted = sorted(keys)

print(*_sorted, sep='\n')
