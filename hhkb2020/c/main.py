# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from heapq import heappush, heappop, heapify

N = int(input())
P = list(map(int, input().split()))

cant_use = set()
cands = [i for i in range(0, N+1)]
heapify(cands)

for p in P:
    cant_use.add(p)
    while True:
        cand = heappop(cands)
        if cand not in cant_use:
            print(cand)
            heappush(cands, cand)
            break
