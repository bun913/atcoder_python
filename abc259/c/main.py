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
from itertools import combinations, groupby
import math

S = input()
T = input()

# SとTを同じグループを作れて、かつグループ化した文字列群を見比べる
gt = [(k, list(g)) for k, g in groupby(list(T))]
gs = [(k, list(g)) for k, g in groupby(list(S))]
# グループ数が違う場合はアウト
if len(gt) != len(gs):
    print('No')
    exit()
# グループ数が同じ場合見比べる
for i in range(len(gt)):
    ks, vs = gs[i]
    kt, vt = gt[i]
    # 文字が違う場合終了
    if ks != kt:
        print('No')
        exit()
    # 同じ文字の場合
    # そもそも数が同じならOK
    if len(vs) == len(vt):
        continue
    # 数が違う場合、sの方が2文字以上、tがs以上の長さならOK
    if len(vs) >= 2 and len(vt) >= len(vs):
        continue
    # ここまできてしまったらNG
    print('No')
    exit()
print('Yes')
