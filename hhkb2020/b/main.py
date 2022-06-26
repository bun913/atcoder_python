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

H, W = list(map(int, input().split()))
# .なら散らかっていない
# #なら散らかっている
# 縦または横に隣接するマス目の内部2ます出会って、いずれのマスも散らかっていない場所に布団をしける
# 言い換えれば、自分自身が.であって、前後左右に.があれば1カウントとできる
# ただ重複が出ないように保持する必要がある
L = [list(input()) for _ in range(H)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

count = 0
for i in range(H):
    for j in range(W):
        cur = L[i][j]
        if cur != '.':
            continue
        for dx, dy in dxy:
            curi = i+dx
            curj = j+dy
            if not (curi < 0 or curj < 0 or curi > H-1 or curj > W-1):
                if L[curi][curj] == '.':
                    count += 1
# 重複度2で割る
print(count // 2)
