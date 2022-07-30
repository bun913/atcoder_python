# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
cands = {25: 'Christmas', 24: 'Christmas Eve',
         23: 'Christmas Eve Eve', 22: 'Christmas Eve Eve Eve'}
D = int(input())
print(cands[D])
