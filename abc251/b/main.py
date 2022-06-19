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

# 単純に100から3種類選んでも10**6 * 5種類(3種類からどれか最低でも一つを使う)
N, W = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = set()

for a in range(N):
    # 1つだけの場合
    if N == 1:
        if A[a] <= W:
            print(1)
            exit()
    for b in range(a+1, N):
        # 2つだけの場合
        if N == 2:
            if A[a] <= W:
                ans.add(A[a])
            if A[b] <= W:
                ans.add(A[b])
            if A[a] + A[b] <= W:
                ans.add(A[a] + A[b])
            print(len(ans))
            exit()
        for c in range(b+1, N):
            # ここから3種類をbit全探索
            for i in range(8):
                uses = []
                for j in range(3):
                    if ((i >> j) & 1):
                        uses.append(True)
                    else:
                        uses.append(False)
                # 全く使わないパターンは想定しない
                if True not in uses:
                    continue
                s = 0
                if uses[0]:
                    s += A[a]
                if uses[1]:
                    s += A[b]
                if uses[2]:
                    s += A[c]
                if s <= W:
                    ans.add(s)
# print(ans)
print(len(ans))
