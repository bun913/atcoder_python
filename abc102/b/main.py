# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが最大100なので単純な全探索でも良い
ただ今回は普通に最小値と最大値を取れば終わりな気がする
"""
N = int(input())
A = list(map(int, input().split()))

_min = min(A)
_max = max(A)

ans = abs(_max - _min)
print(ans)
