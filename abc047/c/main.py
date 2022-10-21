# -*- coding: utf-8 -*-
"""
解く前のメモ用
何個同じ色のグループが続いているかという問題では
ランレングス圧縮してみるか
"""
from itertools import groupby

S = input()
compressed = [k for k, g in groupby(S)]
print(len(compressed) - 1)
