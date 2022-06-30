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

# ビンゴが達成しているか見る
# ますを順に見ていって8方向にみていき3つ穴が揃っていたらOK

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# 穴埋め
for i in range(3):
    for j in range(3):
        for b in B:
            if b == A[i][j]:
                A[i][j] = '#'
                break

# チェック
for i in range(3):
    for j in range(3):
        if A[i][j] != '#':
            continue
        for dx, dy in dxy:
            cnt = 1
            curx = i
            cury = j
            while True:
                is_out_index = curx + dx < 0 or cury + dy < 0 or curx + dx > 2 or cury + dy > 2
                if is_out_index is True:
                    break
                curx += dx
                cury += dy
                if A[curx][cury] == '#':
                    cnt += 1
            if cnt == 3:
                print('Yes')
                exit()
print('No')
