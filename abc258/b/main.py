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
from itertools import combinations
import math

N = int(input())
A = [list(map(int, list(input()))) for _ in range(N)]
# 最初は二次元配列を上下左右プラス斜めの方向に同じものをたすことを考えて
# 取り扱いが面倒そう
# インデックスが+にはみ出るときは % N をとって
# インデックスが-にはみ出るときはNを足してやればうまくいくのではないかと考え直した

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

_max = -1
for i in range(N):
    for j in range(N):
        # 各方向に移動
        for dx, dy in dxy:
            # N-1回だけ移動する
            s = ''
            curx = i
            cury = j
            for _ in range(N):
                # マイナスの場合の補正(Nを足してあげる)
                if curx < 0:
                    curx += N
                if cury < 0:
                    cury += N
                # プラスにはみ出る場合の補正(Nを引く)
                if curx > N - 1:
                    curx -= N
                if cury > N-1:
                    cury -= N
                s += str(A[curx][cury])
                curx -= dx
                cury -= - dy
            num = int(s)
            _max = max(num, _max)
print(_max)
