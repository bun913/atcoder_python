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

# N桁の数字(せいぜい3桁)
# si桁目がciである数字は存在するか
# 存在しない数字を考えてみる

# 1桁目が0
# 適当なi,jにおいて si == sj であり、 ci != cj である
# dictで何が出たかメモっておけば良いか

N, M = list(map(int, input().split()))
cand = [-1 for _ in range(N)]
memo = {}

# 候補を埋めながらダメなパターン探し
for i in range(M):
    s, c = list(map(int, input().split()))
    # N=1 意外で先頭0はNG
    if s == 1 and c == 0 and N != 1:
        print(-1)
        exit()
    if s in memo and memo[s] != c:
        print(-1)
        exit()
    memo[s] = c

# 候補となるリストに数を添えていく
for k, v in memo.items():
    cand[k-1] = v

# ここも条件がなかった場合でNが1桁の場合を考慮
for i in range(N):
    if cand[i] != -1:
        continue
    if i == 0:
        if N == 1:
            cand[i] = 0
        else:
            cand[i] = 1
    else:
        cand[i] = 0

print(*cand, sep='')
