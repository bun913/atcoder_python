# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
n = input()
replaced = ''
for s in n:
    if s == '1':
        replaced += '9'
    elif s == '9':
        replaced += '1'
    else:
        replaced += s
print(replaced)
