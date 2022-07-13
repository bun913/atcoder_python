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

for i in range(len(S)):
    s = S[i]
    if (i+1) % 2 == 0:
        if s in set(['L', 'U', 'D']):
            continue
    if (i+1) % 2 != 0:
        if s in set(['R', 'U', 'D']):
            continue
    print('No')
    exit()
print('Yes')
