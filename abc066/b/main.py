# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
S = input()

# ２文字ずつ減らしていって、条件を満たすか判定する
for i in range(len(S)-2, 1, -2):
    s = S[:i]
    half = s[:i//2]
    if s == half + half:
        print(len(s))
        exit()
