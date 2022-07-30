# -*- coding: utf-8 -*-
"""
問題を解く前のメモ

BTCの時に与えられるのが少数なので、都度円に両替していたら誤差が出る
BTCとYenを別に計算して最後にまとめて換金した方が良さそう
"""

N = int(input())
yen_sum = 0
btc_sum = 0

for _ in range(N):
    val, cur = input().split()
    if cur == 'JPY':
        yen_sum += int(val)
        continue
    btc_sum += float(val)

btc_to_yen = btc_sum * 380000.0
print(yen_sum + btc_to_yen)
