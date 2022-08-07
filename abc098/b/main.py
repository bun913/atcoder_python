# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N = int(input())
S = input()

ans = 0
for i in range(1, N):
    left = S[:i]
    right = S[i:]
    set_l = set(left)
    set_r = set(right)
    inters = set_l.intersection(right)
    ans = max(len(inters), ans)
print(ans)
