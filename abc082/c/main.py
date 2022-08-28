# -*- coding: utf-8 -*-
"""
解く前のメモ

長さNの整数の数列
aをよい数列にしたい
各要素xについてbに値xはちょうどx個含まれる

単純にグループ化して数を見ていけば終わりでは
"""
from itertools import groupby

N = int(input())
A = list(map(int, input().split()))
AD = sorted(A)

grouped = [(k, len(list(g))) for k, g in groupby(AD)]
ans = 0

for n, length in grouped:
    # 要素数が足りない場合は全て消す
    if length < n:
        ans += length
        continue
    # 要素数が大良い場合は差分だけ消す
    if length > n:
        ans += length - n
        continue
print(ans)
