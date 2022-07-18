# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

A, B = list(map(int, input().split()))

# 地道に4パターン調べるか
# と思ったが、AとBが互いに違うことがわかっているので2パターンしかない
cand = (A+B) // 2
if abs(A-cand) == abs(B-cand):
    print(cand)
    exit()
print('IMPOSSIBLE')
