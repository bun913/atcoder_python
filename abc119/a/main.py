# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from datetime import datetime as dt

S = input()
td = dt.strptime(S, '%Y/%m/%d')
base = dt.strptime('2019/04/30', '%Y/%m/%d')

if td <= base:
    print('Heisei')
    exit()
print('TBD')
