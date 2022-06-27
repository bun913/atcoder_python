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

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 成績を計算
# 例えばKが３の時
# K学期の評点は、１個以外掛け合わせる数は同じ
# だからA[i]とA[i-k]を比較してA[i]が大きければ掛け算の合計は必ずおおきくなる
for i in range(K, N):
    bef = A[i-K]
    cur = A[i]
    if cur > bef:
        print('Yes')
        continue
    print('No')
