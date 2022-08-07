# -*- coding: utf-8 -*-
"""
解く前のメモ

まじでランレングス圧縮するだけ
"""
from itertools import groupby

s = input()
compressed = [k + str(len(list(g))) for k, g in groupby(s)]
print(*compressed, sep='')
