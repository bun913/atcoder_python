# -*- coding: utf-8 -*-
"""
解く前のメモ

再帰関数でも解けそうであるが、そもそも計算で求められそう

"""
from math import log2

H = int(input())
n = int(log2(H))

ans = 2 ** (n+1) - 1
print(ans)
